import pygame as pg

from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger
from src.sounds.SFX import SFX
from src.game.map.tiles.Tile import Tile
import src.config.PowerUpsConfig as config


class Lava(Trigger):
    inLava : bool = False
    timer : float = 0

    def __init__(self, path : str):
        super().__init__()

        if path == '':
            path = "assets/textures/traps/lava_1.png"
            print("ERROR: lava texture path is empty!")

        self.loadTexture(path)

        self.collisionSizeX = Tile.size - 8
        self.collisionSizeY = Tile.size - 12
        self.collisionOffsetX = 4
        self.collisionOffsetY = 8

        self.damageDelay : int = config.LAVA_DAMAGE_DELAY_TIME # seconds
        self.playerData : PlayerData = None
        self.sfx = SFX("assets/audio/damage.wav")


    def update(self, dt: float):
        if not self.isActive and self.playerData is not None:
            now = pg.time.get_ticks() / 1000
            if now - Lava.timer > self.damageDelay:
                self.playerData.gotDamaged = True
                self.sfx.play()
                Lava.timer = now
                print(f"HP: {self.playerData.hp}")


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
            print(f"HP: {self.playerData.hp}")
            self.sfx.play()
