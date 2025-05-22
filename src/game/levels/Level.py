import pygame as pg

from src.game.levels.LevelLoader import LevelLoader
from src.game.map.Map import Map

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


    def handleEvents(self, event):
        self.map.handleEvent(event)


    def update(self, dt : float):
        self.map.update(dt)


    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.canvas)
        self.map.draw(screen)
