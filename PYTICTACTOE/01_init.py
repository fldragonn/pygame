# TIC TAC TOE

import pygame

pygame.init()

screen_width  = 450
screen_height = 450
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('TIC TAC TOE')

# 격자 설정
CELL_SIZE = 150
ROW_COUNT = screen_width // 3
COL_COUNT = screen_height // 3
GRAY  = (200, 200, 200)
WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)

            if event.button == 2:
                running = False

    # 격자 그리기
    for x in range(COL_COUNT):
        for y in range(ROW_COUNT):
            cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, cell_rect, 3)    # 3은 테두리 두께

    # 화면 업데이트
    pygame.display.update()
pygame.quit()