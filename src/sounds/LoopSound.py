import pygame as pg

class LoopSound:
    def __init__(self, path : str, delay : float):
        self.path = path
        self.delay = delay

        self.timer : float = delay
        self.playing : bool = False
        self.sound = pg.mixer.Sound(path)

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
