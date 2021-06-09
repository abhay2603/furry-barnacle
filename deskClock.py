import tkinter
from tkinter.ttk import *

from time import strftime

root=tkinter.Tk()

root.title('Digital clock')

def clock():
    tick =strftime('%H:%M:%S %p')

    label.config(text=tick)

    label.after(1000, clock)

label= Label(root, font =('sans', 80), background= 'Black', foreground='blue')

label.pack(anchor= 'center')

clock()
root.mainloop()
