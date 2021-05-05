import pygame

def create_button_content(buttonName, buttonColor):
    font = pygame.font.SysFont('sans', 40)
    return font.render(buttonName, True, buttonColor)

def create_button_rect(content, color,buttonDimension, contentDimension):
    pygame.draw.rect(screen, color, buttonDimension)
    screen.blit(content, contentDimension)

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

# (x, y, width, height)
# (x, y)
K_PLUS_BUTTON_DIMENSION = (850, 50, 50, 50)
K_PLUS_CONTENT_DIMENSION = (860, 50)
K_MINUS_BUTTON_DIMENSION = (950, 50, 50, 50)
K_MINUS_CONTENT_DIMENSION = (960, 50)
RUN_BUTTON_DIMENSION = (850, 150, 150, 50)
RUN_CONTENT_DIMENSION = (900, 150)
RANDOM_BUTTON_DIMENSION = (850, 250, 150, 50)
RANDOM_CONTENT_DIMENSION = (865, 250)
ALGORITHM_BUTTON_DIMENSION = (850, 450, 150, 50)
ALGORITHM_CONTENT_DIMENSION = (850, 450)
RESET_BUTTON_DIMENSION = (850, 550, 150, 50)
RESET_CONTENT_DIMENSION = (850, 550)

TEXT_PLUS = create_button_content('+', WHITE)
TEXT_MINUS = create_button_content('-', WHITE)
TEXT_RUN = create_button_content('Run', WHITE)
TEXT_RANDOM = create_button_content('Random', WHITE)
TEXT_ALGORITHM = create_button_content('Algorithm', WHITE)
TEXT_RESET = create_button_content('Reset', WHITE)

k = 0
error = 0

while running:
    clock.tick(FPS)
    screen.fill(BACKGROUND)

   # Draw interface
    # Draw panel
    pygame.draw.rect(screen, BLACK, (50, 50, 700, 500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55, 55, 690, 490))
    
    # Create button
    create_button_rect(TEXT_PLUS, BLACK, K_PLUS_BUTTON_DIMENSION, K_PLUS_CONTENT_DIMENSION)
    create_button_rect(TEXT_MINUS, BLACK, K_MINUS_BUTTON_DIMENSION, K_MINUS_CONTENT_DIMENSION)
    create_button_rect(TEXT_RUN, BLACK, RUN_BUTTON_DIMENSION, RUN_CONTENT_DIMENSION)
    create_button_rect(TEXT_RANDOM, BLACK, RANDOM_BUTTON_DIMENSION, RANDOM_CONTENT_DIMENSION)
    create_button_rect(TEXT_ALGORITHM, BLACK, ALGORITHM_BUTTON_DIMENSION, ALGORITHM_CONTENT_DIMENSION)
    create_button_rect(TEXT_RESET, BLACK, RESET_BUTTON_DIMENSION, RESET_CONTENT_DIMENSION)

    # Error text
    TEXT_ERROR = create_button_content('Error = ' + str(error), BLACK)
    screen.blit(TEXT_ERROR, (850, 350))

    # K value
    TEXT_K = create_button_content('K = ' + str(k), BLACK)
    screen.blit(TEXT_K, (1050, 50))

    # End draw interface

    mouse_x, mouse_y = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # K + button
            if 850 < mouse_x < 900 and 50 < mouse_y < 100:
                k += 1

            # K - button
            if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
                if k > 0:
                    k -= 1

            # Run button
            if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
                print('Run button')
            
            # Random button
            if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                print('Random button')

            # Algorithm button
            if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                print('Algorithm button')
            
            # Reset button
            if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
                print('Reset button')

    # Update the full display Surface to the screen
    pygame.display.flip()

pygame.quit()