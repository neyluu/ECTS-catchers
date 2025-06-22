import pygame as pg

from src.config import Settings
from src.SceneManager import SceneManager
from src.scenes.MainMenu import MainMenu
from src.scenes.GameScene import GameScene
from src.scenes.EndScene import EndScene
from src.scenes.GameIntro import GameIntro
import ctypes

ctypes.windll.user32.SetProcessDPIAware()

pg.init()

BASE_RESOLUTION = (Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT)

pg.display.set_caption(Settings.TITLE)
programIcon = pg.image.load("assets/textures/logo/icon.png")
pg.display.set_icon(programIcon)

screenWidth = pg.display.Info().current_w
screenHeight = pg.display.Info().current_h

print(screenWidth, screenHeight)

# Final screen to draw content on
screen = pg.display.set_mode((screenWidth, screenHeight), pg.NOFRAME)

# Temporary screen to draw content to be later scaled
surface = pg.Surface(BASE_RESOLUTION)


class CoreEngine():
    def __init__(self):
        super().__init__()

        self.font = pg.font.SysFont("Arial", 18)

        self.sceneManager = SceneManager()
        self.running = True
        self.screen = surface
        self.clock = pg.time.Clock()
        self.scenes = [
            MainMenu(),
            GameScene(),
            GameIntro(),
            EndScene()
        ]
        self.dt = 0
        self.previousSceneIndex = self.sceneManager.getCurrentScene()


    def handleEvent(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.running = False

            self.scenes[self.sceneManager.getCurrentScene()].handleEvent(event)


    def update(self):
        if self.previousSceneIndex != self.sceneManager.getCurrentScene():
            self.scenes[self.previousSceneIndex].stop()
            self.previousSceneIndex = self.sceneManager.getCurrentScene()

        self.scenes[self.sceneManager.getCurrentScene()].update(self.dt)


    def draw(self):
        self.scenes[self.sceneManager.getCurrentScene()].draw(surface)

        fps = self.clock.get_fps()
        fps_text = self.font.render(f"FPS: {int(fps)}", True, pg.Color('lime'))
        surface.blit(fps_text, (0, 0))

        offsetX = 0
        offsetY = (screenHeight - Settings.SCREEN_HEIGHT) / 2
        screen.blit(surface, (offsetX, offsetY))
        pg.display.update()
        # pg.display.flip()


    def run(self):
        while self.running:
            self.handleEvent()
            self.update()
            self.draw()
            self.dt = self.clock.tick(Settings.TARGET_FPS) * 0.001
            self.dt = min(self.dt, 0.05)

