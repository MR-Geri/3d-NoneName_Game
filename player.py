from settings import *
import pygame
import numpy as np


class Player:
    def __init__(self):
        self.cord_x, self.cord_y = player_pos
        self.angle = player_angle

    def move(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_w]:
            self.cord_x += player_speed * np.cos(self.angle)
            self.cord_y += player_speed * np.sin(self.angle)
        if key[pygame.K_s]:
            self.cord_x -= player_speed * np.cos(self.angle)
            self.cord_y -= player_speed * np.sin(self.angle)
        if key[pygame.K_a]:
            self.cord_x += player_speed * np.sin(self.angle)
            self.cord_y -= player_speed * np.cos(self.angle)
        if key[pygame.K_d]:
            self.cord_x -= player_speed * np.sin(self.angle)
            self.cord_y += player_speed * np.cos(self.angle)
        if key[pygame.K_LEFT]:
            self.angle -= player_angle_speed
        if key[pygame.K_RIGHT]:
            self.angle += player_angle_speed

    @property
    def pos(self):
        return int(self.cord_x), int(self.cord_y)

    @property
    def x(self):
        return int(self.cord_x)

    @property
    def y(self):
        return int(self.cord_y)
