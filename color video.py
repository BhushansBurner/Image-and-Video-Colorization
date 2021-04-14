from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

#for displaying video
import imageio
from PIL import Image, ImageTk
import os, sys


root=Tk()
root.title("Video Colorization")
root.geometry("1350x670")
root.configure(bg="#FDF4DC")
fn1 = "firstVideo"
name ="xyz"
fn2 = "secondVideo"
fname = "a"
ext = "b"
#Browse Files
def browseFiles():
    global name,fn1,fn2,fname,ext
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", 
                    filetypes = (("Text files","*.txt*"), ("all files", "*.*")))
    name = os.path.basename(filename)
    (fname,ext) =os.path.splitext(name)
    path = os.path.dirname(r'C:\Users\Bhushan\Desktop\PP\\')
    fn1 = os.path.join(path, fname + '.mp4')
    fn2 = os.path.join(path, fname + '.avi')
    print(fn1)
    print(fn2)
    

#playing Video
size=(450,275)
#1st video
f1=Frame()
l1 = Label(f1)
l1.pack()
f1.place(x=160,y=250)
    
def s1():
    
    video_name = r'%s' % fn1  #Image-path
    video = imageio.get_reader(video_name)
    delay = int(1000 / video.get_meta_data()['fps'])
    stream(video,delay)
def stream(video,delay):    
    try:
        image = video.get_next_data()
        frame_image = Image.fromarray(image)
        frame_image = frame_image.resize(size)
        frame_image=ImageTk.PhotoImage(frame_image)
        l1.config(image=frame_image)
        l1.image = frame_image
        l1.after(delay, lambda: stream(video,delay))
    except:
        video.close()
#2nd video
f2=Frame()
l2 = Label(f2)
l2.pack()
f2.place(x=725,y=250)
       

########### Main Program ############

def s2():
     
    video_name2 = r'%s' % fn2  #  #Image-path
    video2 = imageio.get_reader(video_name2)
    delay2 = int(1000 / video2.get_meta_data()['fps'])
    stream2(video2,delay2)
    

def stream2(video2,delay2):
    try:
        image = video2.get_next_data()
        frame_image = Image.fromarray(image)
        frame_image = frame_image.resize(size)
        frame_image=ImageTk.PhotoImage(frame_image)
        l2.config(image=frame_image)
        l2.image = frame_image
        l2.after(delay2, lambda: stream2(video2,delay2))
    except:
        video2.close()
#clear
import sys
import os
def restart():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)



#gif
from gif import *
import time as t
import threading
lbl = ImageLabel(root)
#lbl.load("Processing.gif")

def processing():
    
    lbl.place(x=550,y=300)
    if (ext!=".mp4"):
        messagebox.showerror("Colorization", "Please select video fie")
    else:
        lbl.load("Processing.gif")
        timer = threading.Timer(10.0,front)
        timer.start()
def front():        
    lbl.destroy()
    s1()
    s2()
    
    
# Play Button
btn_play=Button(root, text="Start",command=lambda:[processing()],width=10,height=2,bg="#fdbb2d",font=("Courier", 18,"bold"))
btn_play.place(x=500,y=580)


# Exit Button
btn_exit=Button(root, text="Exit",command=root.destroy, width=10,height=2,bg="#fdbb2d",font=("Courier", 18,"bold"))
btn_exit.place(x=700,y=580)

#Browse File
btn_explore = Button(root,text = "Browse", command = browseFiles,width=10,height=1,bg="#fdbb2d",font=("Courier", 18,"bold"))
btn_explore.place(x=700,y=130)

# Label
label = Label(root, text="Select Video")
label.config(font=("Courier", 18,"bold"))
label.place(x=500,y=135)
# Label Original Video
label = Label(root, text="Original Video")
label.config(font=("Courier", 18,"bold"))
label.place(x=300,y=215)
# Label Colorized Video
label = Label(root, text="Colorized Video")
label.config(font=("Courier", 18,"bold"))
label.place(x=850,y=215)

label = Label(root, text="VIDEO COLORIZATION")
label.config(font=("Century Gothic", 40,"bold"))
label.place(x=390,y=30)

### Entry Box
##video_link=Entry(root,width=30,bd=5)
##video_link.place(x=200,y=50)


root.mainloop()
