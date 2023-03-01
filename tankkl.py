import pygame
import math
import image

image.convertImage("data/tank.png")
TANK_IMAGE = pygame.image.load("data/tank.png")


class Tank:
    def __init__(self, x, y):
        self.image = TANK_IMAGE
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 5
        self.angle = 0
        self.lives = 3
        self.immune = False
    def rotate(self, angle):
        self.angle += angle
        self.image = pygame.transform.rotate(TANK_IMAGE, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move(self, direction):
        angle_radians = math.radians(self.angle)
        x_move = direction * self.speed * math.cos(angle_radians)
        y_move = direction * self.speed * math.sin(angle_radians)
        self.rect.move_ip(x_move, -y_move)

    def is_hit(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                self.lives -= 1
                enemies.remove(enemy)
                return True
        return False

    def tank_position(self):
        return self.rect.centerx, self.rect.centery

