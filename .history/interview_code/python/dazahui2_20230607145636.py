import turtle

def draw_snowflake(side_length, levels):
    if levels == 0:
        turtle.forward(side_length)
        return
    
    side_length /= 3.0
    
    draw_snowflake(side_length, levels - 1)
    turtle.left(60)
    
    draw_snowflake(side_length, levels - 1)
    turtle.right(120)
    
    draw_snowflake(side_length, levels - 1)
    turtle.left(60)
    
    draw_snowflake(side_length, levels - 1)

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
pen.left(30)

# 画雪花
draw_snowflake(400, 4)

# 关闭画布
turtle.done()
