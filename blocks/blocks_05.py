# 벽돌 깨기
#
# blocks_05
#
# 블록 충돌 처리

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

BLOCKS = []
PADDLE = Block(YELLOW, pygame.Rect(300, 700, 100, 30))
BALL = Block(YELLOW, pygame.Rect(300, 400, 20, 20), 5)

block_colors = [(255, 0, 0), (255, 165, 0), (242, 242, 0),
                (0, 128, 0), (128, 0, 128), (0, 0, 250)]

for y_pos, color in enumerate(block_colors):
    for x_pos in range(5):
        print(x_pos, y_pos, color)
        BLOCKS.append(Block(color, pygame.Rect(x_pos * 100 + 60, y_pos * 50 + 40, 80, 30)))

FPS = pygame.time.Clock()

pygame.key.set_repeat(5, 5)   # (지연시간, 간격 1/1000s)

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

    if BALL.rect.centery < 1000:
        BALL.move()

    # 블록 충돌
    prelen = len(BLOCKS)
    BLOCKS = [x for x in BLOCKS if not x.rect.colliderect(BALL.rect)]
    if len(BLOCKS) != prelen:
        BALL.y_dir *= -1

    # 공과 패들 충돌 확인
    if PADDLE.rect.colliderect(BALL.rect):
        BALL.y_dir *= -1

    # 공과 벽 충돌 확인
    if BALL.rect.centerx < 0 or BALL.rect.centerx > SC_WIDTH:
        BALL.x_dir *= -1
    if BALL.rect.centery < 0:
        BALL.y_dir *= -1

    screen.fill(BLACK)
    BALL.draw()
    PADDLE.draw()
    for one in BLOCKS:
        one.draw()

    if BALL.rect.centery > 800:
        running = False
    pygame.display.update()
    FPS.tick(30)

# 파이게임 종료
pygame.quit()