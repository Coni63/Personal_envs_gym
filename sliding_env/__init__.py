from gym.envs.registration import register

register(
    id='Sliding-v0',
    entry_point='sliding_env.envs:SlidingEnv',
    timestep_limit=1000,
)
