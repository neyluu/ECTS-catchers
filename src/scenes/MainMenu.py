import pygame as pg
import sys

from src.gui.animations.Slide import slideAnimation
from src.scenes.Scene import Scene
from src.gui.Button import Button
import src.config.Settings as Settings


class MainMenu(Scene):
    def __init__(self,
                 backgroundTargetWidth=None, backgroundTargetHeight=None,
                 logoTargetWidth=750, logoTargetHeight=750):
        super().__init__()
        self.screenWidth = Settings.SCREEN_WIDTH
        self.screenHeight = Settings.SCREEN_HEIGHT

        assetsPath = "assets/"
        self.backgroundTexturePath = assetsPath + "textures/background/red_brick_wall_menu.png"
        self.logoTexturePath = assetsPath + "textures/logo/icon.png"
        defaultButtonTexturePath = assetsPath + "textures/gui/gui_button_1.png"
        defaultButtonFontPath = assetsPath + "fonts/timer_and_counter_font.ttf"

        rawBackgroundSurf = pg.image.load(self.backgroundTexturePath).convert()
        targetBgWidth = backgroundTargetWidth if backgroundTargetWidth is not None else self.screenWidth
        targetBgHeight = backgroundTargetHeight if backgroundTargetHeight is not None else self.screenHeight
        self.backgroundSurf = pg.transform.scale(rawBackgroundSurf, (targetBgWidth, targetBgHeight))

        self.logoSurf = pg.image.load(self.logoTexturePath).convert_alpha()
        if logoTargetWidth is not None and logoTargetHeight is not None:
            self.logoSurf = pg.transform.scale(self.logoSurf, (logoTargetWidth, logoTargetHeight))

        self.logoRect = self.logoSurf.get_rect(
            center=(self.screenWidth - 1350, self.screenHeight // 2))

        firstButtonTopY = int(self.screenHeight - 1125)
        buttonVerticalSpacing = -400

        defaultButtonPositionX = self.screenWidth - 950
        defaultButtonTextColor = (250, 250, 250)
        defaultButtonOutlineColor = (0, 0, 0)
        defaultButtonOutlineThickness = 2
        defaultButtonHoverColor = None
        defaultButtonWidth = 850
        defaultButtonHeight = 650
        defaultButtonFontSize = 70

        self.playButton = Button(
            x=defaultButtonPositionX, y=firstButtonTopY,
            width=defaultButtonWidth, height=defaultButtonHeight,
            texturePath=defaultButtonTexturePath,
            text="play",
            rotationAngle=3,
            fontPath=defaultButtonFontPath, fontSize=defaultButtonFontSize,
            textColor=defaultButtonTextColor,
            outlineColor=defaultButtonOutlineColor,
            outlineThickness=defaultButtonOutlineThickness,
            hoverEffectColor=defaultButtonHoverColor,
            action=self.goToGameScene
        )

        settingsButtonTopLeftY = firstButtonTopY + defaultButtonHeight + buttonVerticalSpacing

        self.settingsButton = Button(
            x=defaultButtonPositionX, y=settingsButtonTopLeftY,
            width=defaultButtonWidth, height=defaultButtonHeight,
            texturePath=defaultButtonTexturePath,
            text="settings",
            rotationAngle=-2,
            fontPath=defaultButtonFontPath, fontSize=defaultButtonFontSize,
            textColor=defaultButtonTextColor,
            outlineColor=defaultButtonOutlineColor,
            outlineThickness=defaultButtonOutlineThickness,
            hoverEffectColor=defaultButtonHoverColor,
            action=self.goToSettingsScene
        )

        exitButtonTopLeftY = settingsButtonTopLeftY + defaultButtonHeight + buttonVerticalSpacing

        self.exitButton = Button(
            x=defaultButtonPositionX, y=exitButtonTopLeftY,
            width=defaultButtonWidth, height=defaultButtonHeight,
            texturePath=defaultButtonTexturePath,
            text="exit",
            rotationAngle=-1,
            fontPath=defaultButtonFontPath, fontSize=defaultButtonFontSize,
            textColor=defaultButtonTextColor,
            outlineColor=defaultButtonOutlineColor,
            outlineThickness=defaultButtonOutlineThickness,
            hoverEffectColor=defaultButtonHoverColor,
            action=self.quitGame
        )

        self.buttons = [self.playButton, self.settingsButton, self.exitButton]

        self.sceneChange : bool = False
        self.newScene : int = 0


    def goToGameScene(self):
        print("Switching to Game Scene")
        self.newScene = 3
        self.sceneChange = True
        slideAnimation.start()


    def goToSettingsScene(self):
        print("Switching to Settings Scene")
        self.newScene = 2
        self.sceneChange = True
        slideAnimation.start()


    def quitGame(self):
        print("Exiting game")
        pg.quit()
        sys.exit()


    def handleEvent(self, event: pg.event.Event):
        for button in self.buttons:
            button.handleEvent(event)


    def update(self, dt: float):
        if self.sceneChange:
            if slideAnimation.timeElapsed >= slideAnimation.time / 2:
                self.sceneManager.setCurrentScene(self.newScene)
                print(f"Changing scene to: {self.newScene}")
                self.sceneChange = False


    def draw(self, screen: pg.Surface):
        if self.backgroundSurf:
            screen.blit(self.backgroundSurf, (0, 0))
        else:
            screen.fill((80, 30, 130))

        if self.logoSurf and self.logoRect:
            screen.blit(self.logoSurf, self.logoRect)

        for button in self.buttons:
            button.draw(screen)