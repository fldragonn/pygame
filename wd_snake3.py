import  pygame
import random

# pygame 초기화 및 화면 구성
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("SNAKE")

clock = pygame.time.Clock()

# 색상 설정
WHITE = (255, 255, 255)
GREEN = (  0, 255,   5)
BLACK = (  0,   0,   0)
GRAY  = (128, 128, 128)
BLUE  = (  0,   0, 255)

# 그리드 설정
CELL_SIZE = 40
COL_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

# 방향설정
LEFT = 0
RIGHT = 1
UP = 2
DOWN = 3
direction = DOWN

# 뱀 초기화
bodies = [(COL_COUNT // 2, ROW_COUNT // 2)]

# 먹이 초기화
foods = []
for _ in range(10):
    while True:
        c_idx = random.randint(0, COL_COUNT - 1)
        r_idx = random.randint(0, ROW_COUNT - 1)
        food_pos = (c_idx, r_idx)
        if food_pos not in foods and food_pos not in bodies:
            foods.append(food_pos)
            break

# 게임 루프
while True:

    # 이벤트 처리
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            direction = LEFT
        elif event.key == pygame.K_RIGHT:
            direction = RIGHT
        elif event.key == pygame.K_UP:
            direction = UP
        elif event.key == pygame.K_DOWN:
            direction = DOWN

    head = bodies[0]
    if direction == LEFT:
        c_idx = head[0] - 1
        r_idx = head[1]
    elif direction == RIGHT:
        c_idx = head[0] + 1
        r_idx = head[1]
    elif direction == UP:
        c_idx = head[0]
        r_idx = head[1] - 1
    elif direction == DOWN:
        c_idx = head[0]
        r_idx = head[1] + 1

    bodies.insert(0, (c_idx, r_idx))
    bodies.pop()
    print(bodies[0][0], bodies[0][1])

    # 화면 처리
    screen.fill(BLACK)

    # 격자 그리기
    for r in range(ROW_COUNT):
        for c in range(COL_COUNT):
            grid = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE,
                               CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, grid, 1)

    # 먹이 그리기
    for c, r in foods:
        food = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE,
                           CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, WHITE, food)

    # 뱀 그리기
    for c, r in bodies:
        body = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE,
                           CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, BLUE, body)

    pygame.display.update()
    clock.tick(5)
pygame.quit()