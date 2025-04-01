import pygame as pg

from src.game.PlayerKeymap import PlayerKeymap
from src.game.map.Map import Map
from src.game.map.tiles.Tile import Tile
from src.common import Settings

class Player:
    def __init__(self, isLeft : bool, canvas : pg.Rect, tileMap : Map):
        self.canvas = canvas
        self.isLeft = isLeft
        self.tileMap = tileMap

        self.keymap = Settings.PLAYER_LEFT_KEYMAP if isLeft else Settings.PLAYER_RIGHT_KEYMAP
        self.color = "black"

        self.dt = 0
        self.speed = 200

        # TODO later rebuild to pos in board grid
        self.posX : int = 100
        self.posY : int = 100
        self.newPosX : int = self.posX
        self.newPosY : int = self.posY

        self.movingUp    : bool = False
        self.movingRight : bool = False
        self.movingDown  : bool = False
        self.movingLeft  : bool = False



    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == self.keymap.MOVE_UP:
                self.movingUp = True
            if event.key == self.keymap.MOVE_RIGHT:
                self.movingRight = True
            if event.key == self.keymap.MOVE_DOWN:
                self.movingDown = True
            if event.key == self.keymap.MOVE_LEFT:
                self.movingLeft = True
        if event.type == pg.KEYUP:
            if event.key == self.keymap.MOVE_UP:
                self.movingUp = False
            if event.key == self.keymap.MOVE_RIGHT:
                self.movingRight = False
            if event.key == self.keymap.MOVE_DOWN:
                self.movingDown = False
            if event.key == self.keymap.MOVE_LEFT:
                self.movingLeft = False


    def update(self, dt : float):
        self.dt = dt
        self.move()
        self.checkCollisions()
        print(self.isLeft, self.posX, self.posY)



    def draw(self, screen : pg.Surface):
        pg.draw.rect(screen, self.color, (self.canvas.left + self.posX, self.canvas.top + self.posY, 32, 48))


    def move(self):
        if self.movingUp:
            self.posY = self.posY - self.speed * self.dt

        if self.movingRight:
            self.posX = self.posX + self.speed * self.dt

        if self.movingDown:
            self.posY = self.posY + self.speed * self.dt

        if self.movingLeft:
            self.posX = self.posX - self.speed * self.dt


    def checkCollisions(self):
        for i in range(self.tileMap.sizeY):
            for j in range(self.tileMap.sizeX):
                tile = self.tileMap.tileMap[i][j]
                if not tile.isCollision:
                    continue

                playerCol = pg.Rect(self.canvas.left + self.posX, self.canvas.top + self.posY, 32, 48)
                tileCol = pg.Rect(tile.leftTop.x, tile.leftTop.y, Tile.size, Tile.size)

                if playerCol.colliderect(tileCol):
                    if self.movingLeft or self.movingRight:
                        if playerCol.left > tileCol.left:
                            self.posX = tileCol.left + Tile.size - self.canvas.left
                        if playerCol.left < tileCol.left:
                            self.posX = tileCol.left - Tile.size - self.canvas.left
                    if self.movingUp or self.movingDown:
                        if playerCol.top < tileCol.top:
                            self.posY = tileCol.top - 48
                        if playerCol.top > tileCol.top:
                            self.posY = tileCol.top + Tile.size


