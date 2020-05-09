"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code from the previous mini-project
    compressed_line = []
    previous_tile = None
    for tile in filter(lambda tile: tile != 0, line):
        if not previous_tile:
            previous_tile = tile
        else:
            if tile == previous_tile:
                compressed_line.append(tile + previous_tile)
                previous_tile = None
            else:
                compressed_line.append(previous_tile)
                previous_tile = tile
    if previous_tile is not None:
        compressed_line.append(previous_tile)

    compressed_line += [0] * (len(line) - len(compressed_line))

    return compressed_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._height = grid_height
        self._width = grid_width
        self._grid = []
        self._grid_index = {
            UP: [],
            DOWN: [],
            LEFT: [],
            RIGHT: []
        }
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._grid = []
        self._grid_index = {
            UP: [],
            DOWN: [],
            LEFT: [],
            RIGHT: []
        }

        for row in range(self._height):
            tiles = []
            lt_index = []
            rt_index = []
            for col in range(self._width):
                tiles.append(0)
                lt_index.append([row, col])
                rt_index.append([row, col])

            self._grid.append(tiles)
            self._grid_index[LEFT].append(lt_index)

            # Reverse order to get opposite direction
            rt_index.reverse()
            self._grid_index[RIGHT].append(rt_index)

        for col in range(self._width):
            up_index = []
            dw_index = []

            for row in range(self._height):
                up_index.append([row, col])
                dw_index.append([row, col])

            self._grid_index[UP].append(up_index)

            # Reverse order to get opposite direction
            dw_index.reverse()
            self._grid_index[DOWN].append(dw_index)

        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return "\n".join([str(row) for row in self._grid])

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        for plots in self._grid_index[direction]:
            line = []
            for plot in plots:
                line.append(self.get_tile(plot[0], plot[1]))

            merged = merge(line)
            for index in range(len(merged)):
                plot = plots[index]
                self.set_tile(plot[0], plot[1], merged[index])

        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        value = 2 if random.randint(1,100) < 90 else 4

        empty = []

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == 0:
                    empty.append([row, col])

        if len(empty) > 0:
            rand = empty[random.randrange(len(empty))]
            self.set_tile(rand[0], rand[1], value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
