import pygame as pg

from src.game.map.tiles.Tile import Tile
from src.game.PlayerData import PlayerData
from src.game.SpriteAnimation import SpriteAnimation
from src.game.map.tiles.Trigger import Trigger
from src.sounds.SFX import SFX
import src.config.PowerUpsConfig as config


class SpeedUp(Trigger):
    activeInstances : int = 0

    def __init__(self):
        super().__init__()
        self.isResettable = False

        self.playerData : PlayerData = None

        self.started : bool = False
        self.boostTime : float = config.SPEED_UP_TIME # seconds
        self.boostScale : float = config.SPEED_UP_SPEED_FACTOR
        self.timer : float = 0

        self.animation = SpriteAnimation("assets/animations/speedUp", 0.6)
        self.sfx = SFX("assets/audio/speed_up.wav")


    def update(self, dt: float):
        if not self.isHidden:
            self.animation.update(dt)

        if self.started:
            self.timer += dt
            if self.timer > self.boostTime:
                if SpeedUp.activeInstances <= 1:
                    self.playerData.speed = self.playerData.startSpeed
                    self.playerData.powerUps.speedUp = False
                self.onMapReset()
                SpeedUp.activeInstances -= 1


    def draw(self, screen: pg.Surface):
        if not self.isHidden:
            self.animation.draw(screen, pg.Rect(self.leftTop.x, self.leftTop.y, Tile.size, Tile.size))

        self.DEBUG_drawCollideBoxes(screen)


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        SpeedUp.activeInstances += 1
        self.sfx.play()
        self.playerData : PlayerData = playerData
        self.playerData.powerUps.speedUp = True
        self.started = True
        if SpeedUp.activeInstances == 1:
            playerData.speed *= self.boostScale
        self.hide()


    def onMapReset(self):
        self.isActive = True
        self.started = False
        self.timer = 0
        self.unHide()
