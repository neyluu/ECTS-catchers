import pygame as pg


class Button:
    def __init__(self, x, y, width, height, texturePath,
                 text='Button', rotationAngle=0,
                 fontPath=None, fontSize=30, textColor=(255, 255, 255),
                 outlineColor=(0, 0, 0), outlineThickness=2,
                 hoverEffectColor=(255, 255, 255, 50),
                 action=None):

        self.xPosition = x
        self.yPosition = y
        self.buttonWidth = width
        self.buttonHeight = height
        self.texturePath = texturePath
        self.text = text
        self.rotationAngle = rotationAngle
        self.fontPath = fontPath
        self.fontSize = fontSize
        self.textColor = textColor
        self.outlineColor = outlineColor
        self.outlineThickness = outlineThickness
        self.hoverEffectColor = hoverEffectColor
        self.action = action

        self.isHovered = False

        if not pg.font.get_init():
            pg.font.init()

        if self.fontPath:
            self.font = pg.font.Font(self.fontPath, self.fontSize)
        else:
            self.font = pg.font.Font(None, self.fontSize)

        originalBaseImage = pg.image.load(self.texturePath).convert_alpha()
        self.baseScaledImage = pg.transform.scale(originalBaseImage, (self.buttonWidth, self.buttonHeight))

        self.texture = None
        self.rect = pg.Rect(x, y, 0, 0)
        self.mask = None

        self._rebuildTexture()

        if self.hoverEffectColor and len(self.hoverEffectColor) == 4 and self.hoverEffectColor[3] > 0:
            self.hoverSurface = pg.Surface(self.rect.size, pg.SRCALPHA)
            self.hoverSurface.fill(self.hoverEffectColor)
        else:
            self.hoverSurface = None


    def _rebuildTexture(self):
        imageToTransform = self.baseScaledImage.copy()

        if self.text and self.font:
            mainTextSurf = self.font.render(self.text, True, self.textColor)
            textRenderRect = mainTextSurf.get_rect(center=imageToTransform.get_rect().center)

            if self.outlineThickness > 0 and self.outlineColor:
                for dxOutline in range(-self.outlineThickness, self.outlineThickness + 1):
                    for dyOutline in range(-self.outlineThickness, self.outlineThickness + 1):
                        if dxOutline == 0 and dyOutline == 0:
                            continue
                        outlineSurf = self.font.render(self.text, True, self.outlineColor)
                        imageToTransform.blit(outlineSurf, (textRenderRect.x + dxOutline, textRenderRect.y + dyOutline))

            imageToTransform.blit(mainTextSurf, textRenderRect)

        self.texture = pg.transform.rotate(imageToTransform, self.rotationAngle)

        originalCenterX = self.xPosition + self.buttonWidth / 2
        originalCenterY = self.yPosition + self.buttonHeight / 2
        self.rect = self.texture.get_rect(center=(originalCenterX, originalCenterY))

        self.mask = pg.mask.from_surface(self.texture)


    def _checkCollision(self, pos):
        if self.rect.collidepoint(pos):
            local_x = pos[0] - self.rect.x
            local_y = pos[1] - self.rect.y
            if 0 <= local_x < self.mask.get_size()[0] and \
                    0 <= local_y < self.mask.get_size()[1]:
                if self.mask.get_at((local_x, local_y)):
                    return True
        return False


    def draw(self, screen: pg.Surface):
        screen.blit(self.texture, self.rect.topleft)

        if self.isHovered and self.hoverSurface:
            screen.blit(self.hoverSurface, self.rect.topleft)


    def handleEvent(self, event: pg.event.Event):
        if event.type == pg.MOUSEMOTION:
            self.isHovered = self._checkCollision(event.pos)
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1 and self._checkCollision(event.pos):
                if self.action:
                    self.action()
