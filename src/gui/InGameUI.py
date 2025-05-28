import pygame as pg
from src.gui.Timer import Timer
from src.gui.HealthBar import HealthBar
from src.gui.CoinCounter import CoinCounter


class InGameUI:
    def __init__(self, canvas: pg.Rect, playerData):
        self.canvas = canvas
        self.playerData = playerData

        self.gameTimer = Timer()
        self.timerPosition = (self.canvas.x + self.canvas.width - 450, self.canvas.y + 2)

        self.healthBar = HealthBar(
            playerData=self.playerData,
            heart1ImagePath="assets/textures/gui/Heart_1.png",
            heart2ImagePath="assets/textures/gui/Heart_2.png",
            heart3ImagePath="assets/textures/gui/Heart_3.png",
            displayHeartWidth=60,
            displayHeartHeight=60,
            heartPadding=6
        )
        self.healthBarPosition = (self.canvas.x + 120, self.canvas.y + 10)
        self.coinCounter = CoinCounter(
            playerData=self.playerData,
            maxPoints=30,
            fontSize=60
        )
        self.coinCounterPosition = (self.canvas.x + 700, self.canvas.y + 10)

    def update(self):
        self.gameTimer.update()
        self.healthBar.update()
        self.coinCounter.update()

    def draw(self, screen: pg.Surface):
        self.gameTimer.draw(screen, self.timerPosition)
        self.healthBar.draw(screen, self.healthBarPosition)
        self.coinCounter.draw(screen, self.coinCounterPosition)

    def pauseTimer(self):
        self.gameTimer.pause()

    def resumeTimer(self):
        self.gameTimer.resume()
