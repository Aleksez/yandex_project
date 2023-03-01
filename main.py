import pygame
import tankkl
import turretkl
import bulletkl
import aimkl
import json
import enemykl

lvl1 = True
lvl2 = False
lvl3 = False
pygame.init()
clock = pygame.time.Clock()
filename = "save.txt"
with open(filename, "r") as file:
    text = file.read()
    if text == '2':
        lvl2 = True
    elif text == '3':
        lvl2 = True
        lvl3 = True
    print(text)
# константы
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FPS = 60
FONT = pygame.font.SysFont('Arial', 30)
ENEMY_IMAGE = pygame.image.load("data/enemy.png")
ENEMY_SPEED = 3
# Set the maximum number of enemies
MAX_ENEMIES = 5
# Create a list to store the enemies
enemies = []


# группы спрайтов
class Life:
    def __init__(self, x, y, value):
        self.image = LIFE_IMAGE
        self.rect = self.image.get_rect(topleft=(x, y))
        self.value = value

    def draw(self, surface):
        for i in range(self.value):
            x = self.rect.x + i * (self.image.get_width() + 5)
            surface.blit(self.image, (x, self.rect.y))


LIFE_IMAGE = pygame.image.load("heart.png")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill('white')
life = Life(1600, 900, 3)
# спавн танка
TANK_X = 400
TANK_Y = 400
tank = tankkl.Tank(TANK_X, TANK_Y)
turret = turretkl.Turret(TANK_X, TANK_Y)
aim = aimkl.Aim(turret.rect.centerx, turret.rect.centery)
level1_button = pygame.Rect(100, 200, 200, 50)
level2_button = pygame.Rect(900, 200, 200, 50)
level3_button = pygame.Rect(1600, 200, 200, 50)

home_image = pygame.image.load("data/home.png").convert_alpha()

# создание кнопки home
home_button = pygame.Rect(1800, 10, 100, 104)


class Spike(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("spike.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("wall.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)


class Target(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("target.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)


target_group = pygame.sprite.Group()
spike_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()

win_button = pygame.Rect(900, 400, 300, 200)
font = pygame.font.Font(None, 48)
win_text = font.render("Победа!!!", True, 'black')

win_button.size = (0, 0)


def draw_menu():
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    # Шрифт для текста на кнопках
    font = pygame.font.Font(None, 36)

    # Создание кнопок выбора уровня

    # Отображение кнопок на экране
    pygame.draw.rect(screen, GRAY, level1_button)
    level1_text = font.render("Уровень 1", True, WHITE)
    screen.blit(level1_text, (level1_button.x + 10, level1_button.y + 10))

    pygame.draw.rect(screen, GRAY, level2_button)
    level2_text = font.render("Уровень 2", True, WHITE)
    screen.blit(level2_text, (level2_button.x + 10, level2_button.y + 10))

    pygame.draw.rect(screen, GRAY, level3_button)
    level3_text = font.render("Уровень 3", True, WHITE)
    screen.blit(level3_text, (level3_button.x + 10, level3_button.y + 10))
    screen.blit(home_image, (1800, 10))


trglvl1 = False
trglvl2 = False
trglvl3 = False
lvl3o = False
immune_time = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bulletkl.Bullet(turret.rect.centerx, turret.rect.centery, turret.angle)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if level1_button.collidepoint(event.pos):
                level1_button.size = (0, 0)
                level2_button.size = (0, 0)
                level3_button.size = (0, 0)
                with open('lvl1.json', 'r') as f:
                    data = json.load(f)
                TANK_X = int(data["tank"]["coordX"])
                TANK_Y = int(data["tank"]["coordY"])
                tank = tankkl.Tank(int(TANK_X), int(TANK_Y))
                turret = turretkl.Turret(int(TANK_X), int(TANK_Y))
                aim = aimkl.Aim(turret.rect.centerx, turret.rect.centery)
                wall = Wall(data["walls"]["wall1"][0], data["walls"]["wall1"][1])
                wall_group.add(wall)
                wall = Wall(data["walls"]["wall2"][0], data["walls"]["wall2"][1])
                wall_group.add(wall)
                target = Target(data["targets"]["target"][0], data["targets"]["target"][1])
                target_group.add(target)
                trglvl1 = True



            elif level2_button.collidepoint(event.pos) and lvl2:
                level1_button.size = (0, 0)
                level2_button.size = (0, 0)
                level3_button.size = (0, 0)
                with open('lvl2.json', 'r') as f:
                    data = json.load(f)
                TANK_X = int(data["tank"]["coordX"])
                TANK_Y = int(data["tank"]["coordY"])
                tank = tankkl.Tank(int(TANK_X), int(TANK_Y))
                turret = turretkl.Turret(int(TANK_X), int(TANK_Y))
                aim = aimkl.Aim(turret.rect.centerx, turret.rect.centery)
                spike = Spike(data["spikes"]["spike1"][0], data["spikes"]["spike1"][1])
                spike_group.add(spike)
                spike = Spike(data["spikes"]["spike2"][0], data["spikes"]["spike2"][1])
                spike_group.add(spike)
                target = Target(data["targets"]["target1"][0], data["targets"]["target1"][1])
                target_group.add(target)
                target = Target(data["targets"]["target2"][0], data["targets"]["target2"][1])
                target_group.add(target)
                trglvl2 = True
            elif level3_button.collidepoint(event.pos) and lvl3:
                lvl3o = True
                level1_button.size = (0, 0)
                level2_button.size = (0, 0)
                level3_button.size = (0, 0)
                with open('lvl3.json', 'r') as f:
                    data = json.load(f)
                TANK_X = int(data["tank"]["coordX"])
                TANK_Y = int(data["tank"]["coordY"])
                tank = tankkl.Tank(int(TANK_X), int(TANK_Y))
                turret = turretkl.Turret(int(TANK_X), int(TANK_Y))
                aim = aimkl.Aim(turret.rect.centerx, turret.rect.centery)
                wall = Wall(data["walls"]["wall1"][0], data["walls"]["wall1"][1])
                wall_group.add(wall)
                wall = Wall(data["walls"]["wall2"][0], data["walls"]["wall2"][1])
                wall_group.add(wall)
                spike = Spike(data["spikes"]["spike1"][0], data["spikes"]["spike1"][1])
                spike_group.add(spike)
                spike = Spike(data["spikes"]["spike2"][0], data["spikes"]["spike2"][1])
                spike_group.add(spike)
                target = Target(data["targets"]["target3"][0], data["targets"]["target1"][1])
                target_group.add(target)
                target = Target(data["targets"]["target3"][0], data["targets"]["target2"][1])
                target_group.add(target)
                target = Target(data["targets"]["target3"][0], data["targets"]["target3"][1])
                target_group.add(target)
            elif home_button.collidepoint(event.pos):
                level1_button = pygame.Rect(100, 200, 200, 50)
                level2_button = pygame.Rect(900, 200, 200, 50)
                level3_button = pygame.Rect(1600, 200, 200, 50)
                spike_group = pygame.sprite.Group()
                wall_group = pygame.sprite.Group()
                target_group = pygame.sprite.Group()
                life.value = 3
                draw_menu()
            elif win_button.collidepoint(event.pos):
                pygame.quit()
    for bullet in bulletkl.bullets:
        for target in target_group:
            if bullet.rect.colliderect(target.rect):
                bulletkl.bullets.remove(bullet)
                target_group.remove(target)
    if not target_group.sprites() and not lvl2 and trglvl1:
        lvl2 = True
        with open(filename,'w') as file:
            file.write('2')
    if target_group.sprites() and lvl2:
        trglvl2 = True
    if not target_group.sprites() and trglvl2:
        lvl3 = True
        with open(filename,'w') as file:
            file.write('3')
    if lvl3o and not target_group.sprites():
        trglvl3 = True

    # движение  поворот танка
    if pygame.key.get_pressed()[pygame.K_w]:
        tank.move(1.5)
        turret.move(tank.tank_position())
        aim.move(tank.tank_position())
    if pygame.key.get_pressed()[pygame.K_s]:
        tank.move(-0.75)
        turret.move(tank.tank_position())
        aim.move(tank.tank_position())
    if pygame.key.get_pressed()[pygame.K_d]:
        tank.rotate(-6)
        turret.rotate(-6)
        aim.rotate(-6)
    if pygame.key.get_pressed()[pygame.K_a]:
        tank.rotate(+6)
        turret.rotate(+6)
        aim.rotate(+6)
    # пворот башни
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        turret.rotate(-3)
        aim.rotate(-3)
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        turret.rotate(+3)
        aim.rotate(+3)
    if pygame.sprite.spritecollide(tank, spike_group, False, pygame.sprite.collide_mask):
        if not tank.immune:
            life.value -= 1
            tank.immune = True
    if pygame.sprite.spritecollide(tank, wall_group, False, pygame.sprite.collide_mask):
        dx = abs(tank.rect.centerx - wall.rect.centerx)
        dy = abs(tank.rect.centery - wall.rect.centery)

        # Проверяем, насколько танк заехал в стену
        if dx < tank.rect.width / 2 + wall.rect.width / 2:
            if tank.rect.centerx < wall.rect.centerx:
                tank.rect.right = wall.rect.left
            else:
                tank.rect.left = wall.rect.right

        if dy < tank.rect.height / 2 + wall.rect.height / 2:
            if tank.rect.centery < wall.rect.centery:
                tank.rect.bottom = wall.rect.top
            else:
                tank.rect.top = wall.rect.bottom
    if tank.immune:
        immune_time += 1
        if immune_time > 60:  # 60 кадров (1 секунда)
            tank.immune = False
            immune_time = 0
    if life.value == 0:
        print('GAME OVER')
        pygame.quit()

    # истанция прицела
    # отрисовкаа
    screen.fill('white')
    draw_menu()
    screen.blit(aim.image, aim.rect)
    spike_group.draw(screen)
    wall_group.draw(screen)
    bulletkl.bullets.draw(screen)
    bulletkl.bullets.update()
    target_group.draw(screen)
    screen.blit(tank.image, tank.rect)
    life.draw(screen)
    if not target_group.sprites() and trglvl3:
        screen.blit(win_text, (win_button.x, win_button.y))
        win_button.size = (500, 500)
    screen.blit(turret.image, turret.rect)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()

