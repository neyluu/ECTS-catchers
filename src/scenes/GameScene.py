import pygame as pg

from src.scenes.Scene import Scene
from src.game.Game import Game
from src.config import Settings
from src.gui.PauseMenu import PauseMenu
from src.scenes.SettingsScene import SettingsScene
from src.sounds.Soundtrack import Soundtrack
from src.gui.Button import Button


class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.screenWidth = Settings.SCREEN_WIDTH
        self.screenHeight = Settings.SCREEN_HEIGHT

        self.leftCanvas = pg.Rect(0, 0, self.screenWidth // 2, self.screenHeight)
        self.rightCanvas = pg.Rect(self.screenWidth // 2, 0, self.screenWidth // 2, self.screenHeight)

        self.gameLeft = Game(isLeft=True, canvas=self.leftCanvas)
        self.gameRight = Game(isLeft=False, canvas=self.rightCanvas)

        self.divider = pg.Rect(self.screenWidth // 2 - 2, 0, 4, self.screenHeight)
        self.pauseMenu = PauseMenu()

        self.gameOverButton = Button(
            x=Settings.SCREEN_WIDTH / 2 - 650 / 2,
            y=750,
            width=750, height=475,
            texturePath="assets/textures/gui/gui_button_1.png",
            text="main menu",
            rotationAngle=0,
            fontPath="assets/fonts/timer_and_counter_font.ttf",
            fontSize=70,
            textColor=(250, 250, 250),
            outlineColor=(0, 0, 0),
            outlineThickness=2,
            hoverEffectColor=None,
            action=self.goToMainMenu
        )


    def handleEvent(self, event: pg.event.Event):
        if event.type == pg.KEYDOWN and event.key == Settings.KEYMAP_PAUSE:
            self.pauseMenu.toggle()

        if self.pauseMenu.isActive:
            self.pauseMenu.handleEvent(event)
        else:
            self.gameLeft.handleEvent(event)
            self.gameRight.handleEvent(event)
        if self.bothGameOvers():
            self.gameOverButton.handleEvent(event)


    def update(self, dt: float):
        if self.pauseMenu.isActive:
            self.pauseMenu.update(dt)
            return

        self.gameLeft.update(dt)
        self.gameRight.update(dt)


    def draw(self, screen: pg.Surface):
        self.gameLeft.draw(screen)
        self.gameRight.draw(screen)
        pg.draw.rect(screen, (20, 20, 20), self.divider)
        self.pauseMenu.draw(screen)

        if self.bothGameOvers():
            self.gameOverButton.draw(screen)


    def reset(self):
        self.gameLeft.reset()
        self.gameRight.reset()
        self.pauseMenu.isActive = False

    def onEnter(self, previousScene=None):
        if isinstance(previousScene, SettingsScene):
            self.pauseMenu.isActive = True
        else:
            self.reset()


    def goToMainMenu(self):
        print("Going to main menu")
        self.gameLeft.reset()
        self.gameRight.reset()

        print("Switching to Main Menu")
        if self.sceneManager:
            self.sceneManager.setCurrentScene(0)


    def bothGameOvers(self) -> bool:
        return self.gameLeft.isGameOver and self.gameRight.isGameOver \
                and not self.gameLeft.gameOverAnimation.running and not self.gameRight.gameOverAnimation.running