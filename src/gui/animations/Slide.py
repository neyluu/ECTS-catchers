import pygame as pg

import src.config.Settings as Settings

class Slide:
    def __init__(self,
                 time : float = 1,
                 color = (22,22,22)):
        self.time = time
        self.color = color

        self.offset = 0.4
        self.top = 0
        self.left = 0
        self.width = Settings.SCREEN_WIDTH
        self.height = 0

        self.step : float = 0

        self.timeElapsed : float = 0
        self.running : bool = False


    def update(self, dt : float):
        if not self.running:
            return


        self.timeElapsed += dt


        self.step = Settings.SCREEN_HEIGHT / ((self.time / 2 * (1 - self.offset)) / dt)

        if self.timeElapsed < ((self.time * (1 - self.offset)) / 2):
            self.height += self.step
        if self.timeElapsed > ((self.time * (1 + self.offset)) / 2):
            self.top += self.step

        if self.timeElapsed > self.time:
            self.stop()
            self.reset()


    def draw(self, screen : pg.Surface):
        if not self.running:
            return

        pg.draw.rect(screen, self.color, (self.left, self.top, self.width, self.height))


    def start(self):
        self.running = True


    def stop(self):
        self.running = False


    def reset(self):
        self.timeElapsed = 0
        self.height = 0
        self.top = 0


slideAnimation = Slide()