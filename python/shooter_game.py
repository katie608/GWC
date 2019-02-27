
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
NIGHTSKY=(0, 0, 30)
LIGHTPURPLE=(160, 100, 255)
PURPLE=(130, 0, 220)
DARKPURPLE=(40, 0, 100)
MAGENTA=(200, 0, 200)
PINK=(250, 120, 250)
HEART=(230, 65, 60)
BLACK=(0, 0, 0)
DARKGREY=(60, 60, 60)
GREY=(120, 120, 120)
LIGHTGREY=(180, 180, 180)
WHITE=(255, 255, 255)
TAN=(105, 65, 45)
BROWN=(120, 70, 15)
DARKBROWN=(80, 40, 10)

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


possible_ball_colors = [RED, REDORANGE, ORANGE, YELLOWORANGE, YELLOW, YELLOWGREEN, GREEN, DARKGREEN,BLUEGREEN, CYAN, SKYBLUE, BLUE, INDIGO, LIGHTPURPLE, PURPLE, DARKPURPLE, MAGENTA, PINK, BLACK, DARKGREY, GREY, LIGHTGREY, WHITE, BROWN, DARKBROWN]


class Circle(pygame.sprite.Sprite):
    def __init__(self, x_location, y_location, x_speed):
        pygame.sprite.Sprite.__init__(self)
        self.x_speed = x_speed
        self.y_speed = -5
        self.size = (10, 10)
        self.image = pygame.Surface(self.size)
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.x = x_location
        self.rect.y = SCREEN_HEIGHT
        
    def shoot(self, screen):
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed
        

class Thing(pygame.sprite.Sprite):
    def __init__(self, x_location, y_location):
        pygame.sprite.Sprite.__init__(self)
        self.x_speed = 0
        self.y_speed = 1
        self.size = (40, 40)
        self.image = pygame.Surface(self.size)
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.y = 0
        #thing_y = self.rect.y
        self.rect.x = random.randrange(0, SCREEN_WIDTH)
        
    def fall(self, screen):
        self.rect.y += self.y_speed
        self.rect.x += self.x_speed


ball_list = pygame.sprite.Group()
thing_list = pygame.sprite.Group()

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
            ball_list.add(Circle(350, 490, ((x-350)/40)))
            
    #Background Color
    screen.fill(NIGHTSKY)

    #Draws the sprites in both lists
    ball_list.draw(screen)
    thing_list.draw(screen)

    
    #Gets things to fall from top
    random_number = random.randint(1, 60)
    if random_number is 11:
        thing_list.add(Thing(random.randint(0, 680), -10))
    
    #gets bullets to shoot up and things to fall down
    for Ball in ball_list:
        Ball.shoot(screen)
    for thing in thing_list:
        thing.fall(screen)

    #adds sprites to the list of hit objects after they collide
    pygame.sprite.groupcollide(ball_list, thing_list, True, True)

    #game over
    #if thing_y > 500:
        #print("game over")

    #updates screen every 1/60th of a second
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
exit() 

