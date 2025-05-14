from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger


class Doors(Trigger):
    def __init__(self):
        super().__init__()

        self.color = "orange"


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        playerData.currentLevel += 1
