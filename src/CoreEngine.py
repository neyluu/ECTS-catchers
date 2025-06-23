import pygame as pg

from src.config import Settings
from src.SceneManager import SceneManager
from src.scenes.MainMenu import MainMenu
from src.scenes.GameScene import GameScene
from src.scenes.GameIntro import GameIntro
import src.config.SettingsLoader as SettingsLoader
import ctypes

from src.scenes.SettingsScene import SettingsScene

ctypes.windll.user32.SetProcessDPIAware()

SettingsLoader.loadSettings()

pg.init()

BASE_RESOLUTION = (Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT)

pg.display.set_caption(Settings.TITLE)
programIcon = pg.image.load("assets/textures/logo/icon.png")
pg.display.set_icon(programIcon)

screenWidth = pg.display.Info().current_w
screenHeight = pg.display.Info().current_h

print(screenWidth, screenHeight)

screen = pg.display.set_mode((screenWidth, screenHeight), pg.NOFRAME)
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
            SettingsScene(),
            GameIntro()
        ]

        for scene in self.scenes:
            scene.sceneManager = self.sceneManager
            scene.allScenes = self.scenes

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
        currentSceneIndex = self.sceneManager.getCurrentScene()
        if self.previousSceneIndex != currentSceneIndex:
            previousScene = self.scenes[self.previousSceneIndex]
            currentScene = self.scenes[currentSceneIndex]

            if hasattr(previousScene, 'stop'):
                previousScene.stop()

            if hasattr(currentScene, 'onEnter'):
                currentScene.onEnter(previousScene)

            self.previousSceneIndex = currentSceneIndex

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

    def run(self):
        while self.running:
            self.handleEvent()
            self.update()
            self.draw()
            self.dt = self.clock.tick(Settings.TARGET_FPS) * 0.001
            self.dt = min(self.dt, 0.05)