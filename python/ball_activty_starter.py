"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)





pygame.init()




# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]



x_speed_1 = random.randint(-10, 10)
y_speed_1 = random.randint(-10, 10)

x_speed_2 = random.randint(-10, 10)
y_speed_2= random.randint(-10, 10)

x_speed_3 = random.randint(-10, 10)
y_speed_3= random.randint(-10, 10)

x_location_1 = int(SCREEN_WIDTH/2)
y_location_1 = int(SCREEN_HEIGHT/2)

x_location_2 = int(SCREEN_WIDTH/2)
y_location_2 = int(SCREEN_HEIGHT/2)

x_location_3 = int(SCREEN_WIDTH/2)
y_location_3 = int(SCREEN_HEIGHT/2)

ball_size = random.randint(10, 30)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREY)

    # --- Drawing code should go here

    ball_color_1 = random.choice(possible_ball_colors) # This is outside because of variable scoping.
    ball_color_2 = random.choice(possible_ball_colors)
    ball_color_3 = random.choice(possible_ball_colors)
    
    pygame.draw.circle(screen, ball_color_1, [x_location_1, y_location_1], ball_size)

    pygame.draw.circle(screen, ball_color_2, [x_location_2, y_location_2], ball_size)

    pygame.draw.circle(screen, ball_color_3, [x_location_3, y_location_3], ball_size)

    if x_location_1 >= SCREEN_WIDTH - ball_size or x_location_1 < ball_size:
        x_speed_1 = x_speed_1 * -1

    if y_location_1 >= SCREEN_HEIGHT - ball_size or y_location_1 < ball_size:
        y_speed_1 = y_speed_1 * -1


    if x_location_2 >= SCREEN_WIDTH - ball_size or x_location_2 < ball_size:
        x_speed_2 = x_speed_2 * -1

    if y_location_2 >= SCREEN_HEIGHT - ball_size or y_location_2 < ball_size:
        y_speed_2 = y_speed_2 * -1


    if x_location_3 >= SCREEN_WIDTH - ball_size or x_location_3 < ball_size:
        x_speed_3 = x_speed_2 * -1

    if y_location_3 >= SCREEN_HEIGHT - ball_size or y_location_3 < ball_size:
        y_speed_3 = y_speed_2 * -1
        

    x_location_1 += x_speed_1
    y_location_1 += y_speed_1


    x_location_2 += x_speed_2
    y_location_2 += y_speed_2

    x_location_3 += x_speed_3
    y_location_3 += y_speed_3

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
