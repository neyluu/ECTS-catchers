import random
import time

import pygame as pg

import src.config.PowerUpsConfig as Config
from src.game.map.tiles.Coin import Coin
from src.game.map.tiles.Tile import Tile

class Map:
    def __init__(self, canvas: pg.Rect):
        self.canvas = canvas

        random.seed(time.time())

        self.sizeX = 29
        self.sizeY = 33
        self.offsetX = (canvas.width - self.sizeX * Tile.size) // 2
        self.offsetY = (canvas.height - self.sizeY * Tile.size) // 2

        self.tileMap = []

        self.initTileMap()


    def handleEvent(self, event):
        pass


    def update(self, dt : float):
        for i in range(self.sizeY):
            for j in range(self.sizeX):
                tile = self.tileMap[i][j]
                tile.update(dt)


    def draw(self, screen: pg.Surface):
        for i in range(self.sizeY):
            for j in range(self.sizeX):
                tile = self.tileMap[i][j]
                tile.draw(screen)


    def setTile(self, x : int, y : int,  tile : Tile):
        left = self.canvas.left + (y * Tile.size) + self.offsetX
        top = self.canvas.top + (x * Tile.size) + self.offsetY
        tile.setLeftTop(pg.Vector2(left, top))
        self.tileMap[x][y] = tile


    def initTileMap(self):
        for i in range(self.sizeY):
            innerList = []
            for j in range(self.sizeX):
                innerList.append(None)
            self.tileMap.append(innerList)


    def reset(self):
        for row in self.tileMap:
            for tile in row:
                tile.onMapReset()


    def checkCoins(self):
        coinsSum : int = 0
        coinsCount : int = 0
        coinTiles = []

        for i in range(self.sizeY):
            for j in range(self.sizeX):
                tile = self.tileMap[i][j]
                if isinstance(tile, Coin):
                    coinsSum += tile.points
                    coinsCount += 1
                    coinTiles.append(tile)

        if coinsCount < 7 or coinsCount > 12:
            print("ERROR: invalid number of coins on level!")
            return

        iterations = 0
        MAX_ITERATIONS = 1000

        while coinsSum != 30 and iterations < MAX_ITERATIONS:
            coinsSum = 0
            iterations += 1

            for tile in coinTiles:
                tile.points = random.randint(Config.COIN_MIN_POINTS, Config.COIN_MAX_POINTS)
                coinsSum += tile.points

        if iterations >= MAX_ITERATIONS:
            print("ERROR, max iterations reached")
