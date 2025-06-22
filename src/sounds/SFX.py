import pygame as pg

from src.config.Settings import sounds

class SFX:
    def __init__(self, path : str):
        self.path = path
        self.sound = pg.mixer.Sound(self.path)
        sounds.register(self)
        self.updateVolume()


    def play(self):
        self.sound.play()


    def stop(self):
        self.sound.stop()


    def updateVolume(self):
        self.sound.set_volume(sounds.sfx)