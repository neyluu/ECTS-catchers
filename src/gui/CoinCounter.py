import pygame as pg


class CoinCounter:
    def __init__(self,
                 playerData,
                 maxPoints: int = 30,
                 fontPath: str = "assets/fonts/first.ttf",
                 fontSize: int = 30,
                 color: tuple = (255, 255, 255),
                 iconImagePath: str = "assets/textures/powerups/collectible_coin.png",
                 iconSize: tuple = (64, 64),
                 iconTextPadding: int = 5
                 ):
        pg.font.init()

        self.playerData = playerData
        self.maxPoints = maxPoints
        self.textColor = color
        self.iconImagePath = iconImagePath
        self.iconSize = iconSize
        self.iconTextPadding = iconTextPadding
        self.iconSurface = None

        try:
            self.font = pg.font.Font(fontPath, fontSize)
        except pg.error:
            self.font = pg.font.SysFont(None, fontSize)

        if self.iconImagePath:
            originalIcon = pg.image.load(self.iconImagePath).convert_alpha()
            self.iconSurface = pg.transform.scale(originalIcon, self.iconSize)

        self.currentPointsStr = f"0/{self.maxPoints}"

    def update(self):
        currentPoints = min(self.playerData.points, self.maxPoints)
        self.currentPointsStr = f"{currentPoints}/{self.maxPoints}"

    def draw(self, screen: pg.Surface, position: tuple):
        textSurface = self.font.render(self.currentPointsStr, True, self.textColor)

        currentX = position[0]
        currentY = position[1]

        if self.iconSurface:
            screen.blit(self.iconSurface, (currentX, currentY+4))
            currentX += self.iconSurface.get_width() + self.iconTextPadding

        textRect = textSurface.get_rect()
        if self.iconSurface:
            textY = currentY + (self.iconSurface.get_height() / 2) - (textRect.height / 2)
        else:
            textY = currentY

        screen.blit(textSurface, (currentX, textY))

    def reset(self):
        self.currentPointsStr = f"0/{self.maxPoints}"
