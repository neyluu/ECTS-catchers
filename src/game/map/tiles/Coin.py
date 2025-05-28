import pygame as pg
import random

from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger
import src.config.PowerUpsConfig as config


class Coin(Trigger):
    def __init__(self):
        super().__init__()
        self.isResettable = False
        self.color = "gold"
        self.points = random.randint(config.COIN_MIN_POINTS, config.COIN_MAX_POINTS)


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        self.color = pg.Color(0,0,0,0)

        playerData.points += self.points
        print(f"Points: {playerData.points}")
