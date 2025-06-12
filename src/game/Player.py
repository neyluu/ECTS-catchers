import pygame as pg

import src.config.DebugConfig as Debug
from src.config import Settings
from src.sounds.LoopSound import LoopSound
from src.sounds.SFX import SFX
from src.game.PlayerData import PlayerData
from src.game.SpriteAnimation import SpriteAnimation
from src.game.map.Map import Map
from src.game.map.tiles.Tile import Tile
from src.gui.animations.Blink import Blink


class Player:
    def __init__(self, isLeft : bool, canvas : pg.Rect, tileMap : Map):
        self.canvas = canvas
        self.isLeft = isLeft
        self.tileMap = tileMap

        self.playerData = PlayerData()

        self.moveAnimations = {
            "idle": SpriteAnimation("assets/animations/playerIdle", 0.5),
            "runLeft": SpriteAnimation("assets/animations/playerRunLeft", 0.4),
            "runRight": SpriteAnimation("assets/animations/playerRunRight", 0.4),
            "jump": SpriteAnimation("assets/animations/playerJump", 0.5),
            "jumpRight" : SpriteAnimation("assets/animations/playerJumpRight", 1),
            "jumpLeft" : SpriteAnimation("assets/animations/playerJumpLeft", 1),
        }
        self.currentMoveAnimation = "idle"

        self.deathSFX = SFX("assets/audio/death.wav")
        self.deathSoundPlayed : bool = False

        self.movingSound = LoopSound("assets/audio/step_1.wav", 0.2)
        self.movingSoundPlaying = False
        self.movingSound.start()

        self.deadBlinkAnimation = Blink(canvas)
        self.deadBlinkAnimation.color = pg.Color(100, 20, 20)
        self.deadBlinkAnimation.time = 1

        self.isDead = False
        self.deadHandled = False

        self.keymap = Settings.PLAYER_LEFT_KEYMAP if isLeft else Settings.PLAYER_RIGHT_KEYMAP
        self.color = "black"

        self.dt : float = 0

        self.isJumpInBuffer : bool = False
        self.shouldBufferedJump : bool = False
        self.isJumping = True
        self.doubleJumped = False

        self.dx = 0
        self.dy = 0

        self.jumpPositionY = self.playerData.posY + self.playerData.posX

        self.movingUp    : bool = False
        self.movingRight : bool = False
        self.movingDown  : bool = True
        self.movingLeft  : bool = False

        self.enteredTriggers = []


    def handleEvent(self, event):
        if event.type == pg.KEYDOWN and self.playerData.canMove:
            if event.key == self.keymap.MOVE_UP:
                self.movingUp = True
                self.currentMoveAnimation = "jump"

            if event.key == self.keymap.MOVE_RIGHT:
                self.movingRight = True
                self.currentMoveAnimation = "runRight"

            if event.key == self.keymap.MOVE_LEFT:
                self.movingLeft = True
                self.currentMoveAnimation = "runLeft"


        if event.type == pg.KEYUP:
            if event.key == self.keymap.MOVE_UP:
                self.movingUp = False

            if event.key == self.keymap.MOVE_RIGHT:
                self.movingRight = False

            if event.key == self.keymap.MOVE_LEFT:
                self.movingLeft = False

            self.currentMoveAnimation = "idle"


    def update(self, dt : float):
        self.dt = dt

        self.dx = 0
        self.dy = 0

        self.checkHP()
        self.handleOnDead(dt)

        if self.shouldBufferedJump:
            self.shouldBufferedJump = False
            self.jump()

        if self.playerData.velocityY < 0:
            self.currentMoveAnimation = "jump"
        if self.playerData.velocityY == 0:
            self.currentMoveAnimation = "idle"

        self.checkEnteredTriggers()
        self.move()
        self.checkCollisions()
        self.updatePosition()
        self.moveAnimations[self.currentMoveAnimation].update(dt)
        self.checkMovementSounds(dt)

        self.playerData.gotDamaged = False


    def draw(self, screen : pg.Surface):
        position = (self.canvas.left + self.playerData.posX, self.canvas.top + self.playerData.posY, self.playerData.playerWidth, self.playerData.playerHeight)

        # pg.draw.rect(screen, self.color, (self.canvas.left + self.playerData.posX, self.canvas.top + self.playerData.posY, self.playerData.playerWidth, self.playerData.playerHeight))
        self.moveAnimations[self.currentMoveAnimation].draw(screen, position)
        if Debug.DEBUG_PLAYER_COLLISION_VISIBLE:
            self.DEBUG_drawCollisionBox(screen)

        if self.isDead:
            self.deadBlinkAnimation.draw(screen)


    def handleOnDead(self, dt):
        if self.isDead:
            if not self.deathSoundPlayed:
                self.deathSFX.play()
                self.deathSoundPlayed = True

            if self.deadBlinkAnimation.timeElapsed > self.deadBlinkAnimation.time / 2 and not self.deadHandled:
                self.playerData.hp = self.playerData.startHp
                self.reset()
                self.deadHandled = True
            if not self.deadBlinkAnimation.running:
                self.isDead = False
                self.deadHandled = False
                self.deadBlinkAnimation.reset()
                self.deathSoundPlayed = False
            else:
                self.deadBlinkAnimation.update(dt)


    def checkHP(self):
        if self.playerData.gotDamaged:
            self.playerData.hp -= 1

        if self.playerData.hp <= 0:
            self.isDead = True
            self.playerData.canMove = False
            self.deadBlinkAnimation.start()


    def move(self):
        if self.movingUp:
            if not self.isJumping and self.playerData.velocityY < self.playerData.jumpBufferingDropLevel:
                self.jump()

            # self.playerData.velocityY < self.playerData.jumpBufferingDropLevel is responsible for disabling jumping during falling
            # eventually can be disabled for double jump

            # Version on double jump without possibility of single jump during falling
            # elif self.playerData.canDoubleJump and not self.doubleJumped and self.playerData.velocityY < self.playerData.jumpBufferingDropLevel:

            # Double jump with possible single jump during falling
            elif self.playerData.canDoubleJump and not self.doubleJumped:
                self.jump()
                self.doubleJumped = True
            else:
                if self.playerData.velocityY > 0 and 0 < (self.jumpPositionY - self.playerData.posY) < self.playerData.jumpBufferingLevel and not self.isJumpInBuffer:
                    self.isJumpInBuffer = True

        self.movingUp = False

        if self.movingRight:
            self.dx += self.playerData.speed * self.dt
            if self.isJumping:
                self.currentMoveAnimation = "jumpRight"
            else:
                self.currentMoveAnimation = "runRight"

        if self.movingLeft:
            self.dx -= self.playerData.speed * self.dt
            if self.isJumping:
                self.currentMoveAnimation = "jumpLeft"
            else:
                self.currentMoveAnimation = "runLeft"

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
        mapOffsetX : int = self.tileMap.offsetX
        mapOffsetY : int = self.tileMap.offsetY

        tilePosX : int = int((self.playerData.posX - mapOffsetX) // Tile.size)
        tilePosY : int = int((self.playerData.posY - mapOffsetY) // Tile.size)

        tiles = []
        for dy in range(-2, 3):
            for dx in range(-2, 3):
                try:
                    tile = self.tileMap.tileMap[tilePosY + dy][tilePosX + dx]
                    tiles.append(tile)
                except IndexError:
                    continue

        for tile in tiles:
            if not tile.isTrigger and not tile.isCollision:
                continue

            playerColX = self.getPlayerCollisionX()
            playerColY = self.getPlayerCollisionY()

            tileCol = tile.collision

            if tile.isTrigger:
                if playerColX.colliderect(tileCol):
                    tile.onTrigger(self.playerData)
                    self.enteredTriggers.append(tile)
                continue

            if tile.isCollision:
                self.checkHorizontalCollisions(playerColX, tileCol)
                self.checkVerticalCollisions(playerColY, tileCol)


    def checkHorizontalCollisions(self, playerCollision : pg.Rect, tileCollision: pg.Rect):
        if playerCollision.colliderect(tileCollision):
            collisionOffsetX = self.playerData.playerWidth - playerCollision.width

            if self.dx > 0:  # moving right
                self.playerData.posX = int(tileCollision.left - self.playerData.playerWidth + collisionOffsetX / 2 - self.canvas.left)
            elif self.dx < 0:  # moving left
                self.playerData.posX = int(tileCollision.right - collisionOffsetX / 2 - self.canvas.left)

            self.dx = 0

    def checkVerticalCollisions(self, playerCollision : pg.Rect, tileCollision : pg.Rect):
        if playerCollision.colliderect(tileCollision):
            if self.playerData.velocityY > 0.0 and playerCollision.top < tileCollision.top: # falling
                self.playerData.posY = tileCollision.top - playerCollision.height
                self.dy = 0.0
                self.playerData.velocityY = 0
                self.isJumping = False
                self.doubleJumped = False
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
            if not self.getPlayerCollisionX().colliderect(trigger.collision):
                trigger.reset()
                toPop.append(trigger)

        for element in toPop:
            self.enteredTriggers.remove(element)


    def getPlayerCollisionX(self) -> pg.Rect:
        offset = 2
        return pg.Rect(
            self.canvas.left + self.playerData.posX + self.dx + offset * 2,
            self.canvas.top + self.playerData.posY + offset,
            self.playerData.playerWidth - offset * 4,
            self.playerData.playerHeight - offset * 2
        )

    def getPlayerCollisionY(self) -> pg.Rect:
        offset = 2
        return pg.Rect(
            self.canvas.left + self.playerData.posX + offset * 2,
            self.canvas.top + self.playerData.newPosY + offset // 2,
            self.playerData.playerWidth - offset * 4,
            self.playerData.playerHeight - offset
        )


    def checkMovementSounds(self, dt : float):
        isMovingOnGround = self.dx != 0 and not self.isJumping
        if isMovingOnGround:
            if not self.movingSoundPlaying:
                self.movingSoundPlaying = True
            self.movingSound.update(dt)
        else:
            if self.movingSoundPlaying:
                self.movingSoundPlaying = False


    def reset(self):
        self.moveToStart()
        self.playerData.reset()
        self.tileMap.reset()


    def unPause(self):
        self.movingUp = False
        self.movingRight = False
        self.movingDown = False
        self.movingLeft = False


    def DEBUG_drawCollisionBox(self, screen: pg.Surface):
        pg.draw.rect(screen, (255, 0, 0), self.getPlayerCollisionX(), 1)
        pg.draw.rect(screen, (0, 255, 0), self.getPlayerCollisionY(), 1)
