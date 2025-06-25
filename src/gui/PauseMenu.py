import pygame as pg

from src.config import Settings
from src.gui.Button import Button
from src.gui.animations.Slide import slideAnimation
from src.sounds.SoundtrackManager import soundtrackManager
from src.SceneManager import SceneManager


class PauseMenu:
    def __init__(self, backgroundTexturePath="assets/textures/background/dark_grey_brick_bg.png"):
        self.isActive = False

        self.overlay = pg.Surface((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT), pg.SRCALPHA)
        self.overlay.fill((0, 0, 0, 150))

        self.menuWidth = 440
        self.menuHeight = 460
        self.menuRect = pg.Rect(
            (Settings.SCREEN_WIDTH - self.menuWidth) // 2,
            (Settings.SCREEN_HEIGHT - self.menuHeight) // 2,
            self.menuWidth,
            self.menuHeight
        )
        self.menuBgColor = (30, 30, 40)

        self.backgroundTexture = None
        if backgroundTexturePath:
            rawImage = pg.image.load(backgroundTexturePath).convert_alpha()
            self.backgroundTexture = pg.transform.scale(rawImage, (self.menuWidth, self.menuHeight))

        self.sceneChange: bool = False
        self.newScene: int = 0

        self.createButtons()


    def createButtons(self):
        buttonTexturePath = "assets/textures/gui/gui_button_1.png"
        fontPath = "assets/fonts/timer_and_counter_font.ttf"

        btnWidth = 450
        btnHeight = 320
        centerX = self.menuRect.centerx

        self.resumeButton = Button(
            x=centerX - btnWidth // 2, y=self.menuRect.top - 60,
            width=btnWidth, height=btnHeight,
            text="Resume", texturePath=buttonTexturePath, fontPath=fontPath,
            fontSize=35, action=self.resumeGame,
            hoverEffectColor=None
        )

        self.settingsButton = Button(
            x=centerX - btnWidth // 2, y=self.menuRect.top + 70,
            width=btnWidth, height=btnHeight,
            text="Settings", texturePath=buttonTexturePath, fontPath=fontPath,
            fontSize=35, action=self.goToSettings,
            hoverEffectColor=None
        )

        self.backToMenuButton = Button(
            x=centerX - btnWidth // 2, y=self.menuRect.top + 200,
            width=btnWidth, height=btnHeight,
            text="Back to Menu", texturePath=buttonTexturePath, fontPath=fontPath,
            fontSize=35, action=self.goToMainMenu,
            hoverEffectColor=None
        )

        self.buttons = [self.resumeButton, self.settingsButton, self.backToMenuButton]


    def resumeGame(self):
        self.isActive = False
        print("Menu pauzy: Wznawiam grę.")


    def goToSettings(self):
        self.newScene = 2
        self.sceneChange = True
        slideAnimation.start()


    def goToMainMenu(self):
        self.newScene = 0
        self.sceneChange = True
        slideAnimation.start()


    def handleEvent(self, event):
        if not self.isActive:
            return

        for button in self.buttons:
            button.handleEvent(event)


    def update(self, dt: float):
        if self.sceneChange:
            if slideAnimation.timeElapsed >= slideAnimation.time / 2:
                self.sceneManager.setCurrentScene(self.newScene)
                self.sceneChange = False

                if self.newScene == 0:
                    soundtrackManager.playMenuSoundtrack()


    def draw(self, screen: pg.Surface):
        if not self.isActive:
            return

        screen.blit(self.overlay, (0, 0))

        if self.backgroundTexture:
            screen.blit(self.backgroundTexture, self.menuRect.topleft)
        else:
            pg.draw.rect(screen, self.menuBgColor, self.menuRect, border_radius=15)

        pg.draw.rect(screen, (150, 150, 170), self.menuRect, width=3, border_radius=15)

        for button in self.buttons:
            button.draw(screen)


    def toggle(self):
        self.isActive = not self.isActive