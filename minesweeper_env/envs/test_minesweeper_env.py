#!/usr/bin/env python

from __future__ import absolute_import
import unittest
import numpy as np

import minesweeper_env.envs.minesweeper_env as minesweeper_env

class TestBoard(unittest.TestCase):

    def test_expand(self):
        ms = minesweeper_env.MinesweeperEnv()
        ms.seed(42)
        ms.set_difficulty(width=8, height=8, num_mines=8)
        ms._set_bombs(np.eye(8, 8).astype(np.bool))
        obs, reward, done, info = ms.step((7, 0))
        expected_result = np.array( [[-1, -1, -1, -1, -1, -1, -1, -1],
                                     [-1, -1, -1, -1, -1, -1, -1, -1],
                                     [ 1,  2, -1, -1, -1, -1, -1, -1],
                                     [ 0,  1,  2, -1, -1, -1, -1, -1],
                                     [ 0,  0,  1,  2, -1, -1, -1, -1],
                                     [ 0,  0,  0,  1,  2, -1, -1, -1],
                                     [ 0,  0,  0,  0,  1,  2, -1, -1],
                                     [ 0,  0,  0,  0,  0,  1, -1, -1]])
        self.assertTrue(np.array_equal(obs, expected_result))

        ms = minesweeper_env.MinesweeperEnv()
        ms.seed(42)
        ms.set_difficulty(width=8, height=8, num_mines=8)
        ms._set_bombs(np.eye(8, 8).astype(np.bool))
        obs, reward, done, info = ms.step((0, 7))
        expected_result = np.array( [[-1, -1, -1, -1, -1, -1, -1, -1],
                                     [-1, -1, -1, -1, -1, -1, -1, -1],
                                     [ 1,  2, -1, -1, -1, -1, -1, -1],
                                     [ 0,  1,  2, -1, -1, -1, -1, -1],
                                     [ 0,  0,  1,  2, -1, -1, -1, -1],
                                     [ 0,  0,  0,  1,  2, -1, -1, -1],
                                     [ 0,  0,  0,  0,  1,  2, -1, -1],
                                     [ 0,  0,  0,  0,  0,  1, -1, -1]])
        self.assertTrue(np.array_equal(obs, expected_result.T))

        ms = minesweeper_env.MinesweeperEnv()
        ms.seed(42)
        ms.set_difficulty(width=8, height=8, num_mines=8)
        b =np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 1, 0, 0],
                     [0, 0, 1, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 1, 0, 0],
                     [0, 0, 1, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]])
        ms._set_bombs(b.astype(np.bool))
        obs, reward, done, info = ms.step((0, 0))
        expected_result = np.array( [[ 0,  0,  0,  0,  0,  0,  0,  0],
                                     [ 0,  1,  2,  3,  3,  2,  1,  0],
                                     [ 0,  2, -1, -1, -1, -1,  2,  0],
                                     [ 0,  3, -1, -1, -1, -1,  3,  0],
                                     [ 0,  3, -1, -1, -1, -1,  3,  0],
                                     [ 0,  2, -1, -1, -1, -1,  2,  0],
                                     [ 0,  1,  2,  3,  3,  2,  1,  0],
                                     [ 0,  0,  0,  0,  0,  0,  0,  0]])
        self.assertTrue(np.array_equal(obs, expected_result))

        ms = minesweeper_env.MinesweeperEnv()
        ms.seed(42)
        ms.set_difficulty(width=8, height=8, num_mines=8)
        b =np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 1, 0, 0],
                     [0, 0, 1, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 1, 0, 0],
                     [0, 0, 1, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]])
        ms._set_bombs(b.astype(np.bool))
        obs, reward, done, info = ms.step((4, 4))
        expected_result = np.array( [[ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1,  5, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1]])
        self.assertTrue(np.array_equal(obs, expected_result))

        ms = minesweeper_env.MinesweeperEnv()
        ms.seed(42)
        ms.set_difficulty(width=8, height=8, num_mines=8)
        b =np.array([[1, 0, 0, 0, 0, 0, 1, 0],
                     [0, 1, 0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 1, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0, 1, 0, 0],
                     [0, 1, 0, 0, 0, 0, 1, 0],
                     [1, 0, 0, 0, 0, 0, 0, 1]])
        ms._set_bombs(b.astype(np.bool))
        obs, reward, done, info = ms.step((7, 4))
        expected_result = np.array( [[ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1,  2,  1,  1,  2, -1, -1],
                                     [ -1, -1,  1,  0,  0,  1, -1, -1]])
        self.assertTrue(np.array_equal(obs, expected_result))

        ms = minesweeper_env.MinesweeperEnv()
        ms.seed(42)
        ms.set_difficulty(width=8, height=8, num_mines=8)
        b =np.array([[1, 0, 0, 0, 0, 0, 1, 0],
                     [0, 1, 0, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 1, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 1, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0, 1, 0, 0],
                     [0, 1, 0, 0, 0, 0, 1, 0],
                     [1, 0, 0, 0, 0, 0, 0, 1]])
        ms._set_bombs(b.astype(np.bool))
        obs, reward, done, info = ms.step((0, 3))
        expected_result = np.array( [[ -1, -1,  1,  0,  1, -1, -1, -1],
                                     [ -1, -1,  2,  2,  2, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1],
                                     [ -1, -1, -1, -1, -1, -1, -1, -1]])
        self.assertTrue(np.array_equal(obs, expected_result))

    def test_is_outside(self):
        ms = minesweeper_env.MinesweeperEnv()
        ms.seed(42)
        ms.set_difficulty(width=8, height=8, num_mines=8)
        self.assertTrue(ms._is_outside_board(8, 0))
        self.assertTrue(ms._is_outside_board(0, 8))
        self.assertFalse(ms._is_outside_board(7, 7))
        self.assertFalse(ms._is_outside_board(0, 0))
        self.assertTrue(ms._is_outside_board(-1, -1))

    def test_is_visible(self):
        ms = minesweeper_env.MinesweeperEnv()
        ms.seed(42)
        ms.set_difficulty(width=8, height=8, num_mines=8)
        ms._set_bombs(np.eye(8, 8).astype(np.bool))
        obs, reward, done, info = ms.step((7, 0))
        self.assertTrue(ms._is_visible(7, 0))
        self.assertFalse(ms._is_visible(0, 7))
        self.assertTrue(ms._is_visible(-1, 0))
        self.assertTrue(ms._is_visible(2, 0))
        self.assertFalse(ms._is_visible(0, 0))

    def test_sample(self):
        ms = minesweeper_env.MinesweeperEnv()
        ms.seed(42)
        ms.set_difficulty(width=8, height=8, num_mines=8)
        pos = ms.sample()
        expected_result = not ms._is_outside_board(*pos) and not ms._is_visible(*pos)
        self.assertTrue(expected_result)

    def test_game_done(self):
        ms = minesweeper_env.MinesweeperEnv()
        ms.seed(42)
        ms.set_difficulty(width=8, height=8, num_mines=8)
        b =np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 1, 0, 0],
                     [0, 0, 1, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 1, 0, 0],
                     [0, 0, 1, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]])
        ms._set_bombs(b.astype(np.bool))
        obs, reward, done, info = ms.step((0, 0))
        self.assertFalse(done)
        obs, reward, done, info = ms.step((3, 3))
        self.assertFalse(done)
        obs, reward, done, info = ms.step((4, 3))
        self.assertFalse(done)
        obs, reward, done, info = ms.step((3, 4))
        self.assertFalse(done)
        obs, reward, done, info = ms.step((4, 4))
        self.assertTrue(done)
        self.assertEqual(info["num_moves"], 5)

        ms = minesweeper_env.MinesweeperEnv()
        ms.seed(42)
        ms.set_difficulty(width=8, height=8, num_mines=8)
        b =np.array([[0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 1, 0, 0],
                     [0, 0, 1, 0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0, 1, 0, 0],
                     [0, 0, 1, 1, 1, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0]])
        ms._set_bombs(b.astype(np.bool))
        obs, reward, done, info = ms.step((2, 2))
        self.assertTrue(done)


if __name__ == '__main__':
    unittest.main()