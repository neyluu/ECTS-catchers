import pygame as pg

from src.game.PlayerKeymap import PlayerKeymap
from src.common import Settings

class Player:
    def __init__(self, isLeft : bool, canvas : pg.Rect):
        self.canvas = canvas
        self.isLeft = isLeft
        if self.isLeft:
            self.keymap = Settings.PLAYER_LEFT_KEYMAP
        else:
            self.keymap = Settings.PLAYER_RIGHT_KEYMAP
        self.color = "black"

        self.dt = 0

        # TODO later rebuild to pos in board grid
        self.posX : int = 0
        self.posY : int = 0

        self.movingUp    : bool = False
        self.movingRight : bool = False
        self.movingDown  : bool = False
        self.movingLeft  : bool = False


    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == self.keymap.MOVE_UP:
                self.movingUp = True
            if event.key == self.keymap.MOVE_RIGHT:
                self.movingRight = True
            if event.key == self.keymap.MOVE_DOWN:
                self.movingDown = True
            if event.key == self.keymap.MOVE_LEFT:
                self.movingLeft = True
        if event.type == pg.KEYUP:
            if event.key == self.keymap.MOVE_UP:
                self.movingUp = False
            if event.key == self.keymap.MOVE_RIGHT:
                self.movingRight = False
            if event.key == self.keymap.MOVE_DOWN:
                self.movingDown = False
            if event.key == self.keymap.MOVE_LEFT:
                self.movingLeft = False


    def update(self, dt : float):
        self.dt = dt
        self.move()


    def draw(self, screen : pg.Surface):
        pg.draw.rect(screen, self.color, (self.canvas.left + self.posX, self.canvas.top + self.posY, 32, 32))


    def move(self):
        if self.movingUp:
            self.posY -= 100 * self.dt
        if self.movingRight:
            self.posX += 100 * self.dt
        if self.movingDown:
            self.posY += 100 * self.dt
        if self.movingLeft:
            self.posX -= 100 * self.dt