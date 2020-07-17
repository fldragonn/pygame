# p_snake05.py
#
# display score

import pygame
import random

# 화면 그리기
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYSNAKE")
clock = pygame.time.Clock()

# 변수 초기화
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
direction = DOWN

SCORE = 0

# 글꼴 설정
small_font = pygame.font.SysFont('comicsans', 40)

# 뱀 좌표 리스트 만들기
bodies = [(COL_COUNT // 2, ROW_COUNT // 2)]

# 먹이 10개 위치 리스트 만들기
foods = []

def add_food():
    while True:
        c_idx = random.randint(0, COL_COUNT - 1)
        r_idx = random.randint(0, ROW_COUNT - 1)
        f_pos = (c_idx, r_idx)
        if f_pos not in bodies or f_pos not in foods:
            foods.append(f_pos)
            break

for _ in range(10):
    add_food()

# 게임 루프
while True:
    # 키 처리
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    # 키에 따른 방향 설정
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            direction = LEFT
        elif event.key == pygame.K_RIGHT:
            direction = RIGHT
        elif event.key == pygame.K_UP:
            direction = UP
        elif event.key == pygame.K_DOWN:
            direction = DOWN

    # 뱀 머리를 추출하고 다음 방향으로 이동
    head = bodies[0]
    c_idx = head[0]
    r_idx = head[1]
    if direction == LEFT:
        c_idx = c_idx - 1
    elif direction == RIGHT:
        c_idx = c_idx + 1
    elif direction == UP:
        r_idx = r_idx - 1
    elif direction == DOWN:
        r_idx = r_idx + 1
    bodies.insert(0, (c_idx, r_idx))


    # 먹이 먹기
    if (c_idx, r_idx) in foods:
        foods.remove((c_idx, r_idx))
        add_food()
        SCORE += 10
    else:
        # 뱀 꼬리는 제거
        bodies.pop()

    # 화면 초기화
    screen.fill(BLACK)

    # 격자 그리기
    for c_idx in range(COL_COUNT):
        for r_idx in range(ROW_COUNT):
            one_rect = (c_idx * CELL_SIZE, r_idx * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, one_rect, 1)

    # 먹이 그리기
    for food in foods:
        f_rect = (food[0] * CELL_SIZE, food[1] * CELL_SIZE,
                  CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, GREEN, f_rect)

    # 뱀 그리기
    for one in bodies:
        b_rect = (one[0] * CELL_SIZE, one[1] * CELL_SIZE,
                  CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, BLUE, b_rect)

    # 점수 출력하기
    score_img = small_font.render(f"SCORE: {SCORE}", True, WHITE)
    screen.blit(score_img, (10, 10))

    # 화면 업데이트
    pygame.display.update()
    clock.tick(5)

# 게임 종료
pygame.quit()
