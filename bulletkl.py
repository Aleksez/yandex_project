import pygame
import math
BULLET_IMAGE = pygame.image.load("data/bullet.png")
bullets = pygame.sprite.Group()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super(Bullet, self).__init__(bullets)
        self.image = BULLET_IMAGE
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 25
        self.angle = angle

    def update(self):
        angle_radians = math.radians(self.angle)
        x_move = self.speed * math.cos(angle_radians)
        y_move = self.speed * math.sin(angle_radians)
        self.rect.move_ip(x_move, -y_move)