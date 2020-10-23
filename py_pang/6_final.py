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

balls = []
balls.append({
    'pos_x' : 50,
    'pos_y' : 50,
    'to_x' : 3,
    'to_y' : -6,
    'img_idx' : 0,
    'init_spd_y' : ball_speed_y[0]
})

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

    screen.blit(background_img, (0, 0))
    for one in weapons:
        screen.blit(weapon_img, (one[0], one[1]))

    for cur_ball in balls:
        screen.blit(ball_img[cur_ball['img_idx']], (cur_ball['pos_x'], cur_ball['pos_y']))

    screen.blit(stage_img, (0, screen_height - stage_height))
    screen.blit(character_img, (character_pos_x, character_pos_y))
    pygame.display.update()

# 파이게임 종료
pygame.quit()