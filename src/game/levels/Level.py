import random
import pygame as pg

from src.game.levels.LevelLoader import LevelLoader
from src.game.map.Map import Map
from src.game.map.tiles.Tile import Tile


class Level:
    def __init__(self, isLeft : bool, canvas: pg.Rect, filename : str, startPosX : int, startPosY : int):
        self.isLeft : bool = isLeft
        self.canvas : pg.Rect = canvas
        self.filename : str = filename
        self.startPosX : int = startPosX
        self.startPosY : int = startPosY

        self.color = "black"

        self.levelLoader = LevelLoader()
        self.map = Map(self.canvas)
        self.map = self.levelLoader.load(filename, self.map)
        self.map.checkCoins()

        random.seed(filename)

        self.backgroundX = self.canvas.left + (self.canvas.w - self.map.sizeX * Tile.size) / 2
        self.backgroundY = (self.canvas.h - self.map.sizeY * Tile.size) / 2
        self.backgroundWidth = self.map.sizeX * Tile.size
        self.backgroundHeight = self.map.sizeY * Tile.size
        self.backgroundTextureSize = (400, 400)
        self.backgroundTextures = [
            pg.transform.scale(pg.image.load("assets/textures/background/red_brick_wall_1.png"), self.backgroundTextureSize),
            pg.transform.scale(pg.image.load("assets/textures/background/red_brick_wall_2.png"), self.backgroundTextureSize),
            pg.transform.scale(pg.image.load("assets/textures/background/red_brick_wall_3.png"), self.backgroundTextureSize),
            pg.transform.scale(pg.image.load("assets/textures/background/red_brick_wall_4.png"), self.backgroundTextureSize)
        ]
        self.backgroundSurface : pg.Surface = self.createBackground()


    def handleEvents(self, event):
        self.map.handleEvent(event)


    def update(self, dt : float):
        self.map.update(dt)


    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.canvas)
        screen.blit(self.backgroundSurface, (self.backgroundX, self.backgroundY))
        self.map.draw(screen)


    def createBackground(self) -> pg.Surface:
        background = pg.Surface((self.backgroundWidth, self.backgroundHeight))

        tilesX : int = self.backgroundWidth // self.backgroundTextureSize[0] + 1
        tilesY : int = self.backgroundHeight // self.backgroundTextureSize[0] + 1

        for row in range(tilesY):
            for col in range(tilesX):
                index = random.randint(0, len(self.backgroundTextures) - 1)
                background.blit(self.backgroundTextures[index], (row * self.backgroundTextureSize[0], col * self.backgroundTextureSize[0]))

        return background