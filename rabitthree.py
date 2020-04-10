# raywenderich.org tutorial
# https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python

import pygame

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

while True:
    screen.fill((0, 0, 0))

    # 배경 이미지 그리기
    for bx in range(width // grass.get_width()+1):
        for by in range(height // grass.get_height()+1):
            screen.blit(grass, (bx * 100, by * 100))

    # 캐슬 그리기
    for cy in range(height // castle.get_height()):
        screen.blit(castle, (0, 30 + cy * 100))

    # 토끼 그리기
    screen.blit(player, (100, 100))


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
