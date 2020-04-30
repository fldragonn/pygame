import pygame

from datetime import datetime
from datetime import timedelta

# 사용할 상수 설정
WHITE = 255, 255, 255
BLACK =   0,   0,   0
RED   = 255,   0,   0
GREEN =   0, 255,   0

SCREEN_WIDTH  = 400
SCREEN_HEIGHT = 400
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)

BLOCK_SIZE = 20

DIRECTION_ON_KEY = {
    pygame.K_UP: 'up',
    pygame.K_DOWN: 'down',
    pygame.K_LEFT: 'left',
    pygame.K_RIGHT: 'right'
}


# 블록 그리기 함수 선언
def draw_block(t_screen, color, postion):
    block = pygame.Rect((postion[0] * BLOCK_SIZE, postion[1] * BLOCK_SIZE),
                        (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(t_screen, color, block)


# 파이게임 초기화
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

# 초기값 설정
block_direction = 'right'
block_position = [0, 0]
last_moved_time = datetime.now()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key in DIRECTION_ON_KEY:
                block_direction = DIRECTION_ON_KEY[event.key]
                print(event.key, DIRECTION_ON_KEY[event.key], block_position)

    if timedelta(seconds=0.1) <= datetime.now() - last_moved_time:
        if block_direction == 'up':
            block_position[1] -= 1
        elif block_direction == 'down':
            block_position[1] += 1
        elif block_direction == 'left':
            block_position[0] -= 1
        elif block_direction == 'right':
            block_position[0] += 1
        last_moved_time = datetime.now()

    screen.fill(WHITE)
    draw_block(screen, GREEN, block_position)
    pygame.display.flip()
