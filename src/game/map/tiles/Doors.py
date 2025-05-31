import pygame as pg

from src.game.PlayerData import PlayerData
from src.game.SpriteAnimation import SpriteAnimation
from src.game.map.tiles.Tile import Tile
from src.game.map.tiles.Trigger import Trigger


class Doors(Trigger):
    def __init__(self, isTop : bool):
        super().__init__()

        self.animationTime : float = 0.8

        if isTop:
            self.animation = SpriteAnimation("assets/animations/doorTop", self.animationTime)
        else:
            self.animation = SpriteAnimation("assets/animations/doorBottom", self.animationTime)


    def update(self, dt: float):
        self.animation.update(dt)


    def draw(self, screen: pg.Surface):
        self.animation.draw(screen, pg.Rect(self.leftTop.x, self.leftTop.y, Tile.size, Tile.size))


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered() or playerData.levelChanged:
            return

        playerData.currentLevel += 1
        playerData.levelChanged = True
