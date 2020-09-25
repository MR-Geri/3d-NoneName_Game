from settings import *
import pygame
import numpy as np


def ray_casting(map_, pos, angle):
    cur_angle = angle - HALF_FOV
    x0, y0 = pos
    for ray in range(NUM_RAYS):
        for depth in range(MAX_DEPTH):
            x = x0 + depth * np.cos(cur_angle)
            y = y0 + depth * np.sin(cur_angle)
            # pygame.draw.line(sc, WHITE, pos, (x, y), 3)
            # лучи
            if (x // BLOCK_TITLE * BLOCK_TITLE, y // BLOCK_TITLE * BLOCK_TITLE) in map_.world_map:
                depth *= np.cos(angle - cur_angle)
                height = COEFFICIENT / depth
                color = 255 / (1 + depth * depth / 100000)
                pygame.draw.rect(
                    sc,
                    (color // 2, color, color // 3),
                    (ray * SCALE, HEIGHT // 2 - height // 2, SCALE, height)
                )
                break
        cur_angle += DELTA_ANGLE
