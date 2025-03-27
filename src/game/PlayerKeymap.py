import pygame as pg

class PlayerKeymap:
    def __init__(self):
        self.MOVE_UP = pg.K_w
        self.MOVE_RIGHT = pg.K_d
        self.MOVE_DOWN = pg.K_s
        self.MOVE_LEFT = pg.K_a