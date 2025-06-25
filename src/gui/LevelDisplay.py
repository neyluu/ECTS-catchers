import pygame as pg

class LevelDisplay:
    def __init__(self, playerData,
                 fontPath: str = "assets/fonts/timer_and_counter_font.ttf",
                 fontSize : int = 30,
                 color : tuple = (255, 255, 255)
                 ):
        pg.font.init()

        self.playerData = playerData
        self.fontPath = fontPath
        self.fontSize = fontSize
        self.color = color

        self.font = pg.font.Font(self.fontPath, self.fontSize)

        self.currentLevel = f"{self.playerData.currentLevel + 1}/7"


    def update(self):
        self.currentLevel = f"{self.playerData.currentLevel + 1}/7"


    def draw(self, screen : pg.Surface, position : tuple):
        textSurface = self.font.render(self.currentLevel, True, self.color)

        posX = position[0]
        posY = position[1]

        screen.blit(textSurface, (posX, posY))
