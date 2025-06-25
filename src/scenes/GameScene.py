import pygame as pg

from src.scenes.Scene import Scene
from src.game.Game import Game
from src.config import Settings
from src.gui.PauseMenu import PauseMenu
from src.scenes.SettingsScene import SettingsScene
from src.sounds.Soundtrack import Soundtrack


class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.screenWidth = Settings.SCREEN_WIDTH
        self.screenHeight = Settings.SCREEN_HEIGHT

        self.leftCanvas = pg.Rect(0, 0, self.screenWidth // 2, self.screenHeight)
        self.rightCanvas = pg.Rect(self.screenWidth // 2, 0, self.screenWidth // 2, self.screenHeight)

        self.gameLeft = Game(isLeft=True, canvas=self.leftCanvas)
        self.gameRight = Game(isLeft=False, canvas=self.rightCanvas)

        self.running = False
        self.soundtrack = Soundtrack("assets/audio/soundtrack02.mp3")

        self.divider = pg.Rect(self.screenWidth // 2 - 2, 0, 4, self.screenHeight)
        self.pauseMenu = PauseMenu()

    def handleEvent(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN and event.key == Settings.KEYMAP_PAUSE:
            self.pauseMenu.toggle()

        if self.pauseMenu.isActive:
            self.pauseMenu.handleEvent(event)
        else:
            self.gameLeft.handleEvent(event)
            self.gameRight.handleEvent(event)

    def update(self, dt: float):
        if not self.running:
            self.running = True
            self.soundtrack.play()

        if self.pauseMenu.isActive:
            self.pauseMenu.update(dt)
            return

        self.gameLeft.update(dt)
        self.gameRight.update(dt)

    def draw(self, screen: pg.Surface):
        self.gameLeft.draw(screen)
        self.gameRight.draw(screen)
        pg.draw.rect(screen, (20, 20, 20), self.divider)
        self.pauseMenu.draw(screen)

    def reset(self):
        self.gameLeft.reset()
        self.gameRight.reset()
        self.pauseMenu.isActive = False

    def onEnter(self, previousScene=None):
        if isinstance(previousScene, SettingsScene):
            self.pauseMenu.isActive = True
        else:
            self.reset()