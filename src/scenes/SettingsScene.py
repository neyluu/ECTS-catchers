import pygame as pg
import sys

from src.scenes.Scene import Scene
from src.gui.Button import Button
from src.config import Settings  # <--- IMPORTUJE PLIK KONFIGURACYJNY


class SettingsScene(Scene):
    def __init__(self, screenWidth=1920, screenHeight=1080,
                 backgroundTargetWidth=None, backgroundTargetHeight=None):
        super().__init__()
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        # --- Konfiguracja ścieżek i zasobów ---
        assetsPath = "assets/"
        self.backgroundTexturePath = assetsPath + "textures/background/red_brick_wall_menu.png"
        self.defaultButtonTexturePath = assetsPath + "textures/gui/gui_button_1.png"
        self.fontPath = assetsPath + "fonts/timer_and_counter_font.ttf"

        # --- Tło ---
        rawBackgroundSurf = pg.image.load(self.backgroundTexturePath).convert()
        targetBgWidth = backgroundTargetWidth if backgroundTargetWidth is not None else self.screenWidth
        targetBgHeight = backgroundTargetHeight if backgroundTargetHeight is not None else self.screenHeight
        self.backgroundSurf = pg.transform.scale(rawBackgroundSurf, (targetBgWidth, targetBgHeight))


        self.masterVolume = int(Settings.SOUND_MASTER * 10)
        self.musicVolume = int(Settings.SOUND_MUSIC * 10)
        self.sfxVolume = int(Settings.SOUND_SFX * 10)
        self.currentFpsLimit = Settings.TARGET_FPS

        # --- Elementy interfejsu ---
        self.uiElements = []
        self.buttons = []
        self.createUi()

    def createUi(self):
        """Tworzy wszystkie elementy interfejsu użytkownika dla sceny ustawień."""
        textColor = (255, 255, 255)
        baseX = self.screenWidth // 2
        baseY = self.screenHeight // 4

        self.createText("SOUND", baseX, baseY, 70, textColor)
        self.createVolumeControl("master", baseY + 100, self.changeMasterVolume)
        self.createVolumeControl("music", baseY + 200, self.changeMusicVolume)
        self.createVolumeControl("sfx", baseY + 300, self.changeSfxVolume)

        self.createText("FPS LIMIT:", baseX, baseY + 450, 50, textColor)
        self.fpsButtons = {
            30: Button(x=585, y=baseY + 460, width=250, height=180, text="30",
                       texturePath=self.defaultButtonTexturePath, fontPath=self.fontPath, fontSize=35,
                       action=lambda: self.setFps(30)),
            60: Button(x=835, y=baseY + 460, width=250, height=180, text="60",
                       texturePath=self.defaultButtonTexturePath, fontPath=self.fontPath, fontSize=35,
                       action=lambda: self.setFps(60)),
            144: Button(x=1085, y=baseY + 460, width=250, height=180, text="144",
                        texturePath=self.defaultButtonTexturePath, fontPath=self.fontPath, fontSize=35,
                        action=lambda: self.setFps(144))
        }
        self.buttons.extend(self.fpsButtons.values())
        self.updateFpsButtonVisuals()

        self.backButton = Button(
            x=835, y=self.screenHeight - 200,
            width=250, height=180,
            texturePath=self.defaultButtonTexturePath,
            text="back",
            fontPath=self.fontPath, fontSize=35,
            textColor=(255, 255, 255),
            outlineColor=(0, 0, 0),
            outlineThickness=2,
            action=self.goToMainMenuScene
        )
        self.buttons.append(self.backButton)

    def createText(self, text, centerX, centerY, size, color):
        font = pg.font.Font(self.fontPath, size)
        textSurf = font.render(text, True, color)
        textRect = textSurf.get_rect(center=(centerX, centerY))
        self.uiElements.append((textSurf, textRect))

    def createVolumeControl(self, labelText, yPos, action):
        labelX = self.screenWidth // 2 - 250
        buttonsX = self.screenWidth // 2 + 200

        self.createText(f"{labelText}:", labelX, yPos, 50, (255, 255, 255))

        leftButton = Button(x=buttonsX - 100, y=yPos-85, width=150, height=180, text="<",
                             texturePath=self.defaultButtonTexturePath, fontPath=self.fontPath, fontSize=35,
                             action=lambda: action(-1))
        rightButton = Button(x=buttonsX + 80, y=yPos-85, width=150, height=180, text=">",
                              texturePath=self.defaultButtonTexturePath, fontPath=self.fontPath, fontSize=35,
                              action=lambda: action(1))
        self.buttons.extend([leftButton, rightButton])

    # --- Akcje przycisków ---
    def changeMasterVolume(self, change):
        self.masterVolume = max(0, min(10, self.masterVolume + change))
        # Aktualizacja wartości w pliku config
        Settings.SOUND_MASTER = self.masterVolume / 10.0
        print(f"Master volume set to: {Settings.SOUND_MASTER}")

    def changeMusicVolume(self, change):
        self.musicVolume = max(0, min(10, self.musicVolume + change))
        # Aktualizacja wartości w pliku config
        Settings.SOUND_MUSIC = self.musicVolume / 10.0
        print(f"Music volume set to: {Settings.SOUND_MUSIC}")

    def changeSfxVolume(self, change):
        self.sfxVolume = max(0, min(10, self.sfxVolume + change))
        # Aktualizacja wartości w pliku config
        Settings.SOUND_SFX = self.sfxVolume / 10.0
        print(f"SFX volume set to: {Settings.SOUND_SFX}")

    def setFps(self, fps):
        self.currentFpsLimit = fps
        # Aktualizacja wartości w pliku config
        Settings.TARGET_FPS = self.currentFpsLimit
        self.updateFpsButtonVisuals()
        print(f"FPS limit set to: {Settings.TARGET_FPS}")

    def updateFpsButtonVisuals(self):
        for fps, button in self.fpsButtons.items():
            try:
                if fps == self.currentFpsLimit:
                    button.set_text_color((255, 100, 100))
                else:
                    button.set_text_color((255, 255, 255))
            except AttributeError:
                pass

    def goToMainMenuScene(self):
        if self.sceneManager:
            self.sceneManager.setCurrentScene(0)

    def handleEvent(self, event: pg.event.Event):
        for button in self.buttons:
            button.handleEvent(event)
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.goToMainMenuScene()

    # Brak zmian w update i draw, ponieważ nie zawierają lokalnych zmiennych/metod do zmiany
    def update(self, dt: float):
        pass

    def draw(self, screen: pg.Surface):
        if self.backgroundSurf:
            screen.blit(self.backgroundSurf, (0, 0))
        else:
            screen.fill((80, 30, 130))

        for surf, rect in self.uiElements:
            screen.blit(surf, rect)

        font = pg.font.Font(self.fontPath, 50)
        baseY = self.screenHeight // 4

        masterValSurf = font.render(f"{self.masterVolume}/10", True, (255, 255, 255))
        screen.blit(masterValSurf, masterValSurf.get_rect(center=(self.screenWidth // 2, baseY + 100)))

        musicValSurf = font.render(f"{self.musicVolume}/10", True, (255, 255, 255))
        screen.blit(musicValSurf, musicValSurf.get_rect(center=(self.screenWidth // 2, baseY + 200)))

        sfxValSurf = font.render(f"{self.sfxVolume}/10", True, (255, 255, 255))
        screen.blit(sfxValSurf, sfxValSurf.get_rect(center=(self.screenWidth // 2, baseY + 300)))

        for button in self.buttons:
            button.draw(screen)