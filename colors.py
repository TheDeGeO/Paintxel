# Colors
PASTEL_PINK = (255, 192, 203)
PASTEL_ORANGE = (255, 165, 0)
PASTEL_PURPLE = (204, 153, 204)
PASTEL_RED = (255, 105, 105)
PASTEL_YELLOW = (255, 255, 153)
PASTEL_GREEN = (152, 255, 152)
PASTEL_BLUE = (173, 216, 230)
PASTEL_WHITE = (255, 255, 255)
PASTEL_GREY = (220, 220, 220)

GREY = (100, 100, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
PINK = (255, 192, 203)
BROWN = (165, 42, 42)

FOREGROUND = WHITE
BACKGROUND = GREY

BASE_brushColors = [BLACK, PASTEL_PINK, PASTEL_ORANGE, PASTEL_PURPLE, PASTEL_RED, PASTEL_YELLOW, PASTEL_GREEN, PASTEL_BLUE, PASTEL_WHITE, PASTEL_GREY]

#calculate color brightness using YIQ 
def getColorBrightness(color: tuple[int, int, int]) -> float:
    return color[0] * 0.299 + color[1] * 0.587 + color[2] * 0.114

#brush colors from brightest to darkest using list comprehension
brushColors = sorted(BASE_brushColors, key=getColorBrightness, reverse=True)
ACII_ART_SYMBOLS = [" ", ".", ":", "-", "=", "¡", "&", "$", "%", "@"]
assert len(ACII_ART_SYMBOLS) == len(brushColors), "brushColors and ACII_ART_SYMBOLS must be the same length"

def getInverseColor(color: tuple[int, int, int], colorList: list[tuple[int, int, int]]=brushColors) -> tuple[int, int, int]:
    if color not in colorList:
        raise ValueError("Color not listed")
    index = colorList.index(color)
    if index == 0:
        return colorList[-1]
    elif index == len(colorList) - 1:
        return colorList[0]
    return colorList[index * -1]

def getHighContrastColor(color: tuple[int, int, int], colorList: list[tuple[int, int, int]]=brushColors) -> tuple[int, int, int]:
    if color not in colorList:
        raise ValueError("Color not listed")
    index = colorList.index(color)
    midlength = len(colorList) // 2
    if index < midlength:
        return colorList[1]
    else:
        return colorList[-1]

def getColorNumber(color: tuple[int, int, int], colorList: list[tuple[int, int, int]]=brushColors) -> int:
    if color not in colorList:
        raise ValueError("Color not listed")
    index = colorList.index(color)
    return index

def getAsciiArtSymbol(color: tuple[int, int, int], colorList: list[tuple[int, int, int]]=brushColors) -> str:
    if color not in colorList:
        raise ValueError("Color not listed")
    index = colorList.index(color)
    return ACII_ART_SYMBOLS[index]

def getNumberColor(number: int, colorList: list[tuple[int, int, int]]=brushColors) -> tuple[int, int, int]:
    if number < 0 or number >= len(colorList):
        raise ValueError("Color number out of range")
    return colorList[number]