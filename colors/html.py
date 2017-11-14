"""Contains the implementation of the HTML color group."""
__all__ = (
    'HTML',
)

import enum

from colors import base


class HTML(base.ColorGroup):
    """
    The color group for HTML 4.01 approved colors.

    These are the colors as defined in the HTML 4.01 specification from 1999.

    See Also:
        `Wikipedia <https://en.wikipedia.org/wiki/Web_colors#HTML_color_names>`

    """

    White   = base.sRGBColor(255, 255, 255)
    Silver  = base.sRGBColor(192, 192, 192)
    Gray    = base.sRGBColor(128, 128, 128)
    Black   = base.sRGBColor(  0,   0,   0)
    Red     = base.sRGBColor(255,   0,   0)
    Maroon  = base.sRGBColor(128,   0,   0)
    Yellow  = base.sRGBColor(255, 255,   0)
    Olive   = base.sRGBColor(128, 128,   0)
    Lime    = base.sRGBColor(  0, 255,   0)
    Green   = base.sRGBColor(  0, 128,   0)
    Aqua    = base.sRGBColor(  0, 255, 255)
    Teal    = base.sRGBColor(  0, 128, 128)
    Blue    = base.sRGBColor(  0,   0, 255)
    Navy    = base.sRGBColor(  0,   0, 128)
    Fuchsia = base.sRGBColor(255,   0, 255)
    Purple  = base.sRGBColor(128,   0, 128)
