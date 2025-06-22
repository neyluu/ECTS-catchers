import pygame as pg

from src.scenes.Scene import Scene
from src.game.Game import Game
from src.config import Settings
from src.gui.PauseMenu import PauseMenu
from src.scenes.SettingsScene import SettingsScene


class GameScene(Scene):
    def __init__(self, screenWidth=1920, screenHeight=1080):
        super().__init__()
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.leftCanvas = pg.Rect(0, 0, screenWidth // 2, screenHeight)
        self.rightCanvas = pg.Rect(screenWidth // 2, 0, screenWidth // 2, screenHeight)

        self.gameLeft = Game(isLeft=True, canvas=self.leftCanvas)
        self.gameRight = Game(isLeft=False, canvas=self.rightCanvas)

        self.divider = pg.Rect(screenWidth // 2 - 2, 0, 4, screenHeight)
        self.pauseMenu = PauseMenu(self.sceneManager)

    def handleEvent(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN and event.key == Settings.KEYMAP_PAUSE:
            self.pauseMenu.toggle()

        if self.pauseMenu.isActive:
            self.pauseMenu.handleEvent(event)
        else:
            self.gameLeft.handleEvent(event)
            self.gameRight.handleEvent(event)

    def update(self, dt: float):
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