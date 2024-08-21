#!/usr/bin/env python
# -*- coding: utf-8 -*-

import curses
import os
import random
import click
import importlib.util
import sys


def display_maze(stdscr, maze, wall_color, bg_color, solid_mode, wall_char, space_char, shuffle):
    """
    Displays the maze in the terminal using the curses library.

    Parameters:
        stdscr (curses.window): The curses window object.
        maze (list of list of int): The 2D array representing the maze, where 1 indicates a wall and 0 indicates a space.
        wall_color (int): The color code for the walls.
        bg_color (int): The color code for the background.
        solid_mode (bool): If True, doubles the wall and space characters for a denser maze display.
        wall_char (str): The character to use for the walls.
        space_char (str): The character to use for the spaces.
        shuffle (bool): If True, randomizes the wall and space characters during rendering.
    """
    # Clear the screen
    stdscr.clear()

    # Set up color pairs
    curses.start_color()
    curses.use_default_colors()

    # Convert color inputs to integers if needed
    new_wall_color = int(wall_color) if isinstance(wall_color, str) else wall_color
    new_bg_color = int(bg_color) if isinstance(bg_color, str) else bg_color

    curses.init_pair(1, new_wall_color, new_bg_color)
    stdscr.bkgd(' ', curses.color_pair(1))

    # Get terminal dimensions
    height, width = stdscr.getmaxyx()

    # Track maze dimensions
    maze_height = len(maze)
    maze_width = len(maze[0]) if maze_height > 0 else 0

    # Display the maze
    for y in range(min(height, maze_height)):
        for x in range(min(width // 2 if solid_mode else width, maze_width)):
            if shuffle:
                char = (random.choice(wall_char) + random.choice(wall_char) if solid_mode else random.choice(wall_char)) if maze[y][x] == 1 else (
                    random.choice(space_char) + random.choice(space_char) if solid_mode else random.choice(space_char))
            else:
                char = (wall_char * 2 if solid_mode else wall_char) if maze[y][x] == 1 else (
                    space_char * 2 if solid_mode else space_char)
            try:
                stdscr.addstr(y, x * 2 if solid_mode else x,
                              char, curses.color_pair(1))
            except:
                pass

    # Refresh the screen
    stdscr.refresh()


def get_terminal_size():
    """
    Gets the current size of the terminal.

    Returns:
        os.terminal_size: A named tuple containing the terminal's width and height.
    """
    return os.get_terminal_size()


def default_generate_maze(width, height):
    """
    Generates a maze using the Depth-First Search (DFS) algorithm.

    Parameters:
        width (int): The width of the maze.
        height (int): The height of the maze.

    Returns:
        list of list of int: A 2D array representing the maze, where 1 indicates a wall and 0 indicates a space.
    """
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


@click.command()
@click.option('-c', '--wall-color', default='white', help='Color of the walls (e.g., red, green, blue)')
@click.option('-b', '--bg-color', default='-1', help='Background color (e.g., white, black, red)')
@click.option('--solid-mode', is_flag=True, help='Double characters for a dense maze display')
@click.option('--wall', default='███', help='Character for walls (e.g., #, █)')
@click.option('--space', default=' ', help='Character for spaces (e.g., ., " ")')
@click.option('--shuffle', is_flag=True, help='Randomize wall and space characters')
@click.option('--live', is_flag=True, help='Live updates of the maze display')
@click.option('--rate', default='5', help="Framerate of redraw (works only with --live)" )
@click.option('--source', type=click.Path(exists=True), help='Path to a .py file containing a generate_maze(width, height) function')
@click.help_option('-h', '--help')
def main(wall_color, bg_color, solid_mode, wall, space, shuffle, live, rate, source):
    """
    Main function to display the maze using curses.

    Parameters:
        wall_color (str): The color of the walls (name or integer code).
        bg_color (str): The background color (name or integer code).
        solid_mode (bool): Enables solid mode for dense maze rendering.
        wall (str): Character to represent walls.
        space (str): Character to represent spaces.
        shuffle (bool): Enables random shuffling of wall and space characters.
        live (bool): Enables live maze display updates.
        source (str): Path to a .py file with a custom generate_maze function.
    """
    # Define color map for user-friendly color names
    color_map = {
        'black': curses.COLOR_BLACK,
        'red': curses.COLOR_RED,
        'green': curses.COLOR_GREEN,
        'yellow': curses.COLOR_YELLOW,
        'blue': curses.COLOR_BLUE,
        'magenta': curses.COLOR_MAGENTA,
        'cyan': curses.COLOR_CYAN,
        'white': curses.COLOR_WHITE,
        '-1': -1
    }

    # Translate color names to curses color codes
    if wall_color in color_map:
        wall_color = color_map[wall_color]
    if bg_color in color_map:
        bg_color = color_map[bg_color]

    # Load the custom maze generation function from the provided source file
    if source:
        spec = importlib.util.spec_from_file_location("maze_module", source)
        maze_module = importlib.util.module_from_spec(spec)
        sys.modules["maze_module"] = maze_module
        spec.loader.exec_module(maze_module)

        # Check if the generate_maze function exists in the module
        if not hasattr(maze_module, 'generate_maze'):
            raise AttributeError(
                f"generate_maze function not found in {source}.")
        generate_maze = maze_module.generate_maze
    else:
        generate_maze = default_generate_maze

    def curses_main(stdscr):
        """
        The main curses function to handle the display of the maze.

        Parameters:
            stdscr (curses.window): The curses window object.
        """
        # Disable cursor blinking
        curses.curs_set(0)

        # Get terminal size
        terminal_size = get_terminal_size()
        terminal_width = terminal_size.columns // 2 if solid_mode else terminal_size.columns
        terminal_height = terminal_size.lines

        # Generate the maze
        maze = generate_maze(terminal_width, terminal_height)

        # Display the maze
        display_maze(stdscr, maze, wall_color, bg_color,
                     solid_mode, wall, space, shuffle)

        # Infinite loop for live updates if enabled
        while True:
            # Update maze display if live mode is enabled
            if live:
                display_maze(stdscr, maze, wall_color, bg_color,
                             solid_mode, wall, space, shuffle)
                
                curses.napms(1000 // int(rate))

    # Run the curses application
    curses.wrapper(curses_main)


if __name__ == "__main__":
    main()
