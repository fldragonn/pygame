import pygame
import os

WHITE = (255, 255, 255)

# 화면 설정
SCREEN_WIDTH = SCREEN_HEIGHT = 750
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
WIN = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("SPACE INVADER")
pygame.font.init()

# 배경
BG = pygame.image.load(os.path.join("assets", "background-black.png"))
BG = pygame.transform.scale(BG, (SCREEN_SIZE))

# 비행선 클래스 생성
class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_count = 0

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, 50, 50))


def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 50)

    player_vel = 5

    ship = Ship(300, 650)

    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))

        lives_label = main_font.render(f"Lives: {lives}", 1, WHITE)
        level_label = main_font.render(f"Level: {level}", 1, WHITE)
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (SCREEN_WIDTH - level_label.get_width() - 10, 10))

        ship.draw(WIN)

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ship.x - player_vel > 0:
            ship.x -= player_vel
        if keys[pygame.K_d] and ship.x + player_vel + 50 < SCREEN_WIDTH:
            ship.x += player_vel
        if keys[pygame.K_w] and ship.y - player_vel > 0:
            ship.y -= player_vel
        if keys[pygame.K_s] and ship.y + player_vel + 50 < SCREEN_HEIGHT:
            ship.y += player_vel


main()