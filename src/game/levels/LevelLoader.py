from src.game.map.Map import Map

from src.game.map.tiles.Air import Air
from src.game.map.tiles.Block import Block
from src.game.map.tiles.Cobweb import Cobweb
from src.game.map.tiles.Coin import Coin
from src.game.map.tiles.Doors import Doors
from src.game.map.tiles.Spikes import Spikes


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
                elif classType == "Block":
                    levelMap.setTile(x, y, Block())
                elif classType == "Coin":
                    levelMap.setTile(x, y, Coin())
                elif classType == "Spikes":
                    levelMap.setTile(x, y, Spikes())
                elif classType == "Cobweb":
                    levelMap.setTile(x, y, Cobweb())
                elif classType == "Doors":
                    levelMap.setTile(x, y, Doors())
                else:
                    print("ERROR: class: " + classType + " dont exist!")

        return levelMap