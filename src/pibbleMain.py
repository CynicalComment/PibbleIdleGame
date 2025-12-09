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

sprite = PibbleState[0]
rect = sprite.get_rect(center=(200,200))
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if rect.collidepoint(mouse_pos):
        time_cleaning_elapsed += 1
        if time_cleaning_elapsed >= 10:
            time_elapsed = (time_elapsed + 1) % 5
            sprite = PibbleState[time_elapsed]
            time_cleaning_elapsed = 0
    else:
        time_cleaning_elapsed = 0
            

    screen.fill('black')

    pygame.draw.circle(screen, "pink", mouse_pos,10)
    screen.blit(sprite,rect)
    #RENDER HERE
    pygame.display.flip()

    clock.tick(60)

pygame.quit()