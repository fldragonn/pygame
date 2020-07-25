import pygame
import os

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Py Pang")

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_xpos = (screen_width // 2) - (character_width // 2)
character_ypos = screen_height - stage_height - character_height

# 캐릭터 이동 방향
character_to_x = 0

# 캐릭터 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon.size[0]

# 무기는 한 번에 여러발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

running = True
while running:
    dt = clock.tick(30)

    # 이벤트 처리(키보드, 마우스)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_xpos + (character_width // 2) - (weapon_width // 2)
                weapon_y_pos = character_ypos
                weapons.append([weapon_x_pos, weapon_y_pos])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 게임 캐릭터 위치 정의
    character_xpos += character_to_x

    if character_xpos < 0:
        character_xpos =0
    elif character_xpos > screen_width - character_width:
        character_xpos = screen_width - character_width

    # 무기 위치 조정
    weapons = [ [w[0], w[1]] - weapon_speed for w in weapons]
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    #
    # for idx, one in enumerate(weapons):
    #     weapons[idx][1] = one[1] - weapon_speed

    # 화면 그리기
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    screen.blit(stage, (0, screen_height-stage_height))
    screen.blit(character, (character_xpos, character_ypos))

    pygame.display.update()

pygame.quit()