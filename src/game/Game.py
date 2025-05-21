import math
import pygame as pg

from src.game.Player import Player
from src.game.levels import *
from src.game.levels.Level01 import Level01
from src.game.levels.Level02 import Level02
from src.gui.animations.Blink import Blink
from src.gui.Timer import Timer

class Game:

    def __init__(self, isLeft : bool, canvas : pg.Rect):
        self.canvas = canvas
        self.isLeft = isLeft
        self.backgroundColor = "black"
        self.currentLevel = 0
        self.levels = [
            Level01(self.isLeft, self.canvas),
            Level01(self.isLeft, self.canvas),
            Level02(self.isLeft, self.canvas)
        ]
        self.currentLevel = 0
        self.player = Player(self.isLeft, self.canvas, self.levels[self.currentLevel].map)
        self.nextLevelAnimation = Blink(self.canvas)

        self.addPlayerDataToLevels()

        self.dt : float = 0

        self.nextLevel : int = 0
        self.isLevelChanging : bool = False
        self.levelChanged : bool = False

        self.game_timer = Timer()
        self.timer_position = (self.canvas.x + 320, self.canvas.y + 4)
        self.game_paused = False

    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                self.game_paused = not self.game_paused  # Przełącz stan pauzy
                if self.game_paused:
                    self.game_timer.pause()  # pauza
                else:
                    self.game_timer.resume()  # wznow
                return
            if self.game_paused:
                return

        self.levels[self.currentLevel].handleEvents(event)
        self.player.handleEvent(event)


    def update(self, dt : float):
        self.dt = dt

        if not self.game_paused:
            self.game_timer.update()

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
        # pg.draw.rect(self.screen, self.backgroundColor, self.canvas)
        self.levels[self.currentLevel].draw(screen)
        self.player.draw(screen)

        self.game_timer.draw(screen, self.timer_position)

        if self.isLevelChanging:
            self.nextLevelAnimation.draw(screen)


    def isNextLevel(self) -> bool:
        return self.currentLevel != self.player.playerData.currentLevel


    def setBackgroundColor(self, color : pg.Color):
        self.backgroundColor = color


    def handleLevelChange(self):
        print(f"Changing level to {self.nextLevel}")
        self.currentLevel = self.nextLevel
        self.player.playerData.levelChanged = False

        self.levels[self.currentLevel].reset(self.player.playerData)
        self.player.playerData.startPosX = self.levels[self.currentLevel].startPosX
        self.player.playerData.startPosY = self.levels[self.currentLevel].startPosY

        self.player.tileMap = self.levels[self.currentLevel].map
        self.player.reset()


    def addPlayerDataToLevels(self):
        for level in self.levels:
            level.playerData = self.player.playerData
