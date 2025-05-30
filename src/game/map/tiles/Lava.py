import pygame as pg

from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger
import src.config.PowerUpsConfig as config


class Lava(Trigger):
    inLava : bool = False
    timer : float = 0


    def __init__(self):
        super().__init__()

        self.color = "firebrick"
        self.damageDelay : int = config.LAVA_DAMAGE_DELAY_TIME # seconds
        self.playerData : PlayerData = None


    def update(self, dt: float):
        if not self.isActive and self.playerData is not None:
            now = pg.time.get_ticks() / 1000
            if now - Lava.timer > self.damageDelay:
                self.playerData.gotDamaged = True
                Lava.timer = now


    def reset(self):
        super().reset()
        Lava.inLava = False


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return


        Lava.inLava = True
        self.playerData = playerData

        if not Lava.inLava:
            Lava.timer = pg.time.get_ticks() / 1000
            self.playerData.hp -= 1
