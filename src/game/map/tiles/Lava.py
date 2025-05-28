from src.game.PlayerData import PlayerData
from src.game.map.tiles.Trigger import Trigger
import src.config.PowerUpsConfig as config


class Lava(Trigger):
    def __init__(self):
        super().__init__()

        self.color = "firebrick"

        self.damageDelay : int = config.LAVA_DAMAGE_DELAY_TIME # seconds
        self.timer : float = 0

        self.playerData : PlayerData = None

    def update(self, dt: float):
        if not self.isActive and self.playerData is not None:
            self.timer += dt
            if self.timer > self.damageDelay:
                self.playerData.gotDamaged = True
                self.timer = 0


    def reset(self):
        super().reset()


    def onTrigger(self, playerData : PlayerData):
        if self.wasEntered():
            return

        self.playerData = playerData
