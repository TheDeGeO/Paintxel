import contextlib
with contextlib.redirect_stdout(None):
    import pygame

pygame.init()

import colors as clr

class TextBlock:
    def __init__(self, font: pygame.freetype.Font, text: str, size: int, x: int, y: int, margin: int=10,
                 background: tuple[int, int, int]=clr.BACKGROUND, 
                 foreground: tuple[int, int, int]=clr.FOREGROUND):

        self.font = font
        self.text = text
        self.size = size
        self.x = x
        self.y = y
        self.margin = margin
        self.background = background
        self.foreground = foreground

        textSurface, textRect = self.font.render(self.text, self.foreground, self.background, size = self.size)

        blockSurface = pygame.Surface((textRect.width + 2 * self.margin, textRect.height + 2 * self.margin))
        blockRect = blockSurface.get_rect(center = (self.x, self.y))
        blockSurface.fill(self.background)
        blockSurface.blit(textSurface, (self.margin, self.margin))

        self.surface = blockSurface
        self.rect = blockRect

    def draw(self, window):
        window.blit(self.surface, self.rect)

class Button:
    def __init__(self, font: pygame.freetype.Font, text: str, size: int, x: int, y: int, margin: int=10,
                 background: tuple[int, int, int]=clr.BACKGROUND, 
                 foreground: tuple[int, int, int]=clr.FOREGROUND):

        self.font = font
        self.text = text
        self.size = size
        self.x = x
        self.y = y
        self.margin = margin
        self.background = background
        self.foreground = foreground

        normalButton = TextBlock(self.font, self.text, self.size, self.x, self.y, self.margin, self.background, self.foreground)
        darkBackground = (max(0, self.background[0] - 20), max(0, self.background[1] - 20), max(0, self.background[2] - 20))
        darkButton = TextBlock(self.font, self.text, self.size, self.x, self.y, self.margin, darkBackground, self.foreground)

        self.surface = normalButton.surface
        self.surfaceDark = darkButton.surface
        self.rect = normalButton.rect

    def draw(self, window, cursor):
        if self.rect.collidepoint(cursor):
            window.blit(self.surfaceDark, self.rect)
        else:
            window.blit(self.surface, self.rect)