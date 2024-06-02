import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import guiTools as gui
import colors as clr
import language as lng

#Set default font
font = pygame.freetype.Font("assets/fonts/InconsolataNerdFontMono-Regular.ttf", 32)
#Set default language to English
lng.set_lang("EN")

#Define screen types with draw function
class ScreenType:
    def __init__(self, type: str):
        self.type = type


    def draw(self, window, cursor):
        if self.type == "title":
            #Print title
            paintexlTitle = gui.TextBlock(font, "PaintXel", 64, 400, 100, background = clr.BACKGROUND, foreground = clr.FOREGROUND)
            paintexlTitle.draw(window)

            #Load image button
            loadImgButton = gui.Button(font, "Load image", 32, 400, 300, background = clr.BACKGROUND, foreground = clr.FOREGROUND)
            loadImgButton.draw(window, cursor)

            #Settings button
            settingsButton = gui.Button(font, "Settings", 32, 400, 400, background = clr.BACKGROUND, foreground = clr.FOREGROUND)
            settingsButton.draw(window, cursor)



