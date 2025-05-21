from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger


class Cobweb(Trigger):
    def __init__(self):
        super().__init__()
        self.color = "white"
        self.playerData = None


    def reset(self):
        super().reset()
        self.playerData.speed = self.playerData.startSpeed
        self.playerData.maxFallingSpeed = self.playerData.startMaxFallingSpeed


    def onTrigger(self, playerData : PlayerData):
        self.playerData = playerData

        playerData.speed = playerData.startSpeed / 2
        playerData.maxFallingSpeed = 50
        print(playerData.maxFallingSpeed)