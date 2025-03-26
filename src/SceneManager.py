class SceneManager(object):
    """
     0 - mainMenu
     1 - gameScene
     2 - endScene
    """



    def __init__(self):
        self._MIN_SCENE_ID = 0
        self._MAX_SCENE_ID = 2
        self.currentScene = 0


    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SceneManager, cls).__new__(cls)
        return cls.instance


    def setCurrentScene(self, sceneID):
        if sceneID < self._MIN_SCENE_ID or sceneID > self._MIN_SCENE_ID:
            print("Scene index is out of range!")
            return
        self.currentScene = sceneID


    def getCurrentScene(self):
        return self.currentScene