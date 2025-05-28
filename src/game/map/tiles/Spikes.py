from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger
import src.config.PowerUpsConfig as config


class Spikes(Trigger):
    def __init__(self):
        super().__init__()
        self.color = "green"
        self.damage = config.SPIKES_DAMAGE

    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        playerData.hp -= self.damage
        print(f"HP: {playerData.hp}")
