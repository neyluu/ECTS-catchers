from typing import SupportsAbs

import pygame as pg

from src.scenes.Scene import Scene

class EndScene(Scene):

    def __init__(self):
        super().__init__()


    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_1:
                self.sceneManager.setCurrentScene(1)


    def update(self, dt : float):
        pass


    def draw(self, screen : pg.Surface):
        screen.fill("blue")
        pass
