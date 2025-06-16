import pygame as pg

from src.game.GameStats import GameStats


class GameOver:
    def __init__(self, canvas : pg.Rect):
        self.canvas = canvas
        self.stats : GameStats = None


    def handleEvents(self, event):
        pass


    def update(self, dt : float):
        pass


    def draw(self, screen):
        pg.draw.rect(screen, "red", self.canvas)


    def init(self, gameStats : GameStats):
        self.stats = gameStats

        print(self.stats.deaths)
        print(self.stats.times)