import sys
from math import floor
from random import randint

import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN

# 환경 변수 설정
WIDTH = 20
HEIGHT = 15
SIZE = 50
NUM_OF_BOMBS = 20
EMPTY = 0
BOMB = 1
OPENED = 2
OPEN_COUNT = 0
CHECKED = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

# 파이게임 초기화
pygame.init()
SURFACE = pygame.display.set_mode([WIDTH * SIZE, HEIGHT * SIZE])
FPSCLOCK = pygame.time.Clock()

# 메인 루프
def main():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 배경 그리기
        SURFACE.fill( (0, 0, 0) )

        # 선 그리기
        for index in range(0, WIDTH * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96), (index, 0), (index, HEIGHT * SIZE))

        for index in range(0, HEIGHT * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96), (0, index), (WIDTH * SIZE, index))

        # 화면 업데이트
        pygame.display.update()

if __name__ == '__main__':
    main()
