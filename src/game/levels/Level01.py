import pygame as pg

from src.game.levels.Level import Level

class Level01(Level):
    def __init__(self, isLeft : bool, screen: pg.Surface, canvas: pg.Rect):
        super().__init__(isLeft, screen, canvas)
        self.color = "green"


    def handleEvents(self, event):
        pass


    def update(self, dt: float):
        pass


    def draw(self):
        super().draw()

