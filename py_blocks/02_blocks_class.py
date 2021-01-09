# 벽돌 깨기
#
# 02_blocks_class

# 벽돌 클래스 생성 후 패들 이동하기

import pygame

# 파이게임 초기화
pygame.init()

SC_WIDTH, SC_HEIGHT = 600, 800
SC_SIZE = (SC_WIDTH, SC_HEIGHT)
SCREEN = pygame.display.set_mode(SC_SIZE)

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)


class Block:
    def __init__(self, color, rect, speed=0):
        self.color = color
        self.rect = rect
        self.speed = speed

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, self.rect)


PADDLE = Block(YELLOW, pygame.Rect(300, 700, 100, 30))
BALL = Block(YELLOW, pygame.Rect(300, 400, 20, 20), 10)
print("BALL: {}, PADDLE: {}".format(BALL.speed, PADDLE.speed))

pygame.key.set_repeat(5, 5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PADDLE.rect.centerx -= 10
            elif event.key == pygame.K_RIGHT:
                PADDLE.rect.centerx += 10

    SCREEN.fill(BLACK)
    BALL.draw()
    PADDLE.draw()
    pygame.display.update()

# 파이게임 종료
pygame.quit()
