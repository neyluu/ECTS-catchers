import pygame as pg
import os

class SpriteAnimation:
    def __init__(self, path : str, animationTime : float):
        self.folderPath : str = path
        self.filenames = os.listdir(self.folderPath)
        self.frameFilenames = sorted([f for f in self.filenames if f.endswith(".png")])
        print(self.frameFilenames)
        self.frames = []
        self.loadFrames()

        self.currentFrame : int = 0
        self.animationTime : float = animationTime
        self.timePerFrame : float = self.animationTime / len(self.frames)
        self.timer : float = 0


    def handleEvent(self, event):
        pass


    def update(self, dt: float):
        self.timer += dt
        if self.timer > self.timePerFrame:
            self.currentFrame += 1
            if self.currentFrame >= len(self.frames):
                self.currentFrame = 0
            self.timer = 0


    def draw(self, screen: pg.Surface, position):
        screen.blit(self.frames[self.currentFrame], position)


    def loadFrames(self):
        for filename in self.frameFilenames:
            self.frames.append(pg.image.load(self.folderPath + "/" + filename).convert_alpha())