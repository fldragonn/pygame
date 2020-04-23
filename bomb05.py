import pygame

# 사용 변수 초기화
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)

SCREEN_WIDTH  = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 파이게임 초기화
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# 이미지 불러오기
player_url = 'resources/images/dude.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH // 2 - player_img.get_width() // 2,
                                 centery = SCREEN_HEIGHT - player_img.get_height())

# 키 반복 설정하기
# set_repeat(delay, interval) -> None
# pygame.key.set_repeat(1, 1)
# delay와 interval이 같으면 delay만 기록해도 동일한 효과를 준다.
pygame.key.set_repeat(1)

# 게임 메인 루프
while True:
    screen.fill(BLACK)

    # 키 이벤트 처리
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_pos.left -= 5
        elif event.key == pygame.K_RIGHT:
            player_pos.left += 5

    # 화면 끝 이동 불가
    if player_pos.left < 0:
        player_pos.left += 5
    elif player_pos.left + player_img.get_width() > SCREEN_WIDTH:
        player_pos.left -= 5

    # 주인공 그리기
    screen.blit(player_img, player_pos)

    pygame.display.flip()
    clock.tick(30)