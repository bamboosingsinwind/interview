# 贪吃蛇小游戏的实现


import turtle

# 游戏窗口
wn = turtle.Screen()
wn.title("贪吃蛇小游戏的实现")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# 蛇
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# 食物
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# 游戏状态
game_over = False

# 游戏逻辑
def move_snake():
    if snake.direction != "stop":
        snake.direction = "stop"

    x = snake.xcor()
    y = snake.ycor()

    if snake.direction == "up":
        y -= 15
    elif snake.direction == "down":
        y += 15
    elif snake.direction == "left":
        x -= 15
    elif snake.direction == "right":
        x += 15

    snake.goto(x, y)


def move_food():
    x = food.xcor()
    y = food.ycor()

    food.goto(x, y)


def game_start():
    global game_over
    if snake.distance(food) < 15:
        move_food()
        if snake.xcor() == food.xcor() and snake.ycor() == food.ycor():
            game_over = True
            print("Game Over")
    else:
        move_snake()


# 游戏循环
while not game_over:
    wn.update()
    game_start()

wn.exitonclick()