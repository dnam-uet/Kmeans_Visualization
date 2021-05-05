import pygame
from random import randint
import math

def create_button_content(buttonName, buttonColor,fontSize):
    font = pygame.font.SysFont('sans', fontSize)
    return font.render(buttonName, True, buttonColor)

def create_button_rect(content, color,buttonDimension, contentDimension):
    pygame.draw.rect(screen, color, buttonDimension)
    screen.blit(content, contentDimension)

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

pygame.init()

screen = pygame.display.set_mode((1200, 700))

pygame.display.set_caption("Kmeans Visualization")

running = True

clock = pygame.time.Clock()

FPS = 60

BIG_SIZE = 40
SMALL_SIZE = 20

BACKGROUND = (215, 215, 215)
BACKGROUND_PANEL = (249, 255, 230)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (147, 153, 35)
PURPLE = (255, 0, 255)
SKY = (0, 255, 255)
ORANGE = (255, 125, 25)
GRAPE = (100, 25, 125)
GRASS = (55, 155, 65)

COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, SKY, ORANGE, GRAPE, GRASS]

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

TEXT_PLUS = create_button_content('+', WHITE, BIG_SIZE)
TEXT_MINUS = create_button_content('-', WHITE, BIG_SIZE)
TEXT_RUN = create_button_content('Run', WHITE, BIG_SIZE)
TEXT_RANDOM = create_button_content('Random', WHITE, BIG_SIZE)
TEXT_ALGORITHM = create_button_content('Algorithm', WHITE, BIG_SIZE)
TEXT_RESET = create_button_content('Reset', WHITE, BIG_SIZE)

k = 0
error = 0
points = []
clusters = []
labels = []

while running:
    clock.tick(FPS)
    screen.fill(BACKGROUND)
    mouse_x, mouse_y = pygame.mouse.get_pos()

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

    # K value
    TEXT_K = create_button_content('K = ' + str(k), BLACK, BIG_SIZE)
    screen.blit(TEXT_K, (1050, 50))

    # Draw mouse position when mouse is in panel
    if 50 < mouse_x < 750 and 50 < mouse_y < 550:
        text_mouse = create_button_content("(" + str(mouse_x-50) + "," + str(mouse_y-50) + ")",BLACK, SMALL_SIZE)
        screen.blit(text_mouse, (mouse_x + 15, mouse_y))

    # End draw interface

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            # point position storage
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                labels = []
                point = [mouse_x - 50, mouse_y - 50]
                points.append(point)

            # K + button
            if 850 < mouse_x < 900 and 50 < mouse_y < 100:
                if k < 9:
                    k += 1

            # K - button
            if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
                if k > 0:
                    k -= 1

            # Run button
            if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
                labels = []
                for point in points:
                    distancesToCluster = []
                    for cluster in clusters:
                        distancesToCluster.append(distance(point, cluster))
                    
                    minDistance = min(distancesToCluster)
                    label = distancesToCluster.index(minDistance)
                    labels.append(label)

                # Update clusters
                for i in range(k):
                    sum_x = 0
                    sum_y = 0
                    count = 0
                    for j in range(len(points)):
                        if labels[j] == i:
                            sum_x += points[j][0]
                            sum_y += points[j][1]
                            count += 1
                    if count != 0:
                        new_pos_x = sum_x / count
                        new_pos_y = sum_y / count
                        clusters[i] = [int(new_pos_x), int(new_pos_y)]
            
            # Random button
            if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                clusters = []
                for i in range(k):
                    random_point = [randint(0, 690), randint(0, 490)]
                    clusters.append(random_point)

            # Algorithm button
            if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                print('Algorithm button')
            
            # Reset button
            if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
                print('Reset button')

    # Draw cluster
    for i in range(len(clusters)):
        pygame.draw.circle(screen, COLORS[i], (clusters[i][0] + 50, clusters[i][1] + 50), 10)

    # Draw point
    for i in range(len(points)):
        # surface, color, center, radius
        pygame.draw.circle(screen, BLACK, (points[i][0] + 50, points[i][1] + 50), 6)
        if labels == []:
            pygame.draw.circle(screen, WHITE, (points[i][0] + 50, points[i][1] + 50), 5)   
        else:
            pygame.draw.circle(screen, COLORS[labels[i]], (points[i][0] + 50, points[i][1] + 50), 5)

    # Calculate and draw error
    if clusters != [] and labels != []:
        error = 0
        for i in range(len(points)):
            error += distance(points[i], clusters[labels[i]])
    TEXT_ERROR = create_button_content("Error = " + str(int(error)), BLACK, BIG_SIZE)
    screen.blit(TEXT_ERROR, (850, 350))

    # Update the full display Surface to the screen
    pygame.display.flip()

pygame.quit()