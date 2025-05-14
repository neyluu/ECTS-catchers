import pygame as pg

from src.game.PlayerData import PlayerData
from src.game.levels.Level import Level

class Level01(Level):
    def __init__(self, isLeft : bool, canvas: pg.Rect):
        super().__init__(isLeft, canvas)
        self.color = "green"
        self.map = self.levelLoader.load("testlevel.level", self.map)


    def handleEvents(self, event):
        super().handleEvents(event)


    def update(self, dt: float):
        super().update(dt)


    def draw(self, screen : pg.Surface):
        super().draw(screen)

