from src.game.map.tiles.Tile import Tile

import pygame as pg


class Block(Tile):
    def __init__(self):
        super().__init__()
        self.isCollision = True
        self.path = "assets/textures/blocks/grey_brick_1.png"
        self.loadTexture()
