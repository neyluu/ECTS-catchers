import pygame as pg

class Level:
    def __init__(self, isLeft : bool, screen: pg.Surface, canvas: pg.Rect):
        self.isLeft = isLeft
        self.screen = screen
        self.canvas = canvas
        self.color = "black"


    def handleEvents(self, event):
        pass


    def update(self, dt : float):
        pass


    def draw(self):
        pg.draw.rect(self.screen, self.color, self.canvas)