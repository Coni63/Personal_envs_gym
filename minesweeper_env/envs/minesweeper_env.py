import sys
import numpy as np
from scipy import signal
from collections import deque

import gym
from gym import spaces
from gym.utils import seeding


class MinesweeperEnv(gym.Env):
    WINREWARD = 10
    LOSREWARD = -10
    PROGRESSREWARD = 1
    INVALIDREWARD = 0

    def __init__(self):
        self.seed()
        self.set_difficulty()      

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, pos):
        """
        Select a square to expose. Coordinates are zero based.
        Return the new state, reward, done and info as per gym's rules
        """
        row, col = pos

        if self._is_outside_board(row, col):
            print("Position {}, {} is outside the grid".format(row, col), file = sys.stderr)
            return self.grid, self.INVALIDREWARD, self._is_game_over(), self._get_info()

        if self._is_visible(row, col):
            print("Position {}, {} is already visible".format(row, col), file=sys.stderr)
            return self.grid, self.INVALIDREWARD, self._is_game_over(), self._get_info()

        if self.num_moves == 0:
            self._place_mines(except_pos = (row, col))
            self._init_counts()

        reward = self._update_board(row, col)

        self.num_moves += 1

        return self.grid, reward, self._is_game_over(), self._get_info()

    def render(self):
        print(self.grid)

    def sample(self):
        pos = np.argwhere(self.grid == -1)
        idx = np.random.randint(len(pos))
        return pos[idx]

    def reset(self):
        self.bombs = np.zeros((self.height, self.width), dtype=np.bool)
        self.grid = -1 * np.ones((self.height, self.width), dtype=np.int8)
        self.counts = np.zeros((self.height, self.width), dtype=np.uint8)
        self.num_moves = 0
        self.explosion = False
        return self.grid

    def set_difficulty(self, width=8, height=8, num_mines=10):
        self.num_mines = min(num_mines, width * height // 4)
        self.width = width
        self.height = height
        self.num_safe_squares = self.width * self.height - self.num_mines
        if num_mines > width * height // 4:
            print("Too much bombs - reduced to {}".format(self.num_mines), file=sys.stderr)
        self.reset()
        
    @property
    def num_exposed_squares(self):
        return (self.grid >= 0).sum()

    @property
    def placed_bombs(self):
        return self.bombs.sum()

    def _set_bombs(self, grid):
        self.bombs = grid
        self.grid = -1 * np.ones((self.height, self.width), dtype=np.int8)
        self.counts = np.zeros((self.height, self.width), dtype=np.uint8)
        self.num_moves = 0
        self.explosion = False
        self.num_mines = self.bombs.sum()
        self.num_safe_squares = self.width * self.height - self.num_mines

    def _update_board(self, row, col):
        """
        Finds all the squares to expose based on a selection

        This uses an 8 neighbor region growing algorithm to expand the board if
        the chosen square is not a neighbor to a mine.
        """
        if self.bombs[row, col]:
            self.explosion = True
            self.grid[row, col] = -100
            return self.LOSREWARD

        queue = deque([(row, col)])
        while len(queue) > 0:
            (row_, col_) = queue.pop()
            self.grid[row_, col_] = self.counts[row_, col_]
            if self.counts[row_, col_] == 0:
                for col_offset, row_offset in [[1, -1], [1, 1], [1, 0], [-1, 0], [-1, -1], [-1, 1], [0, 1], [0, -1]]:
                    new_row, new_col = row_ + row_offset, col_ + col_offset
                    if not self._is_outside_board(new_row, new_col):
                        if not self._is_visible(new_row, new_col) :
                            if not self.bombs[new_row, new_col]:
                                queue.append((row_ + row_offset, col_ + col_offset))
        return self.PROGRESSREWARD

    def _is_outside_board(self, row, col):
        if row < 0 or row >= self.height:
            return True
        elif col < 0 or col >= self.width:
            return True
        else:
            return False

    def _is_visible(self, row, col):
        return self.grid[row, col] != -1

    def _is_game_over(self):
        return self.explosion or self.num_exposed_squares == self.num_safe_squares

    def _place_mines(self, except_pos):
        except_row, except_col = except_pos
        while self.placed_bombs < self.num_mines:
            col = np.random.randint(self.width)
            row = np.random.randint(self.height)
            d_max = max(abs(except_row-row), abs(except_col-col))
            if d_max > 1 and not self.bombs[row, col]:
                self.bombs[row, col] = True

    def _init_counts(self):
        """Calculates how many neighboring squares have minds for all squares"""
        filter = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.uint8)
        self.counts = (signal.convolve2d(self.bombs, filter, mode='same', boundary="fill", fillvalue=0))
        self.counts[self.bombs == True] = 0

    def _get_info(self):
        return {
                "safe_squares" : self.num_safe_squares,
                "exposed_squares": self.num_exposed_squares,
                "num_moves": self.num_moves
               }