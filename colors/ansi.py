"""Contains the implementation of the ANSI color group."""
__all__ = (
    'ANSI',
)

import enum

from colors import base


class ANSI(base.ColorGroup):
    """
    The color group for ANSI escape sequences.

    The original specification for ANSI escape sequences had only 8 colors,
    and gave them names. Several terminals implemented "bold" colors as
    brighter colors rather than a different font, providing 8 additional
    foreground colors, however you usually could not get these as background
    colors (there was a trick that sometimes worked using inverse video
    codes).

    One of the fundamental problems with these colors is that different
    terminal emulators implement these as different RGB values.  As a result
    I have implemented this group to handle the values from multiple
    different terminals.

    See Also:
        `Wikipedia <https://en.wikipedia.org/wiki/ANSI_escape_code#Colors>`

    """

    VGA_Black   = base.sRGBColor(  0,   0,   0)
    VGA_Red     = base.sRGBColor(170,   0,   0)
    VGA_Green   = base.sRGBColor(  0, 170,   0)
    VGA_Yellow  = base.sRGBColor(170,  85,   0)
    VGA_Blue    = base.sRGBColor(  0,   0, 170)
    VGA_Magenta = base.sRGBColor(170,   0, 170)
    VGA_Cyan    = base.sRGBColor(  0, 170, 170)
    VGA_White   = base.sRGBColor(170, 170, 170)

    VGA_BrightBlack   = base.sRGBColor( 85,  85,  85)
    VGA_BrightRed     = base.sRGBColor(255,  85,  85)
    VGA_BrightGreen   = base.sRGBColor( 85, 255,  85)
    VGA_BrightYellow  = base.sRGBColor(255, 255,  85)
    VGA_BrightBlue    = base.sRGBColor( 85,  85, 255)
    VGA_BrightMagenta = base.sRGBColor(255,  85, 255)
    VGA_BrightCyan    = base.sRGBColor( 85, 255, 255)
    VGA_BrightWhite   = base.sRGBColor(255, 255, 255)

    CMD_Black   = base.sRGBColor(  0,   0,   0)
    CMD_Red     = base.sRGBColor(128,   0,   0)
    CMD_Green   = base.sRGBColor(  0, 128,   0)
    CMD_Yellow  = base.sRGBColor(128, 128,   0)
    CMD_Blue    = base.sRGBColor(  0,   0, 128)
    CMD_Magenta = base.sRGBColor(128,   0, 128)
    CMD_Cyan    = base.sRGBColor(  0, 128, 128)
    CMD_White   = base.sRGBColor(192, 192, 192)

    CMD_BrightBlack   = base.sRGBColor(128, 128, 128)
    CMD_BrightRed     = base.sRGBColor(255,   0,   0)
    CMD_BrightGreen   = base.sRGBColor(  0, 255,   0)
    CMD_BrightYellow  = base.sRGBColor(255, 255,   0)
    CMD_BrightBlue    = base.sRGBColor(  0,   0, 255)
    CMD_BrightMagenta = base.sRGBColor(255,   0, 255)
    CMD_BrightCyan    = base.sRGBColor(  0, 255, 255)
    CMD_BrightWhite   = base.sRGBColor(255, 255, 255)

    Terminal_app_Black   = base.sRGBColor(  0,   0,   0)
    Terminal_app_Red     = base.sRGBColor(194,  54,  33)
    Terminal_app_Green   = base.sRGBColor( 37, 188,  36)
    Terminal_app_Yellow  = base.sRGBColor(173, 173,  39)
    Terminal_app_Blue    = base.sRGBColor( 73,  46, 255)
    Terminal_app_Magenta = base.sRGBColor(211,  56, 211)
    Terminal_app_Cyan    = base.sRGBColor( 51, 187, 200)
    Terminal_app_White   = base.sRGBColor(203, 204, 205)

    Terminal_app_BrightBlack   = base.sRGBColor(129, 131, 131)
    Terminal_app_BrightRed     = base.sRGBColor(252,  57,  31)
    Terminal_app_BrightGreen   = base.sRGBColor( 49, 231,  34)
    Terminal_app_BrightYellow  = base.sRGBColor(234, 236,  35)
    Terminal_app_BrightBlue    = base.sRGBColor( 88,  51, 255)
    Terminal_app_BrightMagenta = base.sRGBColor(249,  53, 248)
    Terminal_app_BrightCyan    = base.sRGBColor( 20, 240, 240)
    Terminal_app_BrightWhite   = base.sRGBColor(233, 235, 235)

    PuTTY_Black   = base.sRGBColor(  0,   0,   0)
    PuTTY_Red     = base.sRGBColor(187,   0,   0)
    PuTTY_Green   = base.sRGBColor(  0, 187,   0)
    PuTTY_Yellow  = base.sRGBColor(187, 187,   0)
    PuTTY_Blue    = base.sRGBColor(  0,   0, 187)
    PuTTY_Magenta = base.sRGBColor(187,   0, 187)
    PuTTY_Cyan    = base.sRGBColor(  0, 187, 187)
    PuTTY_White   = base.sRGBColor(187, 187, 187)

    PuTTY_BrightBlack   = base.sRGBColor( 85,  85,  85)
    PuTTY_BrightRed     = base.sRGBColor(255,  85,  85)
    PuTTY_BrightGreen   = base.sRGBColor( 85, 255,  85)
    PuTTY_BrightYellow  = base.sRGBColor(255, 255,  85)
    PuTTY_BrightBlue    = base.sRGBColor( 85,  85, 255)
    PuTTY_BrightMagenta = base.sRGBColor(255,  85, 255)
    PuTTY_BrightCyan    = base.sRGBColor( 85, 255, 255)
    PuTTY_BrightWhite   = base.sRGBColor(255, 255, 255)

    mIRC_Black   = base.sRGBColor(  0,   0,   0)
    mIRC_Red     = base.sRGBColor(127,   0,   0)
    mIRC_Green   = base.sRGBColor(  0, 147,   0)
    mIRC_Yellow  = base.sRGBColor(252, 127,   0)
    mIRC_Blue    = base.sRGBColor(  0,   0, 127)
    mIRC_Magenta = base.sRGBColor(156,   0, 156)
    mIRC_Cyan    = base.sRGBColor(  0, 147, 147)
    mIRC_White   = base.sRGBColor(210, 210, 210)

    mIRC_BrightBlack   = base.sRGBColor(127, 127, 127)
    mIRC_BrightRed     = base.sRGBColor(255,   0,   0)
    mIRC_BrightGreen   = base.sRGBColor(  0, 255,   0)
    mIRC_BrightYellow  = base.sRGBColor(255, 255,   0)
    mIRC_BrightBlue    = base.sRGBColor(  0,   0, 255)
    mIRC_BrightMagenta = base.sRGBColor(255,   0, 255)
    mIRC_BrightCyan    = base.sRGBColor(  0, 255, 255)
    mIRC_BrightWhite   = base.sRGBColor(255, 255, 255)

    xterm_Black   = base.sRGBColor(  0,   0,   0)
    xterm_Red     = base.sRGBColor(205,   0,   0)
    xterm_Green   = base.sRGBColor(  0, 205,   0)
    xterm_Yellow  = base.sRGBColor(205, 205,   0)
    xterm_Blue    = base.sRGBColor(  0,   0, 238)
    xterm_Magenta = base.sRGBColor(205,   0, 205)
    xterm_Cyan    = base.sRGBColor(  0, 205, 205)
    xterm_White   = base.sRGBColor(229, 229, 229)

    xterm_BrightBlack   = base.sRGBColor(127, 127, 127)
    xterm_BrightRed     = base.sRGBColor(255,   0,   0)
    xterm_BrightGreen   = base.sRGBColor(  0, 255,   0)
    xterm_BrightYellow  = base.sRGBColor(255, 255,   0)
    xterm_BrightBlue    = base.sRGBColor( 92,  92, 255)
    xterm_BrightMagenta = base.sRGBColor(255,   0, 255)
    xterm_BrightCyan    = base.sRGBColor(  0, 255, 255)
    xterm_BrightWhite   = base.sRGBColor(255, 255, 255)

    X_Black   = base.sRGBColor(  0,   0,   0)
    X_Red     = base.sRGBColor(255,   0,   0)
    X_Green   = base.sRGBColor(  0, 255,   0)
    X_Yellow  = base.sRGBColor(255, 255,   0)
    X_Blue    = base.sRGBColor(  0,   0, 255)
    X_Magenta = base.sRGBColor(255,   0, 255)
    X_Cyan    = base.sRGBColor(  0, 255, 255)
    X_White   = base.sRGBColor(255, 255, 255)

    X_BrightBlack   = None
    X_BrightRed     = None
    X_BrightGreen   = base.sRGBColor(144, 238, 144)
    X_BrightYellow  = base.sRGBColor(255, 255, 224)
    X_BrightBlue    = base.sRGBColor(173, 216, 230)
    X_BrightMagenta = None
    X_BrightCyan    = base.sRGBColor(224, 255, 255)
    X_BrightWhite   = None
