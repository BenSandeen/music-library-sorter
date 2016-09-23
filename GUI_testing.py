from Tkinter import Tk
from tkFileDialog import askdirectory
import os

Tk().withdraw()
dirName = askdirectory()
print(os.listdir(dirName))
