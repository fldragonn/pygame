# raywenderich.org tutorial
# https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python

import pygame

# 파이게임 초기화
pygame.init()

# 화면 설정
width, height = 640, 480

# 게임 스프라이트 초기화
screen = pygame.display.set_mode((width, height))
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

# 키 설정
keys = [False, False, False, False]
playpos = [100, 100]

while True:
    screen.fill((0, 0, 0))

    for bx in range(width // grass.get_width() + 1):
        for by in range(height // grass.get_height() + 1):
            screen.blit(grass, (bx * grass.get_width(), by * grass.get_height()))

    for cy in range(height // castle.get_height()):
        screen.blit(castle, (0, 30 + cy * castle.get_height()))

    screen.blit(player, playpos)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            if event.key == pygame.K_a:
                keys[1] = True
            if event.key == pygame.K_s:
                keys[2] = True
            if event.key == pygame.K_d:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            if event.key == pygame.K_a:
                keys[1] = False
            if event.key == pygame.K_s:
                keys[2] = False
            if event.key == pygame.K_d:
                keys[3] = False

    if keys[0]:
        playpos[1] -= 5
    elif keys[2]:
        playpos[1] += 5
    if keys[1]:
        playpos[0] -= 5
    elif keys[3]:
        playpos[0] += 5