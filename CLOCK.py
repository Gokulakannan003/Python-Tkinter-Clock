# version 1
"""from tkinter import *
from time import strftime

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
"""
# version 2
from customtkinter import *
from time import strftime

root = CTk()
root.title("Clock")
root.geometry("400x150")


def time():
    string = strftime('%H:%M:%S:%p')
    label.configure(text=string)
    label.after(1000, time)


frame1 = CTkFrame(root, height=100, width=350, fg_color="azure")
frame1.place(x=20, y=20)
label = CTkLabel(frame1, font=("ds-digital", 55), bg_color="black", fg_color="azure")
label.place(x=20, y=20)
time()
root.mainloop()
