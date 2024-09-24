import numpy as np
import matplotlib.pyplot as plt

def visualize_maze(maze):
    plt.figure(figsize=(10, 10))
    plt.imshow(maze, cmap='binary')
    plt.xticks([])
    plt.yticks([])
    plt.show()

def solve_maze(maze, start, end):
    rows, cols = maze.shape
    visited = np.zeros_like(maze)
    path = []
    solve_maze_helper(maze, start, end, visited, path)
    return path

def solve_maze_helper(maze, position, end, visited, path):
    if position == end:
        return True
    
    x, y = position
    if maze[x, y] == 1 or visited[x, y] == 1:
        return False
    
    visited[x, y] = 1
    path.append(position)
    
    if x > 0 and solve_maze_helper(maze, (x - 1, y), end, visited, path):
        return True
    if y > 0 and solve_maze_helper(maze, (x, y - 1), end, visited, path):
        return True
    if x < maze.shape[0] - 1 and solve_maze_helper(maze, (x + 1, y), end, visited, path):
        return True
    if y < maze.shape[1] - 1 and solve_maze_helper(maze, (x, y + 1), end, visited, path):
        return True
    
    path.pop()
    return False

# 迷宫示例
maze = np.array([
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
])

start = (0, 0)
end = (6, 5)

path = solve_maze(maze, start, end)
print("Path:", path)

for position in path:
    maze[position] = 2

visualize_maze(maze)
