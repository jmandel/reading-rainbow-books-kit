import sys,os,textwrap
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tokens import tokens,find
# usage: inaudio.py <num> [episodes.tsv] — print exactly the transcript text that is in the podcast audio,
# with a few words of cut context on each side of every kept span, then the end-credits book list if the captions have it.
num=sys.argv[1]; spec=sys.argv[2] if len(sys.argv)>2 else 'episodes.tsv'
row=next(l.rstrip('\n').split('\t') for l in open(spec) if l.split('\t')[0]==num)
season,vid,segs=row[1],row[5],row[6]
T=tokens(f"s{season}/{vid}.en.vtt"); w=lambda a,b:' '.join(x for _,x in T[max(a,0):b])
for n,seg in enumerate(segs.split(' ;; '),1):
    sp,ep,*ea=seg.split('|'); ea=float(ea[0]) if ea else 0
    i,_=find(T,sp); _,j=find(T,ep,after=max(ea,T[i][0]))
    print(f"--- span {n}: {T[i][0]:.0f}s-{T[j][0]:.0f}s")
    print(f"(CUT before: ...{w(i-15,i)})")
    print(textwrap.fill(w(i,j+1),110))
    print(f"(CUT after: {w(j+1,j+16)}...)")
import re
full=' '.join(x for _,x in T); m=None
for m in re.finditer(r"(reading rainbow books|books (that )?you saw|today's books|books on today)",full,flags=re.I): pass
print(f"--- {len(segs.split(' ;; '))} kept span(s); full captions run {T[-1][0]/60:.0f} min")
if m: print("--- credits roll (cut, for identifying books):\n"+textwrap.fill(full[m.start():m.start()+700],110))
else: print("--- no credits roll in these captions (may be a reading-only clip; see INSTRUCTIONS for full-episode captions)")
