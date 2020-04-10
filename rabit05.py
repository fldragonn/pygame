# raywenderich.org tutorial
# https://www.raywenderlich.com/2795-beginning-game-programming-for-teens-with-python

import pygame, math

# 파이게임 초기화
pygame.init()

# 화면 설정
width, height = 640, 480

# 게임 스프라이트 초기화
screen = pygame.display.set_mode((width, height))
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")
arrow = pygame.image.load("resources/images/bullet.png")

acc = [0, 0]
arrows = []

# 키 설정
keys = [False, False, False, False]
playpos = [100, 100]

while True:
    screen.fill((0, 0, 0))

    for bx in range(width // grass.get_width() + 1):
        for by in range(height // grass.get_height() + 1):
            screen.blit(grass, (bx * grass.get_width(), by * grass.get_height()))

    for cy in range(height // castle.get_height()):
        screen.blit(castle, (0, 30 + cy * castle.get_height()))

    # screen.blit(player, playpos)

    position = pygame.mouse.get_pos()
    # 주인공 캐릭터와 마우스 포인터 위치로 각도를 구한다.
    angle = math.atan2(position[1]-(playpos[1] + player.get_width() // 2),
                       position[0]-(playpos[0] + player.get_height() // 2))
    # 각도를 래디언에서 디그리로 변경한다.
    playrot = pygame.transform.rotate(player, 360 - math.degrees(angle))
    # 회전된 캐릭터의 중심을 구해 중심점을 이동한다.
    playpos1 = (playpos[0]-playrot.get_rect().width//2, playpos[1]-playrot.get_rect().height//2)

    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            arrows.pop(index)
        index += 1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360 - math.degrees(projectile[0]))
            screen.blit(arrow1, (projectile[1], projectile[2]))

    screen.blit(playrot, playpos1)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys[0] = True
            if event.key == pygame.K_a:
                keys[1] = True
            if event.key == pygame.K_s:
                keys[2] = True
            if event.key == pygame.K_d:
                keys[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            if event.key == pygame.K_a:
                keys[1] = False
            if event.key == pygame.K_s:
                keys[2] = False
            if event.key == pygame.K_d:
                keys[3] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append([math.atan2(position[1]-(playpos[1] + player.get_width() // 2),
                                     position[0]-(playpos[0] + player.get_height() // 2)),
                          playpos1[0] + player.get_width() // 2,
                          playpos1[1] + player.get_height() // 2])

    if keys[0]:
        playpos[1] -= 5
    elif keys[2]:
        playpos[1] += 5
    if keys[1]:
        playpos[0] -= 5
    elif keys[3]:
        playpos[0] += 5