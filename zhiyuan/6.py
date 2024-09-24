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
        self.timeLbl = Label(self, font=('Arial', 40, 'bold'), fg='Red', bg='#00aaff', anchor='w', textvariable=self.timeString)
        self.timeLbl.pack(anchor='center')
        self.timeLbl.bind("<Enter>", self.onEnter)
        self.timeLbl.bind("<Leave>", self.onLeave)
        self.startClock()

    def startClock(self):
        self.after(1000, self.tick)

    def tick(self):
        self.timeString.set(time.strftime("%H:%M:%S"))
        self.parent.after(1000, self.tick)

    def onEnter(self, event=None):
        self.timeLbl.config(bg='#00aaff')

    def onLeave(self, event=None):
        self.timeLbl.config(bg='#00aaff')

def main():
    root = Tk()
    root.geometry("400x400")
    app = Clock(root)
    root.mainloop()

if __name__ == '__main__':
    main()