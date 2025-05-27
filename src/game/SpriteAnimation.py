import pygame as pg
import os

class SpriteAnimation:
    def __init__(self, path: str, animationTime: float, targetSize: tuple[int, int] = None):
        self.folderPath: str = path
        self.filenames = os.listdir(self.folderPath)
        self.frameFilenames = sorted([f for f in self.filenames if f.endswith(".png")])
        self.frames = []
        self.targetSize = targetSize  # <-- nowy parametr
        self.loadFrames()

        self.currentFrame: int = 0
        self.animationTime: float = animationTime
        self.timePerFrame: float = self.animationTime / len(self.frames)
        self.timer: float = 0

    def handleEvent(self, event):
        pass

    def update(self, dt: float):
        self.timer += dt
        if self.timer > self.timePerFrame:
            self.currentFrame = (self.currentFrame + 1) % len(self.frames)
            self.timer = 0

    def draw(self, screen: pg.Surface, position):
        screen.blit(self.frames[self.currentFrame], position)

    def loadFrames(self):
        for filename in self.frameFilenames:
            image = pg.image.load(os.path.join(self.folderPath, filename)).convert_alpha()
            if self.targetSize:  # Skaluj jeśli podano rozmiar
                image = pg.transform.scale(image, self.targetSize)
            self.frames.append(image)
