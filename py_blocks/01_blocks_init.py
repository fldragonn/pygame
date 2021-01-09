# 벽돌 깨기
#
# 01_blocks_init.py

# 게임 초기화

import pygame

# 파이게임 초기화
pygame.init()

SC_WIDTH, SC_HEIGHT = 600, 800
SC_SIZE = (SC_WIDTH, SC_HEIGHT)

SCREEN = pygame.display.set_mode(SC_SIZE)
pygame.display.set_caption('py BLOCKS')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# 파이게임 종료
pygame.quit()
