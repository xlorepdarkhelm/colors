"""Contains the implementation of the Wikipedia list of colors."""
__all__ = (
    'Wiki',
)

import enum

from colors import base


class Wiki(base.ColorGroup):
    """
    The Wiki color group.

    The following is a list of colors. A number of the color swatches below are
taken from domain-specific naming schemes such as X11 or HTML4. RGB values are
given for each swatch because such standards are defined in terms of the sRGB
color space. It is not possible to accurately convert many of these swatches to
CMYK values because of the differing gamuts of the two spaces, but the color
management systems built into operating systems and image editing software
attempt such conversions as accurately as possible.

    See Also:
        Wikipedia:
        
        * `A-F <https://https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F`
        * `G-M <https://https://en.wikipedia.org/wiki/List_of_colors:_G%E2%80%93M`
        * `N-Z <https://https://en.wikipedia.org/wiki/List_of_colors:_N%E2%80%93Z`

    """

    AbsoluteZero       = base.RGBColor(246, 173, 198)
    Acajou             = base.RGBColor( 76,  47,  39)
    AcidGreen          = base.RGBColor(176, 191,  26)
    Aero               = base.RGBColor(124, 185, 232)
    AeroBlue           = base.RGBColor(201, 255, 229)
    AfricanViolet      = base.RGBColor(178, 132, 190)
    AirForceBlueRAF    = base.RGBColor( 93, 138, 168)
    AirForceBlueUSAF   = base.RGBColor(  0,  48, 143)
    AirSuperiorityBlue = base.RGBColor(114, 160, 193)
    AlabamaCrimson     = base.RGBColor(175,   0,  42)
    Alabaster          = base.RGBColor(242, 240, 230)
    AliceBlue          = base.RGBColor(240, 248, 255)
    AlienArmpit        = base.RGBColor(132, 222,   2)
    AlizarinCrimson	   = base.RGBColor(227,  38,  54)
