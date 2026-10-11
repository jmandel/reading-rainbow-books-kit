import sys,json,urllib.request,urllib.parse,io,re,os
from PIL import Image
# usage: covers_auto.py master.tsv out_dir [min_num] — for each episode's feature book, gather ISBNs from Open Library,
# try Amazon large covers and Apple Books art, keep the largest. Prints size; <1000px means "find better manually".
UA={'User-Agent':'Mozilla/5.0'}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read()
def to10(i):
    if len(i)==10: return i
    if len(i)==13 and i.startswith('978'):
        b=i[3:12]; c=(11-sum((10-k)*int(x) for k,x in enumerate(b))%11)%11; return b+('X' if c==10 else str(c))
def n(s): return re.sub(r'[^a-z0-9]','',s.lower())
master,out=sys.argv[1:3]; lo=int(sys.argv[3]) if len(sys.argv)>3 else 1
for l in open(master):
    num,season,date,title,fb,narr=(l.rstrip('\n').split('\t')+['']*6)[:6]
    if int(num)<lo or os.path.exists(f'{out}/{num}.jpg'): continue
    book=re.split(r'\s+by\s+|,',fb or title)[0].strip() or title
    m=re.search(r'\bby\s+([^,;]+)',fb); author=m.group(1).strip() if m else ''
    surname=author.split()[-1] if author else ''
    isbns=[]
    try:
        q=urllib.parse.urlencode({'title':book,**({'author':surname} if surname else {}),'fields':'isbn,author_name','limit':5})
        for d in json.loads(get(f'https://openlibrary.org/search.json?{q}'))['docs']: isbns+=d.get('isbn',[])
    except Exception as ex: pass
    cands=[]
    for i in [x for x in dict.fromkeys(to10(i) for i in isbns) if x][:30]:
        cands+=[f'https://m.media-amazon.com/images/P/{i}.01._SL1500_.jpg',f'https://images-na.ssl-images-amazon.com/images/P/{i}.01._SCRM_.jpg']
    try:
        r=json.loads(get('https://itunes.apple.com/search?'+urllib.parse.urlencode({'term':book,'media':'ebook','limit':15})))['results']
        for x in r:
            if n(book)==n(x.get('trackName','')) and (not surname or n(surname) in n(x.get('artistName',''))):
                cands.append(re.sub(r'/\d+x\d+bb\.','/2000x2000bb.',x['artworkUrl100']))
    except Exception: pass
    best=None
    for u in cands:
        try: data=get(u); im=Image.open(io.BytesIO(data))
        except Exception: continue
        if im.width<100: continue
        if best is None or im.width*im.height>best[0]: best=(im.width*im.height,u,data,im.size)
    if best:
        open(f'{out}/{num}.jpg' if best[3][0]>=1000 or best[3][1]>=1000 else f'{out}/{num}.low.jpg','wb').write(best[2])
    print(num,book,'|',author,'|',best[3] if best else None,f'({len(isbns)} isbns)',flush=True)
