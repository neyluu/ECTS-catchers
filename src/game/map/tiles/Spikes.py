from src.game.map.tiles.Tile import Tile

import pygame as pg

class Spikes(Tile):
    def __init__(self):
        super().__init__()
        self.isTrigger = True
        self.color = "green"

    def onTrigger(self):
        self.color = "white"