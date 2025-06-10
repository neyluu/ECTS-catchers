import pygame as pg

from src.game.PlayerData import PlayerData
from src.game.SpriteAnimation import SpriteAnimation
from src.game.map.tiles.Tile import Tile
from src.game.map.tiles.Trigger import Trigger
from src.sounds.SFX import SFX
import src.config.PowerUpsConfig as config


class DoubleJump(Trigger):
    def __init__(self):
        super().__init__()

        self.isResettable = False

        self.playerData : PlayerData = None
        self.boostTime : float = config.DOUBLE_JUMP_TIME # seconds
        self.timer : float = 0
        self.started : bool = False

        self.animation = SpriteAnimation("assets/animations/doubleJump", 0.6)
        self.sfx = SFX("assets/audio/double_jump.wav")


    def update(self, dt: float):
        if not self.isHidden:
            self.animation.update(dt)

        if self.started:
            self.timer += dt
            if self.timer > self.boostTime:
                self.playerData.canDoubleJump = False
                self.playerData.powerUps.doubleJump = False
                self.onMapReset()


    def draw(self, screen: pg.Surface):
        if not self.isHidden:
            self.animation.draw(screen, pg.Rect(self.leftTop.x, self.leftTop.y, Tile.size, Tile.size))

        self.DEBUG_drawCollideBoxes(screen)


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        self.sfx.play()
        self.started = True
        self.playerData : PlayerData = playerData
        self.playerData.canDoubleJump = True
        self.playerData.powerUps.doubleJump = True
        self.hide()


    def onMapReset(self):
        self.isActive = True
        self.started = False
        self.timer = 0
        self.unHide()
