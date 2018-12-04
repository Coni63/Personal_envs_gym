import gym
import numpy as np

# from gym_2048_env.envs.game2048_env import Game2048Env
# from gym_2048_env.envs.renderer import Renderer
#
# env = gym.make("2048-v0")
# viewer = Renderer(env.env)
# viewer.start()
#
# for i in range(10):
#     env.reset()
#     viewer.update()
#     while True:
#         obs, reward, done, info = env.step(env.env.sample())
#         viewer.update()
#         if done:
#             break
#
# viewer.finish()

#####################################

# from sliding_env.envs.sliding_env import SlidingEnv
# from sliding_env.envs.renderer import Renderer
#
# env = gym.make("Sliding-v0")
#
# viewer = Renderer(env.env)
# viewer.start()
#
# for i in range(10):
#     env.reset()
#     viewer.update()
#     while True:
#         obs, reward, done, info = env.step(env.env.sample())
#         viewer.update()
#         if done:
#             break
#
# viewer.finish()


#####################################

from minesweeper_env.envs.minesweeper_env import MinesweeperEnv
from minesweeper_env.envs.renderer import Renderer

env = gym.make("Mine-v0")
viewer = Renderer(env.env, show_bomb = True)
viewer.start()

for i in range(10):
    env.reset()
    viewer.update()
    while True:
        obs, reward, done, info = env.step(env.env.sample())
        # test_prob = np.random.random(obs.shape)
        # viewer.update(probs = test_prob)
        viewer.update()
        if done:
            print(info)
            break

viewer.finish()