import pygame as pg

from src.game.map.tiles.Tile import Tile

class Map:
    def __init__(self, canvas: pg.Rect):
        self.canvas = canvas
        self.sizeX = 29
        self.sizeY = 33
        self.offsetX = (canvas.width - self.sizeX * Tile.size) // 2
        self.offsetY = (canvas.height - self.sizeY * Tile.size) // 2

        self.tileMap = []

        self.initTileMap()



    def handleEvent(self, event):
        pass


    def update(self, dt : float):
        pass


    def draw(self, screen: pg.Surface):
        for i in range(self.sizeY):
            for j in range(self.sizeX):
                tile = self.tileMap[i][j]
                tile.draw(screen)


    def setTile(self, x : int, y : int,  tile : Tile):
        left = self.canvas.left + (y * Tile.size) + self.offsetX
        top = self.canvas.top + (x * Tile.size) + self.offsetY
        tile.leftTop = pg.Vector2(left, top)
        self.tileMap[x][y] = tile


    def initTileMap(self):
        for i in range(self.sizeY):
            innerList = []
            for j in range(self.sizeX):
                innerList.append(None)
            self.tileMap.append(innerList)