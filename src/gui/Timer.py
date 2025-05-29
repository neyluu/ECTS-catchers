import pygame as pg


class Timer:
    def __init__(self,
                 fontPath: str = "assets/fonts/timer_and_counter_font.ttf",
                 fontSize: int = 60,
                 color: tuple = (255, 255, 255),
                 iconImagePath: str = None,
                 iconSize: tuple = (50, 50),
                 iconTextPadding: int = 8
                 ):
        pg.font.init()

        self.textColor = color
        self.font = pg.font.Font(fontPath, fontSize)

        self.iconSurface = None
        if iconImagePath:
            originalIcon = pg.image.load(iconImagePath).convert_alpha()
            self.iconSurface = pg.transform.scale(originalIcon, iconSize)

        self.startTimeCurrentSegmentTicks = pg.time.get_ticks()
        self.elapsedTimeWhenPausedMs = 0
        self.elapsedTimeStr = "00:00"
        self.lastDisplayedSecond = -1
        self.running = True
        self.iconTextPadding = iconTextPadding

    def getCurrentTotalElapsedMs(self) -> int:
        if self.running:
            currentSegmentElapsedMs = pg.time.get_ticks() - self.startTimeCurrentSegmentTicks
            return self.elapsedTimeWhenPausedMs + currentSegmentElapsedMs
        else:
            return self.elapsedTimeWhenPausedMs

    def update(self):
        if not self.running:
            return

        totalElapsedMs = self.getCurrentTotalElapsedMs()
        totalSeconds = totalElapsedMs // 1000

        if totalSeconds != self.lastDisplayedSecond:
            minutes = totalSeconds // 60
            seconds = totalSeconds % 60
            self.elapsedTimeStr = f"{minutes:02d}:{seconds:02d}"
            self.lastDisplayedSecond = totalSeconds

    def draw(self, screen: pg.Surface, position: tuple):
        currentX = position[0]
        currentY = position[1]

        iconHeight = 0
        if self.iconSurface:
            screen.blit(self.iconSurface, (currentX, currentY))
            currentX += self.iconSurface.get_width() + self.iconTextPadding
            iconHeight = self.iconSurface.get_height()

        textSurface = self.font.render(self.elapsedTimeStr, True, self.textColor)

        textRect = textSurface.get_rect()
        if self.iconSurface:
            textY = currentY + (iconHeight / 2) - (textRect.height / 2)
        else:
            textY = currentY

        screen.blit(textSurface, (currentX, textY))

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
