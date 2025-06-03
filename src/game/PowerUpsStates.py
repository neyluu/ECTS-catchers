class PowerUpsStates:
    def __init__(self):
        self.doubleJump = False
        self.speedUp = False


    def reset(self):
        self.doubleJump = False
        self.speedUp = False