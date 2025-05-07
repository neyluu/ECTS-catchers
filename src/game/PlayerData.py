class PlayerData():
    def __init__(self):

        self.playerHeight: int = 48
        self.playerWidth: int = 32

        self.speed: float = 200
        self.velocityX: float = 0
        self.velocityY: float = 0
        self.jumpForce: float = 575
        self.gravityForce: float = 2000
        self.maxFallingSpeed: int = 1000
        self.jumpBufferingLevel: int = 32
        self.jumpBufferingDropLevel: int = 350

        # top-left
        self.posX: int = 630
        self.posY: int = 950
        self.newPosX: int = -1
        self.newPosY: int = -1

        self.points: int = 0
        self.hp: int = 3