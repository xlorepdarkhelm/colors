"""Contains the implementation of the Wikipedia list of colors."""
__all__ = (
    'Crayola',
)

import enum

from colors import base


class Crayola(base.ColorGroup):
    """
    The Crayola color group.

    Since the introduction of Crayola drawing crayons by Binney & Smith in
    1903, more than two hundred distinctive colors have been produced in a
    wide variety of assortments. The table below represents all of the
    colors found in regular Crayola assortments from 1903 to the present.
    Since the introduction of fluorescent crayons in the 1970s, the
    standard colors have been complemented by a number of specialty crayon
    assortments, represented in subsequent tables.
    
    See Also:
        `Wikipedia <https://https://en.wikipedia.org/wiki/List_of_Crayola_crayon_colors>`

    """

    Red                   = base.RGBColor(237,  10,  63)
    DarkRed               = base.RGBColor(195,  33,  72)
    Maroon                = base.RGBColor(195,  33,  72)
    TorchRed              = base.RGBColor(253,  14,  53)
    Scarlet               = base.RGBColor(253,  14,  53)
    BrickRed              = base.RGBColor(198,  45,  66)
    EnglishVermilion      = base.RGBColor(204,  71,  75)
    EnglishVermillion     = base.RGBColor(204,  71,  75)
    MadderLake            = base.RGBColor(204,  51,  54)
    PermanentGeraniumLake = base.RGBColor(225,  44,  44)
    MaximumRed            = base.RGBColor(217,  33,  33)
    IndianRed             = base.RGBColor(185,  78,  72)
    Chestnut              = base.RGBColor(185,  78,  72)
    OrangeRed             = base.RGBColor(255,  63,  52)
    SunsetOrange          = base.RGBColor(254,  76,  64)
    Bittersweet           = base.RGBColor(254, 111,  94)
    DarkVenetianRed       = base.RGBColor(179,  59,  36)
    VenetianRed           = base.RGBColor(204,  85,  61)
    LightVenetianRed      = base.RGBColor(230, 115,  92)
    VividTangerine        = base.RGBColor(255, 153, 128)
    MiddleRed             = base.RGBColor(229, 144, 115)
    BurntOrange           = base.RGBColor(255, 112,  52)
    RedOrange             = base.RGBColor(255, 104,  31)
    Orange                = base.RGBColor(255, 136, 100)
    MacaroniAndCheese     = base.RGBColor(255, 185, 123)
    MiddleYellowRed       = base.RGBColor(236, 177, 118)
    MediumOrange          = base.RGBColor(236, 177, 118)
    MangoTango            = base.RGBColor(231, 114,   0)
    YellowOrange          = base.RGBColor(255, 174,  66)
    MaximumYellowRed      = base.RGBColor(242, 186,  73)
    BananaMania           = base.RGBColor(251, 231, 178)
    Maize                 = base.RGBColor(242, 198,  73)
    GoldOchre             = base.RGBColor(242, 198,  73)
    GoldenOchre           = base.RGBColor(242, 198,  73)
    OrangeYellow          = base.RGBColor(248, 213, 104)
    Goldenrod             = base.RGBColor(252, 214, 103)
    MediumChromeYellow    = base.RGBColor(252, 214, 103)
    MediumYellow          = base.RGBColor(252, 214, 103)
