import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import guiTools as gui
import colors as clr

#Set default font
font = pygame.freetype.Font("assets/fonts/InconsolataNerdFontMono-Regular.ttf", 32)


#Define screen types with draw function
class ScreenType:
    def __init__(self, type: str):
        self.type = type

        if self.type == "title":

            self.paintexlTitle = gui.TextBlock(font, "PaintXel", 64, 450, 100)
            self.newImageButton = gui.Button(font, "New Image", 32, 450, 300)
            self.loadImageButton = gui.Button(font, "Load Image", 32, 450, 400)

        elif self.type == "new":
            #Left pannel icons
            self.drawButton = gui.Button(font, "", 32, 20, 20)
            self.eraseButton = gui.Button(font, "󰇾", 32, 20, 72)
            self.zoomInButton = gui.Button(font, "", 32, 20, 124)
            self.rotateRightButton = gui.Button(font, "", 32, 20, 176)
            self.rotateLeftButton = gui.Button(font, "", 32, 20, 228)
            self.saveButton = gui.Button(font, "󰆓", 32, 20, 280)
            #Quit button at bottom left corner
            self.quitButton = gui.Button(font, "", 32, 20, 705, foreground = clr.RED)
            #Color buttons
            self.blackButton = gui.ColorButton(clr.BLACK, 32, 72, 20)
            self.whiteButton = gui.ColorButton(clr.PASTEL_WHITE, 32, 72, 72)
            self.greyButton = gui.ColorButton(clr.PASTEL_GREY, 32, 72, 124)
            self.redButton = gui.ColorButton(clr.PASTEL_RED, 32, 72, 176)
            self.blueButton = gui.ColorButton(clr.PASTEL_BLUE, 32, 72, 228)
            self.greenButton = gui.ColorButton(clr.PASTEL_GREEN, 32, 72, 280)
            self.yellowButton = gui.ColorButton(clr.PASTEL_YELLOW, 32, 72, 332)
            self.pinkButton = gui.ColorButton(clr.PASTEL_PINK, 32, 72, 384)
            self.orangeButton = gui.ColorButton(clr.PASTEL_ORANGE, 32, 72, 436)
            self.purpleButton = gui.ColorButton(clr.PASTEL_PURPLE, 32, 72, 488)
            self.brownButton = gui.ColorButton(clr.PASTEL_BROWN, 32, 72, 540)

            self.actualColor = clr.BLACK
            self.drawing = False

            self.canvas = gui.Canvas(0, 105, 6, 120, 120)
            self.canvasIsDrawn = False



    def draw(self, window, cursor, click):
        if self.type == "title":
            #Print title
            self.paintexlTitle.draw(window)

            #New image button
            self.newImageButton.draw(window, cursor)
            
            #Load image button
            self.loadImageButton.draw(window, cursor)

            if click:
                if self.newImageButton.rect.collidepoint(cursor):
                    return "new"
                if self.loadImageButton.rect.collidepoint(cursor):
                    return "load"
            return "title"

        if self.type == "new":
            #Left pannel
            pygame.draw.rect(window, clr.BACKGROUND, (0, 0, 100, 725))

            #Draw button
            self.drawButton.draw(window, cursor)
            #Erase button
            self.eraseButton.draw(window, cursor)
            #Zoom in button
            self.zoomInButton.draw(window, cursor)
            #Rotate right button
            self.rotateRightButton.draw(window, cursor)
            #Rotate left button
            self.rotateLeftButton.draw(window, cursor)
            #Save button
            self.saveButton.draw(window, cursor)

            #Quit button
            self.quitButton.draw(window, cursor)

            #Colors
            self.whiteButton.draw(window, cursor)
            self.blackButton.draw(window, cursor)
            self.greyButton.draw(window, cursor)
            self.redButton.draw(window, cursor)
            self.greenButton.draw(window, cursor)
            self.blueButton.draw(window, cursor)
            self.purpleButton.draw(window, cursor)
            self.orangeButton.draw(window, cursor)
            self.yellowButton.draw(window, cursor)
            self.pinkButton.draw(window, cursor)
            self.brownButton.draw(window, cursor)

            #Canvas
            draw = self.drawing and click
            self.canvas.draw(window, cursor, draw, self.actualColor)

            if click:
                #Change color
                if self.whiteButton.rect.collidepoint(cursor):
                    self.actualColor = clr.PASTEL_WHITE
                if self.blackButton.rect.collidepoint(cursor):
                    self.actualColor = clr.BLACK
                if self.greyButton.rect.collidepoint(cursor):
                    self.actualColor = clr.PASTEL_GREY
                if self.redButton.rect.collidepoint(cursor):
                    self.actualColor = clr.PASTEL_RED
                if self.greenButton.rect.collidepoint(cursor):
                    self.actualColor = clr.PASTEL_GREEN
                if self.blueButton.rect.collidepoint(cursor):
                    self.actualColor = clr.PASTEL_BLUE
                if self.purpleButton.rect.collidepoint(cursor):
                    self.actualColor = clr.PASTEL_PURPLE
                if self.orangeButton.rect.collidepoint(cursor):
                    self.actualColor = clr.PASTEL_ORANGE
                if self.yellowButton.rect.collidepoint(cursor):
                    self.actualColor = clr.PASTEL_YELLOW
                if self.pinkButton.rect.collidepoint(cursor):
                    self.actualColor = clr.PASTEL_PINK
                if self.brownButton.rect.collidepoint(cursor):
                    self.actualColor = clr.PASTEL_BROWN

                #Draw
                if self.drawButton.rect.collidepoint(cursor):
                    self.drawing = True
                #Erase
                if self.eraseButton.rect.collidepoint(cursor):
                    self.drawing = True
                    self.actualColor = clr.WHITE
                    

            return "new"


        
            



