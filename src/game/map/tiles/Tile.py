import pygame as pg

class Tile:
    size = 32

    def __init__(self, leftTop : pg.Vector2 = pg.Vector2(0,0)):
        self.leftTop = leftTop
        self.color = pg.Color(80,80,80)
        self.isCollision = False
        self.isTrigger = False

        self.path : str = None
        self.texture = None


    def handleEvent(self, event):
        pass


    def update(self, dt: float):
        pass


    def draw(self, screen: pg.Surface):
        if self.path is None:
            pg.draw.rect(screen, self.color, pg.Rect(self.leftTop.x, self.leftTop.y, Tile.size, Tile.size))
        else:
            screen.blit(self.texture, pg.Rect(self.leftTop.x, self.leftTop.y, Tile.size, Tile.size))


    def loadTexture(self):
        self.texture = pg.image.load(self.path).convert_alpha()


    def onMapReset(self):
        pass

