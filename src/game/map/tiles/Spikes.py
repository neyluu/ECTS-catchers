from src.game.PlayerData import PlayerData
from src.game.map.tiles.Tile import Tile
from src.game.map.tiles.Trigger import Trigger
import src.config.PowerUpsConfig as config


class Spikes(Trigger):
    def __init__(self):
        super().__init__()
        self.loadTexture("assets/textures/traps/spikes.png")
        self.damage = config.SPIKES_DAMAGE

        self.collisionSizeX = Tile.size - 8
        self.collisionSizeY = Tile.size - 20
        self.collisionOffsetX = 4
        self.collisionOffsetY = 20


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        playerData.hp -= self.damage
        print(f"HP: {playerData.hp}")
