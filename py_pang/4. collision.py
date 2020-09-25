import pygame
import os

pygame.init()

screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("PyPang!")

clock = pygame.time.Clock()

path = os.path.dirname(__file__)
img_path = os.path.join(path, "images")

# 배경 만들기
background = pygame.image.load(os.path.join(img_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(img_path, "stage.png"))
stage_height = stage.get_rect().size[1]

# 캐릭터 만들기
character = pygame.image.load(os.path.join(img_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - stage_height - character_height
character_to_x = 0
character_speed = 5

# 무기 만들기
weapon = pygame.image.load(os.path.join(img_path, "weapon.png"))
weapon_width = weapon.get_rect().size[0]

# 무기 저장소
weapons = []

# 무기 이동 속도
weapon_speed = 10

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키 입력 처리
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + (character_width // 2) - weapon_width // 2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 캐릭터 위치 업데이트
    character_x_pos += character_to_x

    # 무기 위치 업데이트
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # 화면그리기
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    for one in weapons:
        screen.blit(weapon, (one[0], one[1]))
    pygame.display.update()

pygame.quit()