import pygame as pg

from src.config.Settings import sounds

class Soundtrack:
    def __init__(self, path : str):
        self.path = path
        self.volumeFactor = 0.1
        self.sound = pg.mixer.Sound(self.path)
        sounds.register(self)
        self.updateVolume()


    def play(self):
        self.sound.play(-1)


    def stop(self):
        self.sound.stop()


    def updateVolume(self):
        self.sound.set_volume(sounds.music * self.volumeFactor)