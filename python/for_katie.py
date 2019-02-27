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
RED=(255, 0, 0)
REDORANGE=(230, 50, 0)
ORANGE=(230, 120, 0)
YELLOWORANGE=(250, 160, 0)
YELLOW=(250, 210, 0)
YELLOWGREEN=(230, 230, 0)
GREEN=(0,255 , 0)
DARKGREEN=(0, 100, 0)
BLUEGREEN=(0, 150, 100)
CYAN=(0, 255, 225)
SKYBLUE=(100, 150, 255)
BLUE=(0, 0, 255)
INDIGO=(30, 0, 100)
LIGHTPURPLE=(160, 100, 255)
PURPLE=(130, 0, 220)
DARKPURPLE=(40, 0, 100)
MAGENTA=(200, 0, 200)
PINK=(250, 0, 250)
BLACK=(0, 0, 0)
DARKGREY=(60, 60, 60)
GREY=(120, 120, 120)
LIGHTGREY=(180, 180, 180)
WHITE=(255, 255, 255)
BROWN=(120, 70, 15)
DARKBROWN=(80, 40, 10)

colors = [RED, REDORANGE, ORANGE, YELLOWORANGE, YELLOW, YELLOWGREEN, GREEN, DARKGREEN,BLUEGREEN, CYAN, SKYBLUE, BLUE, INDIGO, LIGHTPURPLE, PURPLE, DARKPURPLE, MAGENTA, PINK, BLACK, DARKGREY, GREY, LIGHTGREY, WHITE, BROWN, DARKBROWN]


def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


class Building():
    def __init__(self, height, y_location, color, speed):
        self.x_speed=speed
        self.y_location=y_location
        self.width=random.randint(40, 80)
        self.height=random.randint(300, 1000)
        self.color=color
        self.x_location=800
        
       
    def move(self, screen):
        self.x_location -= self.x_speed
        pygame.draw.rect(screen, self.color, (self.x_location, self.y_location, self.width, self.height))
        self.x_location += self.x_speed
        if self.x_location<-20:
            rectangle_list.remove


        
    '''def add_building(self, x_location):
        width = random.randint(self.width // 25, self.width // 4)
        max_height = self.base - self.height
        height = random.randint((max_height // 4), max_height - 1)
        y_location = self.base - height
        building = Building(x_location, y_location, width, height, self.color)
        self.buildings.append(building)
        
    def draw(self):
        pygame.draw.rect(screen, self.color,(self.x_point, self.y_point, self.width, self.height))
    
    def draw_buildings(self):
        for building in self.buildings:
            building.draw()

    def move_buildings(self):
        last_building_location = self.buildings[-1].x_point + self.buildings[-1].width
        if last_building_location < (self.width + 10):
            self.add_building(last_building_location)
            if len(self.buildings) > 30:
                self.buildings.remove(self.buildings[0])
        for building in self.buildings:
            building.move(self.speed)'''

building_list=[]
back=Building(Building(200, (random.randint (250, 400)), LIGHTGREY, 1))
middle=Building(Building(200, (random.randint (400, 500)), GREY, 2))
front=Building(Building(100, (random.randint (500, 600)), DARKGREY, 3))

'''
FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)'''
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
    screen.fill(SKYBLUE)

    # --- Drawing code should go here
    '''back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()'''


    random_num_2=random.randint(1, 5)      
    if random_num_2 is 3:
        building_list.append(Building_back)
        building_list.append(Building_middle)
        building_list.append(Building_front)

    for Building in building_list:
        Building.move(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
