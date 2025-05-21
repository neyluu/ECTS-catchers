import pygame as pg

from src.game.PlayerData import PlayerData
from src.game.levels.LevelLoader import LevelLoader
from src.game.map.Map import Map

class Level:
    def __init__(self, isLeft : bool, canvas: pg.Rect):
        self.isLeft = isLeft
        self.canvas = canvas
        self.color = "black"
        self.playerData : PlayerData = None
        self.map = Map(self.canvas)
        self.levelLoader = LevelLoader()
        print(self.canvas)

        self.startPosX: int = 550
        self.startPosY: int = 950


    def handleEvents(self, event):
        self.map.handleEvent(event)


    def update(self, dt : float):
        self.map.update(dt)


    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.canvas)
        self.map.draw(screen)


    def reset(self, playerData : PlayerData):
        pass