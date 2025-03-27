import pygame as pg

class Player:
    def __init__(self, screen : pg.Surface, canvas : pg.Rect):
        self.screen = screen
        self.canvas = canvas
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
            if event.key == pg.K_w:
                self.movingUp = True
            if event.key == pg.K_d:
                self.movingRight = True
            if event.key == pg.K_s:
                self.movingDown = True
            if event.key == pg.K_a:
                self.movingLeft = True
        if event.type == pg.KEYUP:
            if event.key == pg.K_w:
                self.movingUp = False
            if event.key == pg.K_d:
                self.movingRight = False
            if event.key == pg.K_s:
                self.movingDown = False
            if event.key == pg.K_a:
                self.movingLeft = False


    def update(self, dt : float):
        self.dt = dt
        self.move()


    def draw(self):
        pg.draw.rect(self.screen, self.color, (self.canvas.left + self.posX, self.canvas.top + self.posY, 32, 32))


    def move(self):
        if self.movingUp:
            self.posY -= 100 * self.dt
        if self.movingRight:
            self.posX += 100 * self.dt
        if self.movingDown:
            self.posY += 100 * self.dt
        if self.movingLeft:
            self.posX -= 100 * self.dt