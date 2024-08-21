import random


def generate_maze(width, height):
    maze = [[1 for _ in range(width)] for _ in range(height)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_valid(x, y):
        return 0 <= x < width and 0 <= y < height and maze[y][x] == 1

    def dfs(x, y):
        maze[y][x] = 0
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if is_valid(nx, ny):
                maze[y + dy][x + dx] = 0
                dfs(nx, ny)

    start_x = random.randrange(1, width, 2)
    start_y = random.randrange(1, height, 2)
    dfs(start_x, start_y)

    return maze
