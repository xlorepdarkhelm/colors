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
        Wikipedia List of Colors
        
        * `https://https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F`
        * `https://https://en.wikipedia.org/wiki/List_of_colors:_G%E2%80%93M`
        * `https://https://en.wikipedia.org/wiki/List_of_colors:_N%E2%80%93Z`

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
    AmericanRed        = base.RGBColor(179,  33,  52)
    AmericanRose       = base.RGBColor(255,   3,  62)
    AmericanSilver     = base.RGBColor(207, 207, 207)
    AmericanViolet     = base.RGBColor( 85,  27, 140)
    AmericanYellow     = base.RGBColor(242, 180,   0)
    Amethyst           = base.RGBColor(153, 102, 204)
    AndroidGreen       = base.RGBColor(164, 198,  57)
    AntiFlashWhite     = base.RGBColor(242, 243, 244)
    AntiqueBrass       = base.RGBColor(205, 149, 117)
    AntiqueBronze      = base.RGBColor(102,  93,  30)
    AntiqueFuchsia     = base.RGBColor(145,  92, 131)
    AntiqueRuby        = base.RGBColor(132,  27,  45)
    AntiqueWhite       = base.RGBColor(250, 235, 215)
    AoEnglish          = base.RGBColor(  0, 128,   0)
    Apple              = base.RGBColor(102, 180,  71)
    AppleGreen         = base.RGBColor(141, 182,   0)
    Apricot            = base.RGBColor(251, 206, 177)
    Aqua               = base.RGBColor(  0, 255, 255)
    Aquamarine         = base.RGBColor(127, 255, 212)
    ArmyGreen          = base.RGBColor( 75,  83,  32)
    Arsenic            = base.RGBColor( 59,  68,  75)
    Artichoke          = base.RGBColor(143, 151, 121)
    ArylideYellow      = base.RGBColor(233, 214, 107)
    AshGray            = base.RGBColor(178, 190, 181)
    Asparagus          = base.RGBColor(135, 169, 107)
    AteneoBlue         = base.RGBColor(  0,  58, 108)
    AtomicTangerine    = base.RGBColor(255, 153, 102)
    Auburn             = base.RGBColor(165,  42,  42)
    Aureolin           = base.RGBColor(253, 238,   0)
    AuroMetalSaurus    = base.RGBColor(110, 127, 128)
    Avocado            = base.RGBColor( 86, 130,   3)
    Awesome            = base.RGBColor(255,  32,  82)
    Axolotl            = base.RGBColor( 99, 119,  91)
    AztecGold          = base.RGBColor(195, 153,  83)
    Azure              = base.RGBColor(  0, 127, 255)
    AzureWebColor      = base.RGBColor(240, 255, 255)
    AzureMist          = base.RGBColor(240, 255, 255)
    AzureishWhite      = base.RGBColor(219, 233, 244)

    BabyBlue           = base.RGBColor(137, 207, 240)
    BabyBlueEyes       = base.RGBColor(161, 202, 241)
    BabyPink           = base.RGBColor(244, 194, 194)
    BabyPowder         = base.RGBColor(254, 254, 250)
    BakerMillerPink    = base.RGBColor(255, 145, 175)
    BallBlue           = base.RGBColor( 33, 171, 205)
    BananaMania        = base.RGBColor(250, 231, 181)
    BananaYellow       = base.RGBColor(255, 225,  53)
    BangladeshGreen    = base.RGBColor(  0, 106,  78)
    BarbiePink         = base.RGBColor(224,  33, 138)
    BarnRed            = base.RGBColor(124,  10,   2)
    BatteryChargedBlue = base.RGBColor( 29, 172, 214)
    BattleshipGrey     = base.RGBColor(132, 132, 130)
    Bazaar             = base.RGBColor(152, 119, 123)
    BeauBlue           = base.RGBColor(188, 212, 230)
    Beaver             = base.RGBColor(159, 129, 112)
    Begonia            = base.RGBColor(250, 110, 121)
    Beige              = base.RGBColor(245, 245, 220)
    BdazzledBlue       = base.RGBColor( 46,  88, 148)
    BigDipORuby        = base.RGBColor(156,  37,  66)
