# Audio Player 100 days of code 
#python3 -m pip install whatever https://stackoverflow.com/questions/51373063/pip3-bad-interpreter-no-such-file-or-directory

import os #to fetch songs and directories 
from tkinter.filedialog import askdirectory #for selecting our song directory
import pygame  #for playing music 
from mutagen.id3 import ID3  #For tagging meta data to our songs 
from tkinter import *  # for UI 

root = Tk() # creates an empty window
root.minsize(300,300) # set size as 300 * 300 
