from src.game.map.tiles.Tile import Tile

import pygame as pg


class Block(Tile):
    def __init__(self, path : str):
        super().__init__()
        self.isCollision = True

        if path == '':
            path = "assets/textures/blocks/grey_brick.png"
            print("ERROR: block texture path is empty!")

        self.loadTexture(path)
