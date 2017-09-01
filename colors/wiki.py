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
    RoyalAirForceBlue  = base.RGBColor( 93, 138, 168)
    USAirForceBlue     = base.RGBColor(  0,  48, 143)
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
    SAEAmber           = base.RGBColor(255, 126,   0)
    ECEAmber           = base.RGBColor(255, 126,   0)
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
    EnglishAo          = base.RGBColor(  0, 128,   0)
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
    WebAzure           = base.RGBColor(240, 255, 255)
    AzureMist          = base.RGBColor(240, 255, 255)
    AzureishWhite      = base.RGBColor(219, 233, 244)

    BabyBlue            = base.RGBColor(137, 207, 240)
    BabyBlueEyes        = base.RGBColor(161, 202, 241)
    BabyPink            = base.RGBColor(244, 194, 194)
    BabyPowder          = base.RGBColor(254, 254, 250)
    BakerMillerPink     = base.RGBColor(255, 145, 175)
    BallBlue            = base.RGBColor( 33, 171, 205)
    BananaMania         = base.RGBColor(250, 231, 181)
    BananaYellow        = base.RGBColor(255, 225,  53)
    BangladeshGreen     = base.RGBColor(  0, 106,  78)
    BarbiePink          = base.RGBColor(224,  33, 138)
    BarnRed             = base.RGBColor(124,  10,   2)
    BatteryChargedBlue  = base.RGBColor( 29, 172, 214)
    BattleshipGrey      = base.RGBColor(132, 132, 130)
    Bazaar              = base.RGBColor(152, 119, 123)
    BeauBlue            = base.RGBColor(188, 212, 230)
    Beaver              = base.RGBColor(159, 129, 112)
    Begonia             = base.RGBColor(250, 110, 121)
    Beige               = base.RGBColor(245, 245, 220)
    BdazzledBlue        = base.RGBColor( 46,  88, 148)
    BigDipORuby         = base.RGBColor(156,  37,  66)
    BigFootFeet         = base.RGBColor(232, 142,  90)
    Bisque              = base.RGBColor(255, 228, 196)
    Bistre              = base.RGBColor( 61,  43,  31)
    BistreBrown         = base.RGBColor(150, 113,  23)
    BitterLemon         = base.RGBColor(202, 224,  13)
    BitterLime          = base.RGBColor(191, 255,   0)
    Bittersweet         = base.RGBColor(254, 111,  94)
    BittersweetShimmer  = base.RGBColor(191,  79,  81)
    Black               = base.RGBColor(  0,   0,   0)
    BlackBean           = base.RGBColor( 61,  12,   2)
    BlackChocolate      = base.RGBColor( 27,  24,  17)
    BlackCoffee         = base.RGBColor( 59,  47,  47)
    BlackCoral          = base.RGBColor( 84,  98, 111)
    BlackLeatherJacket  = base.RGBColor( 37,  53,  41)
    BlackOlive          = base.RGBColor( 59,  60,  54)
    Blackberry          = base.RGBColor(143,  89, 115)
    BlackShadows        = base.RGBColor(191, 175, 178)
    BlanchedAlmond      = base.RGBColor(255, 235, 205)
    BlastOffBronze      = base.RGBColor(165, 113, 100)
    BleuDeFrance        = base.RGBColor( 49, 140, 231)
    BlizzardBlue        = base.RGBColor(172, 229, 238)
    Blond               = base.RGBColor(250, 240, 190)
    BloodOrange         = base.RGBColor(209,   0,  28)
    BloodRed            = base.RGBColor(102,   0,   0)
    Blue                = base.RGBColor(  0,   0, 255)
    CrayolaBlue         = base.RGBColor( 31, 117, 254)
    MunsellBlue         = base.RGBColor(  0, 147, 175)
    NCSBlue             = base.RGBColor(  0, 135, 189)
    PantoneBlue         = base.RGBColor(  0,  24, 168)
    PigmentBlue         = base.RGBColor( 51,  51, 153)
    RYBBlue             = base.RGBColor(  2,  71, 254)
    BlueBell            = base.RGBColor(162, 162, 208)
    BlueBolt            = base.RGBColor(  0, 185, 251)
    BlueGray            = base.RGBColor(102, 153, 204)
    BlueGreen           = base.RGBColor( 13, 152, 186)
    BlueJeans           = base.RGBColor( 93, 173, 236)
    BlueLagoon          = base.RGBColor(172, 229, 238)
    BlueMagentaViolet   = base.RGBColor( 85,  53, 146)
    BlueSapphire        = base.RGBColor( 18,  97, 128)
    BlueViolet          = base.RGBColor(138,  43, 226)
    BlueYonder          = base.RGBColor( 80, 114, 167)
    Blueberry           = base.RGBColor( 79, 134, 247)
    Bluebonnet          = base.RGBColor( 28,  28, 240)
    Blush               = base.RGBColor(222,  93, 131)
    Bole                = base.RGBColor(121,  68,  59)
    BondiBlue           = base.RGBColor(  0, 149, 182)
    Bone                = base.RGBColor(227, 218, 201)
    BoogerBuster        = base.RGBColor(221, 226, 106)
    BostonUniversityRed = base.RGBColor(204,   0,   0)
    BottleGreen         = base.RGBColor(  0, 106,  78)
    Boysenberry         = base.RGBColor(135,  50,  96)
    BrandeisBlue        = base.RGBColor(  0, 112, 255)
    Brass               = base.RGBColor(181, 166,  66)
    BrickRed            = base.RGBColor(203,  65,  84)
    BrightCerulean      = base.RGBColor( 29, 172, 214)
    BrightGray          = base.RGBColor(235, 236, 240)
    BrightGreen         = base.RGBColor(102, 255,   0)
    BrightLavender      = base.RGBColor(191, 148, 228)
    BrightLilac         = base.RGBColor(216, 145, 239)
    BrightMaroon        = base.RGBColor(195,  33,  72)
    BrightNavyBlue      = base.RGBColor( 25, 116, 210)
    BrightPink          = base.RGBColor(255,   0, 127)
    BrightTurquoise     = base.RGBColor(  8, 232, 222)
    BrightUbe           = base.RGBColor(209, 159, 232)
    CrayolaBrightYellow = base.RGBColor(255, 170,  29)
    BrilliantAzure      = base.RGBColor( 51, 153, 255)
    BrilliantLavender   = base.RGBColor(244, 187, 255)
    BrilliantRose       = base.RGBColor(244, 187, 255)
    BrinkPink           = base.RGBColor(251,  96, 127)
    BritishRacingGreen  = base.RGBColor(  0,  66,  37)
    Bronze              = base.RGBColor(136,  84,  11)
    Bronze2             = base.RGBColor(205, 127,  50)
    MetallicBronze      = base.RGBColor(176, 141,  87)
    BronzeYellow        = base.RGBColor(115, 112,   0)
    Brown               = base.RGBColor(153,  51,   0)
    CrayolaBrown        = base.RGBColor(175,  89,  62)
    TraditionalBrown    = base.RGBColor(150,  75,   0)
    WebBrown            = base.RGBColor(165,  42,  42)
    BrownNose           = base.RGBColor(107,  68,  35)
    BrownSugar          = base.RGBColor(175, 110,  77)
    BrownChocolate      = base.RGBColor( 95,  25,  51)
    BrownCoffee         = base.RGBColor( 74,  44,  42)
    BrownYellow         = base.RGBColor(204, 153, 102)
    BrunswickGreen      = base.RGBColor(204, 153, 102)
    BubbleGum           = base.RGBColor(255, 193, 204)
    Bubbles             = base.RGBColor(231, 254, 255)
    BudGreen            = base.RGBColor(123, 182,  97)
    Buff                = base.RGBColor(240, 220, 130)
    BulgarianRose       = base.RGBColor( 72,   6,   7)
    Burgundy            = base.RGBColor(128,   0,  32)
    Burlywood           = base.RGBColor(222, 184, 135)
    BurnishedBrown      = base.RGBColor(161, 122, 116)
    BurntOrange         = base.RGBColor(204,  85,   0)
    BurntSienna         = base.RGBColor(233, 116,  81)
    BurntUmber          = base.RGBColor(138,  51,  36)
    ButtonBlue          = base.RGBColor( 36, 160, 237)
    Byzantine           = base.RGBColor(189,  51, 164)
    Byzantium           = base.RGBColor(112,  41,  99)

    Cadet                 = base.RGBColor( 83, 104, 114)
    CadetBlue             = base.RGBColor( 95, 158, 160)
    CadetGrey             = base.RGBColor(145, 163, 176)
    CadmiumBlue           = base.RGBColor( 10,  17, 149)
    CadmiumGreen          = base.RGBColor(  0, 107,  60)
    CadmiumOrange         = base.RGBColor(237, 135,  45)
    CadmiumPurple         = base.RGBColor(182,  12,  38)
    CadmiumRed            = base.RGBColor(227,   0,  34)
    CadmiumYellow         = base.RGBColor(255, 246,   0)
    CadmiumViolet         = base.RGBColor(127,  62, 152)
    CaféAuLait            = base.RGBColor(166, 123,  91)
    CaféNoir              = base.RGBColor( 75,  54,  33)
    CalPolyPomonaGreen    = base.RGBColor( 30,  77,  43)
    Calamansi             = base.RGBColor(252, 255, 164)
    CambridgeBlue         = base.RGBColor(163, 193, 173)
    Camel                 = base.RGBColor(193, 154, 107)
    CameoPink             = base.RGBColor(239, 187, 204)
    CamouflageGreen       = base.RGBColor(120, 134, 107)
    Canary                = base.RGBColor(255, 255, 153)
    CanaryYellow          = base.RGBColor(255, 239,   0)
    CandyAppleRed         = base.RGBColor(255,   8,   0)
    CandyPink             = base.RGBColor(228, 113, 122)
    Capri                 = base.RGBColor(  0, 191, 255)
    CaputMortuum          = base.RGBColor( 89,  39,  32)
    Caramel               = base.RGBColor(255, 213, 154)
    Cardinal              = base.RGBColor(196,  30,  58)
    CaribbeanGreen        = base.RGBColor(  0, 204, 153)
    Carmine               = base.RGBColor(150,   0,  24)
    MAndPCarmine          = base.RGBColor(215,   0,  64)
    CarminePink           = base.RGBColor(235,  76,  66)
    CarmineRed            = base.RGBColor(255,   0,  56)
    CarnationPink         = base.RGBColor(255, 166, 201)
    Carnelian             = base.RGBColor(179,  27,  27)
    CarolinaBlue          = base.RGBColor( 86, 160, 211)
    CarrotOrange          = base.RGBColor(237, 145,  33)
    CastletonGreen        = base.RGBColor(  0,  86,  63)
    CatalinaBlue          = base.RGBColor(  6,  42, 120)
    Catawba               = base.RGBColor(112,  54,  66)
    CedarChest            = base.RGBColor(201,  90,  73)
    Ceil                  = base.RGBColor(146, 161, 207)
    Celadon               = base.RGBColor(172, 225, 175)
    CeladonBlue           = base.RGBColor(  0, 123, 167)
    CeladonGreen          = base.RGBColor( 47, 132, 124)
    Celeste               = base.RGBColor(178, 255, 255)
    CelestialBlue         = base.RGBColor( 73, 151, 208)
    Cerise                = base.RGBColor(222,  49,  99)
    CerisePink            = base.RGBColor(236,  59, 131)
    Cerulean              = base.RGBColor(  0, 123, 167)
    CeruleanBlue          = base.RGBColor( 42,  82, 190)
    CeruleanFrost         = base.RGBColor(109, 155, 195)
    CGBlue                = base.RGBColor(  0, 122, 165)
    CGRed                 = base.RGBColor(224,  60,  49)
    Chamoisee             = base.RGBColor(160, 120,  90)
    Champagne             = base.RGBColor(247, 231, 206)
    ChampagnePink         = base.RGBColor(241, 221, 207)
    Charcoal              = base.RGBColor( 54,  69,  79)
    CharlestonGreen       = base.RGBColor( 35,  43,  43)
    Charm                 = base.RGBColor(208, 116, 139)
    CharmPink             = base.RGBColor(230, 143, 172)
    TraditionalChartreuse = base.RGBColor(223, 255,   0)
    WebChartreuse         = base.RGBColor(127, 255,   0)
    Cheese                = base.RGBColor(255, 166,   0)
    Cherry                = base.RGBColor(222,  49,  99)
    CherryBlossomPink     = base.RGBColor(255, 183, 197)
    Chestnut              = base.RGBColor(149,  69,  53)
    ChinaPink             = base.RGBColor(222, 111, 161)
    ChinaRose             = base.RGBColor(168,  81, 110)
    ChineseBlack          = base.RGBColor( 20,  20,  20)
    ChineseBlue           = base.RGBColor( 54,  81, 148)
    ChineseBronze         = base.RGBColor(205, 128,  50)
    ChineseBrown          = base.RGBColor(171,  56,  31)
    ChineseGreen          = base.RGBColor(208, 219,  97)
    ChineseGold           = base.RGBColor(204, 153,   0)
    ChineseOrange         = base.RGBColor(243, 112,  66)
    ChinesePink           = base.RGBColor(222, 112, 161)
    ChinesePurple         = base.RGBColor(114,  11, 152)
    ChineseRed            = base.RGBColor(205,   7,  30)
    ChineseRed2           = base.RGBColor(170,  56,  30)
    ChineseSilver         = base.RGBColor(204, 204, 204)
    ChineseViolet         = base.RGBColor(133,  96, 136)
    ChineseWhite          = base.RGBColor(226, 229, 222)
    ChineseYellow         = base.RGBColor(255, 178,   0)
    ChlorophyllGreen      = base.RGBColor( 74, 255,   0)
    ChocolateKisses       = base.RGBColor( 60,  20,  33)
    TraditionalChocolate  = base.RGBColor(123,  63,   0)
    WebChocolate          = base.RGBColor(210, 105,  30)
    ChristmasBlue         = base.RGBColor( 42, 143, 189)
    ChristmasBlue2        = base.RGBColor( 54,  81, 148)
    ChristmasBrown        = base.RGBColor( 93,  43,  44)
    ChristmasBrown2       = base.RGBColor( 76,  31,   2)
    ChristmasGreen        = base.RGBColor( 60, 141,  13)
    ChristmasGreen2       = base.RGBColor(  0, 117,   2)
    ChristmasGold         = base.RGBColor(202, 169,   6)
    ChristmasOrange       = base.RGBColor(255, 102,   0)
    ChristmasOrange2      = base.RGBColor(213, 108,  43)
    ChristmasPink         = base.RGBColor(255, 204, 203)
    ChristmasPink2        = base.RGBColor(227,  66, 133)
    ChristmasPurple       = base.RGBColor(102,  51, 152)
    ChristmasPurple2      = base.RGBColor( 77,   8,  75)
    ChristmasRed          = base.RGBColor(170,   1,  20)
    ChristmasRed2         = base.RGBColor(176,  27,  46)
    ChristmasSilver       = base.RGBColor(225, 223, 224)
    ChristmasYellow       = base.RGBColor(255, 204,   0)
    ChristmasYellow2      = base.RGBColor(254, 242,   0)
    ChromeYellow          = base.RGBColor(255, 167,   0)
    Cinereous             = base.RGBColor(152, 129, 123)
    Cinnabar              = base.RGBColor(227,  66,  52)
    Cinnamon              = base.RGBColor(210, 105,  30)
    CinnamonSatin         = base.RGBColor(205,  96, 126)
    Citrine               = base.RGBColor(228, 208,  10)
    CitrineBrown          = base.RGBColor(147,  55,   9)
    Citron                = base.RGBColor(159, 169,  31)
    Claret                = base.RGBColor(127,  23,  52)
    ClassicRose           = base.RGBColor(251, 204, 231)
    CobaltBlue            = base.RGBColor(  0,  71, 171)
    CocoaBrown            = base.RGBColor(210, 105,  30)
    Coconut               = base.RGBColor(150,  90,  62)
    Coffee                = base.RGBColor(111,  78,  55)
    Cola                  = base.RGBColor( 60,  48,  36)
    ColumbiaBlue          = base.RGBColor(196, 216, 226)
    Conditioner           = base.RGBColor(255, 255, 204)
    CongoPink             = base.RGBColor(248, 131, 121)
    CoolBlack             = base.RGBColor(  0,  46,  99)
    CoolGrey              = base.RGBColor(140, 146, 172)
    CookiesAndCream       = base.RGBColor(238, 224, 177)
    Copper                = base.RGBColor(184, 115,  51)
    CrayolaCopper         = base.RGBColor(218, 138, 103)
    CopperPenny           = base.RGBColor(173, 111, 105)
    CopperRed             = base.RGBColor(203, 109,  81)
    CopperRose            = base.RGBColor(153, 102, 102)
    Coquelicot            = base.RGBColor(255,  56,   0)
    Coral                 = base.RGBColor(255, 127,  80)
    CoralPink             = base.RGBColor(248, 131, 121)
    CoralRed              = base.RGBColor(255,  64,  64)
    CoralReef             = base.RGBColor(253, 124, 110)
    Cordovan              = base.RGBColor(137,  63,  69)
    Corn                  = base.RGBColor(251, 236,  93)
    CornellRed            = base.RGBColor(179,  27,  27)
    CornflowerBlue        = base.RGBColor(100, 149, 237)
    Cornsilk              = base.RGBColor(255, 248, 220)
    CosmicCobalt          = base.RGBColor( 46,  45, 136)
    CosmicLatte           = base.RGBColor(255, 248, 231)
    CoyoteBrown           = base.RGBColor(129,  97,  60)
    CottonCandy           = base.RGBColor(255, 188, 217)
    Cream                 = base.RGBColor(255, 253, 208)
    Crimson               = base.RGBColor(220,  20,  60)
    CrimsonGlory          = base.RGBColor(190,   0,  50)
    CrimsonRed            = base.RGBColor(153,   0,   0)
    Cultured              = base.RGBColor(245, 245, 245)
    Cyan                  = base.RGBColor(  0, 255, 255)
    CyanAzure             = base.RGBColor( 78, 130, 180)
    CyanBlueAzure         = base.RGBColor( 70, 130, 191)
    CyanCobaltBlue        = base.RGBColor( 40,  88, 156)
    CyanCornflowerBlue    = base.RGBColor( 24, 139, 194)
    ProcessCyan           = base.RGBColor(  0, 183, 235)
    CyberGrape            = base.RGBColor( 88,  66, 124)
    CyberYellow           = base.RGBColor(255, 211,   0)
    Cyclamen              = base.RGBColor(245, 111, 161)
    
    Daffodil               = base.RGBColor(255, 255,  49)
    Dandelion              = base.RGBColor(240, 225,  48)
    DarkBlue               = base.RGBColor(  0,   0, 139)
    DarkBlueGray           = base.RGBColor(102, 102, 153)
    DarkBronze             = base.RGBColor(128,  74,   0)
    DarkBrown              = base.RGBColor(101,  67,  33)
    DarkBrownTangelo       = base.RGBColor(136, 101,  78)
    DarkByzantium          = base.RGBColor( 93,  57,  84)
    DarkCandyAppleRed      = base.RGBColor(164,   0,   0)
    DarkCerulean           = base.RGBColor(  8,  69, 126)
    DarkCharcoal           = base.RGBColor( 51,  51,  51)
    DarkChestnut           = base.RGBColor(152, 105,  96)
    DarkChocolate          = base.RGBColor( 73,   2,   6)
    HersheysDarkChocolate  = base.RGBColor( 60,  19,  33)
    DarkCornflowerBlue     = base.RGBColor( 38,  66, 139)
    DarkCoral              = base.RGBColor(205,  91,  69)
    DarkCyan               = base.RGBColor(  0, 139, 139)
    DarkGoldenrod          = base.RGBColor(184, 134,  11)
    X11DarkGray            = base.RGBColor(169, 169, 169)
    DarkGreen              = base.RGBColor(  1,  50,  32)
    X11DarkGreen           = base.RGBColor(  0, 100,   0)
    DarkGunmetal           = base.RGBColor( 31,  38,  42)
    DarkImperialBlue       = base.RGBColor(  0,  65, 106)
    DarkImperialBlue2      = base.RGBColor(  0,  20, 126)
    DarkJungleGreen        = base.RGBColor( 26,  36,  33)
    DarkKhaki              = base.RGBColor(189, 183, 107)
    DarkLava               = base.RGBColor( 72,  60,  50)
    DarkLavender           = base.RGBColor(115,  79, 150)
    DarkLemonLime          = base.RGBColor(139, 190,  27)
    DarkLiver              = base.RGBColor( 83,  75,  79)
    HorsesDarkLiver        = base.RGBColor( 84,  61,  55)
    DarkMagenta            = base.RGBColor(139,   0, 139)
    DarkMediumGray         = base.RGBColor(169, 169, 169)
    DarkMidnightBlue       = base.RGBColor(  0,  51, 102)
    DarkMossGreen          = base.RGBColor( 74,  93,  35)
    DarkOliveGreen         = base.RGBColor( 85, 107,  47)
    DarkOrange             = base.RGBColor(255, 140,   0)
    DarkOrchid             = base.RGBColor(153,  50, 204)
    DarkPastelBlue         = base.RGBColor(119, 158, 203)
    DarkPastelGreen        = base.RGBColor(  3, 192,  60)
    DarkPastelPurple       = base.RGBColor(150, 111, 214)
    DarkPastelRed          = base.RGBColor(194,  59,  34)
    DarkPink               = base.RGBColor(231,  84, 128)
    DarkPowderBlue         = base.RGBColor(  0,  51, 153)
    DarkPuce               = base.RGBColor( 79,  58,  60)
    DarkPurple             = base.RGBColor( 48,  25,  52)
    DarkRaspberry          = base.RGBColor(135,  38,  87)
    DarkRed                = base.RGBColor(135,  38,  87)
    DarkSalmon             = base.RGBColor(233, 150, 122)
    DarkScarlet            = base.RGBColor( 86,   3,  25)
    DarkSeaGreen           = base.RGBColor(143, 188, 143)
    DarkSienna             = base.RGBColor( 60,  20,  20)
    DarkSkyBlue            = base.RGBColor(140, 190, 214)
    DarkSlateBlue          = base.RGBColor( 72,  61, 139)
    DarkSlateGray          = base.RGBColor( 47,  79,  79)
    DarkSpringGreen        = base.RGBColor( 23, 114,  69)
    DarkTan                = base.RGBColor(145, 129,  81)
    DarkTangerine          = base.RGBColor(255, 168,  18)
    DarkTaupe              = base.RGBColor( 72,  60,  50)
    DarkTerraCotta         = base.RGBColor(204,  78,  92)
    DarkTurquoise          = base.RGBColor(  0, 206, 209)
    DarkVanilla            = base.RGBColor(209, 190, 168)
    DarkViolet             = base.RGBColor(148,   0, 211)
    DarkYellow             = base.RGBColor(155, 135,  12)
    DartmouthGreen         = base.RGBColor(  0, 112,  60)
    DavysGrey              = base.RGBColor( 85,  85,  85)
    DebianRed              = base.RGBColor(215,  10,  83)
    DeepAmethyst           = base.RGBColor(156, 138, 164)
    DeepAquamarine         = base.RGBColor( 64, 130, 109)
    DeepCarmine            = base.RGBColor(169,  32,  62)
    DeepCarminePink        = base.RGBColor(239,  48,  56)
    DeepCarrotOrange       = base.RGBColor(233, 105,  44)
    DeepCerise             = base.RGBColor(218,  50, 135)
    DeepChampagne          = base.RGBColor(250, 214, 165)
    DeepChestnut           = base.RGBColor(185,  78,  72)
    DeepCoffee             = base.RGBColor(112,  66,  65)
    DeepFuchsia            = base.RGBColor(193,  84, 193)
    DeepGreen              = base.RGBColor(  5, 102,   8)
    DeepGreenCyanTurquoise = base.RGBColor( 14, 124,  97)
    DeepJungleGreen        = base.RGBColor(  0,  75,  73)
    DeepKoamaru            = base.RGBColor( 51,  51, 102)
    DeepLemon              = base.RGBColor(245, 199,  26)
    DeepLilac              = base.RGBColor(153,  85, 187)
    DeepMagenta            = base.RGBColor(204,   0, 204)
    DeepMaroon             = base.RGBColor(130,   0,   0)
    DeepMauve              = base.RGBColor(212, 115, 212)
    DeepMossGreen          = base.RGBColor( 53,  94,  59)
    DeepPeach              = base.RGBColor(255, 203, 164)
    DeepPink               = base.RGBColor(255,  20, 147)
    DeepPuce               = base.RGBColor(169,  92, 104)
    DeepRed                = base.RGBColor(133,   1,   1)
    DeepRuby               = base.RGBColor(132,  63,  91)
    DeepSaffron            = base.RGBColor(255, 153,  51)
    DeepSkyBlue            = base.RGBColor(  0, 191, 255)
    DeepSpaceSparkle       = base.RGBColor( 74, 100, 108)
    DeepSpringBud          = base.RGBColor( 85, 107,  47)
    DeepTaupe              = base.RGBColor(126,  94,  96)
    DeepTuscanRed          = base.RGBColor(102,  66,  77)
    DeepViolet             = base.RGBColor( 51,   0, 102)
    Deer                   = base.RGBColor(186, 135,  89)
    Denim                  = base.RGBColor( 21,  96, 189)
    DenimBlue              = base.RGBColor( 34,  67, 182)
    DesaturatedCyan        = base.RGBColor(102, 153, 153)
    Desert                 = base.RGBColor(193, 154, 107)
    DesertSand             = base.RGBColor(237, 201, 175)
    Desire                 = base.RGBColor(234,  60,  83)
    Diamond                = base.RGBColor(185, 242, 255)
    DimGray                = base.RGBColor(105, 105, 105)
    DingyDungeon           = base.RGBColor(197,  49,  81)
    Dirt                   = base.RGBColor(155, 118,  83)
    DirtyBrown             = base.RGBColor(181, 101,  30)
    DirtyWhite             = base.RGBColor(232, 228, 201)
    DodgerBlue             = base.RGBColor( 30, 144, 255)
    DodieYellow            = base.RGBColor(254, 246,  91)
    DogwoodRose            = base.RGBColor(215,  24, 104)
    DollarBill             = base.RGBColor(133, 187, 101)
    DolphinGray            = base.RGBColor(130, 142, 132)
    DonkeyBrown            = base.RGBColor(102,  76,  40)
    Drab                   = base.RGBColor(150, 113,  23)
    DukeBlue               = base.RGBColor(  0,   0, 156)
    DustStorm              = base.RGBColor(229, 204, 201)
    DutchWhite             = base.RGBColor(239, 223, 187)
    
    EarthYellow         = base.RGBColor(225, 169,  95)
    Ebony               = base.RGBColor( 85,  93,  80)
    Ecru                = base.RGBColor(194, 178, 128)
    EerieBlack          = base.RGBColor( 27,  27,  27)
    Eggplant            = base.RGBColor( 97,  64,  81)
    Eggshell            = base.RGBColor(240, 234, 214)
    EgyptianBlue        = base.RGBColor( 16,  52, 166)
    ElectricBlue        = base.RGBColor(125, 249, 255)
    ElectricCrimson     = base.RGBColor(255,   0,  63)
    ElectricCyan        = base.RGBColor(  0, 255, 255)
    ElectricGreen       = base.RGBColor(  0, 255,   0)
    ElectricIndigo      = base.RGBColor(111,   0, 255)
    ElectricLavender    = base.RGBColor(244, 187, 255)
    ElectricLime        = base.RGBColor(204, 255,   0)
    ElectricPurple      = base.RGBColor(191,   0, 255)
    ElectricUltramarine = base.RGBColor( 63,   0, 255)
    ElectricViolet      = base.RGBColor(143,   0, 255)
    ElectricYellow      = base.RGBColor(255, 255,  51)
    Emerald             = base.RGBColor( 80, 200, 120)
    EmeraldGreen        = base.RGBColor(  4,  99,   7)
    Eminence            = base.RGBColor(108,  48, 130)
    EnglishGreen        = base.RGBColor( 27,  77,  62)
    EnglishLavender     = base.RGBColor(180, 131, 149)
    EnglishRed          = base.RGBColor(171,  75,  82)
    EnglishVermillion   = base.RGBColor(204,  71,  75)
    EnglishViolet       = base.RGBColor( 86,  60,  92)
    EtonBlue            = base.RGBColor(150, 200, 162)
    Eucalyptus          = base.RGBColor( 68, 215, 168)
    
    Fallow                 = base.RGBColor(193, 154, 107)
    FaluRed                = base.RGBColor(128,  24,  24)
    Fandango               = base.RGBColor(181,  51, 137)
    FandangoPink           = base.RGBColor(222,  82, 133)
    FashionFuchsia         = base.RGBColor(244,   0, 161)
    Fawn                   = base.RGBColor(229, 170, 112)
    Feldgrau               = base.RGBColor( 77,  93,  83)
    Feldspar               = base.RGBColor(253, 213, 177)
    FernGreen              = base.RGBColor( 79, 121,  66)
    FerrariRed             = base.RGBColor(255,  40,   0)
    FieldDrab              = base.RGBColor(108,  84,  30)
    FieryRose              = base.RGBColor(255,  84, 112)
    Firebrick              = base.RGBColor(178,  34,  34)
    FireEngineRed          = base.RGBColor(206,  32,  41)
    FireOpal               = base.RGBColor(233,  92,  75)
    Flame                  = base.RGBColor(226,  88,  34)
    FlamingoPink           = base.RGBColor(252, 142, 172)
    Flattery               = base.RGBColor(107,  68,  35)
    Flavescent             = base.RGBColor(247, 233, 142)
    Flax                   = base.RGBColor(238, 220, 130)
    Flesh                  = base.RGBColor(255, 233, 209)
    Flirt                  = base.RGBColor(162,   0, 109)
    FloralWhite            = base.RGBColor(255, 250, 240)
    FluorescentBlue        = base.RGBColor( 21, 244, 238)
    FluorescentOrange      = base.RGBColor(255, 191,   0)
    FluorescentPink        = base.RGBColor(255,  20, 147)
    FluorescentYellow      = base.RGBColor(204, 255,   0)
    Folly                  = base.RGBColor(255,   0,  79)
    TraditionalForestGreen = base.RGBColor(  1,  68,  33)
    WebForestGreen         = base.RGBColor( 34, 139,  34)
    FrenchBeige            = base.RGBColor(166, 123,  91)
    FrenchBistre           = base.RGBColor(133, 109,  77)
    FrenchBlue             = base.RGBColor(  0, 114, 187)
    FrenchFuchsia          = base.RGBColor(253,  63, 146)
    FrenchLilac            = base.RGBColor(134,  96, 142)
    FrenchLime             = base.RGBColor(158, 253,  56)
    FrenchMauve            = base.RGBColor(212, 115, 212)
    FrenchPink             = base.RGBColor(253, 108, 158)
    FrenchPuce             = base.RGBColor(129,  20,  83)
    FrenchRaspberry        = base.RGBColor(199,  44,  72)
    FrenchRose             = base.RGBColor(246,  74, 138)
    FrenchSkyBlue          = base.RGBColor(119, 181, 254)
    FrenchViolet           = base.RGBColor(136,   6, 206)
    FrenchWine             = base.RGBColor(172,  30,  68)
    FreshAir               = base.RGBColor(166, 231, 255)
    Frostbite              = base.RGBColor(233,  54, 167)
    Fuchsia                = base.RGBColor(255,   0, 255)
    CrayolaFuchsia         = base.RGBColor(193,  84, 193)
    FuchsiaPink            = base.RGBColor(255, 119, 255)
    FuchsiaPurple          = base.RGBColor(204,  57, 123)
    FuchsiaRose            = base.RGBColor(199,  67, 117)
    Fulvous                = base.RGBColor(228, 132,   0)
    FuzzyWuzzy             = base.RGBColor(204, 102, 102)

    Gainsboro          = base.RGBColor(220, 220, 220)
    Gamboge            = base.RGBColor(228, 155,  15)
    GambogeOrange      = base.RGBColor(153, 102,   0)
    GambogeBrown       = base.RGBColor(153, 102,   0)
    Garnet             = base.RGBColor(115,  54,  53)
    GargoyleGas        = base.RGBColor(255, 223,  70)
    GenericViridian    = base.RGBColor(  0, 127, 102)
    GhostWhite         = base.RGBColor(248, 248, 255)
    GiantsClub         = base.RGBColor(176,  92,  82)
    GiantsOrange       = base.RGBColor(254,  90,  29)
    Glaucous           = base.RGBColor( 96, 130, 182)
    GlossyGrape        = base.RGBColor(171, 146, 179)
    GOGreen            = base.RGBColor(  0, 171, 102)
    Gold               = base.RGBColor(165, 124,   0)
    MetallicGold       = base.RGBColor(212, 175,  55)
    WebGold            = base.RGBColor(255, 215,   0)
    Golden             = base.RGBColor(255, 215,   0)
    CrayolaGold        = base.RGBColor(230, 190, 138)
    GoldFusion         = base.RGBColor(133, 117,  78)
    GoldFoil           = base.RGBColor(189, 155,  22)
    GoldBrown          = base.RGBColor(153, 101,  21)
    GoldPoppy          = base.RGBColor(252,  94,   0)
    GoldYellow         = base.RGBColor(255, 223,   0)
    Goldenrod          = base.RGBColor(218, 165,  32)
    GraniteGray        = base.RGBColor(103, 103, 103)
    GrannySmithApple   = base.RGBColor(168, 228, 160)
    Grape              = base.RGBColor(111,  45, 168)
    Gray               = base.RGBColor(128, 128, 128)
    WebGray            = base.RGBColor(128, 128, 128)
    CSSGray            = base.RGBColor(128, 128, 128)
    X11Gray            = base.RGBColor(190, 190, 190)
    GrayAsparagus      = base.RGBColor( 70,  89,  69)
    GrayBlue           = base.RGBColor(140, 146, 172)
    Green              = base.RGBColor(  0, 128,   1)
    ColorWheelGreen    = base.RGBColor(  0, 255,   0)
    X11Green           = base.RGBColor(  0, 255,   0)
    CrayolaGreen       = base.RGBColor( 28, 172, 120)
    WebGreen           = base.RGBColor(  0, 128,   0)
    CSSGreen           = base.RGBColor(  0, 128,   0)
    MunsellGreen       = base.RGBColor(  0, 168, 119)
    NCSGreen           = base.RGBColor(  0, 159, 107)
    PantoneGreen       = base.RGBColor(  0, 173,  67)
    PigmentGreen       = base.RGBColor(  0, 165,  80)
    RYBGreen           = base.RGBColor(102, 176,  50)
    GreenBlue          = base.RGBColor( 17, 100, 180)
    GreenBlue          = base.RGBColor( 17, 100, 180)
    GreenCyan          = base.RGBColor(  0, 153, 102)
    GreenLizard        = base.RGBColor(167, 244,  50)
    GreenSheen         = base.RGBColor(110, 174, 161)
    GreenYellow        = base.RGBColor(173, 255,  47)
    Grullo             = base.RGBColor(169, 154, 134)
    GuppieGreen        = base.RGBColor(  0, 255, 127)
    Gunmetal           = base.RGBColor( 42,  52,  57)
    
    HalayàÚbe         = base.RGBColor(102,  56,  84)
    HalloweenOrange   = base.RGBColor(235,  97,  35)
    HanBlue           = base.RGBColor( 68, 108, 207)
    HanPurple         = base.RGBColor( 82,  24, 250)
    HansaYellow       = base.RGBColor(233, 214, 107)
    Harlequin         = base.RGBColor( 63, 255,   0)
    HarlequinGreen    = base.RGBColor( 70, 203,  24)
    HarvardCrimson    = base.RGBColor(201,   0,  22)
    HarvestGold       = base.RGBColor(218, 145,   0)
    HeartGold         = base.RGBColor(128, 128,   0)
    HeatWave          = base.RGBColor(255, 122,   0)
    HeidelbergRed     = base.RGBColor(150,   0,  24)
    Heliotrope        = base.RGBColor(223, 115, 255)
    HeliotropeGray    = base.RGBColor(170, 152, 169)
    HeliotropeMagenta = base.RGBColor(170,   0, 187)
    HollywoodCerise   = base.RGBColor(244,   0, 161)
    Honeydew          = base.RGBColor(240, 255, 240)
    HonoluluBlue      = base.RGBColor(  0, 109, 176)
    HookersGreen      = base.RGBColor( 73, 121, 107)
    HotMagenta        = base.RGBColor(255,  29, 206)
    HotPink           = base.RGBColor(255, 105, 180)
    HunterGreen       = base.RGBColor( 53,  94,  59)
    
    Iceberg                             = base.RGBColor(113, 166, 210)
    Icterine                            = base.RGBColor(252, 247,  94)
    IguanaGreen                         = base.RGBColor(113, 188, 120)
    IlluminatingEmerald                 = base.RGBColor( 49, 145, 119)
    Imperial                            = base.RGBColor( 49, 145, 119)
    ImperialBlue                        = base.RGBColor(  0,  35, 149)
    ImperialPurple                      = base.RGBColor(102,   2,  60)
    ImperialRed                         = base.RGBColor(237,  41,  57)
    Inchworm                            = base.RGBColor(178, 236,  93)
    Independence                        = base.RGBColor( 76,  81, 109)
    IndiaGreen                          = base.RGBColor( 19, 136,   8)
    IndianRed                           = base.RGBColor(205,  92,  92)
    IndianYellow                        = base.RGBColor(227, 168,  87)
    Indigo                              = base.RGBColor( 75,   0, 130)
    IndigoDye                           = base.RGBColor(  9,  31, 146)
    RainbowIndigo                       = base.RGBColor( 35,  48, 103)
    WebIndigo                           = base.RGBColor( 75,   0, 130)
    InfraRed                            = base.RGBColor(255,  73, 108)
    InterdimensionalBlue                = base.RGBColor( 54,  12, 204)
    InternationalKleinBlue              = base.RGBColor(  0,  47, 167)
    AerospaceInternationalOrange        = base.RGBColor(255,  79,   0)
    EngineeringInternationalOrange      = base.RGBColor(255,  79,   0)
    GoldenGateBridgeInternationalOrange = base.RGBColor(192,  54,  44)
    Iris                                = base.RGBColor( 90,  79, 207)
    Irresistible                        = base.RGBColor(179,  68, 108)
    Isabelline                          = base.RGBColor(244, 240, 236)
    IslamicGreen                        = base.RGBColor(  0, 144,   0)
    ItalianSkyBlue                      = base.RGBColor(178, 255, 255)
    Ivory                               = base.RGBColor(255, 255, 240)

    Jacarta         = base.RGBColor( 61,  50,  93)
    JackoBean       = base.RGBColor( 65,  54,  40)
    Jade            = base.RGBColor(  0, 168, 107)
    JapaneseCarmine = base.RGBColor(157,  41,  51)
    JapaneseIndigo  = base.RGBColor( 38,  67,  72)
    JapaneseLaurel  = base.RGBColor( 47, 117,  50)
    JapaneseViolet  = base.RGBColor( 91,  50,  86)
    Jasmine         = base.RGBColor(248, 222, 126)
    Jasper          = base.RGBColor(215,  59,  62)
    JasperOrange    = base.RGBColor(222, 143,  78)
    JazzberryJam    = base.RGBColor(165,  11,  94)
    JellyBean       = base.RGBColor(218,  97,  78)
    JellyBeanBlue   = base.RGBColor( 68, 121, 142)
    Jet             = base.RGBColor( 52,  52,  52)
    JetStream       = base.RGBColor(187, 208, 201)
    Jonquil         = base.RGBColor(244, 202,  22)
    JordyBlue       = base.RGBColor(138, 185, 241)
    JuneBud         = base.RGBColor(189, 218,  87)
    JungleGreen     = base.RGBColor( 41, 171, 135)
    
    KellyGreen   = base.RGBColor( 76, 187,  23)
    KenyanCopper = base.RGBColor(124,  28,   5)
    Keppel       = base.RGBColor( 58, 176, 158)
    KeyLime      = base.RGBColor(232, 244, 140)
    Khaki        = base.RGBColor(195, 176, 145)
    WebKhaki     = base.RGBColor(195, 176, 145)
    CSSKhaki     = base.RGBColor(195, 176, 145)
    X11Khaki     = base.RGBColor(240, 230, 140)
    LightKhaki   = base.RGBColor(240, 230, 140)
    Kiwi         = base.RGBColor(142, 229,  63)
    Kobe         = base.RGBColor(136,  45,  23)
    Kobi         = base.RGBColor(231, 159, 196)
    Kobicha      = base.RGBColor(107,  68,  35)
    KombuGreen   = base.RGBColor( 53,  66,  48)
    KSUPurple    = base.RGBColor( 81,  40, 136)
    KUCrimson    = base.RGBColor(232,   0,  13)
