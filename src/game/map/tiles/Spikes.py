from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger


class Spikes(Trigger):
    def __init__(self):
        super().__init__()
        self.color = "green"

    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        self.color = "white"
