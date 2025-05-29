import pygame as pg

from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger
import src.config.PowerUpsConfig as config


class SpeedUp(Trigger):
    def __init__(self):
        super().__init__()
        self.isResettable = False

        self.playerData : PlayerData = None

        self.started : bool = False
        self.boostTime : float = config.SPEED_UP_TIME # seconds
        self.boostScale : float = config.SPEED_UP_SPEED_FACTOR
        self.timer : float = 0

        self.loadTexture("assets/textures/powerups/power_up_speed.png")


    def update(self, dt: float):
        if self.started:
            self.timer += dt
            if self.timer > self.boostTime:
                self.playerData.speed = self.playerData.startSpeed
                self.playerData.powerUps.speedUp = False
                self.onMapReset()


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        self.playerData : PlayerData = playerData
        self.playerData.powerUps.speedUp = True
        self.started = True
        playerData.speed *= self.boostScale
        self.hide()


    def onMapReset(self):
        self.isActive = True
        self.started = False
        self.timer = 0
        self.unHide()
