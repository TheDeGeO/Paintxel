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

class ImageBlock:
    def __init__(self, img: pygame.Surface, size: int, x: int, y: int, margin: int=10, background: tuple[int, int, int]=clr.BACKGROUND):

        self.img = pygame.transform.scale(img, (size, size))
        self.size = size
        self.x = x
        self.y = y
        self.margin = margin
        self.background = background

        blockSurface = pygame.Surface((self.size + 2 * self.margin, self.size + 2 * self.margin))
        blockRect = blockSurface.get_rect(center = (self.x, self.y))
        blockSurface.fill(self.background)
        blockSurface.blit(self.img, (self.margin, self.margin))

        self.surface = blockSurface
        self.rect = blockRect

    def draw(self, window):
        window.blit(self.surface, self.rect)

class ImageButton:
    def __init__(self, img: pygame.Surface, size: int, x: int, y: int, margin: int=10,
                 background: tuple[int, int, int]=clr.BACKGROUND,):

        self.img = pygame.transform.scale(img, (size, size))
        self.size = size
        self.x = x
        self.y = y
        self.margin = margin
        self.background = background

        normalButton = ImageBlock(self.img, self.size, self.x, self.y, self.margin)
        darkBackground = (max(0, self.background[0] - 20), max(0, self.background[1] - 20), max(0, self.background[2] - 20))
        darkButton = ImageBlock(self.img, self.size, self.x, self.y, self.margin, darkBackground)

        self.surface = normalButton.surface
        self.surfaceDark = darkButton.surface
        self.rect = normalButton.rect
        
    def draw(self, window, cursor):
        if self.rect.collidepoint(cursor):
            window.blit(self.surfaceDark, self.rect)
        else:
            window.blit(self.surface, self.rect)

class ColorButton:
    def __init__(self, color: tuple[int, int, int], size: int, x: int, y: int, margin: int=10):

        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.margin = margin

        colorSurface = pygame.Surface((self.size, self.size))
        colorSurface.fill(self.color)

        colorButton = ImageButton(colorSurface, self.size, self.x, self.y, self.margin)

        self.surface = colorButton.surface
        self.surfaceDark = colorButton.surfaceDark
        self.rect = colorButton.rect

    def draw(self, window, cursor):
        if self.rect.collidepoint(cursor):
            window.blit(self.surfaceDark, self.rect)
        else:
            window.blit(self.surface, self.rect)

class ColorBlock:
    def __init__(self, color: tuple[int, int, int], size: int, x: int, y: int, margin: int=10):

        self.color = color
        self.size = size
        self.x = x
        self.y = y
        self.margin = margin

        colorSurface = pygame.Surface((self.size, self.size))
        colorSurface.fill(self.color)

        colorBlock = ImageBlock(colorSurface, self.size, self.x, self.y, self.margin)

        self.surface = colorBlock.surface
        self.rect = colorBlock.rect

    def draw(self, window):
        window.blit(self.surface, self.rect)

#Pixel art canvas composed of (wxh) pixels. Pixels are represented with colorButtons
class Canvas:
    def __init__(self, top: int, left: int, pixel_size: int, width: int, height: int, background: tuple[int, int, int]=clr.BACKGROUND):
        self.top = top
        self.left = left
        self.pixel_size = pixel_size
        self.width = width
        self.height = height
        self.background = background

        self.surface = pygame.Surface((width * pixel_size + 2 * self.pixel_size, height * pixel_size + 2 * self.pixel_size))
        self.surface.fill(self.background)
        self.rect = self.surface.get_rect(topleft=(left, top))

        self.pixels = []
        for i in range(height):
            self.pixels.append([])
            for j in range(width):
                pixel_x = j * pixel_size + self.pixel_size
                pixel_y = i * pixel_size + self.pixel_size
                self.pixels[i].append(ColorBlock(clr.WHITE, pixel_size, pixel_x, pixel_y, 1))
                self.surface.blit(self.pixels[i][j].surface, self.pixels[i][j].rect)

    def draw(self, window, cursor, click, color):
        window.blit(self.surface, self.rect)

        if click:
            cursor = (cursor[0] - self.rect.left, cursor[1] - self.rect.top)
            for row in self.pixels:
                for pixel in row:
                    if pixel.rect.collidepoint(cursor):
                        pixel.surface.fill(color)
                        self.surface.blit(pixel.surface, pixel.rect)
    
    def getPixels(self):
        return self.pixels