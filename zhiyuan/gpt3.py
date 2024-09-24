import turtle

def draw_star(n, side_length):
    angle = 360 / n
    for _ in range(n):
        turtle.forward(side_length)
        turtle.right(angle)
        turtle.forward(side_length)
        turtle.left(2 * angle)

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

# 画21角星
draw_star(21, 100)

# 关闭画布
turtle.done()
