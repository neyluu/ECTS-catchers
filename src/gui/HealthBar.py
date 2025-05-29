import pygame as pg


class HealthBar:
    def __init__(self,
                 playerData,
                 heart1ImagePath: str = "assets/textures/gui/Heart_1.png",
                 heart2ImagePath: str = "assets/textures/gui/Heart_2.png",
                 heart3ImagePath: str = "assets/textures/gui/Heart_3.png",
                 displayHeartWidth=0,
                 displayHeartHeight=0,
                 numberOfPhysicalHearts: int = 4,
                 heartPadding: int = 4
                 ):

        self.playerData = playerData
        self.heartPadding = heartPadding
        self.numberOfPhysicalHearts = numberOfPhysicalHearts
        self.subHpPerFullHeart = 2

        originalHeartImage1 = pg.image.load(heart1ImagePath).convert_alpha()
        originalHeartImage2 = pg.image.load(heart2ImagePath).convert_alpha()
        originalHeartImage3 = pg.image.load(heart3ImagePath).convert_alpha()

        self.heartImage1 = pg.transform.scale(originalHeartImage1, (displayHeartWidth, displayHeartHeight))
        self.heartImage2 = pg.transform.scale(originalHeartImage2, (displayHeartWidth, displayHeartHeight))
        self.heartImage3 = pg.transform.scale(originalHeartImage3, (displayHeartWidth, displayHeartHeight))

        self.heartWidth = self.heartImage1.get_width()
        self.heartHeight = self.heartImage1.get_height()

    def update(self):
        pass

    def draw(self, screen: pg.Surface, position: tuple):
        startX, startY = position

        currentTotalSubHp = max(0, self.playerData.hp)

        remainingSubHp = currentTotalSubHp

        for i in range(self.numberOfPhysicalHearts):
            heartX = startX + i * (self.heartWidth + self.heartPadding)
            heartY = startY

            imageToDrawThisSlot = None

            if remainingSubHp >= self.subHpPerFullHeart:
                imageToDrawThisSlot = self.heartImage1
                remainingSubHp -= self.subHpPerFullHeart
            elif remainingSubHp == self.subHpPerFullHeart - 1:
                imageToDrawThisSlot = self.heartImage2
                remainingSubHp -= (self.subHpPerFullHeart - 1)
            else:
                imageToDrawThisSlot = self.heartImage3
                remainingSubHp = 0

            if imageToDrawThisSlot:
                screen.blit(imageToDrawThisSlot, (heartX, heartY))
