# Audio Player 100 days of code 
#python3 -m pip install whatever https://stackoverflow.com/questions/51373063/pip3-bad-interpreter-no-such-file-or-directory

import os #to fetch songs and directories 
from tkinter.filedialog import askdirectory #for selecting our song directory
import pygame  #for playing music 
from mutagen.id3 import ID3  #For tagging meta data to our songs 
from tkinter import *  # for UI 

root = Tk() # creates an empty window
root.minsize(300,300) # set size as 300 * 300 

listofsongs = []

realnames = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=35)

def directorychooser():

    directory = askdirectory()
    os.chdir(directory)
    #Loop over all the files in that directory
    for file in os.listdir(directory):
        # only add them if they end with .mp3
        if file.endswith(".mp3"):
            realdir = os.path.realpath(file)
	# load the meta data of that song into audio variable. (A dictionary)
            audio = ID3(realdir)
	# TIT2 refers to the TITLE of the song, So let’s append that to realnames
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(file)
    
    # initialize pygame
    pygame.mixer.init()
    # load the first song
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()


def updatelabel():
    global index # If you do not use global, new index variable will be defined
    global songname
    v.set(realnames[index]) # set our StringVar to the real name 
    #return songname

def nextsong(event):
    # get index from globals
    global index 
    # increment index
    index += 1 
    # get the next song from listofsongs
    pygame.mixer.music.load(listofsongs[index])
    # play it away
    pygame.mixer.music.play()
    # do not forget to update the label !
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    #return songname


label = Label(root,text='Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()

#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()
#listofsongs.reverse()


nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()

previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()

stopbutton = Button(root,text='Stop Music')
stopbutton.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()

root.mainloop()



