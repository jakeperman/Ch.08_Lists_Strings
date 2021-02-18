import random
import time
weapon = "weapon"
consumable = "consumable"
junk = "junk"
material = "material"
any_item = "any"
hostile = "hostile"
passive = "passive"
# Creature Class

# Color class
class Color:
    # standard colors
    black = '\u001b[30m'
    red = '\u001b[31m'
    green = '\u001b[32m'
    yellow = '\u001b[93m'
    blue = '\u001b[34m'
    magenta = '\u001b[35m'
    cyan = '\u001b[36m'
    white = '\u001b[37m'
    reset = '\u001b[0m'
    # bold colors
    bold_black = '\u001b[30;1m'
    bold_red = '\u001b[31;1m'
    bold_green = '\u001b[32;1m'
    bold_yellow = '\u001b[33;1m'
    bold_blue = '\u001b[34;1m'
    bold_magenta = '\u001b[35;1m'
    bold_cyan = '\u001b[36;1m'
    bold_white = '\u001b[37;1m'

    # bright colors
    bright_black = '\u001b[90;1m'
    bright_red = '\u001b[91;1m'
    bright_green = '\u001b[92;1m'
    bright_yellow = '\u001b[93;1m'
    bright_blue = '\u001b[94;1m'
    bright_magenta = '\u001b[95;1m'
    bright_cyan = '\u001b[96;1m'
    bright_white = '\u001b[97;1m'

    # standard background colors
    background_black = '\u001b[40m'
    background_red = '\u001b[41m'
    background_green = '\u001b[42m'
    background_yellow = '\u001b[43m'
    background_blue = '\u001b[44m'
    background_magenta = '\u001b[45m'
    background_cyan = '\u001b[46m'
    background_white = '\u001b[47m'

    # decorative
    bold = '\u001b[1m'
    underline = '\u001b[4m'
    reversed = '\u001b[7m'

color = Color


# creates text border to break up dialogue
def border(leng, colour=""):
    # if argument 'leng' is int, set border length equal to it
    if isinstance(leng, int):
        length = leng
    # if argument 'leng' is a string, get the len() and set border length equal to that
    elif isinstance(leng, str):
        length = len(leng)
    else:
        length = 0
    # if color is specified and is of the class 'Color', set argument to that color
    if colour != "":
        col = colour
    # set color to white if no argument, or non-color argument, is specified
    else:
        col = color.reset
    for i in range(0, length+1):
        print(col + '-', end='')
    print('', end='\n')



