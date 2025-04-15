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

        self.tileMap[10][10].isCollision = True
        self.tileMap[11][11].isCollision = True
        self.tileMap[10][11].isCollision = True
        self.tileMap[11][10].isCollision = True
        self.tileMap[10][11].isCollision = True


        self.tileMap[12][13].isCollision = True
        self.tileMap[13][14].isCollision = True
        self.tileMap[14][15].isCollision = True

        self.tileMap[16][15].isCollision = True
        self.tileMap[16][16].isCollision = True
        self.tileMap[16][17].isCollision = True

        self.tileMap[16 + 2][15 + 3].isCollision = True
        self.tileMap[16 + 2][16 + 3].isCollision = True
        self.tileMap[16 + 2][17 + 3].isCollision = True

        self.tileMap[16 + 5][15 + 5].isCollision = True
        self.tileMap[16 + 5][16 + 5].isCollision = True
        self.tileMap[16 + 5][17 + 5].isCollision = True
        self.tileMap[16 + 5][14 + 5].isCollision = True
        self.tileMap[16 + 5][13 + 5].isCollision = True
        self.tileMap[16 + 5][12 + 5].isCollision = True
        self.tileMap[16 + 5][11 + 5].isCollision = True
        self.tileMap[15 + 5][17 + 6].isCollision = True

        self.tileMap[16 + 4][10 + 3].isCollision = True
        self.tileMap[16 + 4][11 + 3].isCollision = True
        self.tileMap[16 + 4][12 + 3].isCollision = True

        self.tileMap[16 + 4][12 - 4].isCollision = True
        self.tileMap[16 + 4][11 - 4].isCollision = True
        self.tileMap[16 + 4][10 - 4].isCollision = True


        self.tileMap[7][1].isCollision = True
        self.tileMap[8][1].isCollision = True
        self.tileMap[9][1].isCollision = True

        self.tileMap[10][2].isCollision = True
        self.tileMap[10][3].isCollision = True
        self.tileMap[10][4].isCollision = True
        self.tileMap[10][5].isCollision = True
        self.tileMap[10][6].isCollision = True
        self.tileMap[10][7].isCollision = True

        self.tileMap[7][5].isCollision = True
        self.tileMap[7][6].isCollision = True
        # self.tileMap[7][7].isCollision = True

        self.tileMap[31][18].isCollision = True
        self.tileMap[30][17].isCollision = True
        self.tileMap[30][16].isCollision = True
        self.tileMap[29][15].isCollision = True
        self.tileMap[29][14].isCollision = True
        self.tileMap[29][13].isCollision = True

        self.tileMap[28][12].isCollision = True
        self.tileMap[27][11].isCollision = True

        self.tileMap[26][10].isCollision = True
        self.tileMap[25][10].isCollision = True
        self.tileMap[24][10].isCollision = True
        self.tileMap[23][11].isCollision = True
        self.tileMap[22][12].isCollision = True
        self.tileMap[22][13].isCollision = True
        self.tileMap[22][14].isCollision = True
        self.tileMap[22][15].isCollision = True

        self.tileMap[25][22].isCollision = True
        self.tileMap[25][23].isCollision = True

        self.tileMap[23][25].isCollision = True
        self.tileMap[23][26].isCollision = True

        self.tileMap[21][27].isCollision = True

        # self.tileMap[26][14].isCollision = True
        self.tileMap[26][15].isCollision = True
        self.tileMap[26][16].isCollision = True
        self.tileMap[27][17].isCollision = True

        self.tileMap[31][21].isCollision = True
        self.tileMap[31][22].isCollision = True
        self.tileMap[30][21].isCollision = True
        self.tileMap[29][21].isCollision = True
        self.tileMap[28][20].isCollision = True
        self.tileMap[27][19].isCollision = True
        self.tileMap[27 ][18].isCollision = True


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
