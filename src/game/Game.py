import math
import pygame as pg

from src.game.Player import Player
from src.game.levels import *
from src.game.levels.Level01 import Level01
from src.game.levels.Level02 import Level02
from src.gui.animations.Blink import Blink


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
        self.nextLevelAnimation = Blink(self.canvas)

        self.addPlayerDataToLevels()

        self.dt : float = 0

        self.nextLevel : int = 0
        self.isLevelChanging : bool = False
        self.levelChanged : bool = False


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
            if self.nextLevelAnimation.timeElapsed > self.nextLevelAnimation.time / 2 and not self.levelChanged:
                self.handleLevelChange()
                self.levelChanged = True

            if not self.nextLevelAnimation.running:
                self.isLevelChanging = False
                self.levelChanged = False
                self.nextLevelAnimation.reset()
            else:
                self.nextLevelAnimation.update(dt)

        if self.isNextLevel():
            self.isLevelChanging = True
            self.nextLevel = self.player.playerData.currentLevel
            self.player.playerData.canMove = False
            self.nextLevelAnimation.start()

        if self.player.playerData.currentLevel >= len(self.levels):
            # print("Game over!")
            pass


    def draw(self, screen : pg.Surface):
        # pg.draw.rect(self.screen, self.backgroundColor, self.canvas)
        self.levels[self.currentLevel].draw(screen)
        self.player.draw(screen)

        if self.isLevelChanging:
            self.nextLevelAnimation.draw(screen)


    def isNextLevel(self) -> bool:
        return self.player.playerData.currentLevel < len(self.levels) and self.currentLevel != self.player.playerData.currentLevel


    def setBackgroundColor(self, color : pg.Color):
        self.backgroundColor = color


    def handleLevelChange(self):
        print(f"Changing level to {self.nextLevel}")
        self.currentLevel = self.nextLevel
        self.levels[self.currentLevel].reset()
        self.player.tileMap = self.levels[self.currentLevel].map
        self.player.playerData.canMove = True


    def addPlayerDataToLevels(self):
        for level in self.levels:
            level.playerData = self.player.playerData
