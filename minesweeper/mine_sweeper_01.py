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

# 폭탄 개수 반환
def num_of_bomb(field, x_pos, y_pos):
    count = 0
    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == BOMB:
                count += 1
    return count


# 타일 오픈
def open_tile(field, x_pos, y_pos):
    global OPEN_COUNT
    if CHECKED[y_pos][x_pos]:
        return

    CHECKED[y_pos][x_pos] = True

    for yoffset in range(-1, 2):
        for xoffset in range(-1, 2):
            xpos, ypos = (x_pos + xoffset, y_pos + yoffset)
            if 0 <= xpos < WIDTH and 0 <= ypos < HEIGHT and field[ypos][xpos] == EMPTY:
                field[ypos][xpos] = OPENED
                OPEN_COUNT += 1
                count = num_of_bomb(field, xpos, ypos)
                if count == 0 and not (xpos == x_pos and ypos == y_pos):
                    open_tile(field, xpos, ypos)

# 메인 루프
def main():
    # 기본 설정
    game_over = False
    smallfont = pygame.font.SysFont(None, 36)
    largefont = pygame.font.SysFont(None, 72)
    message_clear = largefont.render("!!CLEARED!!", True, (0, 255, 255))
    message_over = largefont.render("GAME OVER!!", True, (0, 255, 255))
    message_rect = message_clear.get_rect()
    message_rect.center = (WIDTH * SIZE / 2, HEIGHT * SIZE / 2)

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
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                xpos, ypos = floor(event.pos[0] / SIZE), floor(event.pos[1] / SIZE)
                # click 타일 효과
                rect = (xpos * SIZE, ypos * SIZE, SIZE, SIZE)
                pygame.draw.rect(SURFACE, (92, 92, 92), rect)
                pygame.display.update()
                pygame.time.delay(100)
                if field[ypos][xpos] == BOMB:
                    game_over = True
                else:
                # elif field[ypos][xpos] == EMPTY:
                    open_tile(field, xpos, ypos)

        # 배경 그리기
        SURFACE.fill( (0, 0, 0) )

        for ypos in range(HEIGHT):
            for xpos in range(WIDTH):
                tile = field[ypos][xpos]
                rect = (xpos * SIZE, ypos * SIZE, SIZE, SIZE)

                if tile == EMPTY or tile == BOMB:
                    pygame.draw.rect(SURFACE, (192, 192, 192), rect)
                    if game_over and tile == BOMB:
                        pygame.draw.ellipse(SURFACE, (255, 255, 0), rect)
                elif tile == OPENED:
                    count = num_of_bomb(field, xpos, ypos)
                    if count > 0:
                        num_image = smallfont.render("{}".format(count), True, (255, 255, 0))
                        SURFACE.blit(num_image, (xpos * SIZE + 10, ypos * SIZE + 10))

        # 선 그리기
        for index in range(0, WIDTH * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96), (index, 0), (index, HEIGHT * SIZE))

        for index in range(0, HEIGHT * SIZE, SIZE):
            pygame.draw.line(SURFACE, (96, 96, 96), (0, index), (WIDTH * SIZE, index))

        # 메시지 나타내기
        if OPEN_COUNT == WIDTH * HEIGHT - NUM_OF_BOMBS:
            SURFACE.blit(message_clear, message_rect.topleft)
        elif game_over:
            SURFACE.blit(message_over, message_rect.topleft)

        # 화면 업데이트
        pygame.display.update()

if __name__ == '__main__':
    main()
