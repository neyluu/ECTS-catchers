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

        self.dt : float = 0
        self.speed : float = 200
        self.velocityX : float = 0
        self.velocityY : float = 0
        self.jumpForce : float = 500
        self.gravityForce : float = 2000
        self.maxFallingSpeed : int = 1000
        self.inAir : bool = False
        self.isJumping = True

        self.dx = 0
        self.dy = 0

        self.posX : int = 100
        self.posY : int = 100
        self.newPosX : int = -1
        self.newPosY : int = -1

        self.movingUp    : bool = False
        self.movingRight : bool = False
        self.movingDown  : bool = True
        self.movingLeft  : bool = False


    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == self.keymap.MOVE_UP:
                self.movingUp = True

            if event.key == self.keymap.MOVE_RIGHT:
                self.movingRight = True

            if event.key == self.keymap.MOVE_LEFT:
                self.movingLeft = True

        if event.type == pg.KEYUP:
            if event.key == self.keymap.MOVE_UP:
                self.movingUp = False

            if event.key == self.keymap.MOVE_RIGHT:
                self.movingRight = False

            if event.key == self.keymap.MOVE_LEFT:
                self.movingLeft = False


    def update(self, dt : float):
        self.dt = dt

        self.dx = 0
        self.dy = 0

        self.move()
        self.checkCollisions()
        self.updatePosition()


    def draw(self, screen : pg.Surface):
        pg.draw.rect(screen, self.color, (self.canvas.left + self.posX, self.canvas.top + self.posY, 32, 48))


    def move(self):
        if self.movingUp and not self.isJumping:
            self.velocityY = -self.jumpForce
            self.isJumping = True

        self.movingUp = False

        if self.movingRight:
            self.dx += self.speed * self.dt

        if self.movingLeft:
            self.dx -= self.speed * self.dt

        self.velocityY += self.gravityForce * self.dt
        if self.velocityY > self.maxFallingSpeed:
            self.velocityY = self.maxFallingSpeed

        self.dy += self.velocityY * self.dt
        self.newPosY = self.posY + self.dy


    def updatePosition(self):
        self.posX += self.dx
        self.posY += self.dy

    def checkCollisions(self):
        for i in range(self.tileMap.sizeY):
            for j in range(self.tileMap.sizeX):
                tile = self.tileMap.tileMap[i][j]
                if not tile.isCollision:
                    continue

                playerColX = pg.Rect(self.canvas.left + self.posX + self.dx, self.canvas.top + self.posY, 32, 48)
                tileCol = pg.Rect(tile.leftTop.x, tile.leftTop.y, Tile.size, Tile.size)

                if playerColX.colliderect(tileCol):
                    print("xd: ", self.posX, self.posY)
                    if self.dx > 0:
                        self.posX = tileCol.left - playerColX.width - self.canvas.left
                    elif self.dx < 0:
                        self.posX = tileCol.right - self.canvas.left
                    print(self.posX, self.posY)
                    self.dx = 0

                playerColY = pg.Rect(self.canvas.left + self.posX, self.canvas.top + self.newPosY, 32, 48)
                if playerColY.colliderect(tileCol):
                    if self.velocityY > 0.0:
                        self.posY = tileCol.top - playerColY.height
                        self.dy = 0.0
                        self.velocityY = 0
                        self.isJumping = False

                    elif self.velocityY < 0.0:
                        self.posY = tileCol.bottom
                        self.dy = 0.0
                        self.velocityY = 0
