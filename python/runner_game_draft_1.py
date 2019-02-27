
import pygame
import random
from scrollerclass import Scroller
from scrollerclass import Building

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

class RunnerSprite(pygame.sprite.Sprite):
    def __init__ (self):
        pygame.sprite.Sprite. __init__ (self)
    def run(self, x_location, y_location):
        pygame.draw.circle(screen, LIGHTPURPLE, (x_location, y_location), 30)


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
# -------- Main Program Loop -----------#
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #uncecesary but pretty background
    screen.fill(INDIGO)
    pygame.draw.circle(screen, SKYBLUE, [400, 600], 600)
    pygame.draw.circle(screen, PINK, [400, 600], 500)
    pygame.draw.circle(screen, REDORANGE, [400, 600], 400)
    pygame.draw.circle(screen, ORANGE, [400, 600], 300)
    pygame.draw.circle(screen, YELLOWORANGE, [400, 600], 200)
    pygame.draw.circle(screen, YELLOW, [400, 600], 100)

    #actual code stuff



    # --- Drawing code 
    back_scroller.draw_buildings(screen)
    back_scroller.move_buildings()
    middle_scroller.draw_buildings(screen)
    middle_scroller.move_buildings()
    front_scroller.draw_buildings(screen)
    front_scroller.move_buildings()

    random_num = random.randint(0, 10)
    if random_num is 6:
        square_list.append(Square())
    
    for square in square_list:
        square.Move(screen)

    pos=pygame.mouse.get_pos()
    x=pos[0]
    y=pos[1]
    RunnerSprite.run(screen, x, y)
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
