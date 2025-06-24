class SoundSettings:
    def __init__(self,
                 master : float = 1.0,
                 music : float = 0.0,
                 sfx : float = 1.0):

        self.musicBase  : float = music
        self.sfxBase    : float = sfx

        self.master : float = master
        self.music = self.musicBase * self.master
        self.sfx = self.sfxBase * self.master

        self.listeners = []


    def setMaster(self, volume : float):
        self.master = volume
        self.music = self.musicBase * self.master
        self.sfx = self.sfxBase * self.master
        self._notifyListeners()


    def setMusic(self, volume : float):
        self.musicBase = volume
        self.music = self.musicBase * self.master
        self._notifyListeners()


    def setSFX(self, volume : float):
        self.sfxBase = volume
        self.sfx = self.sfxBase * self.master
        self._notifyListeners()


    def register(self, listener):
        self.listeners.append(listener)


    def _notifyListeners(self):
        for listener in self.listeners:
            listener.updateVolume()