from settings import *
import pygame


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.y -= player_speed
        if key[pygame.K_s]:
            self.y += player_speed
        if key[pygame.K_a]:
            self.x -= player_speed
        if key[pygame.K_d]:
            self.x += player_speed
        if key[pygame.K_LEFT]:
            self.angle -= player_angle_speed
        if key[pygame.K_RIGHT]:
            self.angle += player_angle_speed

    @property
    def pos(self):
        return self.x, self.y
