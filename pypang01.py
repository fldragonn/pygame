import pygame
import os

# pygame 초기화
pygame.init()

# 화면 설정
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("PYPANG!")

# FPS
clock = pygame.time.Clock()

# 게임 초기화
current_path = os.path.dirname(__file__) # 현재 파일의 경로 반환
image_path = os.path.join(current_path, "pypang_img")

# 배경  만들기
bg = pygame.image.load(os.path.join(image_path, "bg.png"))
ground = pygame.image.load(os.path.join(image_path, "ground.png"))
ground_size = ground.get_rect().size
ground_height = ground_size[1]

# 주인공 만들기
player = pygame.image.load(os.path.join(image_path, 'player.png'))
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_x_pos = SCREEN_WIDTH / 2 - player_width / 2
player_y_pos = SCREEN_HEIGHT - player_height - ground_height

running = True
while running:
    dt = clock.tick(30)

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 게임 캐릭터 처리

    # 충돌 처리

    # 화면 출력
    screen.blit(bg, (0, 0))
    screen.blit(ground, (0, SCREEN_HEIGHT - ground_height))
    screen.blit(player, (player_x_pos, player_y_pos))
    pygame.display.update()

pygame.quit()