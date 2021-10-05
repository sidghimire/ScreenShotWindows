import pyautogui
import tkinter as tk
from PIL import ImageTk, Image
import time

root = tk.Tk()
root.title("ScreenShot")
root.resizable(False,False)
root.geometry("300x30")
def takeFullScreen():
    im=Screenshot.grab()
    im.save("Pew.jpg")

def screenshotArea():
    root.withdraw()
    time.sleep(0.5)
    im1 = pyautogui.screenshot()
    
    # Create a toplevel window
    top = tk.Toplevel(root)
    top.attributes('-fullscreen', True)
    im1 = ImageTk.PhotoImage(im1)

    # Add the image in the label widget
    image1 = tk.Label(top, image=im1)
    image1.image = im1
    image1.place(x=0, y=0)
    root.deiconify()
    
    
    
button1=tk.Button(root,text="Full Screen",command=takeFullScreen)
button2=tk.Button(root,text="Select Area",command=screenshotArea)

button1.pack(side= tk.LEFT)
button2.pack(side= tk.LEFT)
root.mainloop()

