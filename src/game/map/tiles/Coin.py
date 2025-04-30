from src.game.map.tiles.Tile import Tile

import pygame as pg

class Coin(Tile):
    def __init__(self):
        super().__init__()
        self.isTrigger = True
        self.color = "pink"

    def onTrigger(self):
        self.color = "blue"