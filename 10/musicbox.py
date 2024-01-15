# Python: musicbox.py
# přehrává a ukládá do wav-souboru sekvence tónů a dvojzvuků v různých laděních
# funkce: playSeq1(seq[,tuning])                   - jednohlas
#         playSeq11(seq1,seq2[,tuning1][,tuning2]) - dvojhlas nezávislých hlasů
#         playSeq2(seq1,seq2[,tuning1][,tuning2])  - dvojhlas po dvojzvucích
#         playTone(s[,tuning])                     - jediný tón
#         playTone2(s1,s2[,tuning1][,tuning2])     - dvojzvuk
#         playFreq(freq,dt)                        - jediný tón daný frekvencí
#         playFreq2(freq1,freq2,dt)                - dvojzvuk daný frekvencemi
# s:      symbolický zápis tónu: [délka]tón[posuvka][oktáva]
#     kde délka je nejvýše jeden znak z xyz123456789 (default 1)
#           tón je   právě jeden znak z -cdefgah  (- pro pomlku)
#       posuvka je nejvýše jeden znak z +-         (default nic)
#        oktáva je nejvýše jeden znak z xyz12345     (default 1)
# seq: př. '2c2 zd2 zc2  g 2h- za zg  2f' pro půlovou a dvě osminové v dvoučárkované oktávě
#                      a čtvrťovou, půlovou, dvě osminové a půlovou v jednočárkované oktávě
# tuning: ftemp (temperované ladění), fjust (přirozené ladění), fpyth (pythagorejské ladění)
# závislost: numpy pro pole
#            scipy pro uložení wav-souboru (při saveWav=True)
#            simpleaudio nebo sounddevice pro přehrávání zvuku z numpy-pole (při playNow=True)

import numpy as np   # pro pole
import scipy         # pro uložení wav-souboru
#import simpleaudio   # pro přehrávání zvuku z numpy-pole (při playSA=True, viz funkce playArray)
import sounddevice   # pro přehrávání zvuku z numpy-pole (při playSA=False,       viz playArray)

playNow=True         # hrát hned?
saveWav=False         # uložit wav?
dispFreq=True        # vypisovat frekvence?
fa1=440              # frekvence komorního a (a1)/concert pitch [440 Hz]
semitone=2**(1/12)   # temperovaný půltón/equal-tempered semitone
fs=44100             # vzorkovací frekvence/sampling frequency [44100 Hz]
tbeat=0.20           # délka doby/beat length (základní časová jednotka) [sec]
if playNow:
  playSA=False                                         # True pro simpleaudio, False pro sounddevice
if saveWav:
  fileWav1='1voice.wav'                               # jméno wav-souboru
  fileWav2='2voices.wav'                              # jméno dvoukanálového wav-souboru
  wav=np.empty((0),dtype=np.int16)                    # pracovní numpy-pole pro wav data
  wav1=np.empty((0),dtype=np.int16)                   # numpy-pole pro 1kanálový wav-soubor
  wav2=np.empty((0,2),dtype=np.int16)                 # numpy-pole pro 2kanálový wav-soubor
# ladicí faktory sedmitónové stupnice c1-d1-e1-f1-g1-a1-h1(-c2)
fjust=np.array([1,9/8,5/4,4/3,3/2,5/3,15/8,2])        # přirozené ladění/just intonation
fpyth=np.array([1,9/8,81/64,4/3,3/2,27/16,243/128,2]) # pythagorejské ladění/pythagorean tuning
ftemp=semitone**np.array([0,2,4,5,7,9,11,12])         # rovnoměrně temperované ladění/equal temperament
class cTone:                                          # datový typ pro tón
  def __init__(self,iton=0,iacc=0,ioct=1,ilen=1):     # pořadí v sedmitónové stupnici, posuvka, oktáva, délka
    self.iton=iton; self.iacc=iacc; self.ioct=ioct; self.ilen=ilen  # tone, accidental, octave, length

# Přehraje zvukové pole a/nebo přidá zvukové pole k wav-poli
def playArray(y,channels=1):
  global wav,wav2
  if playNow:
    if playSA:        # simpleaudio přehrává poněkud nerytmicky, s menšími pomlkami mezi tóny
      obj=simpleaudio.play_buffer(audio_data=y,num_channels=channels,bytes_per_sample=2,sample_rate=fs)
      obj.wait_done()
    else:             # sounddevice přehrává spíše rytmicky, s většími pomlkami mezi tóny
      sounddevice.play(data=y,samplerate=fs)
      sounddevice.wait()
  if saveWav:         # kumulace tónů pro jednorázové uložení
    if channels==1:   wav=np.append(wav,y)            # jednokanálové pole
    elif channels==2: wav2=np.append(wav2,y,axis=0)   # dvoukanálové pole

# Konvertuje frekvenci a délku tónu na zvukové pole
def evalArray(freq,dt):
  tarr=np.linspace(0,dt,round(dt*fs),endpoint=False)    # časové vzorkování
  y=np.cos(2*np.pi*freq*tarr)*32767
  nfade=200                 # počet vzorků pro lineární nástup a útlum tónu
  y[:nfade]*=np.linspace(0,1,nfade)
  y[-nfade:]*=np.linspace(1,0,nfade)
  return y.astype(np.int16)                           # 16bitové int hodnoty

# Zpracuje tón o dané frekvenci a dané délce
def playFreq(freq,dt):
  if dispFreq: print(f'{freq:.1f}',end=' ')
  playArray(evalArray(freq,dt))

# Zpracuje dvojzvuk o daných frekvencích a dané délce
def playFreq2(freq1,freq2,dt):
  if dispFreq: print(f'{freq1:.1f}/{freq2:.1f}',end=' ')
  y1=evalArray(freq1,dt)
  y2=evalArray(freq2,dt)
  playArray(np.column_stack((y1,y2)),channels=2)

# Konvertuje proměnnou třídy cTone na frekvenci a délku tónu v předepsaném ladění
def evalFreq(tone,tuning=ftemp):
  if tone.iton<0: freq=0
  else:
    fc1=fa1/tuning[5]                           # frekvence c1
    freq=fc1*tuning[tone.iton]                  # sedmitónové ladění
    if tone.iacc!=0: freq*=semitone**tone.iacc  # temperované půltóny
    if tone.ioct!=1: freq*=2**(tone.ioct-1)     # oktávové posuny
  dt=tbeat*tone.ilen                            # délka tónu
  return (freq,dt)

# Zpracuje údaje o tónu z proměnné třídy cTone
def playcTone(tone,tuning=ftemp):
  playFreq(*evalFreq(tone,tuning))

# Zpracuje údaje o dvojzvuku z proměnných třídy cTone
def playcTone2(tone1,tone2,tuning1=ftemp,tuning2=[]):
  if len(tuning2)==0: tuning2=tuning1
  (freq1,dt1)=evalFreq(tone1,tuning1)
  (freq2,dt2)=evalFreq(tone2,tuning2)
  playFreq2(freq1,freq2,max(dt1,dt2))

# Konvertuje řetězcový zápis tónu na proměnnou třídy cTone
def evalcTone(s):
  s=s.lower()
  ilen='xyz123456789'.find(s[0])          # délka tónu/tone length
  if ilen<0: ilen=1
  elif ilen<3: ilen=2**(ilen-3); s=s[1:]
  else: ilen=ilen-2; s=s[1:]
  iton='-cdefgah'.find(s[0])              # výška tónu/tone pitch
  if iton<0: return cTone(0,0,0,2)        # error: chybný znak
  elif iton==0: iton=-1; s=s[1:]          # pomlka
  else: iton-=1; s=s[1:]
  if len(s):
    iacc='-+'.find(s[0])                  # posuvka/accidental
    if iacc<0: iacc=0
    elif iacc==0: iacc=-1; s=s[1:]
    else: iacc=1; s=s[1:]
  else: iacc=0
  if len(s):
    ioct='xyz12345'.find(s[0])            # oktáva/octave
    if ioct<0: ioct=1
    else: ioct-=2
  else: ioct=1
  return cTone(iton,iacc,ioct,ilen)

# Zpracuje řetězcový zápis tónu v předepsaném ladění
def playTone(s,tuning=ftemp):
  playcTone(evalcTone(s),tuning)

# Zpracuje řetězcový zápis dvojzvuku v předepsaných laděních
def playTone2(s1,s2,tuning1=ftemp,tuning2=[]):
  tone1=evalcTone(s1)
  tone2=evalcTone(s2)
  playcTone2(tone1,tone2,tuning1,tuning2)

# Zpracuje sekvenci tónů
def playSeq(seq,tuning=ftemp):
  global wav
  if saveWav:
    wav=np.empty((0),dtype=np.int16)    # numpy-pole pro data pro wav-soubor
  for s in seq.split():
    playTone(s,tuning)

# Zpracuje sekvenci tónů z řetězce a uloží jednohlas
def playSeq1(seq,tuning=ftemp):
  global wav1
  playSeq(seq,tuning)
  if dispFreq: print()
  if saveWav:                           # přidání sekvence k wav1
    wav1=np.append(wav1,wav)

# Zpracuje sekvence tónů ze dvou řetězců a uloží dvojhlas (dva nezávislé hlasy)
def playSeq11(seq1,seq2,tuning1=ftemp,tuning2=[]):
  global wav2,playNow
  if len(tuning2)==0: tuning2=tuning1
  playNow=False                         # nezávislé hlasy nelze přehrávat po dvojzvucích
  playSeq(seq1,tuning1)                 # první kanál do wav
  if dispFreq: print()
  if saveWav: wav2a=wav.copy()          # zálohování prvního kanálu
  playSeq(seq2,tuning2)                 # druhý kanál do wav
  if dispFreq: print()
  if saveWav: wav2b=wav.copy()          # zálohování druhého kanálu
  if saveWav:                           # sloučení kanálů a přidání sekvence k wav2
    wav2=np.append(wav2,np.column_stack((wav2a,wav2b)),axis=0)

# Zpracuje sekvenci dvojzvuků z řetězců a uloží dvojhlas (po dvojzvucích)
def playSeq2(seq1,seq2,tuning1=ftemp,tuning2=[]):
  list2=seq2.split()
  for n,s1 in enumerate(seq1.split()):
    s2=list2[n]
    playTone2(s1,s2,tuning1,tuning2)
  if dispFreq: print()

### Syntonické/pythagorejské koma na 440/220 Hz, přírodní/vlčí kvinta/tercie
# playFreq2(440,440*81/80,4)
# playFreq2(220,220*81/80,4)
# playFreq2(440,440*3**12/2**19,4)
# playFreq2(220,220*3**12/2**19,4)
# tbeat=0.50
# playTone2('8c','8g',fjust)
# playTone2('8d','8a',fjust)
# playTone2('8e','8g',fjust)
# playTone2('8d','8f',fjust)
# if dispFreq: print()

### Stupnice C dur, D dur a E dur v různých laděních
# tbeat=0.30
# playSeq1('c d e f g a h 2c2  -  d e f+ g a h c+2 2d2  -  e f+ g+ a h c+2 d+2 2e2  -',fjust)
# playSeq1('c d e f g a h 2c2  -  d e f+ g a h c+2 2d2  -  e f+ g+ a h c+2 d+2 2e2  -',fpyth)
# playSeq1('c d e f g a h 2c2  -  d e f+ g a h c+2 2d2  -  e f+ g+ a h c+2 d+2 2e2  -',ftemp)
### Stupnice C dur paralelně v přirozeném a rovnoměrně temperovaném ladění
# tbeat=2.00
# playSeq2('c d e f g a h 2c2','c d e f g a h 2c2',fjust,ftemp)

### Test ze záhlaví
# tbeat=0.50
# playSeq1('2c2 zd2 zc2  g 2h- za zg  2f')
### Ovčáci čtveráci
# tbeat=0.20
# playSeq1('2c 2e  2g 2-  2c 2e  2g 2-  e e d e  2f 2d  e e d e  2f 2d  2e 2d  4c')
### Koleda: Nesem vám noviny
#tbeat=0.20
#playSeq1('c2 g c2 a d2 h-  c2 g c2 a d2 h-  c2 g a c2 g a  6f  ' +
#          'c2 g c2 a d2 h-  c2 g c2 a d2 h-  c2 g a c2 g a  6f  ' +
#          '2f a f a c2      2f a f g c       2f a f a c2    2f a f g c  c2 g a c2 g a  6f')
### Koleda: Veselé vánoční hody
#tbeat=0.20
#playSeq1('d f+ a a  2a d2 h  2a 2g  4f+  d f+ a a  2a d2 h  2a 2g  4f+  ' +
#          'a a g f+  e f+ g e  a a g f+  e f+ g e  2f+ 2e  4d  ' +
#          'a a g f+  e f+ g e  a a g f+  e f+ g e  2f+ 2e  4d  ')


#Kde domov můj - Smetana
tbeat = 0.40  # Adjust the tempo as needed
playSeq1('2a 1h 1a 1e 2g 1f+ 1e 2d ')


#The Unforgiven - Metallica
tbeat = 0.30
playSeq1('2h 1a 1e 1h 1a 1e 1h 1a 1e 1h 1a 1e 1h 1a 1e 2h 1a 1e')

#Nothing Else Matters - Metallica
tbeat = 0.5
playSeq1('2e 2g 2h 2e 2h 2g 2e 2g 2h 2e 2h 2g 2e 2g 2h 2e 2h 2g 2e 2g 2h 2e 2h 2g 6h 1h 1e 8e 2h 2c 2h 2a 2h 1a 1g 2e 2e 2c 2e f+ 1e 2e 2c')

### Schumann: Chopin
"""
tbeat=0.20
voice1 ='8-                        2e-2 -   e-2  3e-2        f2  3e-2     -  2e-2   2f2      2g-2   2f2   2e-2 2d-2 2e-2 2c2     '
voice2 ='a-y e-z a-z c e- a- c2 a- e- c a-z e-z  g-y e-z g-z h-z e- g- h- g- e- h-z g-z e-z  fy e-z fz az c e- f e- c az fz e-z  '
voice1+='4d-2          4-          2f2  -   f2  3f2        g2 3f2    -  2f2 2g2     2a-2   2g2    2f2  2e-2   yg2 2f2    2d-2    3c2         5-            2e-2 2c2  '
voice2+='h-y fz h-z d- f h- d-2 h- f d- h-z fz  a-y fz a-z c f a- c2 a- f c a-z fz  fy d-z fz a-z d- f gy h-y y-  e-z gz h-z e-  a-y e-z a-z c e- a- c2 a- e- c a-z e-z  '
voice1+='4h-          4a          2h-    2c2     8d-2                        2f2    2d-2  2c2 d-3 c3 h2 h-2 g2 e2 c2 e-2 d-2 c2 h-  '
voice2+='gy d-z ez az h-z d- e d- h-z gz ez d-z  g-y d-z ez g-z h-z e fy d-z fz h-z d- f  2ey cz  ez gz h-z c  e  g  e-  d-  c  h-z  '
voice1+='6a-              2-   2g    2a-    8a                       2g+   2a      6h-                    4e-2       2h      4c2         3-  '
voice2+='fy cz fz a-z c f a- f c a-z fz cz  f-y ay d-z gz az d- g d- az gz d-z ay  e-y h-y e-z a-z h-z d- a- g e- hz gz e-z  a-y e-z a-z c e- 2a-  '
playSeq11(voice1,voice2)"""

# Uloží wav-soubor
if saveWav:
  if wav1.size: scipy.io.wavfile.write(filename=fileWav1,rate=fs,data=wav1)  # jednokanálový soubor
  if wav2.size: scipy.io.wavfile.write(filename=fileWav2,rate=fs,data=wav2)  # dvoukanálový soubor