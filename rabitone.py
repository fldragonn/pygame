# raywenderich.org tutorial
# https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python

import pygame

# pygame 창 생성하기
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# 이미지 불러오기

# 창 유지하기
while True:
    # 화면 흑색 채우기
    screen.fill((0, 0, 0))

    # 화면 다시 그리기
    pygame.display.flip()

    # 닫기 창을 누르면 게임 창을 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)