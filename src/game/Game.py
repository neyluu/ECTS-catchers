import pygame as pg

from src.game.Player import Player
from src.game.levels.Level import Level
from src.gui.animations.Blink import Blink
from src.gui.InGameUI import InGameUI
import src.config.DebugConfig as Debug

class Game:

    def __init__(self, isLeft : bool, canvas : pg.Rect):
        self.canvas = canvas
        self.isLeft = isLeft
        self.currentLevel = 0

        self.levels = [
            Level(self.isLeft, self.canvas, "level01.level", 450, 950),
            Level(self.isLeft, self.canvas, "level02.level", 450, 950),
            Level(self.isLeft, self.canvas, "level03.level", 450, 950),
            Level(self.isLeft, self.canvas, "level04.level", 450, 950),
            Level(self.isLeft, self.canvas, "level05.level", 450, 950),
            Level(self.isLeft, self.canvas, "level06.level", 450, 950)
        ]

        if Debug.DEBUG_LEVELS:
            self.levels.insert(0, Level(self.isLeft, self.canvas, "testlevel.level", 550, 950))
            self.levels.insert(1, Level(self.isLeft, self.canvas, "testlevel2.level", 450, 950))
            print(self.levels)
            print(len(self.levels))

        self.player = Player(self.isLeft, self.canvas, self.levels[self.currentLevel].map)
        self.setPlayerStartingPosition()

        self.dt : float = 0

        self.nextLevel : int = 0
        self.isLevelChanging : bool = False
        self.levelChanged : bool = False
        self.nextLevelAnimation = Blink(self.canvas)

        self.inGameUi = InGameUI(self.canvas, self.player.playerData)

        self.paused = False


    def handleEvent(self, event):
        if self.paused:
            return

        self.levels[self.currentLevel].handleEvents(event)
        self.player.handleEvent(event)


    def update(self, dt : float):
        if self.paused:
            return

        self.dt = dt

        if not self.paused:
            self.inGameUi.update()

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
            self.nextLevel = self.player.playerData.currentLevel

            if self.nextLevel >= len(self.levels):
                print("Game over!")
                self.player.playerData.currentLevel = self.currentLevel
                return

            self.isLevelChanging = True
            self.player.playerData.canMove = False
            self.nextLevelAnimation.start()


    def draw(self, screen : pg.Surface):
        self.levels[self.currentLevel].draw(screen)
        self.player.draw(screen)
        self.inGameUi.draw(screen)

        if self.isLevelChanging:
            self.nextLevelAnimation.draw(screen)


    def isNextLevel(self) -> bool:
        return self.currentLevel != self.player.playerData.currentLevel


    def handleLevelChange(self):
        print(f"Changing level to {self.nextLevel}")
        self.currentLevel = self.nextLevel
        self.player.playerData.levelChanged = False

        self.setPlayerStartingPosition()

        self.player.tileMap = self.levels[self.currentLevel].map
        self.player.reset()


    def setPlayerStartingPosition(self):
        self.player.playerData.startPosX = self.levels[self.currentLevel].startPosX
        self.player.playerData.startPosY = self.levels[self.currentLevel].startPosY


    def pause(self):
        self.paused = True
        self.inGameUi.pauseTimer()


    def unPause(self):
        self.paused = False
        self.inGameUi.resumeTimer()
        self.player.unPause()