import pygame as pg

class Level:
    def __init__(self, isLeft : bool, canvas: pg.Rect):
        self.isLeft = isLeft
        self.canvas = canvas
        self.color = "black"
        print(self.canvas)


    def handleEvents(self, event):
        pass


    def update(self, dt : float):
        pass


    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.canvas)