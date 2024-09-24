import turtle

def draw_regular_polygon(n, side_length):
    angle = 360 / n
    for _ in range(n):
        turtle.forward(side_length)
        turtle.right(angle)

# 设置画布和画笔
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(10)
pen.color("blue")

# 调整初始位置和角度
pen.penup()
pen.goto(-200, 200)
pen.pendown()

# 画正2.1边形
draw_regular_polygon(21, 50)

# 关闭画布
turtle.done()
