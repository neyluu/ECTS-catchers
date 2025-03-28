import pygame as pg

from src.game.Player import Player
from src.game.levels import *
from src.game.levels.Level01 import Level01
from src.game.levels.Level02 import Level02


class Game:

    def __init__(self, isLeft : bool, canvas : pg.Rect):
        self.canvas = canvas
        self.isLeft = isLeft
        self.player = Player(self.isLeft, self.canvas)
        self.backgroundColor = "black"
        self.levels = [
            Level01(self.isLeft, self.canvas),
            Level02(self.isLeft, self.canvas)
        ]
        self.currentLevel = 0


    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_5:
                self.currentLevel = 0 if self.currentLevel - 1 < 0 else self.currentLevel - 1
            if event.key == pg.K_6:
                self.currentLevel = len(self.levels) - 1 if self.currentLevel + 1 > len(self.levels) - 1 else self.currentLevel + 1

        self.levels[self.currentLevel].handleEvents(event)
        self.player.handleEvent(event)


    def update(self, dt : float):
        self.levels[self.currentLevel].update(dt)
        self.player.update(dt)


    def draw(self, screen : pg.Surface):
        # pg.draw.rect(self.screen, self.backgroundColor, self.canvas)
        self.levels[self.currentLevel].draw(screen)
        self.player.draw(screen)


    def setBackgroundColor(self, color : pg.Color):
        self.backgroundColor = color