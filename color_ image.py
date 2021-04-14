from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

#for displaying video
import imageio
from PIL import Image, ImageTk
import os, sys
from Icolorization import *

root=Tk()
root.title("Image Colorization")
root.geometry("1350x670")
root.configure(bg="#FDF4DC")
filename = "x"
#Browse Files
def browseFiles():
    global filename
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", 
                    filetypes = (("Jpeg Files","*.jpg"), ("all files", "*.*")))


size=(450,275)

def image():
    colorized = color(filename)
    f1=Frame()
    l1 = Label(f1)
    l1.pack()
    f1.place(x=160,y=250)
    image = r'%s' % filename  #Image-path
    frame_image = Image.open(image)
    frame_image = frame_image.resize(size)
    frame_image=ImageTk.PhotoImage(frame_image)
    l1.config(image=frame_image)
    l1.image = frame_image
    f2=Frame()
    l2 = Label(f2)
    l2.pack()
    f2.place(x= 725,y=250)
    image2 = "OUTPUT.jpg" #Image-path
    frame_image2 = Image.open(image2)
    frame_image2 = frame_image2.resize(size)
    frame_image2=ImageTk.PhotoImage(frame_image2)
    l2.config(image=frame_image2)
    l2.image = frame_image2    
    



    
# Play Button
btn_play=Button(root, text="Start",command=lambda:[image()],width=10,height=2,bg="#fdbb2d",font=("Courier", 18,"bold"))
btn_play.place(x=500,y=580)

# Exit Button
btn_exit=Button(root, text="Exit",command=root.destroy, width=10,height=2,bg="#fdbb2d",font=("Courier", 18,"bold"))
btn_exit.place(x=700,y=580)

#Browse File
btn_explore = Button(root,text = "Browse", command = browseFiles,width=10,height=1,bg="#fdbb2d",font=("Courier", 18,"bold"))
btn_explore.place(x=700,y=130)

# Label
label = Label(root, text="Select Image")
label.config(font=("Courier", 18,"bold"))
label.place(x=500,y=135)
# Label Original Image
label = Label(root, text="Original Image")
label.config(font=("Courier", 18,"bold"))
label.place(x=300,y=215)
# Label Colorized Image
label = Label(root, text="Colorized Image")
label.config(font=("Courier", 18,"bold"))
label.place(x=850,y=215)
# Label Project Name
label = Label(root, text="IMAGE COLORIZATION")
label.config(font=("Century Gothic", 40,"bold"))
label.place(x=380,y=30)


root.mainloop()
