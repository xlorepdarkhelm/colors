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
    AlizarinCrimson    = base.RGBColor(227,  38,  54)
    AlloyOrange        = base.RGBColor(196,  98,  16)
    Almond             = base.RGBColor(239, 222, 205)
    Amaranth           = base.RGBColor(229,  43,  80)
    AmaranthDeepPurple = base.RGBColor(159,  43, 104)
    AmaranthPink       = base.RGBColor(241, 156, 187)
    AmaranthPurple     = base.RGBColor(171,  39,  79)
    AmaranthRed        = base.RGBColor(211,  33,  45)
    Amazon             = base.RGBColor( 59, 122,  87)
    Amazonite          = base.RGBColor(  0, 196, 176)
    Amber              = base.RGBColor(255, 191,   0)
    AmberSAE           = base.RGBColor(255, 126,   0)
    AmberECE           = base.RGBColor(255, 126,   0)
    AmericanBlue       = base.RGBColor( 59,  59, 109)
    AmericanBrown      = base.RGBColor(128,  64,  64)
    AmericanGold       = base.RGBColor(211, 175,  55)
    AmericanGreen      = base.RGBColor( 52, 179,  52)
    AmericanOrange     = base.RGBColor(255, 139,   0)
    AmericanPink       = base.RGBColor(255, 152, 153)
    AmericanPurple     = base.RGBColor( 67,  28,  83)
