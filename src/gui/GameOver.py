import pygame as pg

class GameOver:
    def __init__(self, canvas : pg.Rect):
        self.canvas = canvas


    def handleEvents(self, event):
        pass


    def update(self, dt : float):
        pass


    def draw(self, screen):
        pg.draw.rect(screen, "red", self.canvas)