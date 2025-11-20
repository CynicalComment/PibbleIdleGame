import pygame

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clicked = False
run = True
while run:

    if (pygame.mouse.get_pressed()[0]) == True:
        print("left mouse click")
    if (pygame.mouse.get_pressed()[2]) == True:
        print("Right mouse click")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()