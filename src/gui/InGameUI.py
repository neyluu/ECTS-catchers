import pygame as pg

from src.gui.LevelDisplay import LevelDisplay
from src.gui.Timer import Timer
from src.gui.HealthBar import HealthBar
from src.gui.CoinCounter import CoinCounter
from src.gui.PowerUpDisplay import PowerUpDisplay


class InGameUI:
    def __init__(self, canvas: pg.Rect, playerData):
        self.canvas = canvas
        self.playerData = playerData

        self.gameTimer = Timer(
            fontSize=48,
            color=(240, 240, 240),
            iconSize=(40, 40),
            iconTextPadding=10
        )
        self.timerPosition = (self.canvas.x + self.canvas.width - 620,
                              self.canvas.y + 15)

        self.healthBar = HealthBar(
            playerData=self.playerData,
            heart1ImagePath="assets/textures/gui/Heart_1.png",
            heart2ImagePath="assets/textures/gui/Heart_2.png",
            heart3ImagePath="assets/textures/gui/Heart_3.png",
            displayHeartWidth=60,
            displayHeartHeight=60,
            heartPadding=6
        )
        self.healthBarPosition = (self.canvas.x + 20, self.canvas.y + 10)

        self.coinCounter = CoinCounter(
            playerData=self.playerData,
            maxPoints=30,
            fontSize=48,
            iconSize=(37, 37),
        )
        self.coinCounterPosition = (self.canvas.x + 710, self.canvas.y + 24)

        self.powerUpDisplay = PowerUpDisplay(
            playerData=self.playerData,
            iconSize=(32, 32),
            iconPadding=8
        )
        self.powerUpDisplayPosition = (self.canvas.x +25,
                                       self.canvas.y + 70)

        self.levelDisplay = LevelDisplay(playerData, fontSize=48)
        self.levelDisplayPosition = (self.canvas.x + 550, self.canvas.y + 16)

    def update(self):
        self.gameTimer.update()
        self.healthBar.update()
        self.coinCounter.update()
        self.powerUpDisplay.update()
        self.levelDisplay.update()

    def draw(self, screen: pg.Surface):
        self.gameTimer.draw(screen, self.timerPosition)
        self.healthBar.draw(screen, self.healthBarPosition)
        self.coinCounter.draw(screen, self.coinCounterPosition)
        self.powerUpDisplay.draw(screen, self.powerUpDisplayPosition)
        self.levelDisplay.draw(screen, self.levelDisplayPosition)

    def pauseTimer(self):
        self.gameTimer.pause()

    def resumeTimer(self):
        self.gameTimer.resume()
