import time
import numpy as np
import pygame
import matplotlib.pyplot as plt


class Renderer:
    TILE_SIZE = 50
    TILE_PADDING = 2
    COLOR_BACKGROUND = (187, 173, 160)
    WINDOW_NAME = '2048'

    def __init__(self, env, delay=0.5):
        pygame.font.init()
        self.env = env
        self.rows, self.cols = self.env.size, self.env.size
        self.font = pygame.font.SysFont("Arial", 20)
        self.screen_width = self.TILE_SIZE * self.cols
        self.screen_height = self.TILE_SIZE * self.rows
        self.screen = None
        self.delay = delay
        self.cmap = plt.get_cmap('Wistia')

    def start(self):
        pygame.init()
        pygame.display.set_caption(self.WINDOW_NAME)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill(self.COLOR_BACKGROUND)

    def update(self):
        grid = self.env.obs.reshape(self.rows, self.cols)
        self.screen.fill(self.COLOR_BACKGROUND)
        pygame.event.pump() # https://stackoverflow.com/questions/20165492/pygame-window-not-responding-after-a-few-seconds
        for row in range(self.rows):
            for col in range(self.cols):
                val = grid[row, col]
                left = self.TILE_SIZE * col
                top = self.TILE_SIZE * row
                r, g, b, a = self.cmap(val / (self.rows * self.cols))
                # render cells
                pygame.draw.rect(self.screen, (255*r, 255*g, 255*b),
                                 (left, top, self.TILE_SIZE - self.TILE_PADDING, self.TILE_SIZE - self.TILE_PADDING))

                # render text
                if val > 0:
                    str_val = str(val)
                    text = self.font.render(str_val, False, (0, 0, 0))
                    text_width, text_height = self.font.size(str_val)
                    left_text = left + (self.TILE_SIZE - self.TILE_PADDING - text_width) / 2
                    top_text = top + (self.TILE_SIZE - self.TILE_PADDING - text_height) / 2
                    self.screen.blit(text, (left_text, top_text))

        pygame.display.flip()
        time.sleep(self.delay)

    def finish(self):
        pygame.quit()