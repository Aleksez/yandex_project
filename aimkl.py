import pygame
import math
import image

image.convertImage('data/aim.png')
AIM_IMAGE = pygame.image.load('data/aim.png')


class Aim:
    def __init__(self, x, y):
        self.image = AIM_IMAGE
        self.angle = 0
        self.rect = self.image.get_rect(center=(x, y))

    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(AIM_IMAGE, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, xy):
        self.rect.centerx, self.rect.centery = xy