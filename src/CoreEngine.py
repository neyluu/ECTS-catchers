import sys
import pygame as pg

from src.common import Settings
from src.SceneManager import SceneManager
from src.scenes.MainMenu import MainMenu
from src.scenes.GameScene import GameScene
from src.scenes.EndScene import EndScene

pg.init()
pg.display.set_caption(Settings.TITLE)
pg.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))


class CoreEngine:
    def __init__(self):
        super().__init__()

        self.sceneManager = SceneManager()
        self.running = True
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()

        self.scenes = [
            MainMenu(),
            GameScene(),
            EndScene()
        ]


    def handleEvent(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                self.running = False

            self.scenes[self.sceneManager.getCurrentScene()].handleEvent(event)


    def update(self):
        self.scenes[self.sceneManager.getCurrentScene()].update()


    def draw(self):
        self.scenes[self.sceneManager.getCurrentScene()].draw()
        pg.display.flip()


    def run(self):
        while self.running:
            self.handleEvent()
            self.update()
            self.draw()
            self.clock.tick(Settings.TARGET_FPS)

