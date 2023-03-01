import pygame
import image
pygame.init()

image.convertImage("data/turret.png")
TURRET_TURRET = pygame.image.load("data/turret.png")


class Turret:
    def __init__(self, x, y):
        self.image = TURRET_TURRET
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.angle = 0

    def move(self, xy):
        self.rect.centerx, self.rect.centery = xy

    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(TURRET_TURRET, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)