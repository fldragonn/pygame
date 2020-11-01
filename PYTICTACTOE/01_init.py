# TIC TAC TOE

import pygame

pygame.init()

screen_width  = 450
screen_height = 450
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('TIC TAC TOE')

# 격자 설정
CELL_SIZE = 150
ROW_COUNT = screen_width // 3
COL_COUNT = screen_height // 3
GRAY  = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
YELLOW = (255, 255, 0)

TTTData = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
Turn = 'X'

running = True

pygame.font.init()
# font_list = pygame.font.get_fonts()
# print(font_list)
turn_font = pygame.font.SysFont('Comic Sans MS', 50)
result_font = pygame.font.SysFont('arialblack', 70)
turn_x = turn_font.render('X', True, YELLOW)
turn_o = turn_font.render('O', True, YELLOW)
victory_x = result_font.render('Winner X', True, WHITE)
victory_o = result_font.render('Winner O', True, WHITE)

def cellpt_to_listpt(m_pos):
    for x in range(COL_COUNT):
        for y in range(ROW_COUNT):
            if m_pos[0] >= x * CELL_SIZE and m_pos[0] < x * CELL_SIZE + CELL_SIZE:
                if m_pos[1] >= y * CELL_SIZE and m_pos[1] < y * CELL_SIZE + CELL_SIZE:
                    row = y
                    col = x
                    break
    return row, col

def print_mark(r, c):
    global Turn
    TTTData[r][c] = Turn
    turn_o_rect = turn_o.get_rect().size
    turn_o_width = turn_o_rect[0]
    turn_o_height = turn_o_rect[1]
    prn_x = c * CELL_SIZE + CELL_SIZE // 2 - turn_o_width // 2
    prn_y = r * CELL_SIZE + CELL_SIZE // 2 - turn_o_height // 2
    if Turn == 'O':
        screen.blit(turn_o, (prn_x, prn_y))
    else:
        screen.blit(turn_x, (prn_x, prn_y))
    print(TTTData)

'''
0, 0 0, 1 0, 2
1, 0 1, 1 1, 2
2, 0 2, 1 2, 2
\ r - c = 0
/ r - c = 2, -2
'''

def resetData():
    global TTTData, Turn
    TTTData = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    Turn = 'X'
    screen.fill(BLACK)
    pygame.display.update()

def print_winner(prnTurn):

        # pygame은 RGBA(alpha)를 지원하지 않는다.
        # 서피스를 생성해 그 서피스에 투명도를 설정해 투명한 이미지를 출력한다.

    result_surface = pygame.Surface( (screen_width, screen_height) )
    result_surface.set_alpha(200)
    result_surface.fill(BLACK)
    screen.blit(result_surface, (0, 0))

    victory_rect = victory_x.get_rect(center = (screen_width // 2, screen_height // 2))
    if prnTurn == 'X':
        screen.blit(victory_x, victory_rect)
    else:
        screen.blit(victory_o, victory_rect)
    pygame.display.update()

    pygame.time.delay(2000)
    resetData()
    py_main()

def check_winner(r, c):
    global running
    mark_col = mark_row = mark_cross = 0
    for i in range(3):
        if TTTData[r][i] == Turn:
            mark_col += 1
        if TTTData[i][c] == Turn:
            mark_row += 1
    if r - c == 0:
        if TTTData[0][0] == Turn and TTTData[1][1] == Turn and TTTData[2][2] == Turn:
            mark_cross = 3
    if abs(r - c) == 2:
        if TTTData[0][2] == Turn and TTTData[1][1] == Turn and TTTData[2][0] == Turn:
            mark_cross = 3

    if mark_row == 3 or mark_col == 3 or mark_cross == 3:
        print("VICTORY", Turn)
        print_winner(Turn)
        running = False

def change_mark():
    global  Turn
    if Turn == 'O':
        Turn = 'X'
    else:
        Turn = 'O'

def py_main():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                r, c = cellpt_to_listpt(mouse_pos)
                if TTTData[r][c] == 0:
                    TTTData[r][c] = Turn
                    print_mark(r, c)
                    check_winner(r, c)
                    change_mark()

                if event.button == 2:
                    running = False

        # 격자 그리기
        for x in range(COL_COUNT):
            for y in range(ROW_COUNT):
                cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, GRAY, cell_rect, 3)    # 3은 테두리 두께

        # 화면 업데이트
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    py_main()