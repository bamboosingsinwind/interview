from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Clock")
root.geometry("300x300")

def time():
    string = time.strftime("%H:%M:%S")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("Arial", 80), background="black", foreground="cyan")
label.pack(anchor=CENTER, expand=YES, padx=20, pady=20)
time()

mainloop()