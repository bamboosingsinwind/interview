import turtle
import datetime

# 设置画笔和画布
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(1)

# 绘制时钟外框
pen.penup()
pen.goto(0, -120)
pen.pendown()
pen.color("black")
pen.pensize(3)
pen.circle(120)

# 绘制刻度
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.setheading(90)
pen.pensize(2)

for i in range(12):
    pen.forward(100)
    pen.pendown()
    pen.forward(10)
    pen.penup()
    pen.goto(0, 0)
    pen.right(30)

# 绘制时针
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.setheading(90)
pen.color("blue")
pen.pensize(4)
current_hour = datetime.datetime.now().hour % 12
hour_angle = (current_hour - 3) * 30
pen.right(hour_angle)
pen.forward(60)

# 绘制分针
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.setheading(90)
pen.color("green")
pen.pensize(3)
current_minute = datetime.datetime.now().minute
minute_angle = (current_minute - 15) * 6
pen.right(minute_angle)
pen.forward(80)

# 绘制秒针
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.setheading(90)
pen.color("red")
pen.pensize(2)
current_second = datetime.datetime.now().second
second_angle = (current_second - 15) * 6
pen.right(second_angle)
pen.forward(100)

# 隐藏画笔
pen.hideturtle()

# 关闭画布
turtle.done()
