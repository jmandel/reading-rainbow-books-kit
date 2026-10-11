import sys,os,glob
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tokens import tokens,find
# usage: check.py rows.tsv — dry-run boundary check (no encoding): for each row, show kept spans, story-chapter time,
# and the words right at each cut so you can confirm nothing important is clipped.
for l in open(sys.argv[1]):
    if not l.strip() or l.startswith('#'): continue
    num,season,date,title,credit,vid,segs,chap=l.rstrip('\n').split('\t')
    vtt=f"s{season}/{vid}.en.vtt"
    try:
        T=tokens(vtt); spans=[]
        for seg in segs.split(' ;; '):
            sp,ep,*ea=seg.split('|'); ea=float(ea[0]) if ea else 0
            i,_=find(T,sp); _,j=find(T,ep,after=max(ea,T[i][0])); spans.append((i,j))
        c,_=find(T,chap,after=T[spans[0][0]][0])
        w=lambda a,b:' '.join(x for _,x in T[max(a,0):b])
        print(f"{num} {title}: "+', '.join(f"{T[i][0]:.0f}-{T[j][0]:.0f}" for i,j in spans)+f" | story@{T[c][0]:.0f}s")
        for i,j in spans:
            print(f"   START ...{w(i-6,i)} [[ {w(i,i+8)}")
            print(f"   END   {w(j-7,j+1)} ]] {w(j+1,j+8)}...")
        if not any(T[i][0]<=T[c][0]<=T[j][0] for i,j in spans): print("   !! chapter phrase outside kept spans")
    except SystemExit as ex: print(f"{num} {title}: ERROR {ex}")
    except FileNotFoundError: print(f"{num} {title}: ERROR no captions at {vtt}")
