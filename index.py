import pyautogui
import pygame
import tkinter as tk
from PIL import ImageTk, Image
import time
from pynput import mouse
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

global initX,initY,finalX,finalY,count,im2
im2=None
top=None
initX=0
initY=0
finalX=0
finalY=0
count=0
root = tk.Tk()
root.title("ScreenShot")
root.resizable(False,False)
root.geometry("300x30")

def on_click(x,y,button,pressed):
    global count,im2,initX,initY,top
    
    if(count==1):
        initX=x
        initY=y
    elif(count==2):
        finalY=y
        finalX=x
        
        final=im2.crop((initX,initY,finalX,finalY))
        open_file=(tk.filedialog.askdirectory())
        open_file=open_file+"/image.jpg"
        final.save(open_file,'JPEG')
        top.destroy()
        
        
    else:
        print("")
    count =count + 1
def takeFullScreen():
    im=Screenshot.grab()
    im.save("Pew.jpg")

def screenshotArea():
    global count
    count=0
    root.withdraw()
    time.sleep(0.5)
    im1 = pyautogui.screenshot()
    global im2,top
    im2=im1
    # Create a toplevel window
    top = tk.Toplevel(root)
    top.attributes('-fullscreen', True)
    im1 = ImageTk.PhotoImage(im1)

    # Add the image in the label widget
    image1 = tk.Label(top, image=im1)
    image1.image = im1
    image1.place(x=0, y=0)
    root.deiconify()
    listener=mouse.Listener(on_click=on_click)
    listener.start()
    
    

  
button1=tk.Button(root,text="Full Screen",command=takeFullScreen)
button2=tk.Button(root,text="Select Area",command=screenshotArea)

button1.pack(side= tk.LEFT)
button2.pack(side= tk.LEFT)
root.mainloop()

