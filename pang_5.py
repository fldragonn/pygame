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

# 공 (스프라이트) 불러오기
enemy = pygame.image.load(os.path.join("pypang_img", "enemy.png"))
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_xpos = screen_width / 2 - enemy_width / 2
enemy_ypos = screen_height / 2 - enemy_height / 2

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks()

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

    # 충돌 처리를 위한 정보 업데이트
    player_rect = player.get_rect()
    player_rect.left = player_xpos
    player_rect.top = player_ypos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_xpos
    enemy_rect.top = enemy_ypos

    # 충돌 처리
    if player_rect.colliderect(enemy_rect):
        print("충돌")
        running = False

    # 배경 그리기
    # screen.fill((0, 200, 255))
    screen.blit(background, (0, 0))

    # 캐릭터 그리기
    screen.blit(player, (player_xpos, player_ypos))

    # 적 그리기
    screen.blit(enemy, (enemy_xpos, enemy_ypos))

    # 시간 경과 (ms을 second으로 변경)
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    screen.blit(timer, (10, 10))

    # 시간 종료 > 게임 종료
    if total_time - elapsed_time < 0:
        print("타임 아웃")
        running = False

    # 화면 다시그리기
    pygame.display.update()

# 대기
pygame.time.delay(2000)

# pygame 종료
pygame.quit()
