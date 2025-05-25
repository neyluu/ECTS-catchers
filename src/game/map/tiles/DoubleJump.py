from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger


class DoubleJump(Trigger):
    def __init__(self):
        super().__init__()

        self.color = "navajowhite2"
        self.playerData = None

    def update(self, dt: float):
        pass


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        print("Double jump")
        self.playerData : PlayerData = playerData
