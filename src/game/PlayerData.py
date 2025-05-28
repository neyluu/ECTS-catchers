class PlayerData():
    def __init__(self):

        self.playerHeight: int = 48
        self.playerWidth: int = 32

        self.startSpeed : float = 200
        self.speed: float = self.startSpeed
        self.velocityX: float = 0
        self.velocityY: float = 0
        self.jumpForce: float = 575
        self.gravityForce: float = 2000
        self.startMaxFallingSpeed: int = 1000
        self.maxFallingSpeed: int = self.startMaxFallingSpeed
        self.jumpBufferingLevel: int = 32
        self.jumpBufferingDropLevel: int = 350

        # top-left
        self.startPosX: int = 550
        self.startPosY: int = 950

        self.posX: int = self.startPosX
        self.posY: int = self.startPosY
        self.newPosX: int = -1
        self.newPosY: int = -1

        self.canMove : bool = True

        self.points: int = 0
        self.startHp = 8
        self.hp: int = self.startHp
        self.gotDamaged : bool = False
        self.canDoubleJump : bool = False

        self.levelChanged = False
        self.currentLevel = 0