import pygame as pg

class Blink:
    def __init__(self, canvas : pg.Rect):
        self.canvas = canvas

        self.color = pg.Color(0, 0, 0)
        self.time : float = 2 # seconds, whole animation
        self.offset : float = 0.1

        self.timeElapsed : float = 0
        self.opacity : float = 0

        self.running : bool = False

    def handleEvent(self, event):
        pass


    def update(self, dt: float):
        if not self.running:
            return

        self.timeElapsed += dt

        if self.timeElapsed < (self.time / 2) - self.offset:
            self.opacity += 255 / ((self.time / 2 - self.offset) / dt)
            if self.opacity > 255:
                self.opacity = 255
        if self.timeElapsed > (self.time / 2) + self.offset:
            self.opacity -= 255 / ((self.time / 2 + self.offset) / dt)
            if self.opacity < 0:
                self.opacity = 0

        if self.timeElapsed > self.time:
            self.stop()


    def draw(self, screen: pg.Surface):
        if not self.running:
            return

        overlay = pg.Surface((self.canvas.width, self.canvas.height), pg.SRCALPHA)
        overlay.fill((self.color.r, self.color.g, self.color.b, self.opacity))
        screen.blit(overlay, (self.canvas.left, self.canvas.top))


    def start(self):
        self.running = True


    def stop(self):
        self.running = False


    def reset(self):
        self.timeElapsed = 0
        self.opacity = 0