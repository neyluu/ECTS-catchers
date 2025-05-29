import pygame as pg
import random

from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger
import src.config.PowerUpsConfig as config


class Coin(Trigger):
    def __init__(self):
        super().__init__()
        self.isResettable = False
        self.points = random.randint(config.COIN_MIN_POINTS, config.COIN_MAX_POINTS)
        self.loadTexture("assets/textures/powerups/collectible_coin.png")

    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        self.color = pg.Color(0,0,0,0)
        self.path = None
        playerData.points += self.points
        print(f"Points: {playerData.points}")


    def onMapReset(self):
        self.color = "gold"
        self.isActive = True