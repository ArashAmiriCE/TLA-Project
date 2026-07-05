"""
The Game of Life (GoL) module named in honour of John Conway

This module defines the classes required for the GoL simulation.

"""
import numpy as np
from scipy import signal, ndimage
import re
import os


def parse_pattern(filepath):
    FileFormat = os.path.splitext(filepath)[1].lower()
    if FileFormat == ".cells":
        FileLines = []
        with open(filepath,"r") as File:
            for line in File:
                if line.startswith("!"):
                    continue
                if not line:
                    continue
                line.rstrip("\n")
                FileLines.append(line)
        height = len(FileLines)
        width = 0
        if FileLines:
            width = max(len(line) for line in FileLines)
        result = []
        for i in range(height):
            for j in range(len(FileLines[i])):
                if FileLines[i][j] == "":
                    continue
                if FileLines[i][j] == "O":
                    result.append((i,j))
        return width, height, result
    elif FileFormat == ".rle":
        row = 0
        col = 0
        width = 0
        height = 0
        result = []
        with open(filepath, "r") as File:
            isEnd = False
            for line in File:
                if isEnd:
                    break
                if line.startswith("#"):
                    continue
                line = line.strip()
                if not line:
                    continue
                if line.startswith("x"):
                    match = re.match(r"x\s*=\s*(\d+)\s*,\s*y\s*=\s*(\d+)", line)
                    if match:
                        width = int(match.group(1))
                        height = int(match.group(2))
                    continue
                number = ""
                for ch in line:
                    if ch.isdigit():
                        number += ch
                        continue
                    else:
                        if number:
                            repeat = int(number)
                        else:
                            repeat = 1
                    number = ""
                    if ch == "b":
                        col += repeat
                        continue
                    elif ch == "$":
                        row += repeat
                        col = 0
                        continue
                    elif ch in "oxyz":
                        for _ in range(repeat):
                            result.append((row,col))
                            col += 1
                    elif ch == "!":
                        isEnd = True
                        break
        return width, height, result
    else:
        raise ValueError(f"Unsupported file format: {FileFormat}")


class GameOfLife:
    """
    Object for computing Conway's Game of Life (GoL) cellular machine/automata
    """

    def __init__(self, N=256, finite=False, fastMode=True):
        self.grid = np.zeros((N, N), np.uint)
        self.neighborhood = np.ones((3, 3), np.uint)  # 8 connected kernel
        self.neighborhood[1, 1] = 0  # do not count centre pixel
        self.finite = finite
        self.fastMode = fastMode
        self.aliveValue = 1
        self.deadValue = 0
        self.rows = N  # use for slow implementation of evolve
        self.cols = N  # use for slow implementation of evolve

    def getStates(self):
        """
        Returns the current states of the cells
        """
        return self.grid

    def getGrid(self):
        """
        Same as getStates()
        """
        return self.getStates()

    def update_grid_fast(self, grid):
        if self.finite:
            neighbors = signal.convolve2d(grid, self.neighborhood, mode='same', boundary='fill')
        else:
            neighbors = signal.convolve2d(grid, self.neighborhood, mode='same', boundary='wrap')
        next_grid = np.zeros((self.rows, self.cols), np.uint)
        next_grid[((grid == 1) & ((neighbors == 2) | (neighbors == 3)))| ((grid == 0) & (neighbors == 3))] = 1
        return next_grid

    def evolve(self):
        if self.fastMode:
            self.grid = self.update_grid_fast(self.grid)
        else:
            next_grid = np.zeros((self.rows, self.cols), np.uint)
            for i in range(self.rows):
                for j in range(self.cols):
                    num_of_allive_neighbors = 0

                    if self.finite:
                        if i-1 < 0:
                            previous_row = i
                        else:
                            previous_row = i - 1
                        if i+1 == self.rows:
                            next_row = i
                        else:
                            next_row = i + 1
                        if j-1 < 0:
                            previous_col = j
                        else:
                            previous_col = j - 1
                        if j+1 == self.cols:
                            next_col = j
                        else:
                            next_col = j + 1
                    else:
                        previous_row = (i - 1) % self.rows
                        next_row = (i + 1) % self.rows
                        previous_col = (j - 1) % self.cols
                        next_col = (j + 1) % self.cols
                    
                    for count_row in range(previous_row, next_row + 1):
                        for count_column in range(previous_col, next_col + 1):
                            if count_row == i and count_column == j:
                                continue
                            num_of_allive_neighbors += self.grid[count_row, count_column]
                    
                    if self.grid[i,j] == 1 and num_of_allive_neighbors < 2:
                        next_grid[i,j] = 0
                    elif self.grid[i,j] == 1 and (num_of_allive_neighbors == 2 or num_of_allive_neighbors == 3):
                        next_grid[i,j] = 1
                    elif self.grid[i,j] == 1 and num_of_allive_neighbors > 3:
                        next_grid[i,j] = 0
                    elif self.grid[i,j] == 0 and num_of_allive_neighbors == 3:
                        next_grid[i,j] = 1
            self.grid = next_grid


    def insertBlinker(self, index=(0, 0)):
        '''
        Insert a blinker oscillator construct at the index position
        '''
        self.grid[index[0], index[1] + 1] = self.aliveValue
        self.grid[index[0] + 1, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 1] = self.aliveValue

    def insertGlider(self, index=(0, 0)):
        '''
        Insert a glider construct at the index position
        '''
        self.grid[index[0], index[1] + 1] = self.aliveValue
        self.grid[index[0] + 1, index[1] + 2] = self.aliveValue
        self.grid[index[0] + 2, index[1]] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 1] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 2] = self.aliveValue

    def insertGliderGun(self, index=(0, 0)):
        '''
        TODO: [Part 1c - Glider Gun Fix]
        The current glider gun pattern is broken. Leave the broken array in the code 
        and instruct the student to debug and fix the coordinates so it loops infinitely.
        '''
        self.grid[index[0] + 1, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 2, index[1] + 24] = self.aliveValue
        self.grid[index[0] + 2, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 3, index[1] + 14] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 15] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 23] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 36] = self.aliveValue
        self.grid[index[0] + 3, index[1] + 37] = self.aliveValue

        self.grid[index[0] + 4, index[1] + 13] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 17] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 23] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 36] = self.aliveValue
        self.grid[index[0] + 4, index[1] + 37] = self.aliveValue

        self.grid[index[0] + 5, index[1] + 1 + 1] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 2 + 1] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 18] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 22] = self.aliveValue
        self.grid[index[0] + 5, index[1] + 23] = self.aliveValue

        self.grid[index[0] + 6, index[1] + 1 + 1] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 2 + 1] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 16] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 18] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 19] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 24] = self.aliveValue
        self.grid[index[0] + 6, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 7, index[1] + 12] = self.aliveValue
        self.grid[index[0] + 7, index[1] + 18] = self.aliveValue
        self.grid[index[0] + 7, index[1] + 26] = self.aliveValue

        self.grid[index[0] + 8, index[1] + 13] = self.aliveValue
        self.grid[index[0] + 8, index[1] + 17] = self.aliveValue

        self.grid[index[0] + 9, index[1] + 14] = self.aliveValue
        self.grid[index[0] + 9, index[1] + 15] = self.aliveValue

    def insertFromFile(self, filename, index=((0, 0))):
        '''
        Insert cells from pattern file using parse_pattern
        '''
        width, height, live_cells = parse_pattern(filename)
        for r, c in live_cells:
            target_r = index[0] + r
            target_c = index[1] + c
            if 0 <= target_r < self.rows and 0 <= target_c < self.cols:
                self.grid[target_r, target_c] = self.aliveValue
