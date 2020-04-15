import pygame
from datetime import datetime
from datetime import timedelta

WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255
BLACK = 0, 0, 0

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
BLOCK_SIZE = 20

def draw_block(screen, color, block_position):
    block = pygame.Rect((block_position[0] * BLOCK_SIZE, block_position[1] * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, color, block)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

block_position = [0, 0]
last_moved_time = datetime.now()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    if timedelta(seconds=1) <= datetime.now() - last_moved_time:
        block_position[0] += 1
        last_moved_time = datetime.now()

    screen.fill(WHITE)
    draw_block(screen, GREEN, block_position)
    pygame.display.flip()