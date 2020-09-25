import pygame

pygame.init()

screen_width = 640
screen_height = 480
screen_size = (screen_width, screen_height)

pygame.display.set_mode(screen_size)
pygame.display.set_caption("PyPang!")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()