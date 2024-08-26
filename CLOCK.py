from tkinter import *
from time import strftime
from tkinter.ttk import *

root = Tk()
root.title("Clock")
root.resizable(False,False)


def time():
    string = strftime('%H:%M:%S:%p')
    label.config(text=string)
    label.after(1000, time)



label = Label(root, font=("ds-digital",120), background="black", foreground="white")
label.pack(anchor="center")
time()
root.mainloop()
