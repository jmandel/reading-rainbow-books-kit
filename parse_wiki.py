import re,sys
# usage: parse_wiki.py wiki_episodes.txt > master.tsv — num, season, air date, title, feature-book line, narrator (LeVar seasons 1-21 only)
txt=open(sys.argv[1]).read()
season=None
for line_block in re.split(r'(?=^===Season )|(?=^\{\{Episode list)',txt,flags=re.M):
    m=re.match(r'===Season (\w+)',line_block)
    if m: season=m.group(1); continue
    if not line_block.startswith('{{Episode list') or season is None: continue
    if season.startswith('22'): break
    f=dict(re.findall(r'^\| *(\w+) *= *(.*)$',line_block,re.M))
    d=re.search(r'(\d{4})\|(\d+)\|(\d+)',f.get('OriginalAirDate',''))
    date=f"{d[1]}-{int(d[2]):02d}-{int(d[3]):02d}" if d else ''
    clean=lambda s:re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]",r'\1',re.sub(r"''+|<[^>]+>|\{\{[^}]*\}\}",'',s)).strip()
    fb=re.search(r'Feature Book[s]?:\s*(.*)',line_block); fb=clean(fb.group(1)) if fb else ''
    print('\t'.join([f.get('EpisodeNumber','').strip(),season,date,clean(f.get('Title','')),fb,clean(f.get('Aux2',''))]))
