import speech_recognition as sr
from gtts import gTTS
import pyglet,os,time,datetime,sys,random


def listen():
    print('Speak')
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    text=r.recognize_google(audio)
    return text

def speak(text):
    try:
        f=gTTS(text=text,lang='en')
        fname='tmp.mp3'
        f.save(fname)
        music=pyglet.media.load(fname,streaming=False)
        print(text)
        music.play()
        time.sleep(music.duration)
        os.remove(fname)
    except:
        print(text)

a=listen()
print(a)
