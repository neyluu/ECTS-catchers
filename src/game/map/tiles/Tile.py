import pygame as pg

import src.config.DebugConfig as Debug

class Tile:
    size = 32

    def __init__(self, leftTop : pg.Vector2 = pg.Vector2(0,0)):
        self.leftTop = leftTop
        self.color = pg.Color(80,80,80)
        self.isCollision : bool = False
        self.isTrigger : bool = False
        self.isHidden : bool = False

        self.collisionSizeX : int = Tile.size
        self.collisionSizeY : int = Tile.size
        self.collisionOffsetX : int = 0
        self.collisionOffsetY : int = 0
        self.collision : pg.Rect = None
        self.updateCollisionBox()

        self.path : str = None
        self.texture = None


    def handleEvent(self, event):
        pass


    def update(self, dt: float):
        pass


    def draw(self, screen: pg.Surface):
        if self.isHidden:
            pg.draw.rect(screen, pg.Color(0,0,0,0), pg.Rect(self.leftTop.x, self.leftTop.y, Tile.size, Tile.size))
        elif self.path is None:
            pg.draw.rect(screen, self.color, pg.Rect(self.leftTop.x, self.leftTop.y, Tile.size, Tile.size))
        else:
            screen.blit(self.texture, pg.Rect(self.leftTop.x, self.leftTop.y, Tile.size, Tile.size))

        self.DEBUG_drawCollideBoxes(screen)


    def loadTexture(self, path : str):
        self.path = path
        self.texture = pg.transform.scale(pg.image.load(self.path).convert_alpha(), (Tile.size, Tile.size))


    def onMapReset(self):
        pass


    def hide(self):
        self.isHidden = True


    def unHide(self):
        self.isHidden = False


    def setLeftTop(self, leftTop):
        self.leftTop = leftTop
        self.updateCollisionBox()


    def updateCollisionBox(self):
        self.collision = pg.Rect(self.leftTop.x + self.collisionOffsetX,
                          self.leftTop.y + self.collisionOffsetY,
                          self.collisionSizeX,
                          self.collisionSizeY)


    def DEBUG_drawCollideBoxes(self, screen : pg.Surface):
        if Debug.DEBUG_TILES_VISUAL_TRIGGER and self.isTrigger:
            pg.draw.rect(screen, "green", (self.leftTop.x, self.leftTop.y, Tile.size, Tile.size), width=1)
        if Debug.DEBUG_TILES_VISUAL_COLLISION and self.isCollision:
            pg.draw.rect(screen, "red", self.collision, width=1)