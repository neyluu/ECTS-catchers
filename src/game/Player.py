import pygame as pg

from src.common import Settings
from src.game.map.Map import Map
from src.game.map.tiles.Tile import Tile


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
        self.jumpForce : float = 575
        self.gravityForce : float = 2000
        self.maxFallingSpeed : int = 1000
        self.jumpBufferingLevel : int = 32
        self.jumpBufferingDropLevel : int = 350
        self.isJumpInBuffer : bool = False
        self.shouldBufferedJump : bool = False
        self.inAir : bool = False
        self.isJumping = True

        self.dx = 0
        self.dy = 0

        # top-left
        self.posX : int = 630
        self.posY : int = 950
        self.newPosX : int = -1
        self.newPosY : int = -1

        self.jumpPositionY = self.posY + 48

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

        if self.shouldBufferedJump:
            self.shouldBufferedJump = False
            self.jump()

        self.move()
        self.checkCollisions()
        self.updatePosition()


    def draw(self, screen : pg.Surface):
        pg.draw.rect(screen, self.color, (self.canvas.left + self.posX, self.canvas.top + self.posY, 32, 48))


    def move(self):
        if self.movingUp:
            if not self.isJumping and self.velocityY < self.jumpBufferingDropLevel:
                self.jump()
            else:
                if self.velocityY > 0 and 0 < (self.jumpPositionY - self.posY) < self.jumpBufferingLevel and not self.isJumpInBuffer:
                    self.isJumpInBuffer = True

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


    def jump(self):
        self.jumpPositionY = self.posY
        self.velocityY = -self.jumpForce
        self.isJumping = True


    def updatePosition(self):
        self.posX += self.dx
        self.posY += self.dy


    def checkCollisions(self):
        for i in range(self.tileMap.sizeY):
            for j in range(self.tileMap.sizeX):
                tile = self.tileMap.tileMap[i][j]

                playerColX = pg.Rect(self.canvas.left + self.posX + self.dx, self.canvas.top + self.posY, 32, 48)
                playerColY = pg.Rect(self.canvas.left + self.posX, self.canvas.top + self.newPosY, 32, 48)
                tileCol = pg.Rect(tile.leftTop.x, tile.leftTop.y, Tile.size, Tile.size)

                if tile.isTrigger:
                    if playerColX.colliderect(tileCol):
                        tile.color = "blue"
                    continue
                if tile.isCollision:
                    self.checkHorizontalCollisions(playerColX, tileCol)
                    self.checkVerticalCollisions(playerColY, tileCol)


    def checkHorizontalCollisions(self, playerCollision : pg.Rect, tileCollision : pg.Rect):
        if playerCollision.colliderect(tileCollision):
            if self.dx > 0: # right
                self.posX = tileCollision.left - playerCollision.width - self.canvas.left
            elif self.dx < 0: # left
                self.posX = tileCollision.right - self.canvas.left
            self.dx = 0


    def checkVerticalCollisions(self, playerCollision : pg.Rect, tileCollision : pg.Rect):
        if playerCollision.colliderect(tileCollision):
            if self.velocityY > 0.0: # falling
                self.posY = tileCollision.top - playerCollision.height
                self.dy = 0.0
                self.velocityY = 0
                self.isJumping = False
                if self.isJumpInBuffer:
                    self.isJumpInBuffer = False
                    self.shouldBufferedJump = True

            elif self.velocityY < 0.0: # jumping
                self.posY = tileCollision.bottom
                self.dy = 0.0
                self.velocityY = 0