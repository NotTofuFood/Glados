import os
import time
import random
from tkinter import *




absoluteFolder = os.path.dirname(os.path.abspath(__file__))


configFile = absoluteFolder + '\config.txt';

appToKill1 =  open(configFile).readlines()[:19][8]
appToKill2 =  open(configFile).readlines()[:19][11]
appToKill3 =  open(configFile).readlines()[:19][14]





def closeApp():
    time.sleep(random.randint(20, 150))

    if random.randint(0, 3) == 1:
        os.system('TASKKILL /F /IM ' + appToKill1)

    if random.randint(0, 3) == 2:
        os.system('TASKKILL /F /IM ' + appToKill2)

    if random.randint(0, 3) == 3:
        os.system('TASKKILL /F /IM ' + appToKill3)


while True:
    closeApp()


def toxin() :
    time.sleep(random.randint(70,150))

    nueroWindow = Tk()
    nueroWindow.title("Flooding Chambers with Neurotoxin")
    nueroWindow.configure(bg='#008000')
    nueroWindow.geometry('900x900')

    nueroWindow1 = Tk()
    nueroWindow1.title("Flooding Chambers with Neurotoxin")
    nueroWindow1.configure(bg='#008000')
    nueroWindow1.geometry('900x900+400+700')


    nueroWindow2 = Tk()
    nueroWindow2.title("Flooding Chambers with Neurotoxin")
    nueroWindow2.configure(bg='#008000')
    nueroWindow2.geometry('900x900+100+500')


    nueroWindow3 = Tk()
    nueroWindow3.title("Flooding Chambers with Neurotoxin")
    nueroWindow3.configure(bg='#008000')
    nueroWindow3.geometry('900x900+600+100')



    nueroWindow.mainloop()
    nueroWindow1.mainloop()
    nueroWindow2.mainloop()
    nueroWindow3.mainloop()

while True:
    toxin()
