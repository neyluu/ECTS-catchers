import pygame as pg

from src.config.SoundSettings import SoundSettings
from src.game.PlayerKeymap import PlayerKeymap

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
TARGET_FPS = 60
FPS_COUNTER = False
TITLE = "ECTS catchers"

PLAYER_LEFT_KEYMAP = PlayerKeymap()
PLAYER_LEFT_KEYMAP.MOVE_UP = pg.K_w
PLAYER_LEFT_KEYMAP.MOVE_RIGHT = pg.K_d
PLAYER_LEFT_KEYMAP.MOVE_DOWN = pg.K_s
PLAYER_LEFT_KEYMAP.MOVE_LEFT = pg.K_a

PLAYER_RIGHT_KEYMAP = PlayerKeymap()
PLAYER_RIGHT_KEYMAP.MOVE_UP = pg.K_UP
PLAYER_RIGHT_KEYMAP.MOVE_RIGHT = pg.K_RIGHT
PLAYER_RIGHT_KEYMAP.MOVE_DOWN = pg.K_DOWN
PLAYER_RIGHT_KEYMAP.MOVE_LEFT = pg.K_LEFT

KEYMAP_PAUSE = pg.K_p

# Sound can be changed from 0 to 1, menu will have 10 steps so sound can change by 0.1
sounds = SoundSettings(1.0, 0.5, 1.0)
