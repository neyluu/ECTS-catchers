import sys
import pygame as pg

from src.common import Settings

pg.init()
pg.display.set_caption(Settings.TITLE)
pg.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))

class CoreEngine():

    def __init__(self):
        self.running = True
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()

    def handleEvent(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        pass

    def draw(self):
        pass

    def run(self):
        while self.running:
            self.handleEvent()
            self.update()
            self.draw()
            self.clock.tick(Settings.TARGET_FPS)
