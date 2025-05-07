from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger


class Spikes(Trigger):
    def __init__(self):
        super().__init__()
        self.color = "green"

    def onTrigger(self, playerData : PlayerData):
        # if self.wasEntered():
        #     return

        playerData.hp -= 1
        playerData.posX = playerData.startPosX
        playerData.posY = playerData.startPosY
        print(f"HP: {playerData.hp}")
        # self.color = "white"
