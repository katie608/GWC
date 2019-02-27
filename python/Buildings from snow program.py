
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
WHITE=(255, 255, 255)
BLACK=(0,0,0)
colors=[GREEN, DARKGREEN,BLUEGREEN, CYAN, SKYBLUE, BLUE, INDIGO]

pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Scroller")

class Circle():
    def __init__(self):
        self.x_speed=random.randint(-3, -1)
        self.y_location=random.randint(0, 200)
        self.size=random.randint(20, 30)
        self.color=(255, 255, 255)
        self.x_location=random.randint(710, 730)
    def scroll(self, screen):
        pygame.draw.circle(screen, self.color, (self.x_location, self.y_location), self.size)
        self.x_location += self.x_speed
        if self.x_location<-20:
            circle_list.remove
            
        
class Rectangle():
    def __init__(self):
        self.x_speed=random.randint(-3, -1)
        self.y_location=random.randint(200, 900)
        self.width=random.randint(40, 80)
        self.height=random.randint(300, 1000)
        self.color=((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)) )
        self.x_location=random.randint(710, 730)
    def scroll(self, screen):
        pygame.draw.rect(screen, self.color, (self.x_location, self.y_location, self.width, self.height))
        self.x_location += self.x_speed
        if self.x_location<-20:
            rectangle_list.remove

done = False

clock = pygame.time.Clock()

circle_list = []
rectangle_list = []

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(SKYBLUE)

    pygame.draw.circle(screen, YELLOW, (450, 50), 40)

    random_num_1=random.randint(1, 10)
    if random_num_1 is 9:
        circle_list.append(Circle())
    
    for circle in circle_list:
        circle.scroll(screen)

    random_num_2=random.randint(1, 5)      
    if random_num_2 is 3:
        rectangle_list.append(Rectangle())


    for rectangle in rectangle_list:
        rectangle.scroll(screen)
    

    pygame.display.flip()

    clock.tick(10)


pygame.quit()
exit()






