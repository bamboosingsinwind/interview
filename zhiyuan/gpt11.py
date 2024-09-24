import turtle

# 设置画笔和画布
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(2)

# 绘制圆形
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.begin_fill()
pen.fillcolor("black")
pen.circle(100)
pen.end_fill()

# 绘制上半部分
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.setheading(60)
pen.circle(-50, 180)

# 绘制下半部分
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.setheading(-60)
pen.circle(50, 180)

# 绘制两个小圆
pen.penup()
pen.goto(0, 35)
pen.pendown()
pen.begin_fill()
pen.fillcolor("white")
pen.circle(15)
pen.end_fill()

pen.penup()
pen.goto(0, -35)
pen.pendown()
pen.begin_fill()
pen.fillcolor("black")
pen.circle(15)
pen.end_fill()

# 隐藏画笔
pen.hideturtle()

# 关闭画布
turtle.done()
