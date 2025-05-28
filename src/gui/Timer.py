import pygame as pg

class Timer:
    def __init__(self,
                 fontPath: str = "assets/fonts/first.ttf",
                 fontSize: int = 60,
                 color: tuple = (255, 255, 255)
                 ):
        pg.font.init()

        self.textColor = color
        self.font = pg.font.Font(fontPath, fontSize)

        self.startTimeCurrentSegmentTicks = pg.time.get_ticks()
        self.elapsedTimeWhenPausedMs = 0
        self.elapsedTimeStr = "00:00"
        self.lastDisplayedSecond = -1
        self.running = True

    def getCurrentTotalElapsedMs(self) -> int:
        if self.running:
            currentSegmentElapsedMs = pg.time.get_ticks() - self.startTimeCurrentSegmentTicks
            return self.elapsedTimeWhenPausedMs + currentSegmentElapsedMs
        else:
            return self.elapsedTimeWhenPausedMs

    def update(self):
        totalElapsedMs = self.getCurrentTotalElapsedMs()
        totalSeconds = totalElapsedMs // 1000

        if totalSeconds != self.lastDisplayedSecond:
            minutes = totalSeconds // 60
            seconds = totalSeconds % 60
            self.elapsedTimeStr = f"{minutes:02d}:{seconds:02d}"
            self.lastDisplayedSecond = totalSeconds

    def draw(self, screen: pg.Surface, position: tuple):
        textSurface = self.font.render(self.elapsedTimeStr, True, self.textColor)
        screen.blit(textSurface, position)

    def reset(self):
        self.startTimeCurrentSegmentTicks = pg.time.get_ticks()
        self.elapsedTimeWhenPausedMs = 0
        self.elapsedTimeStr = "00:00"
        self.lastDisplayedSecond = -1
        self.running = True

    def pause(self):
        if self.running:
            currentTicks = pg.time.get_ticks()
            self.elapsedTimeWhenPausedMs += (currentTicks - self.startTimeCurrentSegmentTicks)
            self.running = False

    def resume(self):
        if not self.running:
            self.startTimeCurrentSegmentTicks = pg.time.get_ticks()
            self.running = True

    def getTimeString(self) -> str:
        return self.elapsedTimeStr

    def getTotalSeconds(self) -> int:
        totalElapsedMs = self.getCurrentTotalElapsedMs()
        return totalElapsedMs // 1000
