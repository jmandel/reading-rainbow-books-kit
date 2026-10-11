import sys,os,re,glob,subprocess,tempfile,json,email.utils,datetime
from xml.sax.saxutils import escape
import markdown  # show notes: src_root/notes/<num>.md
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from tokens import tokens,find
# usage: build.py episodes.tsv src_root out_dir base_url [num ...]
# Book covers come from src_root/covers_final/<num>.jpg (optional).
# Cuts each episode's book segments from the original YouTube audio (one encode, 192k MP3)
# and writes feed.xml for every episode whose MP3 exists in out_dir.
spec,src,out,base=sys.argv[1:5]; only=set(sys.argv[5:])
eps=[dict(zip('num season date title credit id segs chap'.split(),l.rstrip('\n').split('\t')))
     for l in open(spec) if l.strip() and not l.startswith('#')]
def sn(e): return int(re.match(r'\d+',e['season']).group())  # "4A" -> 4
def slug(e): return f"s{sn(e):02d}e{int(e['num']):03d}-"+re.sub(r'[^a-z0-9]+','-',e['title'].lower()).strip('-')+'.mp3'
def art(e):
    # Square 1600px episode art: whole cover centered over a blurred, enlarged copy of itself.
    from PIL import Image,ImageFilter
    src_img=f"{src}/covers_final/{e['num']}.jpg"
    if not os.path.exists(src_img): return None
    os.makedirs(f"{out}/art",exist_ok=True); dst=f"{out}/art/{slug(e)[:-4]}.jpg"
    im=Image.open(src_img).convert('RGB'); S=1600
    bg=im.resize((S,S)).filter(ImageFilter.GaussianBlur(40))
    k=S/max(im.size); fg=im.resize((round(im.width*k),round(im.height*k)),Image.LANCZOS)
    bg.paste(fg,((S-fg.width)//2,(S-fg.height)//2)); bg.save(dst,quality=90)
    return dst
def source(e):
    d=f"{src}/s{e['season']}"
    a=[p for p in glob.glob(f"{d}/{e['id']}.orig.*") if p.endswith(('.webm','.m4a','.opus','.mp3','.mka'))]
    return (a[0] if a else None), f"{d}/{e['id']}.en.vtt"
def cut(e):
    audio,vtt=source(e)
    if not audio: print(f"{e['num']} {e['title']}: no source audio yet"); return
    T=tokens(vtt); spans=[]
    for seg in e['segs'].split(' ;; '):
        sp,ep,*ea=seg.split('|'); ea=float(ea[0]) if ea else 0
        i,_=find(T,sp); _,j=find(T,ep,after=max(ea,T[i][0]))
        nxt=T[j+1][0] if j+1<len(T) else T[j][0]+4
        spans.append((max(0,T[i][0]-0.6), min(T[j][0]+4.0, max(T[j][0]+1.5, nxt-0.5))))
    # One filter graph: trim each span, short fades, 0.8s pause between spans, loudness-normalize, one encode.
    f=[];labels=[]
    for k,(a,b) in enumerate(spans):
        f.append(f"[0:a]atrim={a:.2f}:{b:.2f},asetpts=PTS-STARTPTS,afade=t=in:d=0.3,afade=t=out:st={b-a-0.6:.2f}:d=0.6,aresample=48000,aformat=channel_layouts=stereo[s{k}]")
        labels.append(f"[s{k}]")
        if k<len(spans)-1:
            f.append(f"anullsrc=r=48000:cl=stereo,atrim=0:0.8[g{k}]"); labels.append(f"[g{k}]")
    d=sum(b-a for a,b in spans)+0.8*(len(spans)-1)
    f.append(''.join(labels)+f"concat=n={len(labels)}:v=0:a=1,afade=t=out:st={d-2:.2f}:d=2,loudnorm=I=-18:TP=-1.5[out]")
    # Chapters: "Introduction" from 0, then the book title where the narrator reads it (1s early).
    ct,_=find(T,e['chap'],after=spans[0][0]); ct=T[ct][0]; off=0
    for a,b in spans:
        if a<=ct<=b: chap=max(0,off+ct-a-1.0); break
        off+=b-a+0.8
    else: raise SystemExit(f"chapter phrase outside kept audio: {e['title']}")
    os.makedirs(f"{out}/art",exist_ok=True); open(f"{out}/art/{slug(e)[:-4]}.chap",'w').write(f"{chap:.2f}")
    meta=tempfile.mktemp(suffix='.txt'); ms=lambda x:int(x*1000)
    open(meta,'w').write(f";FFMETADATA1\n[CHAPTER]\nTIMEBASE=1/1000\nSTART=0\nEND={ms(chap)}\ntitle=Introduction\n"
        f"[CHAPTER]\nTIMEBASE=1/1000\nSTART={ms(chap)}\nEND={ms(d)}\ntitle={e['title']}\n")
    cover=art(e); pic=['-i',cover] if cover else []; picmap=['-map','1:v','-c:v','copy','-disposition:v','attached_pic','-metadata:s:v','comment=Cover (front)'] if cover else []
    subprocess.run(['ffmpeg','-loglevel','error','-y','-i',audio,*pic,'-i',meta,'-map_chapters',str(1+len(pic)//2),'-map_metadata',str(1+len(pic)//2),'-filter_complex',';'.join(f),'-map','[out]',*picmap,
        '-ar','44100','-c:a','libmp3lame','-b:a','192k','-id3v2_version','3',
        '-metadata',f"title={e['title']}",'-metadata','artist=Reading Rainbow','-metadata','album=Reading Rainbow Books',
        '-metadata',f"track={e['num']}",'-metadata',f"date={e['date'][:4]}",f"{out}/{slug(e)}"],check=True)
    print(f"{e['num']} {e['title']}: "+', '.join(f'{a:.0f}-{b:.0f}' for a,b in spans)+f" ({d/60:.1f} min, story at {int(chap//60)}:{int(chap%60):02d}) <- {os.path.basename(audio)}")
os.makedirs(out,exist_ok=True)
for e in eps:
    if not only or e['num'] in only: cut(e)
items=[]
for e in eps:
    p=f"{out}/{slug(e)}"
    if not os.path.exists(p): continue
    dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p],capture_output=True,text=True).stdout)
    y,m,dd=map(int,e['date'].split('-'))
    pub=email.utils.format_datetime(datetime.datetime(y,m,dd,12,tzinfo=datetime.timezone.utc))
    url=f"{base}{slug(e)}"
    cf=f"{out}/art/{slug(e)[:-4]}.chap"; chap=float(open(cf).read()) if os.path.exists(cf) else None
    hms=lambda x:f"{int(x//3600):02d}:{int(x%3600//60):02d}:{x%60:06.3f}"
    psc=(f'\n    <psc:chapters version="1.2"><psc:chapter start="00:00:00.000" title="Introduction"/>'
         f'<psc:chapter start="{hms(chap)}" title="{escape(e["title"])}"/></psc:chapters>') if chap is not None else ''
    line=e['title']+', '+e['credit']+'. Reading Rainbow season '+e['season']+', episode '+e['num']+' ('+e['date'][:4]+').'
    nf=f"{src}/notes/{e['num']}.md"
    desc=f"<p>{escape(line)}</p>\n"+markdown.markdown(open(nf).read()) if os.path.exists(nf) else line
    a=f"art/{slug(e)[:-4]}.jpg"; img=f'\n    <itunes:image href="{escape(base+a)}"/>' if os.path.exists(f"{out}/{a}") else ''
    items.append(f"""  <item>
    <title>{escape(e['title'])}</title>
    <description>{escape(desc)}</description>
    <content:encoded><![CDATA[{desc.replace(']]>',']]&gt;')}]]></content:encoded>
    <enclosure url="{escape(url)}" length="{os.path.getsize(p)}" type="audio/mpeg"/>
    <guid isPermaLink="false">reading-rainbow-{e['num']}</guid>
    <pubDate>{pub}</pubDate>
    <itunes:duration>{int(dur)}</itunes:duration>
    <itunes:season>{sn(e)}</itunes:season>
    <itunes:episode>{e['num']}</itunes:episode>{img}{psc}
  </item>""")
open(f"{out}/feed.xml",'w').write(f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:psc="http://podlove.org/simple-chapters" xmlns:content="http://purl.org/rss/1.0/modules/content/">
<channel>
  <title>Reading Rainbow Books</title>
  <link>{base}</link>
  <description>The book readings from Reading Rainbow, with LeVar Burton's lead-in to each story. Private family feed.</description>
  <language>en-us</language>
  <itunes:block>Yes</itunes:block>
  <itunes:type>serial</itunes:type>
  <itunes:image href="{base}cover-books.jpg"/>
  <image><url>{base}cover-books.jpg</url><title>Reading Rainbow Books</title><link>{base}</link></image>
{chr(10).join(items)}
</channel>
</rss>
""")
print(f"feed.xml: {len(items)} episodes")
