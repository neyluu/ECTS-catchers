import pygame as pg

from src.game.PlayerData import PlayerData
from src.game.map.tiles.Tile import Tile


class Trigger(Tile):
    def __init__(self):
        super().__init__()
        self.isTrigger = True
        self.isActive = True
        self.isResettable = True

        self.collisionSizeX = Tile.size - 8
        self.collisionSizeY = Tile.size - 8
        self.collisionOffsetX = 4
        self.collisionOffsetY = 4


    def reset(self):
        if self.isResettable:
            self.isActive = True


    def onTrigger(self, playerData : PlayerData):
        raise NotImplementedError


    def wasEntered(self):
        if not self.isActive:
            return True
        self.isActive = False
        return False
