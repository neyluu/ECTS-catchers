import pygame as pg

from src.scenes.Scene import Scene

class GameScene(Scene):

    def __init__(self):
        super().__init__()


    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                self.sceneManager.setCurrentScene(2)
            elif event.key == pg.K_LEFT:
                self.sceneManager.setCurrentScene(0)

    def update(self):
        pass


    def draw(self):
        self.screen.fill("red")
        pass