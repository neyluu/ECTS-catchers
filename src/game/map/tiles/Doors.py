from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger


class Doors(Trigger):
    def __init__(self, path):
        super().__init__()

        self.loadTexture(path)


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered() or playerData.levelChanged:
            return

        playerData.currentLevel += 1
        playerData.levelChanged = True
