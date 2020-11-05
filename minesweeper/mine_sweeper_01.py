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
    # 맵 정보 리스트 초기화
    field = [[EMPTY for xpos in range(WIDTH)] for ypos in range(HEIGHT)]

    # 폭탄 설치하기
    count = 0
    while count < NUM_OF_BOMBS:
        xpos, ypos = randint(0, WIDTH - 1), randint(0, HEIGHT - 1)
        if field[ypos][xpos] == EMPTY:
            field[ypos][xpos] = BOMB
            count += 1
    # print(field)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        # 배경 그리기
        SURFACE.fill( (0, 0, 0) )

        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos * SIZE, ypos * SIZE, SIZE, SIZE)

                if tile == EMPTY or tile == BOMB:
                    pygame.draw.rect(SURFACE, (192, 192, 192), rect)
                    if tile == BOMB:
                        pygame.draw.ellipse(SURFACE, (255, 255, 0), rect)

        # 선 그리기
        for index in range(0, WIDTH * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96), (index, 0), (index, HEIGHT * SIZE))

        for index in range(0, HEIGHT * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96), (0, index), (WIDTH * SIZE, index))

        # 화면 업데이트
        pygame.display.update()

if __name__ == '__main__':
    main()
