import random
import time

import pygame as pg

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
        print("\nChecking coins...")

        startSum : int = 0
        coinsCount : int = 0
        coinTiles = []
        for i in range(self.sizeY):
            for j in range(self.sizeX):
                tile = self.tileMap[i][j]
                if isinstance(tile, Coin):
                    startSum += tile.points
                    coinsCount += 1
                    coinTiles.append(tile)

        print(f"Start sum: {startSum} coins count: {coinsCount}")

        for tile in coinTiles:
            print(f"{tile.points} ", end="")
        print("")

        difference : int = 30 - startSum

        if difference == 0:
            return
        elif difference < 0:
            if difference == -1:
                index = random.randint(0, len(coinTiles) - 1)
                coinTiles[index].points -= 1
                return

            pointsToReduce = []
            pointsSum : int = 0
            # while pointsSum != abs(difference):
            MAX_ATTEMPTS = 1000  # prevent infinite loops

            attempts = 0
            while attempts < MAX_ATTEMPTS:
                attempts += 1
                pointsToReduce = []
                pointsSum = 0
                for i in range(len(coinTiles)):
                    maxPoint = min(abs(difference) - pointsSum, coinTiles[i].points - 1)
                    if maxPoint <= 0:
                        pointsToReduce.append(0)
                    else:
                        randPoint = random.randint(0, maxPoint)
                        pointsToReduce.append(randPoint)
                        pointsSum += randPoint
                    if pointsSum == abs(difference):
                        break
                if pointsSum == abs(difference):
                    break
            else:
                print("Couldn't find a valid combination within max attempts.")

            print(pointsToReduce)

            for i in range(len(pointsToReduce)):
                coinTiles[i].points -= pointsToReduce[i]

            print("FINAL:")
            for tile in coinTiles:
                print(f"{tile.points} ", end="")
            print("")

            sum = 0
            for tile in coinTiles:
                sum += tile.points
            print(f"FINAL SUM: {sum}")
            if sum != 30:
                print("ERROR: sum is not 30")








