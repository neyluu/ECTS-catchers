import pygame as pg

from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger


class SpeedUp(Trigger):
    def __init__(self):
        super().__init__()
        self.isResettable = False

        self.color = "aqua"

        self.playerData : PlayerData = None

        self.started = False
        self.boostTime : float = 5 # seconds
        self.boostScale : float = 2
        self.timer : float = 0


    def update(self, dt: float):
        if self.started:
            self.timer += dt
            if self.timer > self.boostTime:
                self.playerData.speed = self.playerData.startSpeed
                self.started = False


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        self.playerData : PlayerData = playerData
        self.started = True
        self.color = pg.Color(0, 0, 0, 0)
        playerData.speed *= self.boostScale
