import pygame as pg

from src.SceneManager import SceneManager


class Scene:
    def __init__(self):
        self.sceneManager = SceneManager()
        self.screen = pg.display.get_surface()
        super().__init__()


    def handleEvent(self, event):
        pass


    def update(self):
        pass


    def draw(self):
        pass
