import math
import pygame as pg

from src.game.Player import Player
from src.game.levels import *
from src.game.levels.Level01 import Level01
from src.game.levels.Level02 import Level02


class Game:

    def __init__(self, isLeft : bool, canvas : pg.Rect):
        self.canvas = canvas
        self.isLeft = isLeft
        self.backgroundColor = "black"
        self.currentLevel = 0
        self.levels = [
            Level01(self.isLeft, self.canvas),
            Level02(self.isLeft, self.canvas)
        ]
        self.player = Player(self.isLeft, self.canvas, self.levels[self.currentLevel].map)

        self.addPlayerDataToLevels()

        self.dt = 0

        self.nextLevel = 0
        self.levelChangeTimer : float = 0
        self.levelChangeDelay : float = 2 # seconds
        self.isLevelChanging : bool = False

        self.blinkOpacity = 0


    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_5:
                self.currentLevel = 0 if self.currentLevel - 1 < 0 else self.currentLevel - 1

            # DEBUG level changing
            # if event.key == pg.K_6:
            #     self.currentLevel = len(self.levels) - 1 if self.currentLevel + 1 > len(self.levels) - 1 else self.currentLevel + 1

        self.levels[self.currentLevel].handleEvents(event)
        self.player.handleEvent(event)


    def update(self, dt : float):
        self.dt = dt

        self.levels[self.currentLevel].update(dt)
        self.player.update(dt)

        if self.isLevelChanging:
            self.levelChangeTimer += dt
            if self.levelChangeTimer > self.levelChangeDelay:
                self.handleLevelChange()


        if self.player.playerData.currentLevel < len(self.levels) and self.currentLevel != self.player.playerData.currentLevel:
            self.isLevelChanging = True
            self.nextLevel = self.player.playerData.currentLevel
            self.player.playerData.canMove = False
        if self.player.playerData.currentLevel >= len(self.levels):
            # print("Game over!")
            pass


    def draw(self, screen : pg.Surface):
        # pg.draw.rect(self.screen, self.backgroundColor, self.canvas)
        self.levels[self.currentLevel].draw(screen)
        self.player.draw(screen)

        if self.isLevelChanging:
            self.levelChangeBlink(screen)


    def setBackgroundColor(self, color : pg.Color):
        self.backgroundColor = color


    def handleLevelChange(self):
        print(f"Changing level to {self.nextLevel}")
        self.currentLevel = self.nextLevel
        self.levels[self.currentLevel].reset()
        self.player.tileMap = self.levels[self.currentLevel].map

        self.levelChangeTimer = 0
        self.isLevelChanging = False
        self.player.playerData.canMove = True


    def addPlayerDataToLevels(self):
        for level in self.levels:
            level.playerData = self.player.playerData


    def levelChangeBlink(self, screen : pg.Surface):
        time = (self.levelChangeTimer % (self.levelChangeDelay * 2)) / (self.levelChangeDelay * 2)
        self.blinkOpacity = 255 * math.sin(math.pi * time)

        # print(f"Opacity: {self.blinkOpacity}")

        overlay = pg.Surface((self.canvas.width, self.canvas.height), pg.SRCALPHA)
        overlay.fill((0, 0, 0, self.blinkOpacity))
        screen.blit(overlay, (self.canvas.left, self.canvas.top))
