import pygame as pg

from src.scenes.Scene import Scene


class MainMenu(Scene):
    def __init__(self):
        super().__init__()


    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_2:
                self.sceneManager.setCurrentScene(1)


    def update(self, dt : float):
        pass


    def draw(self):
        self.screen.fill("purple")
        pass
