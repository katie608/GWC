import random
import pygame

#colors
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



colors=[RED, REDORANGE, ORANGE, YELLOWORANGE, YELLOW, YELLOWGREEN, GREEN, DARKGREEN,BLUEGREEN, CYAN, SKYBLUE, BLUE, INDIGO, LIGHTPURPLE, PURPLE, DARKPURPLE, MAGENTA, PINK, BLACK, DARKGREY, GREY, LIGHTGREY, WHITE, BROWN, DARKBROWN]



pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Colors")
done = False
clock = pygame.time.Clock()
while not done:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    screen.fill(TAN)
    pygame.draw.circle(screen, TAN, [0, 300], 150)

    
    pygame.display.flip()
    clock.tick(3)
pygame.quit()
exit()


"=random.choice(colors)"

'''SUNSET
    screen.fill(INDIGO)
    pygame.draw.circle(screen, SKYBLUE, [400, 600], 600)
    pygame.draw.circle(screen, PINK, [400, 600], 500)
    pygame.draw.circle(screen, REDORANGE, [400, 600], 400)
    pygame.draw.circle(screen, ORANGE, [400, 600], 300)
    pygame.draw.circle(screen, YELLOWORANGE, [400, 600], 200)
    pygame.draw.circle(screen, YELLOW, [400, 600], 100)'''


'''Solar System
SUN=YELLOW
MERCURY=GREY
VENUS=(200, 80, 200)
EARTH=BLUE
MARS=REDORANGE
JUPITER=ORANGE
SATURN=(180, 120, 60)
URANUS=CYAN
NEPTUNE=BLUE
    screen.fill(NIGHTSKY)
    pygame.draw.circle(screen, SUN, [0, 300], 150)
    pygame.draw.circle(screen, MERCURY, [200, 300], 5)
    pygame.draw.circle(screen, VENUS, [250, 300], 10)
    pygame.draw.circle(screen, EARTH, [300, 300], 15)
    pygame.draw.circle(screen, GREEN, [296, 306], 7)
    pygame.draw.circle(screen, GREEN, [296, 293], 7)
    pygame.draw.circle(screen, MARS, [350, 300], 10)
    pygame.draw.circle(screen, JUPITER, [450, 300], 37)
    pygame.draw.circle(screen, SATURN, [550, 300], 33)
    pygame.draw.circle(screen, SATURN, [580, 300], 8)
    pygame.draw.circle(screen, SATURN, [520, 300], 8)
    pygame.draw.circle(screen, URANUS, [650, 300], 27)
    pygame.draw.circle(screen, NEPTUNE, [750, 300], 33)'''
    

