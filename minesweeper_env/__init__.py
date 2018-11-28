from gym.envs.registration import register

register(
    id='Mine-v0',
    entry_point='minesweeper_env.envs:MinesweeperEnv',
    timestep_limit=1000,
)
