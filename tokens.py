import re,html
# Word-level (time, word) tokens from a YouTube VTT: exact word timings for auto-captions,
# interpolated across each cue for hand-made captions.
def sec(t):h,m,s=t.split(':');return int(h)*3600+int(m)*60+float(s)
def tokens(path):
    txt=open(path).read()
    cues=re.findall(r'(\d+:\d+:\d+\.\d+) --> (\d+:\d+:\d+\.\d+)[^\n]*\n(.*?)(?:\n\n|\Z)',txt,re.S)
    auto='<c>' in txt
    out=[];seen_end=-1
    for a,b,body in cues:
        a,b=sec(a),sec(b)
        if auto:
            for line in body.split('\n'):
                if '<c>' not in line and not re.search(r'<\d',line): continue
                t=a
                for i,p in enumerate(re.split(r'<(\d+:\d+:\d+\.\d+)>',line)):
                    if i%2: t=sec(p)
                    else: out+=[(t,w) for w in re.sub(r'<[^>]+>','',p).split()]
        else:
            if a<seen_end: continue  # skip overlapping duplicate cues
            seen_end=b
            ws=re.sub(r'\([^)]*\)|\[[^\]]*\]','',html.unescape(re.sub(r'<[^>]+>','',body))).split()
            out+=[(a+(b-a)*i/max(len(ws),1),w) for i,w in enumerate(ws)]
    return [(t,html.unescape(w)) for t,w in out if not re.fullmatch(r'\[[^\]]*\]',w)]
def norm(w): return re.sub(r"[^a-z0-9']","",w.lower().replace('’',"'"))
def find(toks,phrase,after=0):
    ws=[norm(w) for w in phrase.split()]; n=[norm(w) for _,w in toks]
    for i in range(len(n)):
        if toks[i][0]<after: continue
        j=i;k=0
        while k<len(ws) and j<len(n):
            if not n[j]: j+=1; continue
            if n[j]!=ws[k]: break
            j+=1;k+=1
        if k==len(ws): return i,j-1
    raise SystemExit(f"phrase not found: {phrase!r}")
