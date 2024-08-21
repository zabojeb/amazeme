import random


def generate_maze(width, height):
    grid = [[0] * width for _ in range(height)]

    for i in range(height):
        grid[i][0] = grid[i][width-1] = 1
    for j in range(width):
        grid[0][j] = grid[height-1][j] = 1

    for y in range(2, height-2, 2):
        for x in range(2, width-2, 2):
            grid[y][x] = 1
            direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
            grid[y + direction[0]][x + direction[1]] = 1

    return grid
