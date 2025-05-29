import pygame as pg


class PowerUpDisplay:
    def __init__(self,
                 playerData,
                 doubleJumpIconPath: str = "assets/textures/powerups/power_up_double_jump.png",
                 speedUpIconPath: str = "assets/textures/powerups/power_up_speed.png",
                 iconSize: tuple = (30, 30),
                 iconPadding: int = 10
                 ):
        self.playerData = playerData
        self.iconSize = iconSize
        self.iconPadding = iconPadding

        self.doubleJumpIconSurface = None
        self.speedUpIconSurface = None

        if doubleJumpIconPath:
            originalDoubleJumpIcon = pg.image.load(doubleJumpIconPath).convert_alpha()
            self.doubleJumpIconSurface = pg.transform.scale(originalDoubleJumpIcon, self.iconSize)

        if speedUpIconPath:
            originalSpeedUpIcon = pg.image.load(speedUpIconPath).convert_alpha()
            self.speedUpIconSurface = pg.transform.scale(originalSpeedUpIcon, self.iconSize)

    def update(self):
        pass

    def draw(self, screen: pg.Surface, position: tuple):
        currentX = position[0]
        currentY = position[1]

        if self.playerData.powerUps.doubleJump and self.doubleJumpIconSurface:
            screen.blit(self.doubleJumpIconSurface, (currentX, currentY))
            currentX += self.iconSize[0] + self.iconPadding

        if self.playerData.powerUps.speedUp and self.speedUpIconSurface:
            screen.blit(self.speedUpIconSurface, (currentX, currentY))
