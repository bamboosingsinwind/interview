from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Calendar")
root.geometry("500x300")

# 创建一个Frame
frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

# 创建一个Label
label = ttk.Label(frame, text="Simple Calendar")
label.grid(column=1, row=1, sticky=(W, E))

# 创建一个Entry
entry = ttk.Entry(frame, width=12)
entry.grid(column=2, row=1, sticky=(W, E))

# 创建一个Button
button = ttk.Button(frame, text="OK", command=root.destroy)
button.grid(column=3, row=1, sticky=(W, E))

# 显示日历
def show_calendar():
    year = int(entry.get())
    month = int(entry.get())
    cal = calendar.month(year, month)
    label['text'] = cal

# 添加事件
entry.bind("<Return>", show_calendar)

root.mainloop()