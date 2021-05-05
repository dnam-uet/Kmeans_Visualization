import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 700))

pygame.display.set_caption("Kmeans Visualization")

running = True

clock = pygame.time.Clock()

FPS = 60

BACKGROUND = (215, 215, 215)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BACKGROUND_PANEL = (249, 255, 230)

font = pygame.font.SysFont('sans', 40)
TEXT_PLUS = font.render('+', True, WHITE)

while running:
    clock.tick(FPS)
    screen.fill(BACKGROUND)

    # Draw interface
    # Draw panel
    pygame.draw.rect(screen, BLACK, (50, 50, 700, 500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55, 55, 690, 490))
    
    # K button +
    pygame.draw.rect(screen, BLACK, (850, 50, 50, 50))
    screen.blit(TEXT_PLUS, (860, 50))

    # End draw interface

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the full display Surface to the screen
    pygame.display.flip()

pygame.quit()