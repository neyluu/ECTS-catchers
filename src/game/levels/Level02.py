import pygame as pg

from src.game.PlayerData import PlayerData
from src.game.levels.Level import Level

class Level02(Level):
    def __init__(self, isLeft : bool, canvas: pg.Rect):
        super().__init__(isLeft, canvas)
        self.color = "black"

        self.map = self.levelLoader.load("testlevel2.level", self.map)


    def handleEvents(self, event):
        super().handleEvents(event)


    def update(self, dt: float):
        super().update(dt)


    def draw(self, screen : pg.Surface):
        super().draw(screen)


    def reset(self):
        self.playerData.posX = self.playerData.startPosX
        self.playerData.posY = self.playerData.startPosY
        self.playerData.hp = self.playerData.startHp
        self.playerData.points = 0
