import curses
from enum import IntEnum
import time


class Color(IntEnum):
    BLACK = 1
    BLUE = 2
    CYAN = 3
    GREEN = 4
    MAGENTA = 5
    RED = 6
    WHITE = 7
    YELLOW = 8


def init_curses():
    curses.start_color()
    curses.init_pair(Color.BLACK, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(Color.BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(Color.CYAN, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(Color.GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(Color.MAGENTA, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(Color.RED, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(Color.WHITE, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(Color.YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.curs_set(0)


def visualize(f, input):
    def wrapped(window):
        init_curses()
        result = f(input, window)
        time.sleep(2)
        return result

    return curses.wrapper(wrapped)
