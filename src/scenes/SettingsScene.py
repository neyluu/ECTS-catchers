import pygame as pg

from src.gui.animations.Slide import slideAnimation
from src.scenes.Scene import Scene
from src.gui.Button import Button
from src.config import Settings
import src.config.SettingsLoader as SettingsLoader


class SettingsScene(Scene):
    def __init__(self, backgroundTargetWidth=None, backgroundTargetHeight=None):
        super().__init__()
        self.screenWidth = Settings.SCREEN_WIDTH
        self.screenHeight = Settings.SCREEN_HEIGHT

        self.returnIndex = 0

        assetsPath = "assets/"
        self.backgroundTexturePath = assetsPath + "textures/background/red_brick_wall_menu.png"
        self.defaultButtonTexturePath = assetsPath + "textures/gui/gui_button_1.png"
        self.selectedButtonTexturePath = assetsPath + "textures/gui/gui_button_4.png"
        self.fontPath = assetsPath + "fonts/timer_and_counter_font.ttf"

        rawBackgroundSurf = pg.image.load(self.backgroundTexturePath).convert()
        targetBgWidth = backgroundTargetWidth if backgroundTargetWidth is not None else self.screenWidth
        targetBgHeight = backgroundTargetHeight if backgroundTargetHeight is not None else self.screenHeight
        self.backgroundSurf = pg.transform.scale(rawBackgroundSurf, (targetBgWidth, targetBgHeight))

        self.baseY = self.screenHeight // 4 - 150

        self.masterVolume = int(Settings.sounds.master * 10)
        self.musicVolume = int(Settings.sounds.musicBase * 10)
        self.sfxVolume = int(Settings.sounds.sfxBase * 10)
        self.currentFpsLimit = Settings.TARGET_FPS

        self.uiElements = []
        self.buttons = []
        self.createUi()

        self.sceneChange: bool = False

    def onEnter(self, previousScene=None):
        if previousScene and hasattr(self, 'allScenes'):
            try:
                self.returnIndex = self.allScenes.index(previousScene)
            except ValueError:
                self.returnIndex = 0
        else:
            self.returnIndex = 0

    def createUi(self):
        self.defaultTextColor = (255, 255, 255)

        textColor = self.defaultTextColor
        baseX = self.screenWidth // 2

        self.createText("SOUND", baseX, self.baseY, 70, textColor)
        self.createVolumeControl("master", self.baseY + 100, self.changeMasterVolume)
        self.createVolumeControl("music", self.baseY + 200, self.changeMusicVolume)
        self.createVolumeControl("sfx", self.baseY + 300, self.changeSfxVolume)

        self.createText("FPS LIMIT:", baseX, self.baseY + 450, 50, textColor)
        self.fpsButtons = {

            30: Button(textColor=self.defaultTextColor, x=585, y=self.baseY + 460, width=250, height=180, text="30",
                       texturePath=self.defaultButtonTexturePath, fontPath=self.fontPath, fontSize=35,
                       action=lambda: self.setFps(30), hoverEffectColor=None),
            60: Button(textColor=self.defaultTextColor, x=835, y=self.baseY + 460, width=250, height=180, text="60",
                       texturePath=self.defaultButtonTexturePath, fontPath=self.fontPath, fontSize=35,
                       action=lambda: self.setFps(60), hoverEffectColor=None),
            144: Button(textColor=self.defaultTextColor, x=1085, y=self.baseY + 460, width=250, height=180, text="144",
                        texturePath=self.defaultButtonTexturePath, fontPath=self.fontPath, fontSize=35,
                        action=lambda: self.setFps(144), hoverEffectColor=None)

        }
        self.buttons.extend(self.fpsButtons.values())

        self.createText("FPS COUNTER: ", baseX, self.baseY + 650, 50, textColor)
        self.fpsCounterButtons = {
            True: Button(textColor=self.defaultTextColor, x=760, y=self.baseY + 650, width=200, height=180, text="ON",
                         texturePath=self.defaultButtonTexturePath, fontPath=self.fontPath, fontSize=35,
                         action=lambda: self.setFPSCounter(True), hoverEffectColor=None),
            False: Button(textColor=self.defaultTextColor, x=960, y=self.baseY + 650, width=200, height=180, text="OFF",
                          texturePath=self.defaultButtonTexturePath, fontPath=self.fontPath, fontSize=35,
                          action=lambda: self.setFPSCounter(False), hoverEffectColor=None)
        }
        self.buttons.extend(self.fpsCounterButtons.values())

        self.backButton = Button(
            x=835, y=self.screenHeight - 200, width=250, height=180,
            texturePath=self.defaultButtonTexturePath, text="back",
            fontPath=self.fontPath, fontSize=35, textColor=(255, 255, 255),
            outlineColor=(0, 0, 0), outlineThickness=2,
            action=self.goBack,
            hoverEffectColor=None
        )
        self.buttons.append(self.backButton)
        self.updateFpsButtonHighlights()
        self.updateFpsCounterButtonHighlights()

    def createText(self, text, centerX, centerY, size, color):
        font = pg.font.Font(self.fontPath, size)
        textSurf = font.render(text, True, color)
        textRect = textSurf.get_rect(center=(centerX, centerY))
        self.uiElements.append((textSurf, textRect))

    def createVolumeControl(self, labelText, yPos, action):
        labelX = self.screenWidth // 2 - 250
        buttonsX = self.screenWidth // 2 + 200
        self.createText(f"{labelText}:", labelX, yPos, 50, (255, 255, 255))
        leftButton = Button(x=buttonsX - 100, y=yPos - 85, width=150, height=180, text="<",
                            texturePath=self.defaultButtonTexturePath, fontPath=self.fontPath, fontSize=35,
                            action=lambda: action(-1), hoverEffectColor=None)
        rightButton = Button(x=buttonsX + 80, y=yPos - 85, width=150, height=180, text=">",
                             texturePath=self.defaultButtonTexturePath, fontPath=self.fontPath, fontSize=35,
                             action=lambda: action(1), hoverEffectColor=None)
        self.buttons.extend([leftButton, rightButton])

    def changeMasterVolume(self, change):
        self.masterVolume = max(0, min(10, self.masterVolume + change))
        newMasterVolume = self.masterVolume / 10.0
        Settings.sounds.setMaster(newMasterVolume)
        print(f"Changed sound master to: {newMasterVolume}")
        SettingsLoader.saveSettings()

    def changeMusicVolume(self, change):
        self.musicVolume = max(0, min(10, self.musicVolume + change))
        newMusicVolume = self.musicVolume / 10.0
        Settings.sounds.setMusic(newMusicVolume)
        print(f"Changed sound music to: {newMusicVolume}")
        SettingsLoader.saveSettings()

    def changeSfxVolume(self, change):
        self.sfxVolume = max(0, min(10, self.sfxVolume + change))
        newSFXVolume = self.sfxVolume / 10.0
        Settings.sounds.setSFX(newSFXVolume)
        print(f"Changed sound sfx to: {newSFXVolume}")
        SettingsLoader.saveSettings()

    def setFps(self, fps):
        self.currentFpsLimit = fps
        Settings.TARGET_FPS = self.currentFpsLimit
        SettingsLoader.saveSettings()
        self.updateFpsButtonHighlights()

    def updateFpsButtonHighlights(self):
        """Podmienia teksturę przycisków FPS i odświeża ich wygląd."""

        defaultImg = pg.image.load(self.defaultButtonTexturePath).convert_alpha()
        selectedImg = pg.image.load(self.selectedButtonTexturePath).convert_alpha()

        for fps, button in self.fpsButtons.items():
            imageToUse = selectedImg if fps == self.currentFpsLimit else defaultImg
            button.baseScaledImage = pg.transform.scale(imageToUse, (button.buttonWidth, button.buttonHeight))
            button._rebuildTexture()

    def setFPSCounter(self, visible: bool):
        Settings.FPS_COUNTER = visible
        SettingsLoader.saveSettings()
        self.updateFpsCounterButtonHighlights()

    def updateFpsCounterButtonHighlights(self):
        """Podmienia teksturę przycisków licznika FPS i odświeża ich wygląd."""
        defaultImg = pg.image.load(self.defaultButtonTexturePath).convert_alpha()
        selectedImg = pg.image.load(self.selectedButtonTexturePath).convert_alpha()

        for state, button in self.fpsCounterButtons.items():
            imageToUse = selectedImg if state == Settings.FPS_COUNTER else defaultImg
            button.baseScaledImage = pg.transform.scale(imageToUse, (button.buttonWidth, button.buttonHeight))
            button._rebuildTexture()

    def goBack(self):
        self.sceneChange = True
        slideAnimation.start()

    def handleEvent(self, event: pg.event.Event):
        for button in self.buttons:
            button.handleEvent(event)
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.goBack()

    def update(self, dt: float):
        if self.sceneChange:
            if slideAnimation.timeElapsed >= slideAnimation.time / 2:
                self.sceneManager.setCurrentScene(self.returnIndex)
                self.sceneChange = False

    def draw(self, screen: pg.Surface):
        if self.backgroundSurf:
            screen.blit(self.backgroundSurf, (0, 0))
        else:
            screen.fill((80, 30, 130))

        for surf, rect in self.uiElements:
            screen.blit(surf, rect)

        font = pg.font.Font(self.fontPath, 50)

        masterValSurf = font.render(f"{self.masterVolume}/10", True, (255, 255, 255))
        screen.blit(masterValSurf, masterValSurf.get_rect(center=(self.screenWidth // 2, self.baseY + 100)))

        musicValSurf = font.render(f"{self.musicVolume}/10", True, (255, 255, 255))
        screen.blit(musicValSurf, musicValSurf.get_rect(center=(self.screenWidth // 2, self.baseY + 200)))

        sfxValSurf = font.render(f"{self.sfxVolume}/10", True, (255, 255, 255))
        screen.blit(sfxValSurf, sfxValSurf.get_rect(center=(self.screenWidth // 2, self.baseY + 300)))

        for button in self.buttons:
            button.draw(screen)
