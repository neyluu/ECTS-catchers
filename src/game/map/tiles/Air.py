from src.game.map.tiles.Tile import Tile


class Air(Tile):
    def __init__(self):
        super().__init__()
        self.isCollision = False
        self.loadTexture("assets/textures/void.png")
