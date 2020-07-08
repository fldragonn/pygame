import pygame
import os

# 파이게임 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("PyPang")

# 배경 이미지 설정하기
background = pygame.image.load(os.path.join("pypang_img", "bg_img.png"))

# event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 배경 그리기
    # screen.fill((0, 200, 255))
    screen.blit(background, (0, 0))
    pygame.display.update()

# pygame 종료
pygame.quit()
