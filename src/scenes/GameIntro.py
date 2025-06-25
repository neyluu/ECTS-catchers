import pygame as pg

from src.scenes.Scene import Scene
from src.sounds.SFX import SFX
from src.sounds.SoundtrackManager import soundtrackManager
from src.gui.animations.Slide import slideAnimation


class GameIntro(Scene):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("assets/textures/gui/intro.png").convert()
        self.sceneChange : bool = False

        self.sfx = SFX("assets/audio/click.mp3")


    def handleEvent(self, event):
        if event.type == pg.KEYDOWN or event.type == pg.MOUSEBUTTONDOWN:
            self.sceneChange = True
            self.sfx.play()
            slideAnimation.start()


    def update(self, dt : float):
        if self.sceneChange:
            if slideAnimation.timeElapsed >= slideAnimation.time / 2:
                self.sceneManager.setCurrentScene(1)
                soundtrackManager.playGameSoundtrack()
                self.sceneChange = False


    def draw(self, screen : pg.Surface):
        screen.blit(self.image, (0,0))
