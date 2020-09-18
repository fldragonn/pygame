import os
import pygame

# pygame 초기화
pygame.init()

# 화면 설정
screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PYPANG!")

# FPS
clock = pygame.time.Clock()

# 이미지 경로 설정
current_path = os.path.dirname(__file__)
img_path = os.path.join(current_path, 'pypang_img')

# 배경 불러오기
bg = pygame.image.load(os.path.join(img_path, 'bg.png'))
ground = pygame.image.load(os.path.join(img_path, 'ground.png'))
ground_size = ground.get_rect().size
ground_height = ground_size[1]

# 플레이어 불러오기
player = pygame.image.load(os.path.join(img_path, 'player.png'))
player_size = player.get_rect().size
player_width = player_size[0]
player_height = player_size[1]
player_xpos = screen_width / 2 - player_width / 2
player_ypos = screen_height - ground_height - player_height

# 캐릭터 이동 방향, 속도
player_to_x = 0
player_speed = 5

# 무기 불러오기
weapon = pygame.image.load(os.path.join(img_path, 'arrow.png'))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# 무기 초기화, 속도
weapons = []
weapon_speed = 10

# 게임 루프
running = True

while running:
    dt = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키 입력 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_to_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_to_x += player_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = player_xpos + player_width / 2 - weapon_width / 2
                weapon_y_pos = player_ypos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_to_x = 0

    # 플레이어 이동하기
    player_xpos += player_to_x

    # 플레이어 화면 위치 확인
    if player_xpos < 0:
        player_xpos = 0
    elif player_xpos > screen_width - player_width:
        player_xpos = screen_width - player_width

    # 무기 이동
    # print(weapons)
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]
    # print("=" * 30)
    # print(weapons)

    # a = [x * 2 for x in range(1, 10)]
    # a = [x * 2 for x in range(1, 10) if x * 2 > 10]

    # 화면 출력
    screen.blit(bg, (0, 0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(ground, (0, screen_height - ground_height))
    screen.blit(player, (player_xpos, player_ypos))

    pygame.display.update()

# 게임 종료
pygame.quit()