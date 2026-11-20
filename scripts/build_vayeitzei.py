from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.colors import HexColor
from pypdf import PdfReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('DejaVu','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVu-Bold','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
pdfmetrics.registerFontFamily('DejaVu',normal='DejaVu',bold='DejaVu-Bold')
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'weeks/2026-11-21-vayeitzei/content.json').read_text())
P=str(ROOT/'weeks/2026-11-21-vayeitzei/Vayeitzei_Who_Am_I.pdf')
c=canvas.Canvas(P,pagesize=(612,792))
c.setTitle('Parshas Vayeitzei - Who Am I? | Family Game')
ink=HexColor('#202020'); gray=HexColor('#606060')
def para(text,x,top,w,size=10.5,leading=13,bold=False):
 s=ParagraphStyle('p',fontName='DejaVu-Bold' if bold else 'DejaVu',fontSize=size,leading=leading,textColor=ink)
 p=Paragraph(text,s); ww,h=p.wrap(w,1000);p.drawOn(c,x,top-h);return h
def header(sub):
 c.setFillColor(ink); c.setFont('DejaVu-Bold',26);c.drawString(36,746,'WHO AM I?')
 c.setFont('DejaVu-Bold',12);c.drawRightString(576,750,'PARSHAS VAYEITZEI')
 c.setFont('DejaVu',10);c.drawRightString(576,734,'Family game  |  November 21, 2026')
 c.setStrokeColor(ink);c.line(36,721,576,721)
 para(sub,36,709,540,10.5,14)
def footer(n):
 c.setStrokeColor(HexColor('#cccccc'));c.line(36,38,576,38)
 c.setFillColor(gray);c.setFont('DejaVu',8);c.drawString(36,25,'VAYEITZEI  /  FAMILY PARSHA GAME');c.drawRightString(576,25,f'{n} / 2')
qs=data['questions']
header('Read one clue, then pause. The clues get clearer as you go. Let the child whose turn it is<br/>guess first. Easy answers are familiar, but listen carefully! Answers are on the back.')
for col,(label,note) in enumerate([('EASY','Get everyone rolling'),('MEDIUM','Detective work'),('HARD','Extra challenge')]):
 x=36+col*184
 c.setFillColor(HexColor('#eeeeee'));c.rect(x,632,172,30,fill=1,stroke=0)
 para(label,x+8,656,156,11,13,True);para(note,x+8,643,156,8,10)
 for row in range(5):
  idx=col*5+row;title,clues=qs[idx];top=619-row*113
  para(f'{idx+1}. {title}',x+2,top,168,11,13,True)
  text='<br/>'.join(f'{i+1}) {clue}' for i,clue in enumerate(clues))
  h=para(text,x+2,top-19,168,10,12)
  assert h<=88,(idx,h)
  if row<4:
   c.setStrokeColor(HexColor('#dddddd'));c.line(x,top-103,x+172,top-103)
footer(1);c.showPage()
header('BONUS ROUNDS &amp; PARENT ANSWER KEY<br/>Keep this side facing the grown-up until the guessing round is over.')
def section(title,top):
 c.setFillColor(HexColor('#eeeeee'));c.rect(36,top-23,540,25,fill=1,stroke=0);para(title,45,top-3,522,12,15,True)
section('CATCH THE GROWN-UP',655)
para('Say: "If I make a mistake, shout STOP and fix it!"',44,620,524,11,15)
lines=data['silly_round']
y=594
for a,b in lines:
 h=para(f'\u2022 {a} <font color="#606060">({b})</font>',44,y,524,11,15);y-=h+9
para('<b>Switch roles:</b> Each child invents a wrong version for you to catch.',44,y-2,524,11,15)
section('ACT IT OUT - NO TALKING!',451)
para('Whisper a scene to the actor. Everyone else guesses:',44,416,524,11,15)
para('1. Yaakov waking up amazed after his dream.<br/>2. A shepherd trying to move the heavy stone.<br/>3. Rachel leading thirsty sheep to the well.<br/>4. Yaakov caring for his flock on a very hot day.',44,391,524,11,19)
section('ANSWER KEY',293)
answers=data['answers']
for col in range(3):
 for row in range(5):
  idx=col*5+row;para(f'<b>{idx+1}.</b> {answers[idx]}',44+col*181,256-row*24,174,9.5,12)
para('<b>After Shabbos:</b> Which clues were too easy, too hard, or got the biggest laughs?<br/>We\'ll use your feedback to tune next week\'s game.',44,113,524,10,14)
para('Source: Bereishis 28:10-32:3. Calendar: Hebcal, Vayetzei, November 21, 2026.',44,64,524,8,10)
footer(2);c.save()
r=PdfReader(P);assert len(r.pages)==2
print(P, 'pages:',len(r.pages))
