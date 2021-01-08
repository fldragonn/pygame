# 벽돌 깨기
#
# blocks_01
#
# 패들 이동하기

import pygame

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


class Block:
    def __init__(self, col, rect, speed=0):
        self.col = col
        self.rect = rect
        self.speed = speed
        self.x_dir = 1
        self.y_dir = -1

    def move(self):
        self.rect.centerx += self.x_dir * self.speed
        self.rect.centery += self.y_dir * self.speed

    def draw(self):
        if self.speed == 0:
            pygame.draw.rect(screen, self.col, self.rect)
        else:
            pygame.draw.ellipse(screen, self.col, self.rect)


# 파이게임 초기화
pygame.init()

SC_WIDTH, SC_HEIGHT = 600, 800
SC_SIZE = (SC_WIDTH, SC_HEIGHT)
screen = pygame.display.set_mode(SC_SIZE)

pygame.display.set_caption('BLOCKS')

PADDLE = Block(YELLOW, pygame.Rect(300, 700, 100, 30))
BALL = Block(YELLOW, pygame.Rect(300, 400, 20, 20))

pygame.key.set_repeat(5, 5) # (지연시간, 간격 1/1000s)

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

    screen.fill(BLACK)
    BALL.draw()
    PADDLE.draw()
    pygame.display.update()

# 파이게임 종료
pygame.quit()