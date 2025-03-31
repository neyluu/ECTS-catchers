import pygame as pg

from src.game.map.tiles.Tile import Tile

class Map:
    def __init__(self, canvas: pg.Rect):
        self.canvas = canvas
        self.sizeX = 29
        self.sizeY = 33
        self.tileMap = [[Tile() for _ in range(self.sizeX)] for _ in range(self.sizeY)]
        self.offsetX = (canvas.width - self.sizeX * self.tileMap[0][0].sizeX) // 2
        self.offsetY = (canvas.height - self.sizeY * self.tileMap[0][0].sizeY) // 2

        # TMP
        for i in range(self.sizeX):
            self.tileMap[0][i].isCollision = True
            self.tileMap[self.sizeY - 1][i].isCollision = True
        for i in range(self.sizeY):
            self.tileMap[i][0].isCollision = True
            self.tileMap[i][self.sizeX - 1].isCollision = True


    def handleEvent(self, event):
        pass


    def update(self, dt : float):
        pass


    def draw(self, screen: pg.Surface):
        for i in range(self.sizeY):
            for j in range(self.sizeX):
                color = (22, 22, 22) if (i + j) % 2 == 0 else (33, 33, 33)
                tile = self.tileMap[i][j]
                if tile.isCollision:
                    color = 'red'
                left = self.canvas.left + (j * tile.sizeX) + self.offsetX
                top = self.canvas.top + (i * tile.sizeY) + self.offsetY
                pg.draw.rect(screen, color, (left, top, tile.sizeX, tile.sizeY))