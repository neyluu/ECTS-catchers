import pygame as pg

from src.game.Player import Player
from src.game.levels.Level import Level
from src.game.map.tiles.DoubleJump import DoubleJump
from src.game.map.tiles.SpeedUp import SpeedUp
from src.gui.GameOver import GameOver
from src.gui.animations.Blink import Blink
from src.gui.InGameUI import InGameUI
import src.config.DebugConfig as Debug

class Game:

    def __init__(self, isLeft : bool, canvas : pg.Rect):
        self.canvas = canvas
        self.isLeft = isLeft
        self.currentLevel = 0

        self.DEBUG_levels = [
            Level(self.canvas, "testlevel.level", 550, 950),
            Level(self.canvas, "testlevel2.level", 450, 950)
        ]

        self.levels = [
            Level(self.canvas, "level01.level", 450, 950),
            Level(self.canvas, "level02.level", 385, 950),
            Level(self.canvas, "level03.level", 365, 955),
            Level(self.canvas, "level04.level", 450, 950),
            Level(self.canvas, "level05.level", 460, 890),
            Level(self.canvas, "level06.level", 70, 760),
            Level(self.canvas, "level07.level", 50, 950)
        ]

        if Debug.DEBUG_LEVELS:
            for i in range(len(self.DEBUG_levels)):
                self.levels.insert(i, self.DEBUG_levels[i])

        self.player = Player(self.isLeft, self.canvas, self.levels[self.currentLevel].map)
        self.setPlayerStartingPosition()

        self.gameOver = GameOver(self.canvas)
        self.isGameOver = False
        self.gameOverAnimation = Blink(self.canvas)
        self.gameOverAnimation.time = 10

        self.dt : float = 0

        self.nextLevel : int = 0
        self.isLevelChanging : bool = False
        self.levelChanged : bool = False
        self.nextLevelAnimation = Blink(self.canvas)

        self.inGameUi = InGameUI(self.canvas, self.player.playerData)
        self.timerStarted : bool = False
        self.lastLevelTime : int = 0

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

        if not self.timerStarted:
            self.inGameUi.gameTimer.start()
            self.timerStarted = True


        self.dt = dt

        if not self.paused:
            self.inGameUi.update()

        if self.isGameOver:
            self.gameOver.update(dt)
            self.gameOverAnimation.update(dt)
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
        if self.isGameOver and self.gameOverAnimation.timeElapsed > self.gameOverAnimation.time / 2:
            self.gameOver.draw(screen)
        else:
            self.levels[self.currentLevel].draw(screen)
            self.player.draw(screen)
            self.inGameUi.draw(screen)

            if self.isLevelChanging:
                self.nextLevelAnimation.draw(screen)

        self.gameOverAnimation.draw(screen)


    def isNextLevel(self) -> bool:
        return self.currentLevel != self.player.playerData.currentLevel


    def changeLevel(self):
        if Debug.DEBUG_LEVELS:
            if self.currentLevel >= len(self.DEBUG_levels):
                index = self.currentLevel - len(self.DEBUG_levels) + 1
                self.player.playerData.stats.times[index] = self.inGameUi.gameTimer.getTotalSeconds() - self.lastLevelTime
                self.player.playerData.stats.deaths[index] = self.player.deaths
        else:
            self.player.playerData.stats.times[self.currentLevel + 1] = self.inGameUi.gameTimer.getTotalSeconds() - self.lastLevelTime
            self.player.playerData.stats.deaths[self.currentLevel + 1] = self.player.deaths

        self.lastLevelTime = self.inGameUi.gameTimer.getTotalSeconds()
        self.player.deaths = 0

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
        DoubleJump.activeInstances = 0
        SpeedUp.activeInstances = 0

        if self.nextLevel >= len(self.levels):
            print("Game over!")
            self.gameOverAnimation.start()
            self.isGameOver = True
            self.player.playerData.currentLevel = self.currentLevel

            self.player.playerData.stats.times[7] = self.inGameUi.gameTimer.getTotalSeconds() - self.lastLevelTime
            self.player.playerData.stats.deaths[7] = self.player.deaths

            self.player.playerData.stats.calculateTotal()
            self.gameOver.init(self.player.playerData.stats)
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


    def reset(self):
        self.currentLevel = 0
        self.player.playerData.currentLevel = 0
        self.player.playerData.levelChanged = False
        self.player.tileMap = self.levels[self.currentLevel].map
        self.setPlayerStartingPosition()
        self.player.reset()
        self.player.playerData.hp = self.player.playerData.startHp
        self.isGameOver = False
        self.gameOverAnimation.reset()
        self.nextLevel = 0
        self.isLevelChanging = False
        self.levelChanged = False
        self.nextLevelAnimation.reset()
        self.timerStarted = False
        self.lastLevelTime = 0
        self.paused = False
        self.playerPaused = False
        self.inGameUi.resumeTimer()

        self.DEBUG_changeLevel = False



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


