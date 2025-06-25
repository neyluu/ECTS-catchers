from src.sounds.Soundtrack import Soundtrack

class SoundtrackManager:
    def __init__(self):
        self.menuSoundtrack  = Soundtrack("assets/audio/soundtrack02.mp3")

        self.gameSoundtrack1 = Soundtrack("assets/audio/soundtrack01.mp3", False)
        self.gameSoundtrack2 = Soundtrack("assets/audio/soundtrack03.mp3", False)

        self.menuChannel = None
        self.game1Channel = None
        self.game2Channel = None

        self.menuPlaying = False
        self.gamePlaying = False

        self.game1Playing = False
        self.game2Playing = False

    def update(self, dt):
        if self.menuPlaying:
            return

        if self.game1Playing:
            if self.game1Channel and not self.game1Channel.get_busy():
                self.game1Playing = False
                self.game2Channel = self.gameSoundtrack2.play()
                self.game2Playing = True
                return

        if self.game2Playing:
            if self.game2Channel and not self.game2Channel.get_busy():
                self.game2Playing = False
                self.game1Channel = self.gameSoundtrack1.play()
                self.game1Playing = True
                return


    def playMenuSoundtrack(self):
        if self.menuPlaying:
            return

        print("Playing menu soundtrack")
        self.menuPlaying = True

        self.gamePlaying = False
        self.game1Playing = False
        self.game2Playing = False
        self.gameSoundtrack1.stop()
        self.gameSoundtrack2.stop()
        self.game1Channel = None
        self.game2Channel = None

        self.menuChannel = self.menuSoundtrack.play()


    def playGameSoundtrack(self):
        if self.gamePlaying:
            return

        print("Playing game soundtrack")
        self.gamePlaying = True

        self.menuPlaying = False
        self.menuSoundtrack.stop()

        self.game1Channel = self.gameSoundtrack1.play()
        self.game1Playing = True



soundtrackManager = SoundtrackManager()
