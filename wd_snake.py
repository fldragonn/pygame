import pygame

pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

CELL_SIZE = 40
COLUMN_COUNT = SCREEN_WIDTH // CELL_SIZE
ROW_COUNT = SCREEN_HEIGHT // CELL_SIZE

bodies = [(COLUMN_COUNT // 2, ROW_COUNT // 2)]

while True:
    screen.fill(BLACK)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    for column_index in range(COLUMN_COUNT):
        for row_index in range(ROW_COUNT):
            rect = (CELL_SIZE * column_index, CELL_SIZE * row_index,
                    CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

    for column_index, row_index in bodies:
        pygame.draw.rect(screen, BLUE, (CELL_SIZE * column_index,
                                        CELL_SIZE * row_index,
                                        CELL_SIZE, CELL_SIZE))
    pygame.display.update()
    clock.tick(5)

pygame.quit()