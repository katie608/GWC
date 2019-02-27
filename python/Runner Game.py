
import pygame
import random

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
colors = [BLACK, GREEN, BLUE, RED]

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
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color,(self.x_point, self.y_point, self.width, self.height))
        

    def move(self, speed):
        self.x_point -= speed
        

class Scroller(object):
    def __init__(self, width, height, base, color, speed):
        self.width = width
        self.height = height
        self.base = base
        self.color = color
        self.speed = speed
        self.buildings = []
        self.add_buildings()

    def add_buildings(self):
        total_width=0
        while(total_width)<SCREEN_WIDTH:
            self.add_building(total_width)
            total_width+=self.buildings[-1].width
    
    def add_building(self, x_location):
        width = random.randint(20, 70)
        max_height = self.base - self.height
        height = random.randint((max_height // 4), max_height - 1)
        y_location = self.base - height
        building = Building(x_location, y_location, width, height, self.color)
        self.buildings.append(building)
        
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
            building.move(self.speed)

class Square():
    def __init__(self):
        self.x_speed=random.randint(1, 3)
        self.y_location=random.randint(0, 700)
        self.height=20
        self.width=20
        self.color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.x_location=random.randint(800, 810)
    def Move(self, screen):
        pygame.draw.rect(screen, self.color, (self.x_location, self.y_location, self.width, self.height))
        self.x_location -= self.x_speed

FRONT_SCROLLER_COLOR = (80,80,80)
MIDDLE_SCROLLER_COLOR = (120, 120, 120)
BACK_SCROLLER_COLOR = (180,180,180)
BACKGROUND_COLOR = (100, 150, 255)

square_list = []

back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 50), BACK_SCROLLER_COLOR, 1)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 10), MIDDLE_SCROLLER_COLOR, 2)
front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
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
    screen.fill(INDIGO)
    pygame.draw.circle(screen, SKYBLUE, [400, 600], 600)
    pygame.draw.circle(screen, PINK, [400, 600], 500)
    pygame.draw.circle(screen, REDORANGE, [400, 600], 400)
    pygame.draw.circle(screen, ORANGE, [400, 600], 300)
    pygame.draw.circle(screen, YELLOWORANGE, [400, 600], 200)
    pygame.draw.circle(screen, YELLOW, [400, 600], 100)

    # --- Drawing code should go here
    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()

    random_num = random.randint(0, 10)
    if random_num is 6:
        square_list.append(Square())
    
    for square in square_list:
        square.Move(screen)


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
