'''
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
'''
import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (220,100, 0)
YELLOW = (230, 200, 0)
GREEN = (0, 255, 0)
CYAN = (0, 225, 225)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 240)
GREY = (127, 127, 127)

my_colors=["BLACK", "WHITE", "RED", "ORANGE", "YELLOW", "GREEN", "CYAN", "BLUE", "PURPLE", "GREY"]

pygame.init()

#Defining variables
circle_x=400
circle_y=200
c_radius=random.randint(10, 20)

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Bouncing Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# WRITE YOUR CODE HERE
x_speed=5
y_speed=5


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    
    circle_x+=x_speed
    circle_y+=y_speed

    if circle_x>(700-c_radius):
        x_speed=(-1)*(x_speed)
    if circle_x<(c_radius):
        x_speed= (-1)*(x_speed)
    if circle_y>(500-c_radius):
        y_speed=(-1)*(y_speed)
    if circle_y<(c_radius):
        y_speed=(-1)*(y_speed)
        
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(CYAN)

    # --- Drawing code should go here
    pygame.draw.circle(screen, BLUE, (circle_x, circle_y), c_radius)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE








