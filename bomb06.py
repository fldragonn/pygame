# 폭탄 피하기

import pygame

# 사용 변수 초기화
BLACK = (0,     0,   0)
WHITE = (255, 255, 255)

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 파이게임 초기화
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# 키입력 반복 설정
pygame.key.set_repeat(1)

# 이미지 불러오기
player_url = "resources/images/dude.png"
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH // 2 - player_img.get_width() // 2,
                                 centery = SCREEN_HEIGHT - player_img.get_height())

bomb_url = "resources/images/badguy.png"
bomb_img = pygame.image.load(bomb_url)
bombs_pos = list()
for cnt in range(3):
    bomb_pos = bomb_img.get_rect(left = cnt * 100 + 100, top = cnt * 100 + 100)
    bombs_pos.append(bomb_pos)

while True:
    # 화면 클리어
    screen.fill(BLACK)

    # 키 입력 처리
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_pos.left -= 5
        if event.key == pygame.K_RIGHT:
            player_pos.left += 5

    # 화면 이동 범위 처리
    if player_pos.left < 0:
        player_pos.left += 5
    elif player_pos.left + player_img.get_width() > SCREEN_WIDTH:
        player_pos.left -= 5

    # 이미지 화면 출력
    screen.blit(player_img, player_pos)
    for tmp_pos in bombs_pos:
        screen.blit(bomb_img, tmp_pos)

    # 이미지 화면 업데이트
    pygame.display.flip()
    clock.tick(30)