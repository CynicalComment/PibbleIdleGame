import pygame

pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clicked = False
clock = pygame.time.Clock()
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('black')

    pygame.draw.circle(screen, "red", mouse_pos,20)
    #RENDER HERE
    pygame.display.flip()

    clock.tick(120)

pygame.quit()