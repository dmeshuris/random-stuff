import pygame

pygame.init()

screenX = 500
screenY = 500

screen = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption('shapes IDK')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((225, 225, 225))

    pygame.draw.rect(screen, (210, 175, 125), (100, 100, 150, 300))

    pygame.draw.rect(screen, (225, 200, 150), (250, 100, 150, 300))

    pygame.display.update()