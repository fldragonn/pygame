# 벽돌 깨기
#
# 04_blocks_makeblock.py

import pygame

BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# 파이게임 초기화
pygame.init()

# 화면 생성
SC_WIDTH, SC_HEIGHT = 600, 800
SC_SIZE = (SC_WIDTH, SC_HEIGHT)
SCREEN = pygame.display.set_mode(SC_SIZE)


class Block:
    def __init__(self, color, rect, speed=0):
        self.color = color
        self.rect = rect
        self.speed = speed

    def draw(self):
        pygame.draw.rect(SCREEN, self.color, self.rect)


# 블록 객체 생성
BLOCKS = []
block_colors = [(250, 0, 0), (250, 160, 0), (240, 240, 0),
                (0, 130, 0), (130, 0, 130), (0, 0, 255)]

for y_pos, color in enumerate(block_colors):
    for x_pos in range(5):
        BLOCKS.append(Block(color, pygame.Rect(x_pos * 100 + 60, y_pos * 50 + 40, 80, 30)))

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면 그리기
    SCREEN.fill(BLACK)

    # 블록 그리기
    for one in BLOCKS:
        one.draw()

    pygame.display.update()

# 파이게임 종료
pygame.quit()
