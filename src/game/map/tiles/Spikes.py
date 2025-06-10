import pygame as pg

from src.config.Settings import SOUND_SFX
from src.game.PlayerData import PlayerData
from src.game.map.tiles.Tile import Tile
from src.game.map.tiles.Trigger import Trigger
import src.config.PowerUpsConfig as config


class Spikes(Trigger):
    def __init__(self, direction : int = 0):
        super().__init__()
        self.loadTexture("assets/textures/traps/spikes.png")
        self.damage = config.SPIKES_DAMAGE

        self.sound = pg.mixer.Sound("assets/audio/damage.wav")
        self.sound.set_volume(SOUND_SFX)

        # bottom
        if direction == 0:
            self.collisionSizeX = Tile.size - 10
            self.collisionSizeY = Tile.size - 22
            self.collisionOffsetX = 5
            self.collisionOffsetY = 22
        # right
        elif direction == 1:
            self.texture = pg.transform.rotate(self.texture, 90)
            self.collisionSizeX = Tile.size - 22
            self.collisionSizeY = Tile.size - 10
            self.collisionOffsetX = 22
            self.collisionOffsetY = 5
        # top
        elif direction == 2:
            self.texture = pg.transform.rotate(self.texture, 180)
            self.collisionSizeX = Tile.size - 10
            self.collisionSizeY = Tile.size - 22
            self.collisionOffsetX = 5
            self.collisionOffsetY = 0
        # left
        elif direction == 3:
            self.texture = pg.transform.rotate(self.texture, 270)
            self.collisionSizeX = Tile.size - 22
            self.collisionSizeY = Tile.size - 10
            self.collisionOffsetX = 0
            self.collisionOffsetY = 5



    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        playerData.hp -= self.damage
        self.sound.play()
        print(f"HP: {playerData.hp}")
