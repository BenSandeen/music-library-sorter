from Tkinter import Tk
from tkFileDialog import askdirectory

Tk().withdraw()
dirName = askdirectory()
print(dirName)
