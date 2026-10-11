import sys,re
# usage: lint_notes.py notes/<num>.md ... — mechanical checks on show notes; prints problems, exit 1 if any.
SECS={'About the book':(120,180),'Author and illustrator':(120,180),'In this episode':(80,160),
      'Also recommended':(0,999),'Episode details':(0,999),'Sources':(0,999)}
META=r"no biography|(could not|couldn't|did not|didn't) (find|turn up|locate)|not found in|sources? (checked|consulted)|claimed here|this note|turned up in"
bad=0
for f in sys.argv[1:]:
    t=open(f).read(); errs=[]
    if not t.startswith('## About the book'): errs.append('must start with "## About the book" (no title line)')
    parts=re.split(r'^## (.+)$',t,flags=re.M)[1:]; got=dict(zip(parts[::2],parts[1::2]))
    if list(got)!=list(SECS): errs.append(f'sections {list(got)} != {list(SECS)}')
    for s,(lo,hi) in SECS.items():
        n=len(got.get(s,'').split())
        if not lo<=n<=hi: errs.append(f'{s}: {n} words (want {lo}-{hi})')
    total=sum(len(v.split()) for k,v in got.items() if k!='Sources')
    if not 450<=total<=550: errs.append(f'total {total} words without Sources (want 450-550)')
    for k,v in got.items():
        if k=='Sources': continue
        for m in re.finditer(META,v,flags=re.I): errs.append(f'{k}: meta/first-person "{v[max(0,m.start()-30):m.end()+30].strip()}"')
    if not re.search(r'season \d+, episode \d+ \(episode \d+ overall\)',got.get('Episode details','')): errs.append('episode details line format')
    for e in errs: print(f'{f}: {e}')
    bad|=bool(errs)
sys.exit(bad)
