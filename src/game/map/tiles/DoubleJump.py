import pygame as pg

from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger
import src.config.PowerUpsConfig as config


class DoubleJump(Trigger):
    def __init__(self):
        super().__init__()

        self.isResettable = False
        self.color = "olivedrab1"

        self.playerData : PlayerData = None
        self.boostTime : float = config.DOUBLE_JUMP_TIME # seconds
        self.timer : float = 0
        self.started : bool = False


    def update(self, dt: float):
        if self.started:
            self.timer += dt
            if self.timer > self.boostTime:
                self.playerData.canDoubleJump = False
                self.started = False


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        self.started = True
        self.color = pg.Color(0, 0, 0, 0)
        self.playerData : PlayerData = playerData
        self.playerData.canDoubleJump = True


    def onMapReset(self):
        self.isActive = True
        self.color = "olivedrab1"
        self.started = False
        self.timer = 0
    