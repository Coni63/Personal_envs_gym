import time
import numpy as np
import pygame
import matplotlib.pyplot as plt


class Renderer:
    TILE_SIZE = 30
    TILE_PADDING = 2
    COLOR_HIDDEN = (189, 189, 189)
    COLOR_VISIBLE = (100, 100, 100)
    COLOR_BACKGROUND = (0, 0, 0)
    COLOR_BOMB = (255, 0 ,0)
    WINDOW_NAME = 'Minesweeper'

    def __init__(self, env, delay=0.5, show_bomb=False):
        pygame.font.init()
        self.env = env
        self.rows, self.cols = self.env.grid.shape
        self.font = pygame.font.SysFont("Arial", 20)
        self.screen_width = self.TILE_SIZE * self.cols
        self.screen_height = self.TILE_SIZE * self.rows
        self.screen = None
        self.show_bomb = show_bomb
        self.cmap = plt.get_cmap('bwr')
        self.delay = delay

    def start(self):
        pygame.init()
        pygame.display.set_caption(self.WINDOW_NAME)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.screen.fill(self.COLOR_BACKGROUND)

    def update(self, probs=None):
        self.screen.fill(self.COLOR_BACKGROUND)
        pygame.event.pump() # https://stackoverflow.com/questions/20165492/pygame-window-not-responding-after-a-few-seconds
        for row in range(self.rows):
            for col in range(self.cols):
                val = self.env.grid[row, col]
                left = self.TILE_SIZE * col
                top = self.TILE_SIZE * row

                # render cells
                if val == -1:
                    if probs is not None:
                        prob = probs[row, col]
                        r, g, b, a = self.cmap(prob)
                        pygame.draw.rect(self.screen, (255*r, 255*g, 255*b),
                                         (left, top, self.TILE_SIZE - self.TILE_PADDING,
                                          self.TILE_SIZE - self.TILE_PADDING))
                    else:
                        pygame.draw.rect(self.screen, self.COLOR_HIDDEN,
                                     (left, top, self.TILE_SIZE - self.TILE_PADDING, self.TILE_SIZE - self.TILE_PADDING))
                elif val == -100:
                    pygame.draw.rect(self.screen, self.COLOR_BOMB,
                                     (left, top, self.TILE_SIZE - self.TILE_PADDING, self.TILE_SIZE - self.TILE_PADDING))
                else:
                    pygame.draw.rect(self.screen, self.COLOR_VISIBLE,
                                     (left, top, self.TILE_SIZE - self.TILE_PADDING, self.TILE_SIZE - self.TILE_PADDING))

                # render text
                if val > -1:
                    str_val = str(val)
                    text = self.font.render(str_val, False, (255, 255, 255))
                    text_width, text_height = self.font.size(str_val)
                    left_text = left + (self.TILE_SIZE - self.TILE_PADDING - text_width) / 2
                    top_text = top + (self.TILE_SIZE - self.TILE_PADDING - text_height) / 2
                    self.screen.blit(text, (left_text, top_text))

                # render bombs
                if self.show_bomb and self.env.bombs[row, col]:
                    str_val = "X"
                    text = self.font.render(str_val, True, (255, 0, 0))
                    text_width, text_height = self.font.size(str_val)
                    left_text = left + (self.TILE_SIZE - self.TILE_PADDING - text_width) / 2
                    top_text = top + (self.TILE_SIZE - self.TILE_PADDING - text_height) / 2
                    self.screen.blit(text, (left_text, top_text))

        pygame.display.flip()
        time.sleep(self.delay)

    def finish(self):
        pygame.quit()