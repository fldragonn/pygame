# 벽돌 깨기
#
# 03_blocks_ball

# 공 이동하기

import pygame

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)


class Block:
    def __init__(self, color, rect, speed = 0):
        self.color = color
        self.rect = rect
        self.speed = speed
        self.x_dir = 1
        self.y_dir = -1

    def move(self):
        self.rect.centerx += self.x_dir * self.speed
        self.rect.centery += self.y_dir * self.speed

    def draw(self):
        if self.speed == 0:
            pygame.draw.rect(SCREEN, self.color, self.rect)
        else:
            pygame.draw.ellipse(SCREEN, self.color, self.rect)



# 파이게임 초기화
pygame.init()

# 화면 생성
SC_WIDTH, SC_HEIGHT = (600, 800)
SC_SIZE = (SC_WIDTH, SC_HEIGHT)
SCREEN = pygame.display.set_mode(SC_SIZE)
pygame.display.set_caption('PY BLOCKS')

# 게임 객체 생성
PADDLE = Block(YELLOW, pygame.Rect(300, 700, 100, 30))
BALL = Block(YELLOW, pygame.Rect(300, 400, 20, 20), 10)

# 키 반복 설정
pygame.key.set_repeat(5, 5)

# 프레임 설정
FPS = pygame.time.Clock()

running = True
while running:
    FPS.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                PADDLE.rect.centerx -= 10
            if event.key == pygame.K_RIGHT:
                PADDLE.rect.centerx += 10

    # 공 이동
    if BALL.rect.centery < 1000:
        BALL.move()

    # 패들 충돌 확인
    if PADDLE.rect.colliderect(BALL.rect):
        BALL.y_dir *= -1

    # 공 벽 충돌 확인
    if BALL.rect.centerx < 0 or BALL.rect.centerx > SC_WIDTH:
        BALL.x_dir *= -1
    if BALL.rect.centery < 0:
        BALL.y_dir *= -1

    # 화면 그리기
    SCREEN.fill(BLACK)
    BALL.draw()
    PADDLE.draw()
    pygame.display.update()

# 파이게임 종료
pygame.quit()