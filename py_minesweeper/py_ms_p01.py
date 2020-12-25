# py_ms_p01.py
#
# 화면 구성하기

import pygame

pygame.init()

COL_COUNT = 20
ROW_COUNT = 15
CELL_SIZE = 50
GRAY = (200, 200, 200)
SCREEN_SIZE = (COL_COUNT * CELL_SIZE, ROW_COUNT * CELL_SIZE)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('PY MINE SWEEPER')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # for row in range(ROW_COUNT):
    #     for col in range(COL_COUNT):
    #         cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE,
    #                                 col * CELL_SIZE + CELL_SIZE,
    #                                 row * CELL_SIZE + CELL_SIZE)
    #         pygame.draw.rect(screen, GRAY, cell_rect, 1)

    for row in range(ROW_COUNT):
        pygame.draw.line(screen, GRAY, (0, row * CELL_SIZE), (COL_COUNT * CELL_SIZE, row * CELL_SIZE))

    for col in range(COL_COUNT):
        pygame.draw.line(screen, GRAY, (col * CELL_SIZE, 0), (col * CELL_SIZE, ROW_COUNT * CELL_SIZE))

    pygame.display.update()


pygame.quit()