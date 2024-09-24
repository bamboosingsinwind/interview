import pygame
import random

# 游戏窗口大小
window_width = 640
window_height = 480

# 蛇身和食物大小
snake_size = 20
food_size = 20

# 初始化Pygame
pygame.init()

# 创建游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("贪吃蛇")

# 定义颜色
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

# 设置帧率
clock = pygame.time.Clock()
fps = 10

# 初始化蛇的位置
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# 初始化食物的位置
food_position = [random.randrange(1, (window_width // 20)) * 20, random.randrange(1, (window_height // 20)) * 20]
food_spawned = True

# 初始化蛇的方向
direction = "RIGHT"
change_to = direction

# 定义游戏结束函数
def game_over():
    font = pygame.font.SysFont(None, 72)
    text = font.render("Game Over", True, red)
    window.blit(text, (window_width/2 - text.get_width()/2, window_height/2 - text.get_height()/2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    quit()

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = "LEFT"
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = "UP"
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = "DOWN"

    # 根据输入的方向更新蛇的移动方向
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"

    # 更新蛇的位置
    if direction == "RIGHT":
        snake_position[0] += snake_size
    if direction == "LEFT":
        snake_position[0] -= snake_size
    if direction == "UP":
        snake_position[1] -= snake_size
    if direction == "DOWN":
        snake_position[1] += snake_size

    # 增加蛇的长度
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
        food_spawned = False
    else:
        snake_body.pop()