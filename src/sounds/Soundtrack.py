import pygame as pg

from src.config.Settings import sounds

class Soundtrack:
    def __init__(self, path : str, loop : bool = True):
        self.path = path
        self.loop = loop
        self.volumeFactor = 0.1
        self.sound = pg.mixer.Sound(self.path)
        sounds.register(self)
        self.updateVolume()


    def play(self):
        return self.sound.play(-1 if self.loop else 0)


    def stop(self):
        self.sound.stop()


    def updateVolume(self):
        self.sound.set_volume(sounds.music * self.volumeFactor)