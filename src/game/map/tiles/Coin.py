import pygame as pg
import random

from src.game.map.tiles.Tile import Tile
from src.game.PlayerData import PlayerData
from src.game.SpriteAnimation import SpriteAnimation
from src.game.map.tiles.Trigger import Trigger
import src.config.PowerUpsConfig as config


class Coin(Trigger):
    def __init__(self):
        super().__init__()
        self.isResettable = False
        self.points = random.randint(config.COIN_MIN_POINTS, config.COIN_MAX_POINTS)
        self.animation = SpriteAnimation("assets/animations/coin", 0.55)


    def update(self, dt: float):
        if not self.isHidden:
            self.animation.update(dt)


    def draw(self, screen: pg.Surface):
        if not self.isHidden:
            self.animation.draw(screen, pg.Rect(self.leftTop.x, self.leftTop.y, Tile.size, Tile.size))


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        self.hide()
        playerData.coins += self.points
        print(f"Points: {playerData.coins}")


    def onMapReset(self):
        self.unHide()
        self.isActive = True