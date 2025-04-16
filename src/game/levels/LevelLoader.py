from src.game.map.Map import Map
from src.game.map.tiles.Air import Air
from src.game.map.tiles.Block import Block


class LevelLoader:

    def load(self, filename : str, levelMap : Map):
        path = "assets/levels/" + filename

        with open(path, 'r') as f:
            for line in f.readlines():

                parts = line.split(";")
                parts.pop()

                x = int(parts[0])
                y = int(parts[1])
                classType = parts[2]
                arguments = parts[3]

                if classType == "Air":
                    levelMap.setTile(x, y, Air())
                if classType == "Block":
                    levelMap.setTile(x, y, Block())

        return levelMap