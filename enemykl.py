import pygame
import math
import random

ENEMY_IMAGE = pygame.image.load("data/enemy.png")
enemies = []
ENEMY_SPEED = 3
MAX_ENEMIES = 5


def spawn_enemy(SCREEN_WIDTH, SCREEN_HEIGHT):
    for i in range(MAX_ENEMIES):
        enemy_x = random.randint(0, SCREEN_WIDTH - ENEMY_IMAGE.get_width())
        enemy_y = random.randint(0, SCREEN_HEIGHT - ENEMY_IMAGE.get_height())
        enemy_angle = random.randint(0, 360)
        enemies.append(Enemy(enemy_x, enemy_y, enemy_angle, ENEMY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT, enemies))


class Enemy:
    def __init__(self, x, y, angle, speed, SCREEN_WIDTH, SCREEN_HEIGHT, enemies):
        self.enemies = enemies
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = SCREEN_WIDTH, SCREEN_HEIGHT
        self.image = ENEMY_IMAGE
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        self.angle = angle

    def move(self):
        angle_radians = math.radians(self.angle)
        x_move = self.speed * math.cos(angle_radians)
        y_move = self.speed * math.sin(angle_radians)
        new_rect = self.rect.move(x_move, -y_move)

        if new_rect.left < 0 or new_rect.right > self.SCREEN_WIDTH or new_rect.top < 0 \
                or new_rect.bottom > self.SCREEN_HEIGHT:
            # Change direction and stop moving
            self.angle = random.randint(0, 360)
            self.image = pygame.transform.rotate(ENEMY_IMAGE, self.angle)

        else:
            # Move the enemy
            self.rect = new_rect
