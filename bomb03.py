import pygame

BLACK = 0, 0, 0
WHITE = 255, 255, 255

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

player_url = "resources/images/dude.png"
player_image = pygame.image.load(player_url)
player_position = (SCREEN_WIDTH // 2 - player_image.get_width() // 2,
                   SCREEN_HEIGHT - player_image.get_height())

while True:
    screen.fill(BLACK)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()

    # 원점에 주인공 그리기
    screen.blit(player_image, player_position)

    pygame.display.flip()
    clock.tick(30)