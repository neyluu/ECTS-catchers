from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger

import pygame as pg
import random

class Coin(Trigger):
    def __init__(self):
        super().__init__()

        self.color = "gold"
        self.points = random.randint(1, 5)


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        self.color = pg.Color(0,0,0,0)

        playerData.points += self.points
        print(f"Points: {playerData.points}")
