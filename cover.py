import sys
from PIL import Image,ImageDraw,ImageFont
# usage: cover.py out.png — 1400x1400 rainbow-arc podcast cover
S=1400; im=Image.new('RGB',(S,S),'#fdf6e3'); d=ImageDraw.Draw(im)
cols=['#e63946','#f4a261','#e9c46a','#2a9d8f','#457b9d','#6a4c93']
cx,cy,r,w=S//2,S//2+170,560,62
for k,c in enumerate(cols):
    rr=r-k*w; d.pieslice([cx-rr,cy-rr,cx+rr,cy+rr],180,360,fill=c)
rr=r-len(cols)*w; d.pieslice([cx-rr,cy-rr,cx+rr,cy+rr],180,360,fill='#fdf6e3')
f=ImageFont.truetype('/usr/share/fonts/noto/NotoSans-Bold.ttf',150)
g=ImageFont.truetype('/usr/share/fonts/noto/NotoSans-Bold.ttf',110)
for t,y,font in [('Reading',cy+60,f),('Rainbow',cy+225,f)]:
    d.text((cx,y),t,font=font,fill='#264653',anchor='mt')
im.save(sys.argv[1])
