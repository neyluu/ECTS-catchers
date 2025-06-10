import pygame as pg

from src.game.Player import Player
from src.game.levels.Level import Level
from src.gui.GameOver import GameOver
from src.gui.animations.Blink import Blink
from src.gui.InGameUI import InGameUI
import src.config.DebugConfig as Debug

class Game:

    def __init__(self, isLeft : bool, canvas : pg.Rect):
        self.canvas = canvas
        self.isLeft = isLeft
        self.currentLevel = 0

        self.levels = [
            Level(self.canvas, "level01.level", 450, 950),
            Level(self.canvas, "level02.level", 450, 950),
            Level(self.canvas, "level03.level", 450, 950),
            Level(self.canvas, "level04.level", 450, 950),
            Level(self.canvas, "level05.level", 450, 950),
            Level(self.canvas, "level06.level", 450, 950),
            Level(self.canvas, "level07.level", 450, 950)
        ]

        if Debug.DEBUG_LEVELS:
            pass
            self.levels.insert(0, Level(self.canvas, "testlevel.level", 550, 950))
            self.levels.insert(1, Level(self.canvas, "testlevel2.level", 450, 950))

        self.player = Player(self.isLeft, self.canvas, self.levels[self.currentLevel].map)
        self.setPlayerStartingPosition()

        self.gameOver = GameOver(self.canvas)
        self.isGameOver = False

        self.dt : float = 0

        self.nextLevel : int = 0
        self.isLevelChanging : bool = False
        self.levelChanged : bool = False
        self.nextLevelAnimation = Blink(self.canvas)

        self.inGameUi = InGameUI(self.canvas, self.player.playerData)

        self.paused = False
        self.playerPaused = False


        self.DEBUG_changeLevel = False


    def handleEvent(self, event):
        if self.paused:
            return

        if Debug.DEBUG_LEVEL_CHANGE_SHORTCUTS:
            self.DEBUG_checkLevelChange(event)

        if self.isGameOver:
            self.gameOver.handleEvents(event)
        else:
            self.levels[self.currentLevel].handleEvents(event)
            self.player.handleEvent(event)


    def update(self, dt : float):
        if self.paused:
            return

        self.dt = dt

        if not self.paused:
            self.inGameUi.update()

        if self.isGameOver:
            self.gameOver.update(dt)
        else:
            self.levels[self.currentLevel].update(dt)

            if not self.playerPaused:
                self.player.update(dt)

            if self.isLevelChanging:
                if self.nextLevelAnimation.timeElapsed > self.nextLevelAnimation.time / 2 and not self.levelChanged:
                    self.changeLevel()
                    self.levelChanged = True

                if not self.nextLevelAnimation.running:
                    self.isLevelChanging = False
                    self.levelChanged = False
                    self.nextLevelAnimation.reset()
                    self.playerPaused = False
                    self.inGameUi.resumeTimer()
                else:
                    self.nextLevelAnimation.update(dt)

            if self.isNextLevel() or self.DEBUG_changeLevel :
                self.prepareForLevelChange()
            self.DEBUG_changeLevel = False


    def draw(self, screen : pg.Surface):
        if self.isGameOver:
            self.gameOver.draw(screen)
        else:
            self.levels[self.currentLevel].draw(screen)
            self.player.draw(screen)
            self.inGameUi.draw(screen)

            if self.isLevelChanging:
                self.nextLevelAnimation.draw(screen)


    def isNextLevel(self) -> bool:
        return self.currentLevel != self.player.playerData.currentLevel


    def changeLevel(self):
        print(f"Changing level to {self.nextLevel}")
        self.currentLevel = self.nextLevel
        self.player.playerData.levelChanged = False

        self.setPlayerStartingPosition()

        self.player.tileMap = self.levels[self.currentLevel].map
        self.player.reset()


    def prepareForLevelChange(self):
        self.playerPaused = True
        self.inGameUi.pauseTimer()
        self.nextLevel = self.player.playerData.currentLevel

        if self.nextLevel >= len(self.levels):
            print("Game over!")
            self.isGameOver = True
            self.player.playerData.currentLevel = self.currentLevel
            return
        if self.nextLevel < 0:
            print("Theres no more previous levels! Setting level to 0")
            self.player.playerData.currentLevel = 0
            return

        self.isLevelChanging = True
        self.player.playerData.canMove = False
        self.nextLevelAnimation.start()


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



    def DEBUG_checkLevelChange(self, event):
        if self.isLeft:
            prevKey = pg.K_4
            nextKey = pg.K_5
        else:
            prevKey = pg.K_6
            nextKey = pg.K_7

        if event.type == pg.KEYDOWN:
            if event.key == prevKey:
                self.player.playerData.currentLevel -= 1
                self.DEBUG_changeLevel = True
            elif event.key == nextKey:
                self.player.playerData.currentLevel += 1
                self.DEBUG_changeLevel = True


