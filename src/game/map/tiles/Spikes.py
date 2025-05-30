import pygame as pg

from src.game.PlayerData import PlayerData
from src.game.map.tiles.Tile import Tile
from src.game.map.tiles.Trigger import Trigger
import src.config.PowerUpsConfig as config


class Spikes(Trigger):
    def __init__(self, direction : int = 0):
        super().__init__()
        self.loadTexture("assets/textures/traps/spikes.png")
        self.damage = config.SPIKES_DAMAGE

        # bottom
        if direction == 0:
            self.collisionSizeX = Tile.size - 8
            self.collisionSizeY = Tile.size - 20
            self.collisionOffsetX = 4
            self.collisionOffsetY = 20
        # right
        elif direction == 1:
            self.texture = pg.transform.rotate(self.texture, 90)
            self.collisionSizeX = Tile.size - 20
            self.collisionSizeY = Tile.size - 8
            self.collisionOffsetX = 20
            self.collisionOffsetY = 4
        # top
        elif direction == 2:
            self.texture = pg.transform.rotate(self.texture, 180)
            self.collisionSizeX = Tile.size - 8
            self.collisionSizeY = Tile.size - 20
            self.collisionOffsetX = 4
            self.collisionOffsetY = 4
        # left
        elif direction == 3:
            self.texture = pg.transform.rotate(self.texture, 270)
            self.collisionSizeX = Tile.size - 20
            self.collisionSizeY = Tile.size - 8
            self.collisionOffsetX = 4
            self.collisionOffsetY = 4



    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        playerData.hp -= self.damage
        print(f"HP: {playerData.hp}")
