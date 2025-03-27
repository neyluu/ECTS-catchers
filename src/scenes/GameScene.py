import pygame as pg

from src.common import Settings
from src.scenes.Scene import Scene
from src.game.Game import Game

class GameScene(Scene):

    def __init__(self):
        super().__init__()
        self.leftGame  = Game(self.screen, pg.Rect(0, 0, Settings.SCREEN_WIDTH // 2, Settings.SCREEN_HEIGHT))
        self.rightGame = Game(self.screen, pg.Rect(Settings.SCREEN_WIDTH // 2, 0, Settings.SCREEN_WIDTH // 2, Settings.SCREEN_HEIGHT))

        self.leftGame.setBackgroundColor(pg.Color(255, 0, 0, 0))
        self.rightGame.setBackgroundColor(pg.Color(0, 0, 255, 0))

        self.leftGame.player.color = pg.Color(0, 0, 0, 0)
        self.rightGame.player.color = pg.Color(255, 255, 255, 0)


    def handleEvent(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                self.sceneManager.setCurrentScene(2)
            elif event.key == pg.K_LEFT:
                self.sceneManager.setCurrentScene(0)

        self.leftGame.handleEvent(event)
        self.rightGame.handleEvent(event)


    def update(self, dt : float):
        self.leftGame.update(dt)
        self.rightGame.update(dt)


    def draw(self):
        self.screen.fill("red")

        self.leftGame.draw()
        self.rightGame.draw()
