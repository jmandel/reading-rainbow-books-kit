import sys
# usage: add_rows.py rows.tsv ... — merge rows into episodes.tsv (replacing same episode numbers), sorted by number.
new=[l for f in sys.argv[1:] for l in open(f).read().splitlines() if l.strip() and not l.startswith('#')]
rows=open('episodes.tsv').read().splitlines(); nums={r.split('\t')[0] for r in new}
rows=[r for r in rows if r.split('\t')[0] not in nums]+new
hdr=[r for r in rows if not r.split('\t')[0].isdigit()]; body=sorted([r for r in rows if r.split('\t')[0].isdigit()],key=lambda r:int(r.split('\t')[0]))
open('episodes.tsv','w').write('\n'.join(hdr+body)+'\n'); print(len(body),'episodes')
