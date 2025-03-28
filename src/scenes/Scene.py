import pygame as pg

from src.SceneManager import SceneManager


class Scene:
    def __init__(self):
        self.sceneManager = SceneManager()
        super().__init__()


    def handleEvent(self, event):
        pass


    def update(self, dt : float):
        pass


    def draw(self, screen : pg.Surface):
        pass
