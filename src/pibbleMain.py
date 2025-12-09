import pygame

pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clicked = False
clock = pygame.time.Clock()

PibbleState = [
    pygame.image.load("Pibble-01.png"),
    pygame.image.load("Pibble-02.png"),
    pygame.image.load("Pibble-03.png"),
    pygame.image.load("Pibble-04.png"),
    pygame.image.load("Pibble-05.png"),
]

time_elapsed = 0
time_cleaning_elapsed = 0
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

    clock.tick(60)

pygame.quit()