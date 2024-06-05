# Define a set of colors
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

# Set the foreground and background colors
FOREGROUND = WHITE
BACKGROUND = GREY

# Define a list of base brush colors
BASE_brushColors = [BLACK, PASTEL_PINK, PASTEL_ORANGE, PASTEL_PURPLE, PASTEL_RED, PASTEL_YELLOW, PASTEL_GREEN, PASTEL_BLUE, PASTEL_WHITE, PASTEL_GREY]

# Calculate the brightness of a color using the YIQ formula
def getColorBrightness(color: tuple[int, int, int]) -> float:
    return color[0] * 0.299 + color[1] * 0.587 + color[2] * 0.114

# Sort the brush colors from brightest to darkest
brushColors = sorted(BASE_brushColors, key=getColorBrightness, reverse=True)

# Define a list of ASCII art symbols
ACII_ART_SYMBOLS = [" ", ".", ":", "-", "=", "¡", "&", "$", "%", "@"]
assert len(ACII_ART_SYMBOLS) == len(brushColors), "brushColors and ACII_ART_SYMBOLS must be the same length"

# Get the inverse color of a given color
def getInverseColor(color: tuple[int, int, int], colorList: list[tuple[int, int, int]]=brushColors) -> tuple[int, int, int]:
    if color not in colorList:
        raise ValueError("Color not listed")
    index = colorList.index(color)
    if index == 0:
        return colorList[-1]
    elif index == len(colorList) - 1:
        return colorList[0]
    return colorList[index * -1]

# Get the high contrast color of a given color
def getHighContrastColor(color: tuple[int, int, int], colorList: list[tuple[int, int, int]]=brushColors) -> tuple[int, int, int]:
    if color not in colorList:
        raise ValueError("Color not listed")
    index = colorList.index(color)
    midlength = len(colorList) // 2
    if index < midlength:
        return colorList[1]
    else:
        return colorList[-1]

# Get the number of a given color
def getColorNumber(color: tuple[int, int, int], colorList: list[tuple[int, int, int]]=brushColors) -> int:
    if color not in colorList:
        raise ValueError("Color not listed")
    index = colorList.index(color)
    return index

# Get the ASCII art symbol corresponding to a given color
def getAsciiArtSymbol(color: tuple[int, int, int], colorList: list[tuple[int, int, int]]=brushColors) -> str:
    if color not in colorList:
        raise ValueError("Color not listed")
    index = colorList.index(color)
    return ACII_ART_SYMBOLS[index]

# Get the color corresponding to a given number
def getNumberColor(number: int, colorList: list[tuple[int, int, int]]=brushColors) -> tuple[int, int, int]:
    if number < 0 or number >= len(colorList):
        raise ValueError("Color number out of range")
    return colorList[number]