# py mine sweeper
#
# py_ms_05_pre.py

# 05. 타일 클릭 처리

import pygame
from random import randint

# 파이게임 초기화
pygame.init()

# 화면 변수 초기화
COL_COUNT = 20
ROW_COUNT = 15
CELL_SIZE = 50
SCREEN_SIZE = (COL_COUNT * CELL_SIZE, ROW_COUNT * CELL_SIZE)

# 색상 변수 초기화
GRAY_LINE = (100, 100, 100)
GRAY_TILE = (200, 200, 200)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# 게임 변수 초기화
EMPTY = 0
BOMB = 1
OPENED = 2
NUM_OF_BOMBS = 50
OPEN_COUNT = 0
game_over = False

# 파이게임 화면 생성
pygame.display.set_caption('py minesweeper')
screen = pygame.display.set_mode(SCREEN_SIZE)

# font init
small_font = pygame.font.SysFont(None, 36)
large_font = pygame.font.SysFont(None, 72)

# set message
message_clear = large_font.render("!!CLEARED!!", True, (0, 255, 255))
message_over = large_font.render("!!GAME OVER!!", True, (0, 255, 255))
message_rect = message_clear.get_rect()
message_rect.center = (COL_COUNT * CELL_SIZE // 2, ROW_COUNT * CELL_SIZE // 2)

# 폭탄 생성
field = [[EMPTY for x in range(COL_COUNT)] for y in range(ROW_COUNT)]

# checked tile
checked = [[0 for x in range(COL_COUNT)] for y in range(ROW_COUNT)]

# filed, 폭탄 생성
bomb_cnt = 0
while bomb_cnt < NUM_OF_BOMBS:
    b_x = randint(0, COL_COUNT - 1)
    b_y = randint(0, ROW_COUNT - 1)
    if field[b_y][b_x] == EMPTY:
        field[b_y][b_x] = BOMB
        bomb_cnt += 1


# return number of bombs
def num_of_bomb(tx_pos, ty_pos):
    b_count = 0
    for y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            x_pos = tx_pos + x_offset
            y_pos = ty_pos + y_offset
            if 0 <= x_pos < COL_COUNT and 0 <= y_pos < ROW_COUNT:
                if field[y_pos][x_pos] == BOMB:
                    b_count += 1
    return b_count


# open tile - recursive function
def open_tile(tx_pos, ty_pos):
    global OPEN_COUNT
    global checked, field
    print("opentile: {}, {}, {}".format(tx_pos, ty_pos, checked[ty_pos][tx_pos]))
    if checked[ty_pos][tx_pos]:
        return

    checked[ty_pos][tx_pos] = True
    print("({}, {})".format(ty_pos, tx_pos))

    for y_offset in range(-1, 2):
        for x_offset in range(-1, 2):
            x_pos = tx_pos + x_offset
            y_pos = ty_pos + y_offset
            if 0 <= x_pos < COL_COUNT and 0 <= y_pos < ROW_COUNT:
                if field[y_pos][x_pos] == EMPTY:
                    field[y_pos][x_pos] = OPENED
                    OPEN_COUNT += 1
                    b_count = num_of_bomb(x_pos, y_pos)
                    # print("({}, {}): {}".format(y_pos, x_pos, b_count))
                    if b_count == 0 and not (x_pos == tx_pos and y_pos == ty_pos):
                        open_tile(x_pos, y_pos)
                        # print("({}. {}) tiles opened!".format(tx_pos, ty_pos))


# 게임루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = event.pos[0] // CELL_SIZE
                y = event.pos[1] // CELL_SIZE
                if field[y][x] == BOMB:
                    game_over = True
                else:
                    if field[y][x] != OPENED:
                        open_tile(x, y)
                    # print(x, y, checked)

    # 필드 그리기
    for y in range(ROW_COUNT):
        for x in range(COL_COUNT):
            one_rect = (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY_TILE, one_rect)
            if field[y][x] == OPENED:
                pygame.draw.rect(screen, BLACK, one_rect)
                count = num_of_bomb(x, y)
                if count > 0:
                    num_img = small_font.render('{}'.format(count), True, YELLOW)
                    screen.blit(num_img, (x * CELL_SIZE + 10, y * CELL_SIZE + 10))
            if game_over and field[y][x] == BOMB:
                pygame.draw.ellipse(screen, YELLOW, one_rect)

    # 격자 그리기
    for col in range(COL_COUNT):
        pygame.draw.line(screen, GRAY_LINE, (col * CELL_SIZE, 0), (col * CELL_SIZE, ROW_COUNT * CELL_SIZE))
    for row in range(ROW_COUNT):
        pygame.draw.line(screen, GRAY_LINE, (0, row * CELL_SIZE), (COL_COUNT * CELL_SIZE, row * CELL_SIZE))

    # message print
    if OPEN_COUNT == COL_COUNT * ROW_COUNT - NUM_OF_BOMBS:
        screen.blit(message_clear, message_rect)
    elif game_over:
        screen.blit(message_over, message_rect)

    pygame.display.update()

# 파이게임 종료
pygame.quit()
