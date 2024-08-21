import random


def generate_maze(width, height):
    grid = [[1] * width for _ in range(height)]
    walls = [(1, 1)]
    grid[1][1] = 0
    directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]

    while walls:
        cx, cy = random.choice(walls)
        walls.remove((cx, cy))
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 < nx < width-1 and 0 < ny < height-1 and grid[ny][nx] == 1:
                if grid[cy + dy//2][cx + dx//2] == 1:
                    grid[cy + dy//2][cx + dx//2] = 0
                    grid[ny][nx] = 0
                    walls.append((nx, ny))
    return grid
