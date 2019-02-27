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
DARKGREEN=(0, 100, 0)
SKYBLUE=(100, 150, 255)

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


possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY, DARKGREEN]



class BouncingBall():
    def __init__(self, x_location, y_location):  
        self.x_location=x_location
        self.y_location=y_location
        self.x_speed = 10
        self.y_speed = 10
        self.ball_size = 30
 

    def flashBounce(self, screen, colors, screen_width, screen_height):
        #ball_color = random.choice(colors)
        
        if self.x_location >= screen_width - self.ball_size or self.x_location < self.ball_size:
            self.x_speed = self.x_speed * -1

        if self.y_location >= screen_height - self.ball_size or self.y_location < self.ball_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed 

        pygame.draw.circle(screen, DARKGREEN, [self.x_location, self.y_location], self.ball_size)

ball_list = []
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()
            x=pos[0]
            y=pos[1]
            ball_list.append(BouncingBall(x, y))
    
    screen.fill(SKYBLUE) 
    
    #pygame.mouse.get_pressed
    #pygame.mouse.get_position

    for Ball in ball_list:
        Ball.flashBounce(screen, BLUE, SCREEN_WIDTH, SCREEN_HEIGHT)

    #ball_2.flashBounce(screen, GREEN, SCREEN_WIDTH, SCREEN_HEIGHT)

    pygame.display.flip()


    clock.tick(60)


pygame.quit()
exit() 

