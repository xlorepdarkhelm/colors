import enum

from colors import base

class ANSI(enum.Enum, metaclass=base.ColorEnumMeta):
    Normal_Black   = base.RGBColor(  0,   0,   0)
    Normal_Red     = base.RGBColor(128,   0,   0)
    Normal_Green   = base.RGBColor(  0, 128,   0)
    Normal_Yellow  = base.RGBColor(128, 128,   0)
    Normal_Blue    = base.RGBColor(  0,   0, 128)
    Normal_Magenta = base.RGBColor(128,   0, 128)
    Normal_Cyan    = base.RGBColor(  0, 128, 128)
    Normal_White   = base.RGBColor(192, 192, 192)

    Bright_Black   = base.RGBColor(128, 128, 128)
    Bright_Red     = base.RGBColor(255,   0,   0)
    Bright_Green   = base.RGBColor(  0, 255,   0)
    Bright_Yellow  = base.RGBColor(255, 255,   0)
    Bright_Blue    = base.RGBColor(  0,   0, 255)
    Bright_Magenta = base.RGBColor(255,   0, 255)
    Bright_Cyan    = base.RGBColor(  0, 255, 255)
    Bright_White   = base.RGBColor(255, 255, 255)
