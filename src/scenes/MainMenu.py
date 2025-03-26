import pygame as pg

from src.scenes.Scene import Scene


class MainMenu(Scene):
    def __init__(self):
        super().__init__()


    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                print("test")
                self.sceneManager.setCurrentScene(1)
                print("  " + str(self.sceneManager.getCurrentScene()))


    def update(self):
        pass


    def draw(self):
        self.screen.fill("purple")
        pass
