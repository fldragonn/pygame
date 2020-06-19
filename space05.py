# 스페이스 인베이더

import pygame
import os
import random

# 변수 설정
WHITE = (255, 255, 255)
SCREEN_WIDTH = SCREEN_HEIGHT = 750
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 창 타이틀 설정
pygame.display.set_caption("SPACE INVADER")

# 파이게임 초기화
pygame.init()
pygame.font.init()
WIN = pygame.display.set_mode(SCREEN_SIZE)

# 배경 이미지 처리
bg_img = pygame.image.load(os.path.join('assets', 'background-black.png'))
bg_img = pygame.transform.scale(bg_img, SCREEN_SIZE)

# 메인 함수
def main():
    run = True

    # 화면 갱신
    def redraw_window():
        WIN.blit(bg_img, (0, 0))

        pygame.display.update()

    while run:
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

main()