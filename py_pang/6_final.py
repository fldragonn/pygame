# PYPANG

import pygame
import os

# 파이게임 초기화
pygame.init()

# 창 만들기
screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PYPANG!!!")

# 이미지 경로 추출
cur_path = os.path.dirname(__file__)
img_path = os.path.join(cur_path, 'images')

# 이미지 불러오기
background_img = pygame.image.load(os.path.join(img_path, 'background.png'))

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background_img, (0, 0))
    pygame.display.update()

# 파이게임 종료
pygame.quit()