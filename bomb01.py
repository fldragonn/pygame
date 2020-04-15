import pygame

BLACK = 0, 0, 0
WHITE = 255, 255, 255

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

player_url = "resources/images/dude.png"
player_image = pygame.image.load(player_url)

while True:
    screen.fill(BLACK)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()

    screen.blit(player_image, (0, 0))

    pygame.display.flip()
    clock.tick(30)