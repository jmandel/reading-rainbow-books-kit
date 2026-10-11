import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tokens import tokens
# usage: show.py file.vtt [from_min] [to_min] -> transcript in ~20s lines
T=tokens(sys.argv[1]); a=float(sys.argv[2])*60 if len(sys.argv)>2 else 0; b=float(sys.argv[3])*60 if len(sys.argv)>3 else 1e9
line=[];t0=None
for t,w in T:
    if t<a or t>b: continue
    if t0 is None: t0=t
    line.append(w)
    if t-t0>20: print(f"[{int(t0//60):02d}:{int(t0%60):02d}] "+' '.join(line)); line=[];t0=None
if line: print(f"[{int(t0//60):02d}:{int(t0%60):02d}] "+' '.join(line))
