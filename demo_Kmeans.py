import pygame

def create_button(buttonName, buttonColor):
    font = pygame.font.SysFont('sans', 40)
    return font.render(buttonName, True, buttonColor)

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


TEXT_PLUS = create_button('+', WHITE)
TEXT_MINUS = create_button('-', WHITE)
TEXT_RUN = create_button('Run', WHITE)
TEXT_RANDOM = create_button('Random', WHITE)
TEXT_ALGORITHM = create_button('Algorithm', WHITE)
TEXT_RESET = create_button('Reset', WHITE)

k = 0

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

    # K button -
    pygame.draw.rect(screen, BLACK, (950, 50, 50, 50))
    screen.blit(TEXT_MINUS, (960, 50))

    # K value
    TEXT_K = create_button('K = ' + str(k), BLACK)
    screen.blit(TEXT_K, (1050, 50))

    # Run button

    # End draw interface

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Change K button +
            if 850 < mouse_x < 900 and 50 < mouse_y < 100:
                k += 1
            if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
                if k > 0:
                    k -= 1

    # Update the full display Surface to the screen
    pygame.display.flip()

pygame.quit()