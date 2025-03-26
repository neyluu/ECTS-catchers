class SceneManager(object):
    """
     0 - mainMenu
     1 - gameScene
     2 - endScene
    """

    def __init__(self):
        self.currentScene = 0


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SceneManager, cls).__new__(cls)
        return cls.instance


    def setCurrentScene(self, sceneID):
        if sceneID < 0 or sceneID > 2:
            print("Scene index is out of range!")
            return
        self.currentScene = sceneID


    def getCurrentScene(self):
        return self.currentScene