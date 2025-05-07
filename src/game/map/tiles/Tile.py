import pygame as pg

class Tile:
    size = 32

    def __init__(self, leftTop : pg.Vector2 = pg.Vector2(0,0)):
        self.leftTop = leftTop
        self.color = "red"
        self.isCollision = False
        self.isTrigger = False


    def handleEvent(self, event):
        pass


    def update(self, dt: float):
        pass


    def draw(self, screen: pg.Surface):
        pg.draw.rect(screen, self.color, pg.Rect(self.leftTop.x, self.leftTop.y, Tile.size, Tile.size))

