import pygame as pg
from pygame import Surface

from src.game.GameStats import GameStats


class GameOver:
    def __init__(self, canvas : pg.Rect):
        self.canvas = canvas
        self.stats : GameStats = None

        self.initialized = False

        pg.font.init()
        self.fontColor = "white"
        self.fontSize = 50
        self.font = pg.font.Font("assets/fonts/timer_and_counter_font.ttf", self.fontSize)

        self.backgroundTexture = pg.image.load("assets/textures/background/dark_grey_brick_bg.png").convert()
        self.textureSize = self.backgroundTexture.get_size()[0] / 8
        self.backgroundTexture = pg.transform.scale(self.backgroundTexture, (self.textureSize, self.textureSize))
        self.backgroundSurface = self.createBackground()

        self.headerText01 = self.font.render("CONGRATULATIONS!", True, self.fontColor)
        textSize = self.headerText01.get_rect()
        self.headerText01X = self.canvas.left + self.canvas.width / 2 - textSize.width / 2
        self.headerText01Y = 30

        self.headerText02 = self.font.render("YOU FINISHED GAME!", True, self.fontColor)
        textSize = self.headerText02.get_rect()
        self.headerText02Y = 100
        self.headerText02X = self.canvas.left + self.canvas.width / 2 - textSize.width / 2

        self.statsSurface = None


    def handleEvents(self, event):
        pass


    def update(self, dt : float):
        pass


    def draw(self, screen):
        screen.blit(self.backgroundSurface, (self.canvas.left,0))

        if not self.initialized:
            return


        screen.blit(self.headerText01, (self.headerText01X, self.headerText01Y))
        screen.blit(self.headerText02, (self.headerText02X, self.headerText02Y))
        screen.blit(self.statsSurface, (self.canvas.left, 0))


    def init(self, gameStats : GameStats):
        self.stats = gameStats
        self.initialized = True
        self.statsSurface = self.createStats()

        # print(f"{self.stats.deaths} {len(self.stats.deaths)}")
        # print(f"{self.stats.times} {len(self.stats.times)}")


    def parseTime(self, seconds : int) -> str:
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"


    def createBackground(self) -> pg.Surface:
        background = pg.Surface((self.canvas.width, self.canvas.height))

        tilesX : int = int(self.canvas.width // self.textureSize + 1)
        tilesY : int = int(self.canvas.height // self.textureSize + 1)

        for y in range(tilesY):
            for x in range(tilesX):
                background.blit(self.backgroundTexture, (x * self.textureSize, y * self.textureSize))

        return background


    def createStats(self) -> Surface | None:
        if self.stats is None:
            print("ERROR: stats is None")
            return None

        surface = pg.Surface((self.canvas.width, self.canvas.height), pg.SRCALPHA)
        surface.fill((0, 0, 0, 0))

        textY = 250

        for i in range(len(self.stats.deaths)):
            if i == 0:
                label = "TOTAL  :"
            else:
                label = "LEVEL " + str(i) + ":"

            text = self.font.render(f"{label}{self.stats.deaths[i]:3d}  {self.parseTime(self.stats.times[i])}", True, self.fontColor)
            textSize = text.get_rect()
            textY += 70
            textX = self.canvas.width / 2 - textSize.width / 2
            surface.blit(text, (textX, textY))

        return surface
