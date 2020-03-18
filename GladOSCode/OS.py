import atexit
import winsound as glados
import speech_recognition as spRec

from pygame import mixer
import time

import MathCore

from pygame.pypm import TRUE
import sys as system
import os


absoluteFolder = os.path.dirname(os.path.abspath(__file__))


configFile = absoluteFolder + '\config.txt';

print(open(configFile).readlines()[:2][1])
print(open(configFile).readlines()[:7][5])
glados.PlaySound("HelloAndWelcome", glados.SND_FILENAME)



readPath1 = open(configFile).readlines()[:2][1]
readPath2 = open(configFile).readlines()[:7][5]


path1 = readPath1.replace("\n", "");
path2 = readPath2.replace("\n", "");



repeat = TRUE


def closeGlados():
    glados.PlaySound("Goodnight", glados.SND_FILENAME)


Rec = spRec.Recognizer()
with spRec.Microphone() as audioManager:
    glados.PlaySound("Starting", glados.SND_FILENAME)
    while repeat:

        print('Aperture Load')
        print('Speak Anything: ')
        glados.PlaySound("NewQuestion", glados.SND_FILENAME)
        listener = Rec.listen(audioManager)

        text = Rec.recognize_google(listener)
        print('{}'.format(text))

        if 'open app 1' in text:
            os.startfile(path1)
            glados.PlaySound("Opening", glados.SND_FILENAME)
        if 'open app to' in text:
            os.startfile(path2)
            glados.PlaySound("Opening", glados.SND_FILENAME)
        if 'hey' in text:
            glados.PlaySound("Hey", glados.SND_FILENAME)

        if 'hi' in text:
            glados.PlaySound("Hey", glados.SND_FILENAME)
        if "how's it going" in text:
            glados.PlaySound("Hey", glados.SND_FILENAME)
        if 'hello' in text:
            glados.PlaySound("Hey", glados.SND_FILENAME)
        if 'hola' in text:
            glados.PlaySound("Hey", glados.SND_FILENAME)
        if 'greetings' in text:
            glados.PlaySound("Hey", glados.SND_FILENAME)
        if 'are you' in text:
            glados.PlaySound("Introduce", glados.SND_FILENAME)
        if 'is the date' in text:
            glados.PlaySound("Time", glados.SND_FILENAME)
            mixer.init()
            mixer.music.load('currentTime.mp3')
            mixer.music.play()
            time.sleep(5)
        if 'is the day' in text:
            glados.PlaySound("Time", glados.SND_FILENAME)
            mixer.init()
            mixer.music.load('currentTime.mp3')
            mixer.music.play()
            time.sleep(5)
        if 'is today' in text:
            glados.PlaySound("Time", glados.SND_FILENAME)
            mixer.init()
            mixer.music.load('currentTime.mp3')
            mixer.music.play()
            time.sleep(5)
        if "what's today's date" in text:
            glados.PlaySound("Time", glados.SND_FILENAME)
            mixer.init()
            mixer.music.load('currentTime.mp3')
            mixer.music.play()
            time.sleep(5)

        if '+' in text:
            glados.PlaySound("Math", glados.SND_FILENAME)
            MathCore.DoMath(text)
        elif '-' in text:
            glados.PlaySound("Math", glados.SND_FILENAME)
            MathCore.DoMath(text)
        elif '*' in text:
            glados.PlaySound("Math", glados.SND_FILENAME)
            MathCore.DoMath(text)
        elif '/' in text:
            glados.PlaySound("Math", glados.SND_FILENAME)
            MathCore.DoMath(text)
        if 'exit' in text:
            closeGlados()
            system.exit()
        if 'bye' in text:
            closeGlados()
            system.exit()
        if 'is the weather' in text:
            mixer.init()
            mixer.music.load('temp.mp3')
            mixer.music.play()
            time.sleep(5)
        if 'forecast' in text:
            mixer.init()
            mixer.music.load('temp.mp3')
            mixer.music.play()
            time.sleep(5)
        if "what's your" in text:
            glados.PlaySound("Introduce", glados.SND_FILENAME)


