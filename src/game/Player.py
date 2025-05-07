import pygame as pg

from src.common import Settings
from src.game.PlayerData import PlayerData
from src.game.map.Map import Map
from src.game.map.tiles.Tile import Tile
from src.game.map.tiles.Trigger import Trigger


class Player:
    def __init__(self, isLeft : bool, canvas : pg.Rect, tileMap : Map):
        self.canvas = canvas
        self.isLeft = isLeft
        self.tileMap = tileMap

        self.playerData = PlayerData()

        self.keymap = Settings.PLAYER_LEFT_KEYMAP if isLeft else Settings.PLAYER_RIGHT_KEYMAP
        self.color = "black"

        self.dt : float = 0

        self.isJumpInBuffer : bool = False
        self.shouldBufferedJump : bool = False
        self.inAir : bool = False
        self.isJumping = True

        self.dx = 0
        self.dy = 0

        self.jumpPositionY = self.playerData.posY + self.playerData.posX

        self.movingUp    : bool = False
        self.movingRight : bool = False
        self.movingDown  : bool = True
        self.movingLeft  : bool = False

        self.enteredTriggers = []


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

        if self.playerData.hp <= 0:
            self.playerData.hp = self.playerData.startHp
            self.moveToStart()

        if self.shouldBufferedJump:
            self.shouldBufferedJump = False
            self.jump()


        self.checkEnteredTriggers()
        self.move()
        self.checkCollisions()
        self.updatePosition()


    def draw(self, screen : pg.Surface):
        pg.draw.rect(screen, self.color, (self.canvas.left + self.playerData.posX, self.canvas.top + self.playerData.posY, self.playerData.playerWidth, self.playerData.playerHeight))


    def move(self):
        if self.movingUp:
            if not self.isJumping and self.playerData.velocityY < self.playerData.jumpBufferingDropLevel:
                self.jump()
            else:
                if self.playerData.velocityY > 0 and 0 < (self.jumpPositionY - self.playerData.posY) < self.playerData.jumpBufferingLevel and not self.isJumpInBuffer:
                    self.isJumpInBuffer = True

        self.movingUp = False

        if self.movingRight:
            self.dx += self.playerData.speed * self.dt

        if self.movingLeft:
            self.dx -= self.playerData.speed * self.dt

        self.playerData.velocityY += self.playerData.gravityForce * self.dt
        if self.playerData.velocityY > self.playerData.maxFallingSpeed:
            self.playerData.velocityY = self.playerData.maxFallingSpeed

        self.dy += self.playerData.velocityY * self.dt
        self.playerData.newPosY = self.playerData.posY + self.dy


    def jump(self):
        self.jumpPositionY = self.playerData.posY
        self.playerData.velocityY = -self.playerData.jumpForce
        self.isJumping = True


    def updatePosition(self):
        self.playerData.posX += self.dx
        self.playerData.posY += self.dy


    def checkCollisions(self):
        for i in range(self.tileMap.sizeY):
            for j in range(self.tileMap.sizeX):
                tile = self.tileMap.tileMap[i][j]

                playerColX = self.getPlayerCollisionX()
                playerColY = self.getPlayerCollisionY()
                tileCol = self.getTileCollision(tile)

                if tile.isTrigger:
                    # Scale collision to be 24x24 inside block, to give player more space to movement error
                    tileCol.left += 4
                    tileCol.top += 4
                    tileCol.width -= 4
                    tileCol.height -= 4

                    if playerColX.colliderect(tileCol):
                        tile.onTrigger(self.playerData)
                        self.enteredTriggers.append(tile)
                    continue
                if tile.isCollision:
                    self.checkHorizontalCollisions(playerColX, tileCol)
                    self.checkVerticalCollisions(playerColY, tileCol)


    def checkHorizontalCollisions(self, playerCollision : pg.Rect, tileCollision : pg.Rect):
        if playerCollision.colliderect(tileCollision):
            if self.dx > 0: # right
                self.playerData.posX = tileCollision.left - playerCollision.width - self.canvas.left
            elif self.dx < 0: # left
                self.playerData.posX = tileCollision.right - self.canvas.left
            self.dx = 0


    def checkVerticalCollisions(self, playerCollision : pg.Rect, tileCollision : pg.Rect):
        if playerCollision.colliderect(tileCollision):
            if self.playerData.velocityY > 0.0: # falling
                self.playerData.posY = tileCollision.top - playerCollision.height
                self.dy = 0.0
                self.playerData.velocityY = 0
                self.isJumping = False
                if self.isJumpInBuffer:
                    self.isJumpInBuffer = False
                    self.shouldBufferedJump = True

            elif self.playerData.velocityY < 0.0: # jumping
                self.playerData.posY = tileCollision.bottom
                self.dy = 0.0
                self.playerData.velocityY = 0


    def moveToStart(self):
        self.playerData.posX = self.playerData.startPosX
        self.playerData.posY = self.playerData.startPosY


    def checkEnteredTriggers(self):
        toPop = []

        for trigger in self.enteredTriggers:
            if not self.getPlayerCollisionX().colliderect(self.getTileCollision(trigger)):
                trigger.reset()
                toPop.append(trigger)

        for element in toPop:
            self.enteredTriggers.remove(element)


    def getPlayerCollisionX(self) -> pg.Rect:
        return pg.Rect(self.canvas.left + self.playerData.posX + self.dx, self.canvas.top + self.playerData.posY, self.playerData.playerWidth, self.playerData.playerHeight)


    def getPlayerCollisionY(self) -> pg.Rect:
        return pg.Rect(self.canvas.left + self.playerData.posX, self.canvas.top + self.playerData.newPosY, self.playerData.playerWidth, self.playerData.playerHeight)


    def getTileCollision(self, tile : Tile) -> pg.Rect:
        return pg.Rect(tile.leftTop.x, tile.leftTop.y, Tile.size, Tile.size)