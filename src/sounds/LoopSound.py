import pygame as pg

from src.config.Settings import sounds

class LoopSound:
    def __init__(self, path : str, delay : float):
        self.path = path
        self.delay = delay

        self.timer : float = delay
        self.playing : bool = False
        self.sound = pg.mixer.Sound(path)
        sounds.register(self)
        self.updateVolume()

        self.start()


    def update(self, dt : float):
        if not self.playing:
            return

        self.timer += dt
        if self.timer >= self.delay:
            self.sound.stop()
            self.sound.play()
            self.timer -= self.delay


    def start(self):
        self.playing = True


    def stop(self):
        self.playing = False

    def updateVolume(self):
        self.sound.set_volume(sounds.sfx)
