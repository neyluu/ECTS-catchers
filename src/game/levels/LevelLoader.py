from src.game.map.Map import Map

from src.game.map.tiles.Air import Air
from src.game.map.tiles.Block import Block
from src.game.map.tiles.Cobweb import Cobweb
from src.game.map.tiles.Coin import Coin
from src.game.map.tiles.Doors import Doors
from src.game.map.tiles.DoubleJump import DoubleJump
from src.game.map.tiles.Lava import Lava
from src.game.map.tiles.SpeedUp import SpeedUp
from src.game.map.tiles.Spikes import Spikes


def loadLevel(filename : str, levelMap : Map):
    path = "assets/levels/" + filename

    print(f"Loading level: {filename}")

    with open(path, 'r') as f:
        for line in f.readlines():

            parts = line.split(";")
            parts.pop()

            x = int(parts[0])
            y = int(parts[1])
            classType = parts[2]
            arguments = parts[3]
            arguments = arguments.split(" ")

            if classType == "Air":
                levelMap.setTile(x, y, Air())
            elif classType == "Block":
                levelMap.setTile(x, y, Block(arguments[0]))
            elif classType == "Coin":
                levelMap.setTile(x, y, Coin())
            elif classType == "Spikes":
                levelMap.setTile(x, y, Spikes(int(arguments[0])))
            elif classType == "Cobweb":
                levelMap.setTile(x, y, Cobweb())
            elif classType == "Doors":
                arg = True if arguments[0] == "True" else False
                levelMap.setTile(x, y, Doors(arg))
            elif classType == "Lava":
                levelMap.setTile(x, y, Lava(arguments[0]))
            elif classType == "SpeedUp":
                levelMap.setTile(x, y, SpeedUp())
            elif classType == "DoubleJump":
                levelMap.setTile(x, y, DoubleJump())
            else:
                print("ERROR: class: " + classType + " dont exist!")

    return levelMap