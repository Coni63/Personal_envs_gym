import unittest
import sliding_env.envs.sliding_env as sliding_env
import numpy as np

class SlidingTest(unittest.TestCase):

    def test_checkGrid(self):
        env = sliding_env.SlidingEnv(3)
        self.assertRaises(Exception, env.setGrid, [1, 2, 3, 4, 5, 6, 7, 8])  # incorrect shape
        self.assertRaises(Exception, env.setGrid, [1, 2, 3, 4, 5, 6, 7, 10, 0])  # incorrect checksum
        self.assertRaises(Exception, env.setGrid, [1, 2, 3, 4, 5, 6, 7, 9, -1])  # incorrect numbers
        self.assertRaises(Exception, env.setGrid, [1, 2, 3, 4, 5, 6, 7, 8, 0])  # sorted
        self.assertRaises(Exception, env.setGrid, [1, 2, 3, 4, 5, 6, 7, 0, 8])  # not solvable
        try:
            env.setGrid, [1, 2, 3, 4, 5, 0, 7, 8, 6]
        except:
            self.fail("Grid should be fine but raise an error")

    def test_moveup(self):
        env = sliding_env.SlidingEnv(3)

        # no moves
        env.setGrid([1, 2, 0, 3, 5, 6, 7, 8, 4])
        env.step(0)
        self.assertTrue(np.array_equal(env.obs, [1, 2, 0, 3, 5, 6, 7, 8, 4]))

        # move
        env.setGrid([1, 2, 5, 3, 7, 0, 6, 8, 4])
        env.step(0)
        self.assertTrue(np.array_equal(env.obs, [1, 2, 0, 3, 7, 5, 6, 8, 4]))

    def test_movedown(self):
        env = sliding_env.SlidingEnv(3)

        # no moves
        env.setGrid([1, 2, 7, 3, 5, 8, 0, 6, 4])
        env.step(2)
        self.assertTrue(np.array_equal(env.obs, [1, 2, 7, 3, 5, 8, 0, 6, 4]))

        # move
        env.setGrid([1, 2, 5, 3, 7, 0, 6, 8, 4])
        env.step(2)
        self.assertTrue(np.array_equal(env.obs, [1, 2, 5, 3, 7, 4, 6, 8, 0]))

    def test_moveleft(self):
        env = sliding_env.SlidingEnv(3)

        # no moves
        env.setGrid([1, 2, 7, 3, 5, 8, 0, 6, 4])
        env.step(3)
        self.assertTrue(np.array_equal(env.obs, [1, 2, 7, 3, 5, 8, 0, 6, 4]))

        # move
        env.setGrid([1, 2, 5, 3, 7, 0, 6, 8, 4])
        env.step(3)
        self.assertTrue(np.array_equal(env.obs, [1, 2, 5, 3, 0, 7, 6, 8, 4]))

    def test_moveright(self):
        env = sliding_env.SlidingEnv(3)

        # move
        env.setGrid([1, 2, 5, 3, 7, 0, 6, 8, 4])
        env.step(1)
        self.assertTrue(np.array_equal(env.obs, [1, 2, 5, 3, 7, 0, 6, 8, 4]))

        # no moves
        env.setGrid([1, 2, 7, 3, 5, 8, 0, 6, 4])
        env.step(1)
        self.assertTrue(np.array_equal(env.obs, [1, 2, 7, 3, 5, 8, 6, 0, 4]))

    def test_loyd(self):
        # not really required with setGrid
        pass

    def test_metric(self):
        env = sliding_env.SlidingEnv(3)
        env.setGrid([1, 2, 5, 3, 7, 0, 6, 8, 4])
        self.assertEqual(env.metric, 13)

    # def test_reward(self):
    #     self.assertEqual(, )

if __name__ == "__main__":
    test = SlidingTest()
    test.main()