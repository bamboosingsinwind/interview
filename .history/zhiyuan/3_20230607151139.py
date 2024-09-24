# 设计一个简单的登录界面



from tkinter import *

root = Tk()
root.title("登录界面")
root.geometry("300x200")

# 定义一个函数，用于判断用户是否登录
def login():
    if login_var.get() == "admin":
        print("登录成功")
        root.destroy()
    else:
        print("登录失败")

# 定义一个登录框
login_var = StringVar()
login_var.set("admin")
login_label = Label(root, text="账号:")
login_label.grid(row=0, column=0)
login_entry = Entry(root, textvariable=login_var)
login_entry.grid(row=0, column=1)

# 定义一个密码框
password_var = StringVar()
password_label = Label(root, text="密码:")
password_label.grid(row=1, column=0)
password_entry = Entry(root, textvariable=password_var, show="*")
password_entry.grid(row=1, column=1)

# 定义一个登录按钮
login_button = Button(root, text="登录", command=login)
login_button.grid(row=2, column=1)

root.mainloop()