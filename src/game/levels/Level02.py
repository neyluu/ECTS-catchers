import pygame as pg

from src.game.levels.Level import Level

class Level02(Level):
    def __init__(self, isLeft : bool, canvas: pg.Rect):
        super().__init__(isLeft, canvas)
        self.color = "yellow"


    def handleEvents(self, event):
        pass


    def update(self, dt: float):
        pass


    def draw(self, screen : pg.Surface):
        super().draw(screen)

