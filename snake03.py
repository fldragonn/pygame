import pygame
import time

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
PURPLE = 127, 0, 127
BLACK = 0, 0, 0
GRAY = 127, 127, 127
WHITE = 255, 255, 255

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLOCK_SIZE = 20

def draw_block(screen, color, position):
    block = pygame.Rect((position[0] * BLOCK_SIZE, position[1] * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

pygame.init()

# 게임 화면 설정
screen = pygame.display.set_mode(SCREEN_SIZE)
screen.fill(WHITE)

# 블록 그리기
draw_block(screen, RED, (1, 1))
draw_block(screen, RED, (1, 3))
draw_block(screen, RED, (1, 5))
draw_block(screen, RED, (1, 7))

draw_block(screen, GREEN, (10, 10))
draw_block(screen, GREEN, (11, 10))
draw_block(screen, GREEN, (12, 10))
draw_block(screen, GREEN, (13, 10))

for bx in range(3, 10, 2):
    for by in range(1, 10, 2):
        draw_block(screen, PURPLE, (bx, by))
        time.sleep(0.1)
        pygame.display.flip()

# pygame.display.flip()
time.sleep(3)