import pygame
pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ball Game")

done = False

clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if event.type==pygame.MOUSEBUTTONUS:
        pos=pygame.mouse.get_pos()
    
    if event.type==pygame.MOUSEBUTTONUS:
        pos=pygame.mouse.get_pos()

    print(pos)
  
 
    pygame.display.flip()


    clock.tick(60)


pygame.quit()
exit() 
