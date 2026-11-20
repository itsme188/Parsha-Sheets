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
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
P=str(ROOT/'weeks/2026-11-14-toldos/Toldos_Who_Am_I.pdf')
c=canvas.Canvas(P,pagesize=(612,792))
c.setTitle('Parshas Toldos - Who Am I? | Family Game')
ink=HexColor('#202020'); gray=HexColor('#606060')
def para(text,x,top,w,size=10.5,leading=13,bold=False):
 s=ParagraphStyle('p',fontName='DejaVu-Bold' if bold else 'DejaVu',fontSize=size,leading=leading,textColor=ink)
 p=Paragraph(text,s); ww,h=p.wrap(w,1000);p.drawOn(c,x,top-h);return h
def header(sub):
 c.setFillColor(ink); c.setFont('DejaVu-Bold',26);c.drawString(36,746,'WHO AM I?')
 c.setFont('DejaVu-Bold',12);c.drawRightString(576,750,'PARSHAS TOLDOS')
 c.setFont('DejaVu',10);c.drawRightString(576,734,'Family game  |  November 14, 2026')
 c.setStrokeColor(ink);c.line(36,721,576,721)
 para(sub,36,709,540,10.5,14)
def footer(n):
 c.setStrokeColor(HexColor('#cccccc'));c.line(36,38,576,38)
 c.setFillColor(gray);c.setFont('DejaVu',8);c.drawString(36,25,'TOLDOS  /  FAMILY PARSHA GAME');c.drawRightString(576,25,f'{n} / 2')
qs=[
('Who am I?',['I have a twin brother.','I like the fields and hunting.','I am hairy. My brother is Yaakov.']),
('Who am I?',['I have a twin brother, too!','At birth, I held his heel.','My name starts with "Y."']),
('What am I?',['Eat me with a spoon.','I am red and made with lentils.','Hungry Esav wanted some of me from Yaakov.']),
('Who am I?',['I am the twins\' mother.','I made delicious food for my husband, Yitzchak.','I helped Yaakov get ready for the bracha.']),
('What am I?',['Dig down to make me.','People get water from me.','Yitzchak\'s servants dug me. No faucet needed!']),
('Who am I?',['My father is Avraham.','In my old age, I could not see.','I heard Yaakov\'s voice, but the hands felt like Esav\'s.']),
('What am I?',['I am special and connected to being the oldest son.','Esav did not value me.','He sold me to Yaakov for food.']),
('What are we?',['We came from animals.','Rivkah put us on Yaakov\'s hands and neck.','We made smooth skin feel hairy.']),
('What are we?',['We belonged to the older brother.','The younger brother wore us to see his father.','Rivkah kept us in the house.']),
('Who am I?',['My sister is Rivkah.','I live where Yaakov is sent at the end of the parsha.','I am Yaakov\'s uncle.']),
('What am I?',['I am a number connected to Yitzchak\'s farming.','Hashem blessed his harvest.','"Me\'ah she\'arim" means this many times as much.']),
('What am I?',['I am a well with a name.','Earlier wells caused fights. Nobody fought over me.','My name means there is room: "Hashem made room for us."']),
('Who am I?',['I am a king.','I tell Yitzchak to leave because he is so powerful.','Later, I come to make a peace agreement with him.']),
('What am I?',['I am part of a bracha.','Find me outdoors early in the morning.','I am moisture from heaven: "tal hashamayim."']),
('Where am I?',['Rivkah\'s brother lives here.','Yaakov is sent here to stay with family and find a wife.','My name is Charan! (Guess before this clue.)'])]
header('Read one clue at a time and pause for guesses. Give the child whose turn it is first dibs.<br/>Easy for younger children; medium and hard for older children. Both can try any level! Answers are on the back.')
for col,(label,note) in enumerate([('EASY','Get everyone rolling'),('MEDIUM','Detective work'),('HARD','Extra challenge')]):
 x=36+col*184
 c.setFillColor(HexColor('#eeeeee'));c.rect(x,632,172,30,fill=1,stroke=0)
 para(label,x+8,656,156,11,13,True);para(note,x+8,643,156,8,10)
 for row in range(5):
  idx=col*5+row;title,clues=qs[idx];top=619-row*113
  para(f'{idx+1}. {title}',x+2,top,168,11,13,True)
  text='<br/>'.join(f'{i+1}) {clue}' for i,clue in enumerate(clues))
  h=para(text,x+2,top-19,168,10.5,13)
  assert h<=88,(idx,h)
  if row<4:
   c.setStrokeColor(HexColor('#dddddd'));c.line(x,top-103,x+172,top-103)
footer(1);c.showPage()
header('BONUS ROUNDS &amp; PARENT ANSWER KEY<br/>Keep this side facing the grown-up until the guessing round is over.')
def section(title,top):
 c.setFillColor(HexColor('#eeeeee'));c.rect(36,top-23,540,25,fill=1,stroke=0);para(title,45,top-3,522,12,15,True)
section('CATCH THE GROWN-UP',655)
para('Say: "If I make a mistake, shout STOP and fix it!"',44,620,524,11,15)
lines=[('Esav came home hungry and asked Yaakov for a slice of pizza.','Red lentil stew.'),('Yaakov was born holding his brother\'s nose.','His heel.'),('Rivkah put fluffy winter mittens on Yaakov to make him hairy.','Goat skins.'),('Yitzchak\'s servants dug deep and found lemonade.','Water.')]
y=594
for a,b in lines:
 h=para(f'\u2022 {a} <font color="#606060">({b})</font>',44,y,524,11,15);y-=h+9
para('<b>Switch roles:</b> Each child invents a wrong version for you to catch.',44,y-2,524,11,15)
section('ACT IT OUT - NO TALKING!',451)
para('Whisper a scene to the actor. Everyone else guesses:',44,416,524,11,15)
para('1. Esav coming home very hungry.<br/>2. Yaakov stirring a pot.<br/>3. A servant digging a well - and finally finding water!<br/>4. Yitzchak feeling someone\'s hands to work out who is there.',44,391,524,11,19)
section('ANSWER KEY',293)
answers=['Esav','Yaakov','Red lentil stew','Rivkah','A well','Yitzchak','The bechorah (birthright)','Goat skins','Esav\'s clothes','Lavan','One hundred / a hundredfold','Rechovos','Avimelech','Dew','Charan']
for col in range(3):
 for row in range(5):
  idx=col*5+row;para(f'<b>{idx+1}.</b> {answers[idx]}',44+col*181,256-row*24,174,10.5,13)
para('<b>After Shabbos:</b> Which clues were too easy, too hard, or got the biggest laughs?<br/>We\'ll use your feedback to tune next week\'s game.',44,113,524,10,14)
para('Source: Bereishis 25:19-28:9. Calendar: Hebcal, Toldot, November 14, 2026.',44,64,524,8,10)
footer(2);c.save()
r=PdfReader(P);assert len(r.pages)==2
print(P, 'pages:',len(r.pages))
