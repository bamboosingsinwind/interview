import pygame
import random

# 初始化游戏
pygame.init()

# 游戏窗口尺寸
window_width = 800
window_height = 600

# 创建游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("打砖块游戏")

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# 砖块相关参数
brick_width = 80
brick_height = 20
brick_gap = 10
brick_rows = 5
brick_cols = window_width // (brick_width + brick_gap)

# 球相关参数
ball_radius = 10
ball_speed = 5
ball_direction = [random.choice([-1, 1]), 1]

# 板相关参数
paddle_width = 100
paddle_height = 10
paddle_speed = 8

# 砖块列表
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * (brick_width + brick_gap)
        brick_y = row * (brick_height + brick_gap) + 50
        bricks.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))

# 板的初始位置
paddle = pygame.Rect(window_width // 2 - paddle_width // 2, window_height - paddle_height - 10, paddle_width, paddle_height)

# 球的初始位置和速度
ball = pygame.Rect(window_width // 2 - ball_radius, window_height // 2 - ball_radius, ball_radius * 2, ball_radius * 2)

# 游戏主循环
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 移动板
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < window_width:
        paddle.right += paddle_speed
    
    # 移动球
    ball.x += ball_direction[0] * ball_speed
    ball.y += ball_direction[1] * ball_speed
    
    # 球和窗口边界碰撞检测
    if ball.left < 0 or ball.right > window_width:
        ball_direction[0] = -ball_direction[0]
    if ball.top < 0:
        ball_direction[1] = -ball_direction[1]
    
    # 球和板碰撞检测
    if ball.colliderect(paddle):
        ball_direction[1] = -ball_direction[1]
    
    # 球和砖块碰撞检测
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_direction[1] = -ball_direction[1]
            break
    
    # 绘制游戏画面
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, paddle)
    pygame.draw.circle(window, RED, ball.center, ball_radius)
    for brick in bricks:
        pygame.draw.rect(window, BLUE, brick)
    pygame.display.flip()
    
    # 判断游戏结束条件
    if ball.bottom > window_height:
        running = False
    
    clock.tick(60)

# 游戏结束
pygame.quit()
