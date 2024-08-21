<h1 align="center">
  aMAZEme
</h1>
<p align="center">
  Maze generation tool that will amaze you!
</p>

![demo](/assets/demo.png)

`amazeme` is a terminal-based maze generator and viewer implemented in Python using the `curses` library. This tool allows users to visualize mazes directly in the terminal, customize the appearance with various options, and even provide their own maze generation algorithms.

## Features

- **Custom Algorithms**: Ability to load and use custom maze generation algorithms from external Python files.
- **Customizable Appearance**: Adjust wall and background colors, use different characters for walls and spaces.
- **Solid Mode**: Option to double the wall and space characters for a denser display.
- **Shuffle Mode**: Randomize the characters used for walls and spaces.
- **Real-Time Updates**: Option to continuously refresh the maze display.

## Installation

To install `amazeme`, you need to have Python 3 and `pip` installed. 

You can then install `amazeme` via **pip** using the following command:

```bash
pip install amazeme
```

You can also install it via **pipx**:

```bash
pipx install amazeme
```

## Usage

After installation, you can run `amazeme` from the terminal with various options to customize the maze display.

To display a maze with default settings:

```bash
amazeme
```

### Options

- `-c`, `--wall-color`:
  Set the color of the walls. You can use color names (e.g., `red`, `blue`) or integer color codes. Use `-1` for default terminal foreground.

- `-b`, `--bg-color`:
  Set the background color. Use color names or integer color codes. Use `-1` for default terminal background.

- `--solid-mode`:
  Enable solid mode to double the characters used for walls and spaces.

- `--wall`:
  Specify the string for walls (e.g., `#`, `█`, `><`). Defaults to `███`.

- `--space`:
  Specify the character for spaces (e.g., `.`, ` `). Defaults to a single space.

- `--shuffle`:
  Randomly shuffle the wall and space characters during rendering.

- `--live`:
  Enable live updates of the maze display. The maze will continuously refresh.

- `--rate`:
  Framerate to refresh maze. Works only with `--live`.
  
- `--source`:
  Provide the path to a `.py` file containing a custom `generate_maze(width, height)` function. This allows you to use your own maze generation algorithm.

### Example Commands

- Display a maze with red walls and black background:

  ```bash
  amazeme -c red -b black
  ```

- Use custom characters for walls and spaces with solid mode:

  ```bash
  amazeme --wall "###" --space "." --solid-mode
  ```

- Enable live updates and shuffle 123 characters:

  ```bash
  amazeme --live --shuffle --wall "123"
  ```

- Use a custom maze generation algorithm from `custom_maze.py`:

  ```bash
  amazeme --source /path/to/custom_maze.py
  ```

## Custom Maze Generation

To provide your own maze generation algorithm, create a Python file with a function `generate_maze(width, height)`. This function should return a 2D list (list of lists) where each element is `0` for spaces and `1` for walls.

Example of a custom maze generation file (`custom_maze.py`):

```python
def generate_maze(width, height):
    """ My incredible maze generation function """
    return [[1 if (x + y) % 2 == 0 else 0 for x in range(width)] for y in range(height)]
```

There is also a bunch of different generators in `generators` folder in GitHub repository of project.

Feel free to contribute and add your own generators!

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/zabojeb">zabojeb</a>
</p>
