from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger


class Coin(Trigger):
    def __init__(self):
        super().__init__()

        self.color = "pink"


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        self.color = "blue"

        # TODO TMP
        playerData.speed *= 2
        print("test" + str(playerData.speed))
