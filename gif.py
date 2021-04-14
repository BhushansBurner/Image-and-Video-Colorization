# importing libraries
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count
import time as t


class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []
        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()
           

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

def timer():
    seconds = 10
    for i in range(seconds):
     #print(str(seconds-i) + " seconds remaining \n")
     ##we also need the loop to wait for 1 second between each iteration
     t.sleep(1)
    print("Time's up")
    root = tk.Tk()
    root.geometry("512x420")
    lbl = ImageLabel(root)
    lbl.destroy()

'''
root = tk.Tk()
root.geometry("512x420")
lbl = ImageLabel(root)
lbl.place(x=100,y=200)
#lbl.load("Processing.gif")
#button_exit = Button(root,text = "Start", command = lambda : [lbl.load("Processing.gif"),lbl.timer()])
#button_exit.pack()

#lbl.load("Processing.gif") # enter your file location here
root.mainloop()'''
