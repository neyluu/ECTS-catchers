import pygame as pg

class Tile:
    def __init__(self):
        self.sizeX = 32
        self.sizeY = 32
        self.color = "red"
        self.isCollision = False


    def handleEvent(self, event):
        pass


    def update(self, dt: float):
        pass


    def draw(self, screen: pg.Surface):
        pass

