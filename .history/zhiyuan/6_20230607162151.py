from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time

class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock")
        self.root.geometry("300x300")
        self.root.resizable(False, False)
        self.root.config(bg="white")

        self.time_label = Label(self.root, font=("Arial", 40), fg="black", bg="white", text="00:00:00")
        self.time_label.pack(anchor=CENTER)

        self.date_label = Label(self.root, font=("Arial", 30), fg="black", bg="white", text="")
        self.date_label.pack(anchor=CENTER)

        self.time()

    def time(self):
        self.time_str = time.strftime("%H:%M:%S")
        self.time_label.config(text=self.time_str)
        self.time_label.after(1000, self.time)

        self.date_str = time.strftime("%Y-%m-%d")
        self.date_label.config(text=self.date_str)
        self.date_label.after(1000, self.date)

if __name__ == "__main__":
    root = Tk()
    Clock(root)
    root.mainloop()