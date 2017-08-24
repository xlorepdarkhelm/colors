"""Contains the implementation of the HTML color group."""
__all__ = (
    'HTML',
)

import enum

from colors import base


class Web(base.ColorGroup):
    """
    The color group for HTML 4.01 approved colors.

    These are the colors as defined in the HTML 4.01 specification from 1999.

    See Also:
        `Wikipedia <https://en.wikipedia.org/wiki/Web_colors#HTML_color_names>'

    """

    White   = base.RGBColor(255, 255, 255)
    Silver  = base.RGBColor(192, 192, 192)
    Gray    = base.RGBColor(128, 128, 128)
    Black   = base.RGBColor(  0,   0,   0)
    Red     = base.RGBColor(255,   0,   0)
    Maroon  = base.RGBColor(128,   0,   0)
    Yellow  = base.RGBColor(255, 255,   0)
    Olive   = base.RGBColor(128, 128,   0)
    Lime    = base.RGBColor(  0, 255,   0)
    Green   = base.RGBColor(  0, 128,   0)
    Aqua    = base.RGBColor(  0, 255, 255)
    Teal    = base.RGBColor(  0, 128, 128)
    Blue    = base.RGBColor(  0,   0, 255)
    Navy    = base.RGBColor(  0,   0, 128)
    Fuchsia = base.RGBColor(255,   0, 255)
    Purple  = base.RGBColor(128,   0, 128)
