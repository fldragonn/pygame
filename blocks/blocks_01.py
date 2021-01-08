# 벽돌 깨기
#
# blocks_01
#
# 게임 초기화

import pygame

BLACK = (0, 0, 0)

# 파이게임 초기화
pygame.init()

SC_WIDTH, SC_HEIGHT = 600, 800
SC_SIZE = (SC_WIDTH, SC_HEIGHT)
screen = pygame.display.set_mode(SC_SIZE)

pygame.display.set_caption('BLOCKS')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    pygame.display.update()

# 파이게임 종료
pygame.quit()