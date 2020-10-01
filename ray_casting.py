from map import world_map
from settings import *
import pygame
import math


def mapping(x, y):
    return x // BLOCK_TITLE * BLOCK_TITLE, y // BLOCK_TITLE * BLOCK_TITLE


def ray_casting(sc, pos, angle):
    x0, y0 = pos
    xm, ym = mapping(x0, y0)
    cur_angle = angle - HALF_FOV
    for ray in range(NUM_RAYS):
        sin = math.sin(cur_angle)
        sin = sin if sin else 0.000001
        cos = math.cos(cur_angle)
        cos = cos if cos else 0.000001
        x, dx = (xm + BLOCK_TITLE, 1) if cos >= 0 else (xm, -1)
        for i in range(0, WIDTH, BLOCK_TITLE):
            w_depth = (x - x0) / cos
            y = y0 + w_depth * sin
            if mapping(x + dx, y) in world_map:
                break
            x += dx * BLOCK_TITLE
        y, dy = (ym + BLOCK_TITLE, 1) if sin >= 0 else (ym, -1)
        for i in range(0, HEIGHT, BLOCK_TITLE):
            h_depth = (y - y0) / sin
            x = x0 + h_depth * cos
            if mapping(x, y + dy) in world_map:
                break
            y += dy * BLOCK_TITLE
        #
        depth = w_depth if w_depth < h_depth else h_depth
        depth *= math.cos(angle - cur_angle)
        height = min(int(COEFFICIENT / depth), HEIGHT * 2)
        color = 255 / (1 + depth * depth / 100000)
        pygame.draw.rect(
            sc,
            (color // 2, color, color // 3),
            (ray * SCALE, HEIGHT // 2 - height // 2, SCALE, height)
        )
        cur_angle += DELTA_ANGLE
