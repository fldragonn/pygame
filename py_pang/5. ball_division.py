import pygame
import os

pygame.init()

clock = pygame.time.Clock()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode( (screen_width, screen_height) )

pygame.display.set_caption("PYPANG!")

cur_path = os.path.dirname(__file__)
img_path = os.path.join(cur_path, "images")

bg = pygame.image.load(os.path.join(img_path, "background.png"))

stage = pygame.image.load(os.path.join(img_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

character = pygame.image.load(os.path.join(img_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width // 2 - character_width // 2
character_y_pos = screen_height - stage_height - character_height
character_speed = 0

weapon = pygame.image.load(os.path.join(img_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_height = weapon_size[1]
weapon_x_pos = character_x_pos - weapon_width // 2
weapon_y_pos = character_y_pos
weapon_speed = 10

weapons = []

ball_imgs = [
    pygame.image.load(os.path.join(img_path, "balloon1.png")),
    pygame.image.load(os.path.join(img_path, "balloon2.png")),
    pygame.image.load(os.path.join(img_path, "balloon3.png")),
    pygame.image.load(os.path.join(img_path, "balloon4.png"))
]

ball_spd_y = [-18, -15, -12, -9]

balls = []

balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx" : 0,
    "to_x" : 3,
    "to_y" : -6,
    "init_y_spd" : ball_spd_y[0]
})

b_to_remove = -1
w_to_remove = -1

game_font = pygame.font.Font(None, 40)

total_time = 30
start_time = pygame.time.get_ticks()

game_result = "GAME OVER"

running = True
print(balls)
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_speed -= 5
            if event.key == pygame.K_RIGHT:
                character_speed += 5
            if event.key == pygame.K_SPACE:
                weapon_x_pos = character_x_pos + character_width // 2 - weapon_width // 2
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_speed = 0

    character_x_pos += character_speed

    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    for b_idx, one in enumerate(balls):
        one_size = ball_imgs[one["img_idx"]].get_rect().size
        one_width = one_size[0]
        one_height = one_size[1]

        if one["pos_y"] >= screen_height - stage_height - one_height:
            one["to_y"] = one["init_y_spd"]
        else:
            one["to_y"] += 0.5
        if one["pos_x"] > screen_width - one_width or one["pos_x"] < 0:
            one["to_x"] *= -1

        one["pos_x"] += one["to_x"]
        one["pos_y"] += one["to_y"]

    # 충돌 처
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for b_idx, ball_one in enumerate(balls):
        ball_one_pos_x = ball_one["pos_x"]
        ball_one_pos_y = ball_one["pos_y"]
        ball_one_img_idx = ball_one["img_idx"]

        ball_one_rect = ball_imgs[ball_one_img_idx].get_rect()
        ball_one_rect.left = ball_one_pos_x
        ball_one_rect.top = ball_one_pos_y

        if character_rect.colliderect(ball_one_rect):
            running = False
            break

        for w_idx, w_one in enumerate(weapons):
            w_one_pos_x = w_one[0]
            w_one_pos_y = w_one[1]

            w_one_rect = weapon.get_rect()
            w_one_rect.left = w_one_pos_x
            w_one_rect.top = w_one_pos_y

            if w_one_rect.colliderect(ball_one_rect):
                w_to_remove = w_idx
                b_to_remove = b_idx

                if ball_one_img_idx < 3:
                    ball_one_width = ball_one_rect.size[0]
                    ball_one_height = ball_one_rect.size[1]

                    small_ball_rect = ball_imgs[ball_one_img_idx + 1].get_rect()
                    small_ball_width = small_ball_rect[0]
                    small_ball_height = small_ball_rect[1]

                    balls.append({
                        "pos_x": ball_one_pos_x + (ball_one_width / 2) - (small_ball_width / 2),
                        "pos_y": ball_one_pos_y + (ball_one_height / 2) - (small_ball_height / 2),
                        "img_idx": ball_one_img_idx + 1,
                        "to_x": -3,
                        "to_y": -6,
                        "init_y_spd": ball_spd_y[ball_one_img_idx + 1]
                    })

                    balls.append({
                        "pos_x": ball_one_pos_x + (ball_one_width / 2) - (small_ball_width / 2),
                        "pos_y": ball_one_pos_y + (ball_one_height / 2) - (small_ball_height / 2),
                        "img_idx": ball_one_img_idx + 1,
                        "to_x": 3,
                        "to_y": -6,
                        "init_y_spd": ball_spd_y[ball_one_img_idx + 1]
                    })
                    print(balls)
                break

        if b_to_remove > -1:
            del balls[b_to_remove]
            b_to_remove = -1
            print("DEL Ball!!!")
            if len(balls) == 0:
                game_result = "MISSION COMPLETE"
                running = False
                break

        if w_to_remove > -1:
            del weapons[w_to_remove]
            w_to_remove = -1

    screen.blit(bg, (0, 0))
    for one in weapons:
        screen.blit(weapon, (one[0], one[1]))
    for one in balls:
        screen.blit(ball_imgs[one["img_idx"]], (one["pos_x"], one["pos_y"]))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
    timer = game_font.render("TIME : {}".format(int(total_time - elapsed_time)), True, (255, 255, 0))

    screen.blit(timer, (10, 10))

    if total_time - elapsed_time <= 0:
        game_result = "TIME OVER"
        running = False

    pygame.display.update()

msg = game_font.render(game_result, True, (255, 255, 255))
msg_rect = msg.get_rect(center=(screen_width // 2, screen_height // 2))
screen.blit(msg, msg_rect)
pygame.display.update()

print(game_result)
pygame.time.delay(2000)

pygame.quit()