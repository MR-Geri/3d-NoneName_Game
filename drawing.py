from settings import *
from ray_casting import ray_casting

import pygame


class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.font = pygame.font.SysFont('TimesNewRoman', 36, bold=True)

    def background(self):
        pygame.draw.rect(self.sc, BLUE, (0, 0, WIDTH, HEIGHT // 2))
        pygame.draw.rect(self.sc, GRAY, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    def world(self, pos, angle):
        ray_casting(self.sc, pos, angle)

    def fps(self, clock):
        render = self.font.render(f'{int(clock.get_fps())}', 0, RED)
        self.sc.blit(render, FPS_POS)
