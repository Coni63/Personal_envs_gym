import gym

# from gym_2048_env.envs.game2048_env import Game2048Env
#
# env = gym.make("2048-v0")

# from minesweeper_env.envs.minesweeper_env import MinesweeperEnv
#
# env = gym.make("Mine-v0")

from sliding_env.envs.sliding_env import SlidingEnv

env = gym.make("Sliding-v0")

obs = env.reset()
print(obs)

obs, reward, done, info = env.step(0)
print(obs, reward, done, info, sep="\n")
