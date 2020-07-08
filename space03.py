import pygame
import os
import time
import random

WHITE = (255, 255, 255)

# 화면 설정
SCREEN_WIDTH = SCREEN_HEIGHT = 750
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WIN = pygame.display.set_mode(SCREEN_SIZE)
<<<<<<< HEAD
pygame.display.set_caption("SPACE INVADER")
pygame.font.init()

# 이미지 불러오기
=======
# WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("SPACE INVADER")
pygame.font.init()

# player 비행기
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Load images
>>>>>>> origin/master
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

<<<<<<< HEAD
# player 비행기
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# laser
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
=======
# laser
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
>>>>>>> origin/master

# 배경
BG = pygame.image.load(os.path.join("assets", "background-black.png"))
BG = pygame.transform.scale(BG, (SCREEN_SIZE))

<<<<<<< HEAD
# 비행선 클래스 생성
class Ship:
=======

class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return (self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

# 비행선 클래스 생성
class Ship:
    COOLDOWN = 30
>>>>>>> origin/master
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_count = 0

    def draw(self, window):
<<<<<<< HEAD
        # pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))
        window.blit(self.ship_img, (self.x, self.y))
=======
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(SCREEN_HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_count >= self.COOLDOWN:
            self.cool_down_count = 0
        elif self.cool_down_count > 0:
            self.cool_down_count += 1

    def shoot(self):
        if self.cool_down_count == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_count = 1
>>>>>>> origin/master

    def get_width(self):
        return  self.ship_img.get_width()

    def get_height(self):
        return  self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

<<<<<<< HEAD

class Enemy(Ship):
    COLOR_MAP = {'red': (RED_SPACE_SHIP, RED_LASER),
                 'green': (GREEN_SPACE_SHIP, GREEN_LASER),
                 'blue': (BLUE_SPACE_SHIP, BLUE_LASER)
                 }
=======
    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(SCREEN_HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    laser.collision(obj)
                    objs.remove(obj)
                    if laser in self.lasers:
                        self.lasers.remove(laser)


class Enemy(Ship):
    COLOR_MAP = {
        "red" : (RED_SPACE_SHIP, RED_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER),
        "green": (GREEN_SPACE_SHIP, GREEN_LASER)
    }

>>>>>>> origin/master
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

<<<<<<< HEAD
=======
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != none

>>>>>>> origin/master

def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5
<<<<<<< HEAD
    player = Player(300, 650)

    lost_count = 0

=======
    laser_vel = 4
    player = Player(300, 650)

    lost_count = 0
>>>>>>> origin/master
    # ship = Ship(300, 650)

    clock = pygame.time.Clock()

<<<<<<< HEAD
    lost = False

=======
>>>>>>> origin/master
    def redraw_window():
        WIN.blit(BG, (0, 0))

        lives_label = main_font.render(f"Lives: {lives}", 1, WHITE)
        level_label = main_font.render(f"Level: {level}", 1, WHITE)
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (SCREEN_WIDTH-level_label.get_width()-10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
<<<<<<< HEAD
            lost_label = lost_font.render("YOU LOST!!", 1, WHITE)
            WIN.blit(lost_label,
                     (SCREEN_WIDTH / 2 - lost_label.get_width() / 2, 350))
=======
            lost_label = lost_font.render("YOU LOST!!", 1, (255, 255, 255))
            WIN.blit(lost_label, (SCREEN_WIDTH/2-lost_label.get_width()/2, 350))
>>>>>>> origin/master

        pygame.display.update()

    while run:
        clock.tick(FPS)
<<<<<<< HEAD
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost_count += 1
            lost = True
=======

        if lives < 0 or player.health <=0:
            lost = True
            lost_count += 1
>>>>>>> origin/master

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, SCREEN_WIDTH-100),
<<<<<<< HEAD
                              random.randrange(-1500, -100),
                              random.choice(['red', 'green', 'blue']))
                enemies.append(enemy)

=======
                              random.randrange(-200, -100),
                              random.choice(['red', 'green', 'blue']))
                enemies.append(enemy)

        redraw_window()

>>>>>>> origin/master
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel+ player.get_width() < SCREEN_WIDTH:
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel+ player.get_width() < SCREEN_HEIGHT:
            player.y += player_vel
<<<<<<< HEAD


        for enemy in enemies:
            enemy.move(enemy_vel)
=======
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
>>>>>>> origin/master
            if enemy.y + enemy.get_height() > SCREEN_HEIGHT:
                lives -= 1
                enemies.remove(enemy)

<<<<<<< HEAD

=======
        player.move_lasers(-laser_vel, enemies)
>>>>>>> origin/master
main()