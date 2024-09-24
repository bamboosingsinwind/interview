import turtle

# 设置画笔和画布
screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(2)

# 绘制正2.1边形
num_sides = 21  # 边的数量
side_length = 50  # 边的长度

for _ in range(num_sides):
    pen.forward(side_length)
    pen.right(360 / num_sides)

# 隐藏画笔
pen.hideturtle()

# 关闭画布
turtle.done()
