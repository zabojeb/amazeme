import random

def generate_maze(width, height):
    # Создаем массив, заполненный стенами (1)
    maze = [[1 for _ in range(width)] for _ in range(height)]
    
    def in_bounds(x, y):
        return 0 <= x < width and 0 <= y < height

    def neighbors(x, y):
        # Восемь направлений движения (лево, право, вверх, вниз)
        dirs = [(0, -2), (2, 0), (0, 2), (-2, 0)]
        result = []
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny):
                result.append((nx, ny))
        return result
    
    def random_walk(x, y):
        maze[y][x] = 0  # Отмечаем начальную позицию как пустую
        while True:
            unvisited_neighbors = [(nx, ny) for nx, ny in neighbors(x, y) if maze[ny][nx] == 1]
            if not unvisited_neighbors:
                break
            nx, ny = random.choice(unvisited_neighbors)
            maze[(y + ny) // 2][(x + nx) // 2] = 0  # Убираем стену между клетками
            x, y = nx, ny
            maze[y][x] = 0  # Отмечаем текущую клетку как пустую
    
    def hunt():
        for y in range(1, height, 2):
            for x in range(1, width, 2):
                if maze[y][x] == 1:
                    neighbors_visited = [(nx, ny) for nx, ny in neighbors(x, y) if maze[ny][nx] == 0]
                    if neighbors_visited:
                        maze[y][x] = 0  # Отмечаем текущую клетку как пустую
                        nx, ny = random.choice(neighbors_visited)
                        maze[(y + ny) // 2][(x + nx) // 2] = 0  # Убираем стену между клетками
                        return x, y
        return None, None

    # Начинаем с произвольной клетки (например, 1,1)
    x, y = 1, 1
    random_walk(x, y)

    while True:
        x, y = hunt()
        if x is None:  # Если не нашлось ни одной новой клетки для охоты
            break
        random_walk(x, y)

    return maze
