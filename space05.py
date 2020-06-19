# 스페이스 인베이더

import pygame
import os
import random

# 변수 설정
WHITE = (255, 255, 255)
SCREEN_WIDTH = SCREEN_HEIGHT = 750
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 창 타이틀 설정
pygame.display.set_caption("SPACE INVADER")

# 파이게임 초기화
pygame.init()
pygame.font.init()
WIN = pygame.display.set_mode(SCREEN_SIZE)

# 배경 이미지 처리
bg_img = pygame.image.load(os.path.join('assets', 'background-black.png'))
bg_img = pygame.transform.scale(bg_img, SCREEN_SIZE)

# 비행선 이미지 불러오기
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_yellow.png'))
RED_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_red_small.png'))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_green_small.png'))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join('assets', 'pixel_ship_blue_small.png'))

# 레이저 불러오기
YELLOW_LASER = pygame.image.load(os.path.join('assets', 'pixel_laser_yellow.png'))


# Laser 클래스
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)


# 비행선 클래스
class Ship:
    COOLDOWN = 10

    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.max_health = health

    def move_lasers(self, vel):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(SCREEN_HEIGHT):
                self.lasers.remove(laser)


class Enemy(Ship):
    COLOR_MAP = {
        "red"   : RED_SPACE_SHIP,
        "blue"  : BLUE_SPACE_SHIP,
        "green" : GREEN_SPACE_SHIP
    }

    def __init__(self, x, y, color, health = 100):
        super().__init__(x, y, health)
        self.ship_img = self.COLOR_MAP[color]

    def move(self, vel):
        self.y += vel


# 메인 함수
def main():
    run = True
    FPS = 60

    player_vel = 5
    player = Player(300, 650)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    laser_vel = 5

    clock = pygame.time.Clock()

    # 화면 갱신
    def redraw_window():
        WIN.blit(bg_img, (0, 0))

        for enemy in enemies:
            enemy.draw(WIN)
        player.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if len(enemies) == 0:
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randint(50, 700),
                              random.randint(-1000, -100),
                              random.choice(['red', 'green', 'blue']))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel < SCREEN_WIDTH - player.get_width():
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel < SCREEN_HEIGHT - player.get_height():
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies:
            enemy.move(enemy_vel)
            if enemy.y > SCREEN_HEIGHT:
                enemies.remove(enemy)

        player.move_lasers(-laser_vel)
main()