import atexit
import winsound as glados
import speech_recognition as spRec
from gtts import gTTS

import datetime
from pygame import mixer
import os
import time

#Thx https://stackoverflow.com/questions/19080499/transparent-background-in-a-tkinter-window
#Thx https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python

import tkinter as tk
from tkinter import *

import ctypes
user32 = ctypes.windll.user32

screenWidth = user32.GetSystemMetrics(0);
screenHeight = user32.GetSystemMetrics(1);


root = tk.Tk()
# The image must be stored to Tk or it will be garbage collected.
root.image = tk.PhotoImage(file='Glados.png')
label = tk.Label(root, image=root.image, bg='white')
root.overrideredirect(True)
root.geometry('%dx%d+%d+%d' % (screenWidth, screenHeight, 0, 0))
root.lift()
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")
label.pack()
label.mainloop()