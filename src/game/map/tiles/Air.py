from src.game.map.tiles.Tile import Tile

import pygame as pg

class Air(Tile):
    def __init__(self):
        super().__init__()
        self.isCollision = False
        self.color = "black"