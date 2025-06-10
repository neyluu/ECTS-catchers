import pygame as pg

from src.config.Settings import SOUND_SFX

class SFX:
    def __init__(self, path : str):
        self.path = path
        self.volume = SOUND_SFX
        self.sound = pg.mixer.Sound(self.path)
        self.sound.set_volume(self.volume)


    def play(self):
        self.sound.play()


    def stop(self):
        self.sound.stop()