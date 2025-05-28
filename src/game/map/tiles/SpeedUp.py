import pygame as pg

from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger
import src.config.PowerUpsConfig as config


class SpeedUp(Trigger):
    def __init__(self):
        super().__init__()
        self.isResettable = False

        self.color = "aqua"

        self.playerData : PlayerData = None

        self.started = False
        self.boostTime : float = config.SPEED_UP_TIME # seconds
        self.boostScale : float = config.SPEED_UP_SPEED_FACTOR
        self.timer : float = 0


    def update(self, dt: float):
        if self.started:
            self.timer += dt
            if self.timer > self.boostTime:
                self.playerData.speed = self.playerData.startSpeed
                self.started = False
                self.onMapReset()


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        self.playerData : PlayerData = playerData
        self.started = True
        self.color = pg.Color(0, 0, 0, 0)
        playerData.speed *= self.boostScale


    def onMapReset(self):
        self.isActive = True
        self.color = "aqua"
        self.started = False
        self.timer = 0
