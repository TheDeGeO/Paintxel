import contextlib
with contextlib.redirect_stdout(None):
    import pygame
import guiTools as gui
import colors as clr
import fileManager as fm

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

        elif self.type == "new" or self.type == "load":
            #Left pannel icons
            self.drawButton = gui.Button(font, "", 32, 20, 20)
            self.eraseButton = gui.Button(font, "󰇾", 32, 20, 72)
            self.zoomInButton = gui.Button(font, "", 32, 20, 124)
            self.rotateRightButton = gui.Button(font, "", 32, 20, 176)
            self.rotateLeftButton = gui.Button(font, "", 32, 20, 228)
            self.reflectVerticalButton = gui.Button(font, "󰨏", 32, 20, 280)
            self.reflectHorizontalButton = gui.Button(font, "󰨎", 32, 20, 332)
            self.saveButton = gui.Button(font, "󰆓", 32, 20, 384)
            self.reloadButton = gui.Button(font, "", 32, 20, 436)
            #Quit button at bottom left corner
            self.quitButton = gui.Button(font, "", 32, 20, 705, foreground = clr.PASTEL_RED)
            #Clear button on top of quit
            self.clearButton = gui.Button(font, "", 32, 20, 665, foreground = clr.PASTEL_RED)
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

            #Right pannel icons
            self.highContrastButton = gui.Button(font, "󰆗", 32, 880, 20, foreground = clr.PASTEL_YELLOW)
            self.negativeButton = gui.Button(font, "󰌁", 32, 880, 72, foreground = clr.PASTEL_YELLOW)
            self.asciiButton = gui.Button(font, "󱔁󰈈", 32, 880, 124, foreground = clr.PASTEL_YELLOW)
            self.saveASCIIButton = gui.Button(font, "󱔁", 32, 880, 176, foreground = clr.PASTEL_YELLOW)

            self.drawASCII = False
            self.surfaceASCII = None

            self.zommSurface = None
            self.zoom = False

            #Canvas
            self.actualColor = clr.BLACK
            self.drawing = False
            self.canvasIsDrawn = False

            if self.type == "new":
                self.canvas = gui.Canvas(0, 105, 6, 120, 120)

            elif self.type == "load":
                pixels = fm.loadFile(6)
                self.canvas = gui.Canvas(0, 105, 6, 120, 120, pixels=pixels)
        
    def draw(self, window, cursor, click, singleClick):
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
            return self.type

        if self.type == "new" or self.type == "load":
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
            #Reflect vertical button
            self.reflectVerticalButton.draw(window, cursor)
            #Reflect horizontal button
            self.reflectHorizontalButton.draw(window, cursor)
            #Save button
            self.saveButton.draw(window, cursor)
            #Reload button
            self.reloadButton.draw(window, cursor)

            #Clear button
            self.clearButton.draw(window, cursor)
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

            #Right pannel
            pygame.draw.rect(window, clr.BACKGROUND, (100, 0, 800, 725))
            #High contrast button
            self.highContrastButton.draw(window, cursor)
            #Negative button
            self.negativeButton.draw(window, cursor)
            #See ASCII button
            self.asciiButton.draw(window, cursor)
            #Save ASCII button
            self.saveASCIIButton.draw(window, cursor)

            #Canvas
            draw = self.drawing and click
            self.canvas.draw(window, cursor, draw, self.actualColor)

            if singleClick:
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

                #Draw
                if self.drawButton.rect.collidepoint(cursor):
                    self.drawing = True
                #Erase
                if self.eraseButton.rect.collidepoint(cursor):
                    self.drawing = True
                    self.actualColor = clr.WHITE

                #ROTATE LEFT
                if self.rotateLeftButton.rect.collidepoint(cursor):
                    self.canvas.rotate(False)
                
                #ROTATE RIGHT
                if self.rotateRightButton.rect.collidepoint(cursor):
                    self.canvas.rotate(True)
                
                #REFLECT VERTICAL
                if self.reflectVerticalButton.rect.collidepoint(cursor):
                    self.canvas.reflect(True)
                
                #REFLECT HORIZONTAL
                if self.reflectHorizontalButton.rect.collidepoint(cursor):
                    self.canvas.reflect(False)

                #SAVE
                if self.saveButton.rect.collidepoint(cursor):
                    numPixels = self.canvas.getNumericPixels()
                    fm.saveFile(numPixels)

                #RELOAD
                if self.reloadButton.rect.collidepoint(cursor):
                    self.canvas.reDraw()

                #CLEAR
                if self.clearButton.rect.collidepoint(cursor):
                    self.canvas.clear()                    
                #QUIT

                if self.quitButton.rect.collidepoint(cursor):
                    return "title"

                #HIGH CONTRAST
                if self.highContrastButton.rect.collidepoint(cursor):
                    newPixels = self.canvas.getHighContrastPixels()
                    self.canvas.pixels = newPixels
                    self.canvas.reDraw()

                #NEGATIVE
                if self.negativeButton.rect.collidepoint(cursor):
                    newPixels = self.canvas.getInversePixels()
                    self.canvas.pixels = newPixels
                    self.canvas.reDraw()

                #ASCII
                if self.asciiButton.rect.collidepoint(cursor):
                    newPixels = self.canvas.getASCIIpixels()
                    self.surfaceASCII = pygame.Surface((self.canvas.rect.width, self.canvas.rect.height))
                    charX = 0
                    charY = 0
                    for row in newPixels:
                        for char in row:
                            charSurface = font.render(char, bgcolor = clr.BLACK, fgcolor = clr.WHITE, size = self.canvas.pixel_size)[0]
                            self.surfaceASCII.blit(charSurface, (charX, charY))
                            charX += self.canvas.pixel_size
                        charX = 0
                        charY += self.canvas.pixel_size
                    self.drawASCII = True
                else:
                    self.drawASCII = False
                
                #SAVE ASCII
                if self.saveASCIIButton.rect.collidepoint(cursor):
                    matrixASCII = self.canvas.getASCIIpixels()
                    fm.saveFile(matrixASCII)
                
                #ZOOM
                if self.zoomInButton.rect.collidepoint(cursor):
                    self.zoom = True
                else:
                    self.zoom = False
                    
            
                    
            if self.drawASCII:
                window.blit(self.surfaceASCII, (100, 0))

            if self.zoom:
                self.zoomSurface = self.canvas.magnifyingGlass(cursor)
                window.blit(self.zoomSurface, (cursor))
                    
                    

            return self.type
