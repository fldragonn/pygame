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
SCREEN_HEIGHT = 80
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE)

# 화면 전체에 하얀 사각형 그리기
screen.fill(WHITE)

# 화면 왼쪽에 녹색 정사각형 그리기
rect = pygame.Rect((10, 10), (30, 30))
pygame.draw.rect(screen, GREEN, rect)

# 화면 오른쪽 아래에 적색 직사각형 그리기
rect = pygame.Rect((310, 40), (80, 30))
pygame.draw.rect(screen, RED, rect)

pygame.display.update()

time.sleep(3)