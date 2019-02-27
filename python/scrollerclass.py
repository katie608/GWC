import pygame
import random
class Building():
    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
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
        while(total_width)<self.width:
            self.add_building(total_width)
            total_width+=self.buildings[-1].width
    
    def add_building(self, x_location):
        width = random.randint(20, 70)
        max_height = self.base - self.height
        height = random.randint((max_height // 4), max_height - 1)
        y_location = self.base - height
        building = Building(x_location, y_location, width, height, self.color)
        self.buildings.append(building)
        
    def draw_buildings(self, screen):
        for building in self.buildings:
            building.draw(screen)

    def move_buildings(self):
        last_building_location = self.buildings[-1].x_point + self.buildings[-1].width
        if last_building_location < (self.width + 10):
            self.add_building(last_building_location)
            if len(self.buildings) > 30:
                self.buildings.remove(self.buildings[0])
        for building in self.buildings:
            building.move(self.speed)
