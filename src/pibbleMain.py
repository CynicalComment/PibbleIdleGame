import pygame

pygame.init()
SCREEN_WIDTH = 600  
SCREEN_HEIGHT = 600
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

isCleaning = False
sprite = PibbleState[0]
rect = sprite.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
collision_rect = rect.inflate(-50, -100)

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if collision_rect.collidepoint(mouse_pos):
        isCleaning = True
        time_cleaning_elapsed += 1
        if time_cleaning_elapsed >= 100:
            time_elapsed = (time_elapsed + 1) % 5
            sprite = PibbleState[time_elapsed]
            rect = sprite.get_rect(center=rect.center)
            time_cleaning_elapsed = 0
    else:
        time_cleaning_elapsed = 0
        isCleaning = False
            

    screen.fill('black')

    
    screen.blit(sprite,rect)
    #screen.blit(pygame.draw.circle(screen,'pink',collision_rect,20),collision_rect)
    if isCleaning:
        pygame.draw.circle(screen, "pink", mouse_pos,10)
    #RENDER HERE
    pygame.display.flip()

    clock.tick(60)

pygame.quit()