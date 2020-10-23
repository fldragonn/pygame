# PYPANG

import pygame
import os

# 파이게임 초기화
pygame.init()

# fps
clock = pygame.time.Clock()

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
stage_img = pygame.image.load(os.path.join(img_path, 'stage.png'))
stage_rect = stage_img.get_rect().size
stage_height = stage_rect[1]

# 캐릭터 초기화
character_img = pygame.image.load(os.path.join(img_path, 'character.png'))
character_rect = character_img.get_rect().size
character_width = character_rect[0]
character_height = character_rect[1]
character_pos_x = screen_width // 2 - character_width // 2
character_pos_y = screen_height - stage_height - character_height
character_speed = 0;

# 무기 초기화
weapon_img = pygame.image.load(os.path.join(img_path, 'weapon.png'))
weapon_rect = weapon_img.get_rect().size
weapon_width = weapon_rect[0]
weapon_height = weapon_rect[1]
weapon_pos_x = character_pos_x + character_width // 2 - weapon_width // 2
weapon_pos_y = character_pos_y
weapon_speed = 10
weapons = []  # 무기 리스트 초기화

# 공 초기화
ball_img = [
    pygame.image.load(os.path.join(img_path, 'balloon1.png')),
    pygame.image.load(os.path.join(img_path, 'balloon2.png')),
    pygame.image.load(os.path.join(img_path, 'balloon3.png')),
    pygame.image.load(os.path.join(img_path, 'balloon4.png'))
]

ball_speed_y = [-18, -15, -12, -9]

balls = [{
    'pos_x': 50,
    'pos_y': 50,
    'to_x': 3,
    'to_y': -6,
    'img_idx': 0,
    'init_spd_y': ball_speed_y[0]
}]

# 사라질 공, 무기 인덱스
remove_weapon_idx = -1
remove_ball_idx = -1

# 폰트 설정 및 타이머 초기화
game_font = pygame.font.Font(None, 40)

total_time = 30
start_time = pygame.time.get_ticks()

game_result = "GAME OVER"

# 게임 루프
running = True
while running:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_speed -= 5
            elif event.key == pygame.K_RIGHT:
                character_speed += 5
            # elif event.key == pygame.K_SPACE and len(weapons) < 1:
            elif event.key == pygame.K_SPACE:
                weapon_pos_x = character_pos_x + character_width // 2 - weapon_width // 2
                weapon_pos_y = character_pos_y
                weapons.append([weapon_pos_x, weapon_pos_y])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_speed = 0

    # 캐릭터 이동
    character_pos_x += character_speed

    # 무기 이동
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # 공 이동
    for cur_ball in balls:
        cur_ball_img = ball_img[cur_ball['img_idx']]
        cur_ball_rect = cur_ball_img.get_rect().size
        cur_ball_width = cur_ball_rect[0]
        cur_ball_height = cur_ball_rect[1]

        if cur_ball['pos_x'] < 0 or cur_ball['pos_x'] > screen_width - cur_ball_width:
            cur_ball['to_x'] *= -1
        if cur_ball['pos_y'] > screen_height - stage_height - cur_ball_height:
            cur_ball['to_y'] = cur_ball['init_spd_y']
        else:
            cur_ball['to_y'] += 0.5

        cur_ball['pos_x'] += cur_ball['to_x']
        cur_ball['pos_y'] += cur_ball['to_y']

    # 충돌 처리
    for idx_ball, one_ball in enumerate(balls):
        one_ball_rect = ball_img[one_ball['img_idx']].get_rect()
        one_ball_rect.top =one_ball['pos_y']
        one_ball_rect.left = one_ball['pos_x']

        character_rect = character_img.get_rect()
        character_rect.top = character_pos_y
        character_rect.left = character_pos_x

        # 공과 캐릭터 충돌 처
        if one_ball_rect.colliderect(character_rect):
            running = False
            # print("DEAD")

        # 무기와 공 출동 처리
        for idx_weapon, one_weapon in enumerate(weapons):
            one_weapon_rect = weapon_img.get_rect()
            one_weapon_rect.top = one_weapon[1]
            one_weapon_rect.left = one_weapon[0]
            if one_ball_rect.colliderect(one_weapon_rect):
                remove_ball_idx = idx_ball
                remove_weapon_idx = idx_weapon
                if one_ball['img_idx'] < 3:
                    one_ball_width = one_ball_rect.size[0]
                    one_ball_height = one_ball_rect.size[1]

                    small_ball_rect = ball_img[one_ball['img_idx']].get_rect().size
                    small_ball_width = small_ball_rect[0]
                    small_ball_height = small_ball_rect[1]

                    balls.append({
                        "pos_x": one_ball['pos_x'] + one_ball_width // 2 - small_ball_width // 2,
                        "pos_y": one_ball['pos_y'] + one_ball_height // 2 - small_ball_height // 2,
                        "img_idx": one_ball['img_idx'] + 1,
                        "to_x": 3,
                        "to_y": -6,
                        "init_spd_y": ball_speed_y[one_ball['img_idx'] + 1]
                    })
                    balls.append({
                        "pos_x": one_ball['pos_x'] + one_ball_width // 2 - small_ball_width // 2,
                        "pos_y": one_ball['pos_y'] + one_ball_height // 2 - small_ball_height // 2,
                        "img_idx": one_ball['img_idx'] + 1,
                        "to_x": -3,
                        "to_y": -6,
                        "init_spd_y": ball_speed_y[one_ball['img_idx'] + 1]
                    })
                break
                # print("HIT!")

        # 충돌 객체 지우기
        if remove_ball_idx > -1:
            del balls[remove_ball_idx]
            remove_ball_idx = -1

            if len(balls) == 0:
                running = False
                game_result = "YOU WIN!"

        if remove_weapon_idx > -1:
            del weapons[remove_weapon_idx]
            remove_weapon_idx = -1

    # 화면 그리기
    screen.blit(background_img, (0, 0))
    for one in weapons:
        screen.blit(weapon_img, (one[0], one[1]))

    for cur_ball in balls:
        screen.blit(ball_img[cur_ball['img_idx']], (cur_ball['pos_x'], cur_ball['pos_y']))

    screen.blit(stage_img, (0, screen_height - stage_height))
    screen.blit(character_img, (character_pos_x, character_pos_y))

    # 타이머 출력
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    timer = game_font.render("TIME: {}".format(int(total_time - elapsed_time)), True, (255, 255, 0))
    screen.blit(timer, (10, 10))

    if int(total_time - elapsed_time) < 1:
        game_result = "TIME OVER"
        start_time = pygame.time.get_ticks()
        running = False

    pygame.display.update()

# 메세지 출력
msg = game_font.render(game_result, True, (255, 255, 0))
msg_rect = msg.get_rect(center = (screen_width // 2, screen_height // 2))
screen.blit(msg, msg_rect)
pygame.display.update()
pygame.event.pump()  # pygame 내부 동작 처리

pygame.time.delay(2000)

# 파이게임 종료
pygame.quit()