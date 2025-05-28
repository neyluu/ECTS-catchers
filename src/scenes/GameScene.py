import pygame as pg

from src.config import Settings
from src.gui.PauseMenu import PauseMenu
from src.scenes.Scene import Scene
from src.game.Game import Game
from src.game.PlayerKeymap import PlayerKeymap

class GameScene(Scene):

    def __init__(self):
        super().__init__()
        self.leftGame  = Game(True, pg.Rect(0, 0, Settings.SCREEN_WIDTH // 2, Settings.SCREEN_HEIGHT))
        self.rightGame = Game(False, pg.Rect(Settings.SCREEN_WIDTH // 2, 0, Settings.SCREEN_WIDTH // 2, Settings.SCREEN_HEIGHT))


        self.leftGame.setBackgroundColor(pg.Color(255, 0, 0, 0))
        self.rightGame.setBackgroundColor(pg.Color(0, 0, 255, 0))

        self.leftGame.player.color = pg.Color(255, 255, 0, 0)
        self.rightGame.player.color = pg.Color(0, 255, 255, 0)

        self.paused : bool = False
        self.pauseMenu = PauseMenu()


    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_2:
                self.sceneManager.setCurrentScene(2)
            elif event.key == pg.K_1:
                self.sceneManager.setCurrentScene(0)
            if event.key == Settings.KEYMAP_PAUSE:
                self.paused = not self.paused
                if self.paused:
                    self.onPause()
                else:
                    self.onUnPause()

        self.leftGame.handleEvent(event)
        self.rightGame.handleEvent(event)

        if self.paused:
            self.pauseMenu.handleEvent(event)


    def update(self, dt : float):
        self.leftGame.update(dt)
        self.rightGame.update(dt)

        if self.paused:
            self.pauseMenu.update(dt)


    def draw(self, screen : pg.Surface):
        screen.fill("red")

        self.leftGame.draw(screen)
        self.rightGame.draw(screen)

        if self.paused:
            self.pauseMenu.draw(screen)


    def onPause(self):
        pass


    def onUnPause(self):
        pass

