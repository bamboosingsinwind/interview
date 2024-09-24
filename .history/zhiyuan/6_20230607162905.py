from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time

class Clock(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Clock")
        self.pack(fill=BOTH, expand=1)
        self.createClock()

    def createClock(self):
        self.timeString = StringVar()
        self.timeString.set('00:00:00')
        self.timeLbl = Label(self, font=('Arial', 40, 'bold'), fg='Red',
                              textvariable=self.timeString)
        self.timeLbl.pack(anchor=CENTER)
        self.timeString.set(time.strftime("%H:%M:%S"))
        self.after(1000, self.tick)

    def tick(self):
        self.timeString.set(time.strftime("%H:%M:%S"))
        self.parent.after(1000, self.tick)

if __name__ == '__main__':
    app = Tk()
    app.geometry('400x200')
    app.mainloop()