import pygame as pg

from src.game.Player import Player

class Game:

    def __init__(self, isLeft : bool, screen : pg.Surface, canvas : pg.Rect):
        self.screen = screen
        self.canvas = canvas
        self.isLeft = isLeft
        self.player = Player(self.isLeft, self.screen, self.canvas)
        self.backgroundColor = "black"


    def handleEvent(self, event):
        self.player.handleEvent(event)


    def update(self, dt : float):
        self.player.update(dt)


    def draw(self):
        pg.draw.rect(self.screen, self.backgroundColor, self.canvas)
        self.player.draw()


    def setBackgroundColor(self, color : pg.Color):
        self.backgroundColor = color