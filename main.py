import pygame

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

X = 1920
Y = 1080

display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

font = pygame.font.Font('freesansbold.ttf', 220)

text = font.render('Intermission', True, green, white)
textRect = text.get_rect()
textRect.center = (X // 2, Y // 2)


while True:
    display_surface.fill(white)
    display_surface.blit(text, textRect)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:
                text = font.render('Get Bows', True, green, white)
                textRect = text.get_rect()
                textRect.center = (X // 2, Y // 2)
            elif event.key == pygame.K_KP2:
                text = font.render('Shoot', True, green, white)
                textRect = text.get_rect()
                textRect.center = (X // 2, Y // 2)
            elif event.key == pygame.K_KP3:
                text = font.render('Get Arrows', True, green, white)
                textRect = text.get_rect()
                textRect.center = (X // 2, Y // 2)
            elif event.key == pygame.K_KP4:
                text = font.render('STOP', True, (255, 0, 0), white)
                textRect = text.get_rect()
                textRect.center = (X // 2, Y // 2)

        pygame.display.update()
