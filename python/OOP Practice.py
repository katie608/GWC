import pygame

BLACK=(0, 0, 0)
DARKGREY=(60, 60, 60)
GREY=(120, 120, 120)
LIGHTGREY=(180, 180, 180)
WHITE=(255, 255, 255)
BROWN=(120, 70, 15)
DARKBROWN=(80, 40, 10)

class Dog():
    def __init__(self, name, furType, color, height):
        self.name=name
        self.furType=furType
        self.color=color
        self.height=height
        self.bark=0
    def bark(self):
        print("woof")
        self.barks+=1
    def shakeHands(self):
        print("nice to meet you, i'm" + self.name)
        self.bark()
    def returnFurType(self):
        return self.furType
    def draw(self, x, y):
        pygame.draw.circle(screen, self.color, (x, y), ((self.height)//2))
        
BassetHound= Dog("Luther", "short", BROWN, 100)
import pygame
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
            
    screen.fill(WHITE)

    BassetHound.draw(100, 100)
    
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
exit()
