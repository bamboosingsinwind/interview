import turtle

# 设置画笔和画布
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(2)

# 画黑色半圆
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.begin_fill()
pen.fillcolor("black")
pen.circle(100, 180)
pen.end_fill()

# 画白色半圆
pen.penup()
pen.goto(0, 100)
pen.pendown()
pen.begin_fill()
pen.fillcolor("white")
pen.circle(100, 180)
pen.end_fill()

# 画两个小圆
pen.penup()
pen.goto(0, -40)
pen.pendown()
pen.begin_fill()
pen.fillcolor("black")
pen.circle(20)
pen.end_fill()

pen.penup()
pen.goto(0, 40)
pen.pendown()
pen.begin_fill()
pen.fillcolor("white")
pen.circle(20)
pen.end_fill()

# 隐藏画笔
pen.hideturtle()

# 关闭画布
turtle.done()
