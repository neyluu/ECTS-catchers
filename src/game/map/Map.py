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

                # color = (22, 22, 22) if (i + j) % 2 == 0 else (33, 33, 33)
                # if tile.isCollision:
                #     color = 'red'
                #
                # left = self.canvas.left + (j * Tile.size) + self.offsetX
                # top = self.canvas.top + (i * Tile.size) + self.offsetY
                #
                # pg.draw.rect(screen, color, (left, top, Tile.size, Tile.size))


    def initTileMap(self):
        for i in range(self.sizeY):
            innerList = []
            for j in range(self.sizeX):
                left = self.canvas.left + (j * Tile.size) + self.offsetX
                top = self.canvas.top + (i * Tile.size) + self.offsetY
                leftTop = pg.Vector2(left, top)
                innerList.append(Tile(leftTop))
            self.tileMap.append(innerList)

        # TODO TMP collisions
        for i in range(self.sizeX):
            self.tileMap[0][i].isCollision = True
            self.tileMap[self.sizeY - 1][i].isCollision = True
        for i in range(self.sizeY):
            self.tileMap[i][0].isCollision = True
            self.tileMap[i][self.sizeX - 1].isCollision = True

        for i in range(self.sizeY):
            for j in range(self.sizeX):
                newColor = (22, 22, 22) if (i + j) % 2 == 0 else (33, 33, 33)
                if self.tileMap[i][j].isCollision:
                    newColor = (
                        min(newColor[0] + 100, 255),
                        min(newColor[1], 255),
                        min(newColor[2], 255)
                    )
                self.tileMap[i][j].color = newColor
