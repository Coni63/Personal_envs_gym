# Personal Gym envs

This repository group few envs for gym. They don't have clean render (yet... maybe later). It can be a simple matrix printed in the console or sometimes a small rendering with pygame.

Currently, there is:

- 2048 ("2048-v0")

<img src="https://github.com/Coni63/Personal_envs_gym/blob/master/img/2048.jpg" alt="2048" height="300"/>

- Sliding puzzle ("Sliding-v0")

<img src="https://github.com/Coni63/Personal_envs_gym/blob/master/img/sliding.png" alt="Sliding" height="300"/>

- Minesweeper ("Mine-v0")

<img src="https://github.com/Coni63/Personal_envs_gym/blob/master/img/minesweeper.jpg " alt="Minesweeper" height="300"/>

## How to use

#### Loading

To use those environments in your project, add the library into your project, load it and "make" the env as follow

```
import gym
from gym_2048_env.envs.game2048_env import Game2048Env

env = gym.make("2048-v0")
```

*Attention* : For the Minesweeper you chan change the difficulty as you want but you should create the renderer afterward :

```
import gym
from minesweeper_env.envs.minesweeper_env import MinesweeperEnv
from minesweeper_env.envs.renderer import Renderer

easy = {"width":8, "height":8, "num_mines":10}
medium = {"width":16, "height":16, "num_mines":40}
hard = {"width":16, "height":30, "num_mines":99}

env = gym.make("Mine-v0")
env.env.set_difficulty(**hard)
viewer = Renderer(env.env, show_bomb = True)   # always create the rendered after the difficulty

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

# viewer.finish()
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

Nearly all environments needs to have a better _render_ method. Currently it's an external file using pygame to have a visual. 