import pygame

WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

player_url = 'resources/images/dude.png'
player_img = pygame.image.load(player_url)
# player_pos = [SCREEN_WIDTH // 2 - player_img.get_width() // 2,
#              SCREEN_HEIGHT - player_img.get_height()]
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH // 2 - player_img.get_width() // 2,
                                 centery = SCREEN_HEIGHT - player_img.get_height())
pygame.key.set_repeat(1, 1)

while True:
    screen.fill(BLACK)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_pos.left -= 5
        elif event.key == pygame.K_RIGHT:
            player_pos.left += 5

    # 주인공 그리기
    screen.blit(player_img, player_pos)

    pygame.display.flip()
    clock.tick(30)

