# raywenderich.org tutorial
# https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python

import pygame

# pygame 초기화
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 이미지 불러오기
player = pygame.image.load("resources/images/dude.png")

while True:
    screen.fill((0, 0, 0))
    screen.blit(player, (100, 100))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
