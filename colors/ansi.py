import collections.abc
import colorsys
import enum
import functools
import typing

from colors import RGBColor

class ANSI(enum.Enum):
    Normal_Black   = RGBColor(  0,   0,   0)
    Normal_Red     = RGBColor(128,   0,   0)
    Normal_Green   = RGBColor(  0, 128,   0)
    Normal_Yellow  = RGBColor(128, 128,   0)
    Normal_Blue    = RGBColor(  0,   0, 128)
    Normal_Magenta = RGBColor(128,   0, 128)
    Normal_Cyan    = RGBColor(  0, 128, 128)
    Normal_White   = RGBColor(192, 192, 192)

    Bright_Black   = RGBColor(128, 128, 128)
    Bright_Red     = RGBColor(255,   0,   0)
    Bright_Green   = RGBColor(  0, 255,   0)
    Bright_Yellow  = RGBColor(255, 255,   0)
    Bright_Blue    = RGBColor(  0,   0, 255)
    Bright_Magenta = RGBColor(255,   0, 255)
    Bright_Cyan    = RGBColor(  0, 255, 255)
    Bright_White   = RGBColor(255, 255, 255)
