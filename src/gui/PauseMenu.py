import pygame as pg

from src.config import Settings

class PauseMenu:
    def __init__(self,
                 posX : int = 0,
                 posY : int = 0,
                 width : int = 550,
                 height : int = 700,
                 centered : bool = True,
                 backgroundColor : pg.Color = (200, 200, 200)
                ):
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.centered = centered
        self.backgroundColor = backgroundColor

        if centered:
            self.centerPosition()


    def handleEvent(self, event):
        pass


    def update(self, dt: float):
        pass


    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.backgroundColor, (self.posX, self.posY, self.width, self.height))


    def centerPosition(self):
        self.posX = (Settings.SCREEN_WIDTH / 2) - (self.width / 2)
        self.posY = (Settings.SCREEN_HEIGHT / 2) - (self.height / 2)

