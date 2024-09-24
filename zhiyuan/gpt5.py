import turtle

def pikachu_curve(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        pikachu_curve(length / 3, depth - 1)
        turtle.left(60)
        pikachu_curve(length / 3, depth - 1)
        turtle.right(120)
        pikachu_curve(length / 3, depth - 1)
        turtle.left(60)
        pikachu_curve(length / 3, depth - 1)

# 设置画布和画笔
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(10)
pen.color("black")

# 调整初始位置和角度
pen.penup()
pen.goto(-200, -200)
pen.pendown()
pen.left(90)

# 画Pikachu Curve
pikachu_curve(400, 4)

# 关闭画布
turtle.done()
