# Python: testScale.py
# přehraje a uloží do wav-souboru stupnici C dur v různých laděních
# ladění: temperované (ftemp), přirozené (fjust), pythagorejské (fpyth)

import numpy as np   # pro pole
import scipy         # pro uložení wav-souboru
#import simpleaudio   # pro přehrávání zvuku z numpy-pole (při playSA=True, viz funkce playArray)
import sounddevice   # pro přehrávání zvuku z numpy-pole (při playSA=False,       viz playArray)

playNow=True         # hrát hned?
saveWav=True         # uložit wav?
dispFreq=True        # vypisovat frekvence?
fa1=440              # frekvence komorního a (a1)/concert pitch [440 Hz]
semitone=2**(1/12)   # temperovaný půltón/equal-tempered semitone
fs=44100             # vzorkovací frekvence/sampling frequency [44100 Hz]
tbeat=0.50           # délka doby/beat length (základní časová jednotka) [sec]
if playNow:
  playSA=False                                         # True pro simpleaudio, False pro sounddevice
if saveWav:
  fileWav='scale.wav'                                 # jméno wav-souboru
  wav=np.empty((0),dtype=np.int16)                    # numpy-pole pro uložení do wav-souboru
# ladicí faktory sedmitónové stupnice c1-d1-e1-f1-g1-a1-h1(-c2)
fjust=np.array([1,9/8,5/4,4/3,3/2,5/3,15/8,2])        # přirozené ladění/just intonation
fpyth=np.array([1,9/8,81/64,4/3,3/2,27/16,243/128,2]) # pythagorejské ladění/pythagorean tuning
ftemp=semitone**np.array([0,2,4,5,7,9,11,12])         # rovnoměrně temperované ladění/equal temperament

# Přehraje zvukové pole a/nebo přidá zvukové pole k wav-poli
def playArray(y,channels=1):
  global wav
  if playNow:
    if playSA:        # simpleaudio přehrává poněkud nerytmicky, s menšími pomlkami mezi tóny
      obj=simpleaudio.play_buffer(audio_data=y,num_channels=channels,bytes_per_sample=2,sample_rate=fs)
      obj.wait_done()
    else:             # sounddevice přehrává spíše rytmicky, s většími pomlkami mezi tóny
      sounddevice.play(data=y,samplerate=fs)
      sounddevice.wait()
  if saveWav:
    wav=np.append(wav,y)  # kumulace tónů pro jednorázové uložení

# Konvertuje frekvenci a délku tónu na zvukové pole
def evalArray(freq,dt):
  tarr=np.linspace(0,dt,round(dt*fs),endpoint=False)  # časové vzorkování
  y=np.cos(2*np.pi*freq*tarr)*32767
  nfade=200             # počet vzorků pro lineární nástup a útlum tónu
  y[:nfade]*=np.linspace(0,1,nfade)
  y[-nfade:]*=np.linspace(1,0,nfade)
  return y.astype(np.int16)                         # 16bitové int hodnoty

# Zpracuje tón o dané frekvenci a dané délce
def playFreq(freq,dt):
  if dispFreq: print(f'{freq:.1f}',end=' ')
  playArray(evalArray(freq,dt))

# délka 7+1 tónů stupnice
dt=tbeat*np.ones(8); dt[-1]=tbeat*2

# rovnoměrně temperované ladění
fc1=fa1/ftemp[5]          # frekvence c1
freq=fc1*ftemp            # frekvence celé stupnice
for n in range(8): playFreq(freq[n],dt[n])
if dispFreq: print()

# přirozené ladění
fc1=fa1/fjust[5]
freq=fc1*fjust
for n in range(8): playFreq(freq[n],dt[n])
if dispFreq: print()

# pythagorejské ladění
fc1=fa1/fpyth[5]
freq=fc1*fpyth
for n in range(8): playFreq(freq[n],dt[n])
if dispFreq: print()

# uloží wav-soubor
if saveWav:
  if wav.size: scipy.io.wavfile.write(filename=fileWav,rate=fs,data=wav)