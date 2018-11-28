# Personal Gym envs

This repository group few envs for gym. They don't have clean render (yet... maybe later). It can be a simple matrix printed in the console or sometimes a small rendering with pygame.

Currently, there is:

- 2048 ("2048-v0")

![2048](https://github.com/Coni63/Personal_envs_gym/blob/master/img/2048.jpg)

- Sliding puzzle ("Sliding-v0")

![Sliding](https://github.com/Coni63/Personal_envs_gym/blob/master/img/sliding.png)

- Minesweeper ("Mine-v0")

![Minesweeper](https://github.com/Coni63/Personal_envs_gym/blob/master/img/minesweeper.jpg)


## How to use

#### Loading

To use those environments in your project, add the library into your project, load it and "make" the env as follow

```
import gym
from gym_2048_env.envs.game2048_env import Game2048Env

env = gym.make("2048-v0")
```

#### Playing

Each environments have the following methods:
- render()
- step(action) 
- reset()

The method _step_ returns:
- observation
- reward
- done
- extra info (option)

## Authors

* **Nicolas MINE** - *Initial work* - [Coni63](https://github.com/Coni63)


## Acknowledgments

The game of 2048 is a modified version of the one from [Rgal](https://github.com/rgal/gym-2048). I only slightly modified the code to run using numpy (faster)

## To be done

Nearly all environments needs to have a better _render_ method. Only Sliding_env have a rendering using the renderer of Gym but the quality is not perfect.