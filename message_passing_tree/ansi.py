def ansi_color(r, g, b):
    return "\033[38;2;" +";".join([str(r), str(g), str(b)]) + "m"

NOCOLOR = "\033[m"
RED = "\x1b[31m"
BLUE = ansi_color(100, 100, 255)
LIME_GREEN = ansi_color(30, 220, 30)
ORANGE = ansi_color(255, 165, 0)

INFO = BLUE
MISTAKE = RED
CORRECTION = LIME_GREEN
HIGHLIGHT = ORANGE

def info(s):
    return INFO + str(s) + NOCOLOR

def mistake(s):
    return MISTAKE + str(s) + NOCOLOR

def correction(s):
    return CORRECTION + str(s) + NOCOLOR

def highlight(s):
    return HIGHLIGHT + str(s) + NOCOLOR
