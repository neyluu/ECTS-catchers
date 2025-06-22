import pygame as pg

from src.scenes.Scene import Scene

class GameIntro(Scene):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("assets/textures/gui/intro.png").convert()


    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            self.sceneManager.setCurrentScene(1)


    def update(self, dt : float):
        pass


    def draw(self, screen : pg.Surface):
        screen.blit(self.image, (0,0))
        pass
