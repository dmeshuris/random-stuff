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

    screen.fill((0, 225, 225))

# armor (chest-piece)
    pygame.draw.polygon(screen, (147, 147, 147), [(100, 200), (150, 175), (175, 375), (300, 375), (325, 175), (375, 200)])

# armor (helmet)

# skin
    pygame.draw.polygon(screen, (225, 200, 150), [(185, 199), (285, 199), (285, 124), (260, 99), (210, 99), (185, 124)])

# skin shadow left
    pygame.draw.polygon(screen, (210, 175, 125), [(154, 199), (195, 199), (185, 169), (151, 180)])

# skin shadow right
    pygame.draw.polygon(screen, (210, 175, 125), [(324, 180), (321, 199), (275, 199), (286, 169)])

    pygame.display.update()