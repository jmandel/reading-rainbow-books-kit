import re,sys,json,subprocess
# usage: match_sources.py master.tsv > sources_all.tsv — pick a YouTube source per episode.
# Preference: official STORY clip > Kidzuko full episode > fan full episode > YouTube search hit (full-length, title match).
def n(s): return re.sub(r'[^a-z0-9]','',s.lower().replace('&','and'))
def load(f,kind,minlen=0,need=None):
    out=[]
    for l in open(f):
        i,d,t=l.rstrip('\n').split('\t')[:3]
        try: d=float(d)
        except: d=0
        if d<minlen or (need and need not in t): continue
        out.append((i,d,t,kind))
    return out
pool=load('official.tsv','official-story',need='STORY')+load('kidzuko.tsv','kidzuko',1400)+load('fan.tsv','fan',1400)
eps=[l.rstrip('\n').split('\t') for l in open(sys.argv[1])]
def hit(title,cands):
    k=n(title); return [c for c in cands if k and k in n(c[2])]
search=[]
for e in eps:
    num,title=e[0],e[3]
    h=hit(title,pool)
    if not h:
        r=subprocess.run(['uvx','--from','yt-dlp[default]@latest','yt-dlp','--flat-playlist','--no-warnings','--print','%(id)s\t%(duration)s\t%(title)s\t%(channel)s',f'ytsearch12:Reading Rainbow {title}'],capture_output=True,text=True)
        cands=[]
        for l in r.stdout.splitlines():
            p=l.split('\t')
            try: d=float(p[1])
            except: continue
            if 1300<=d<=2100 and 'rainbow' in p[2].lower(): cands.append((p[0],d,p[2]+' ['+p[3]+']','search'))
        h=hit(title,cands)
    if h: i,d,t,k=h[0]; print('\t'.join([num,i,k,str(int(d)),t]),flush=True)
    else: print('\t'.join([num,'','MISSING','',title]),flush=True)
