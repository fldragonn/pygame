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

# FPS
clock = pygame.time.Clock()

# 배경 이미지 설정하기
background = pygame.image.load(os.path.join("pypang_img", "bg_img.png"))

# 캐릭터(스프라이트) 불러오기
player = pygame.image.load(os.path.join("pypang_img", "player.png"))
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_xpos = screen_width / 2 - player_width / 2
player_ypos = screen_height - player_height

# 이동할 좌표
player_speed = 0.6;
to_x = 0
to_y = 0

# event loop
running = True
while running:
    dt = clock.tick(30)

    # print("fps: " + str(clock.get_fps()))

    # 1초당 100픽셀씩 이동 시
    # 10 fps: 1초에 10프레임 - 1번에 10만큼 이동: 10 * 10 = 100
    # 20 fps: 1초에 20프레임 - 1번에 5만큼 이동: 20 * 5 = 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                to_x += player_speed
            elif event.key == pygame.K_UP:
                to_y -= player_speed
            elif event.key == pygame.K_DOWN:
                to_y += player_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    player_xpos += to_x * dt
    player_ypos += to_y * dt

    if player_xpos < 0:
        player_xpos = 0
    elif player_xpos > screen_width - player_width:
        player_xpos = screen_width - player_width
    if player_ypos < 0:
        player_ypos = 0
    elif player_ypos > screen_height - player_height:
        player_ypos = screen_height - player_height

# 배경 그리기
    # screen.fill((0, 200, 255))
    screen.blit(background, (0, 0))

    # 캐릭터 그리기
    screen.blit(player, (player_xpos, player_ypos))
    pygame.display.update()

# pygame 종료
pygame.quit()