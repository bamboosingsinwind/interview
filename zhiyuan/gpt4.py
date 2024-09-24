import pygame
import random

# 游戏窗口尺寸
window_width = 800
window_height = 600

# 蛇身和食物大小
cell_size = 20

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 初始化游戏
pygame.init()

# 创建游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("贪吃蛇游戏")

# 蛇头的初始位置
snake_head_x = window_width // 2
snake_head_y = window_height // 2

# 蛇身初始长度
snake_length = 1

# 蛇身列表
snake_body = [(snake_head_x, snake_head_y)]

# 食物的初始位置
food_x = random.randint(0, (window_width - cell_size) // cell_size) * cell_size
food_y = random.randint(0, (window_height - cell_size) // cell_size) * cell_size

# 蛇的初始移动方向
snake_direction = "right"

# 游戏主循环
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "down":
                snake_direction = "up"
            elif event.key == pygame.K_DOWN and snake_direction != "up":
                snake_direction = "down"
            elif event.key == pygame.K_LEFT and snake_direction != "right":
                snake_direction = "left"
            elif event.key == pygame.K_RIGHT and snake_direction != "left":
                snake_direction = "right"
    
    # 根据移动方向更新蛇头位置
    if snake_direction == "up":
        snake_head_y -= cell_size
    elif snake_direction == "down":
        snake_head_y += cell_size
    elif snake_direction == "left":
        snake_head_x -= cell_size
    elif snake_direction == "right":
        snake_head_x += cell_size
    
    # 检测是否吃到食物
    if snake_head_x == food_x and snake_head_y == food_y:
        # 生成新的食物位置
        food_x = random.randint(0, (window_width - cell_size) // cell_size) * cell_size
        food_y = random.randint(0, (window_height - cell_size) // cell_size) * cell_size
        # 增加蛇身长度
        snake_length += 1
    
    # 将蛇头加入蛇身列表
    snake_body.append((snake_head_x, snake_head_y))
    
    # 如果蛇身长度大于实际长度，删除蛇尾
    if len(snake_body) > snake_length:
        del snake_body[0]
    
    # 检测是否碰到边界或自身
    if (
        snake_head_x < 0
        or snake_head_x >= window_width
        or snake_head_y < 0
        or snake_head_y >= window_height
        or (snake_head_x, snake_head_y) in snake_body[:-1]
    ):
        running = False
    
    # 绘制游戏画面
    window.fill(BLACK)
    
    # 绘制蛇身
    for segment in snake_body:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], cell_size, cell_size))
    
    # 绘制食物
    pygame.draw.rect(window, RED, (food_x, food_y, cell_size, cell_size))
    
    pygame.display.flip()
    
    clock.tick(10)

# 游戏结束
pygame.quit()
