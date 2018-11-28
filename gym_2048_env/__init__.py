from gym.envs.registration import register

register(
    id='2048-v0',
    entry_point='gym_2048_env.envs:Game2048Env',
    timestep_limit=1000,
)