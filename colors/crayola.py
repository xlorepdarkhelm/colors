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

    # Standard Colors
    Red                    = base.sRGBColor(237,  10,  63)
    DarkRed                = base.sRGBColor(195,  33,  72)
    Maroon                 = base.sRGBColor(195,  33,  72)
    TorchRed               = base.sRGBColor(253,  14,  53)
    Scarlet                = base.sRGBColor(253,  14,  53)
    BrickRed               = base.sRGBColor(198,  45,  66)
    EnglishVermilion       = base.sRGBColor(204,  71,  75)
    EnglishVermillion      = base.sRGBColor(204,  71,  75)
    MadderLake             = base.sRGBColor(204,  51,  54)
    PermanentGeraniumLake  = base.sRGBColor(225,  44,  44)
    MaximumRed             = base.sRGBColor(217,  33,  33)
    IndianRed              = base.sRGBColor(185,  78,  72)
    Chestnut               = base.sRGBColor(185,  78,  72)
    OrangeRed              = base.sRGBColor(255,  63,  52)
    SunsetOrange           = base.sRGBColor(254,  76,  64)
    Bittersweet            = base.sRGBColor(254, 111,  94)
    DarkVenetianRed        = base.sRGBColor(179,  59,  36)
    VenetianRed            = base.sRGBColor(204,  85,  61)
    LightVenetianRed       = base.sRGBColor(230, 115,  92)
    VividTangerine         = base.sRGBColor(255, 153, 128)
    MiddleRed              = base.sRGBColor(229, 144, 115)
    BurntOrange            = base.sRGBColor(255, 112,  52)
    RedOrange              = base.sRGBColor(255, 104,  31)
    Orange                 = base.sRGBColor(255, 136, 100)
    MacaroniAndCheese      = base.sRGBColor(255, 185, 123)
    MiddleYellowRed        = base.sRGBColor(236, 177, 118)
    MediumOrange           = base.sRGBColor(236, 177, 118)
    MangoTango             = base.sRGBColor(231, 114,   0)
    YellowOrange           = base.sRGBColor(255, 174,  66)
    MaximumYellowRed       = base.sRGBColor(242, 186,  73)
    BananaMania            = base.sRGBColor(251, 231, 178)
    Maize                  = base.sRGBColor(242, 198,  73)
    GoldOchre              = base.sRGBColor(242, 198,  73)
    GoldenOchre            = base.sRGBColor(242, 198,  73)
    OrangeYellow           = base.sRGBColor(248, 213, 104)
    Goldenrod              = base.sRGBColor(252, 214, 103)
    MediumChromeYellow     = base.sRGBColor(252, 214, 103)
    MediumYellow           = base.sRGBColor(252, 214, 103)
    Dandelion              = base.sRGBColor(254, 216,  93)
    Yellow                 = base.sRGBColor(252, 232, 131)
    GreenYellow            = base.sRGBColor(241, 231, 136)
    MiddleYellow           = base.sRGBColor(255, 235,   0)
    OliveGreen             = base.sRGBColor(181, 179,  92)
    SpringGreen            = base.sRGBColor(236, 235, 189)
    MaximumYellow          = base.sRGBColor(250, 250,  55)
    Canary                 = base.sRGBColor(255, 255, 153)
    LemonYellow            = base.sRGBColor(255, 255, 159)
    LightChromeYellow      = base.sRGBColor(255, 255, 159)
    LightYellow            = base.sRGBColor(255, 255, 159)
    MaximumGreenYellow     = base.sRGBColor(217, 230,  80)
    MiddleGreenYellow      = base.sRGBColor(172, 191,  96)
    Inchworm               = base.sRGBColor(175, 227,  19)
    LightChromeGreen       = base.sRGBColor(190, 230,  75)
    LightGreen             = base.sRGBColor(190, 230,  75)
    YellowGreen	           = base.sRGBColor(197, 225, 122)
    MaximumGreen           = base.sRGBColor( 94, 140,  49)
    Asparagus              = base.sRGBColor(123, 160,  91)
    GrannySmithApple       = base.sRGBColor(157, 224, 147)
    Fern                   = base.sRGBColor( 99, 183, 108)
    MiddleGreen            = base.sRGBColor( 77, 140,  87)
    Green                  = base.sRGBColor( 58, 166,  85)
    MediumChromeGreen      = base.sRGBColor(108, 166, 124)
    MediumGreen            = base.sRGBColor(108, 166, 124)
    ForestGreen            = base.sRGBColor( 95, 167, 119)
    DarkGreen              = base.sRGBColor( 95, 167, 119)
    SeaGreen               = base.sRGBColor(147, 223, 184)
    LightGreen             = base.sRGBColor(147, 223, 184)
    Shamrock               = base.sRGBColor( 51, 204, 153)
    MountainMeadow         = base.sRGBColor( 26, 179, 133)
    JungleGreen            = base.sRGBColor( 41, 171, 135)
    CaribbeanGreen         = base.sRGBColor(  0, 204, 153)
    TropicalRainForest     = base.sRGBColor(  0, 117,  94)
    MiddleBlueGreen        = base.sRGBColor(141, 217, 204)
    PineGreen              = base.sRGBColor(  1, 120, 111)
    DarkChromeGreen        = base.sRGBColor(  1, 120, 111)
    DarkGreen2             = base.sRGBColor(  1, 120, 111)
    MaximumBlueGreen       = base.sRGBColor( 48, 191, 191)
    RobinsEggBlue          = base.sRGBColor(  0, 204, 204)
    TealBlue               = base.sRGBColor(  0, 128, 128)
    LightBlue              = base.sRGBColor(143, 216, 216)
    Aquamarine             = base.sRGBColor(149, 224, 232)
    LightTurquoiseBlue     = base.sRGBColor(149, 224, 232)
    TurquoiseBlue          = base.sRGBColor(108, 218, 231)
    OuterSpace             = base.sRGBColor( 45,  56,  58)
    SkyBlue                = base.sRGBColor(118, 215, 234)
    MiddleBlue             = base.sRGBColor(126, 212, 230)
    BlueGreen              = base.sRGBColor(  0, 149, 183)
    MiddleBlueGreen        = base.sRGBColor(  0, 149, 183)
    PacificBlue            = base.sRGBColor(  0, 157, 196)
    Cerulean               = base.sRGBColor(  2, 164, 211)
    MaximumBlue            = base.sRGBColor( 71, 171, 204)
    BlueGreen2             = base.sRGBColor( 71, 171, 204)
    Blue                   = base.sRGBColor( 46, 180, 230)
    Blue1                  = base.sRGBColor( 46, 180, 230)
    BlueI                  = base.sRGBColor( 46, 180, 230)
    CelestialBlue          = base.sRGBColor( 46, 180, 230)
    AzureBlue              = base.sRGBColor( 46, 180, 230)
    CeruleanBlue           = base.sRGBColor( 51, 154, 204)
    Cornflower             = base.sRGBColor(147, 204, 234)
    GreenBlue              = base.sRGBColor( 40, 135, 200)
    MidnightBlue           = base.sRGBColor(  0,  70, 140)
    PrussianBlue           = base.sRGBColor(  0,  70, 140)
    NavyBlue               = base.sRGBColor(  0, 102, 204)
    Denim                  = base.sRGBColor( 21,  96, 189)
    Blue3                  = base.sRGBColor(  0, 102, 255)
    BlueIII                = base.sRGBColor(  0, 102, 255)
    CadetBlue              = base.sRGBColor(169, 178, 195)
    Periwinkle             = base.sRGBColor(195, 205, 230)
    Blue2                  = base.sRGBColor( 69, 112, 230)
    BlueII                 = base.sRGBColor( 69, 112, 230)
    WildBlueYonder         = base.sRGBColor(122, 137, 184)
    Indigo                 = base.sRGBColor( 79, 105, 198)
    Manatee                = base.sRGBColor(141, 144, 161)
    CobaltBlue             = base.sRGBColor(140, 144, 200)
    CelestialBlue2         = base.sRGBColor(112, 112, 204)
    BlueBell               = base.sRGBColor(153, 153, 204)
    MaximumBluePurple      = base.sRGBColor(172, 172, 230)
    VioletBlue             = base.sRGBColor(118, 110, 200)
    BlueViolet             = base.sRGBColor(118, 110, 200)
    BlueViolet2            = base.sRGBColor(100,  86, 183)
    Violet                 = base.sRGBColor(100,  86, 183)
    UltramarineBlue        = base.sRGBColor( 63,  38, 191)
    MiddleBluePurple       = base.sRGBColor(139, 114, 190)
    PurpleHeart            = base.sRGBColor(101,  45, 193)
    RoyalPurple            = base.sRGBColor(107,  63, 160)
    Violet2                = base.sRGBColor(131,  89, 163)
    VioletII               = base.sRGBColor(131,  89, 163)
    VioletPurple           = base.sRGBColor(131,  89, 163)
    MediumViolet           = base.sRGBColor(143,  71, 179)
    Wisteria               = base.sRGBColor(201, 160, 220)
    Lavender               = base.sRGBColor(191, 143, 204)
    LavenderI              = base.sRGBColor(191, 143, 204)
    VividViolet            = base.sRGBColor(128,  55, 144)
    MaximumPurple          = base.sRGBColor(115,  51, 128)
    PurpleMountainsMajesty = base.sRGBColor(214, 174, 221)
    PurpleMountainMajesty  = base.sRGBColor(214, 174, 221)
    Fuchsia                = base.sRGBColor(193,  84, 193)
    PinkFlamingo           = base.sRGBColor(252, 116, 253)
    Violet                 = base.sRGBColor(115,  46, 108)
    VioletI                = base.sRGBColor(115,  46, 108)
    Purple                 = base.sRGBColor(115,  46, 108)
    BrilliantRose          = base.sRGBColor(230, 103, 206)
    Orchid                 = base.sRGBColor(226, 156, 210)
    MediumRedViolet        = base.sRGBColor(226, 156, 210)
    Plum                   = base.sRGBColor(142,  49, 121)
    MediumRose             = base.sRGBColor(217, 108, 190)
    Thistle                = base.sRGBColor(235, 176, 215)
    LightMagenta           = base.sRGBColor(235, 176, 215)
    Mulberry               = base.sRGBColor(200,  80, 155)
    RedViolet              = base.sRGBColor(187,  51, 133)
    MiddlePurple           = base.sRGBColor(217, 130, 181)
    MaximumRedPurple       = base.sRGBColor(166,  58, 121)
    JazzberryJam           = base.sRGBColor(165,  11,  94)
    Eggplant               = base.sRGBColor(97,   64,  81)
    Magenta                = base.sRGBColor(246,  83, 166)
    PermanentMagenta       = base.sRGBColor(246,  83, 166)
    Cerise                 = base.sRGBColor(218,  50, 135)
    WildStrawberry         = base.sRGBColor(255,  51, 153)
    Lavender2              = base.sRGBColor(251, 174, 210)
    LavenderII             = base.sRGBColor(251, 174, 210)
    CottonCandy            = base.sRGBColor(255, 183, 213)
    CarnationPink          = base.sRGBColor(255, 166, 201)
    RosePink               = base.sRGBColor(255, 166, 201)
    Pink                   = base.sRGBColor(255, 166, 201)
    VioletRed              = base.sRGBColor(247,  70, 138)
    Razzmatazz             = base.sRGBColor(227,  11,  92)
    PigPink                = base.sRGBColor(253, 215, 228)
    PiggyPink              = base.sRGBColor(253, 215, 228)
    Carmine                = base.sRGBColor(230,  46, 107)
    CarmineRed             = base.sRGBColor(230,  46, 107)
    Blush                  = base.sRGBColor(219,  80, 121)
    Cranberry              = base.sRGBColor(219,  80, 121)
    TickleMePink           = base.sRGBColor(252, 128, 165)
    Mauvelous              = base.sRGBColor(240, 145, 169)
    Salmon                 = base.sRGBColor(255, 145, 164)
    MiddleRedPurple        = base.sRGBColor(165,  83,  83)
    Mahogany               = base.sRGBColor(202,  52,  53)
    Melon                  = base.sRGBColor(254, 186, 173)
    PinkSherbert           = base.sRGBColor(247, 163, 142)
    BurntSienna            = base.sRGBColor(233, 116,  81)
    Brown                  = base.sRGBColor(175,  89,  62)
    Sepia                  = base.sRGBColor(158,  91,  64)
    FuzzyWuzzy             = base.sRGBColor(135,  66,  31)
    FuzzyWuzzyBrown        = base.sRGBColor(135,  66,  31)
    Beaver                 = base.sRGBColor(146, 111,  91)
    Tumbleweed             = base.sRGBColor(222, 166, 129)
    RawSienna              = base.sRGBColor(210, 125,  70)
    VanDykeBrown           = base.sRGBColor(102,  66,  40)
    Brown2                 = base.sRGBColor(102,  66,  40)
    Tan                    = base.sRGBColor(217, 154, 108)
    DesertSand             = base.sRGBColor(237, 201, 175)
    Peach                  = base.sRGBColor(255, 203, 164)
    FleshTint              = base.sRGBColor(255, 203, 164)
    Flesh                  = base.sRGBColor(255, 203, 164)
    PinkBeige              = base.sRGBColor(255, 203, 164)
    BurntUmber             = base.sRGBColor(128,  85,  51)
    Apricot                = base.sRGBColor(253, 213, 177)
    Almond                 = base.sRGBColor(238, 217, 196)
    RawUmber               = base.sRGBColor(102,  82,  51)
    Shadow                 = base.sRGBColor(131, 112,  80)
    RawSienna              = base.sRGBColor(230, 188,  92)
    RawSiennaI             = base.sRGBColor(230, 188,  92)
    Timberwolf             = base.sRGBColor(217, 214, 207)
    Gold                   = base.sRGBColor(146, 146, 110)
    GoldI                  = base.sRGBColor(146, 146, 110)
    GoldII                 = base.sRGBColor(230, 190, 138)
    Silver                 = base.sRGBColor(201, 192, 187)
    Copper                 = base.sRGBColor(218, 138, 103)
    AntiqueBrass           = base.sRGBColor(200, 138, 101)
    Black                  = base.sRGBColor(  0,   0,   0)
    CharcoalGray           = base.sRGBColor(115, 106,  98)
    Gray                   = base.sRGBColor(139, 134, 128)
    Grey                   = base.sRGBColor(139, 134, 128)
    MiddleGray             = base.sRGBColor(139, 134, 128)
    MiddleGrey             = base.sRGBColor(139, 134, 128)
    NeutralGray            = base.sRGBColor(139, 134, 128)
    NeutralGrey            = base.sRGBColor(139, 134, 128)
    BlueGray               = base.sRGBColor(200, 200, 205)
    White                  = base.sRGBColor(255, 255, 255)

    # Fluorescent
    RadicalRed       = base.sRGBColor(255,  53,  94)
    WildWatermelon   = base.sRGBColor(253,  91, 120)
    UltraRed         = base.sRGBColor(253,  91, 120)
    OutrageousOrange = base.sRGBColor(255,  96,  55)
    UltraOrange      = base.sRGBColor(255,  96,  55)
    AtomicTangerine  = base.sRGBColor(255, 153, 102)
    UltraYellow      = base.sRGBColor(255, 153, 102)
    NeonCarrot       = base.sRGBColor(255, 153,  51)
    Sunglow          = base.sRGBColor(255, 204,  51)
    LaserLemon       = base.sRGBColor(255, 255, 102)
    Chartreuse       = base.sRGBColor(255, 255, 102)
    UnmellowYellow   = base.sRGBColor(255, 255, 102)
    ElectricLime     = base.sRGBColor(204, 255,   0)
    ScreaminGreen    = base.sRGBColor(102, 255, 102)
    UltraGreen       = base.sRGBColor(102, 255, 102)
    MagicMint        = base.sRGBColor(170, 240, 209)
    BlizzardBlue     = base.sRGBColor( 80, 191, 230)
    UltraBlue        = base.sRGBColor( 80, 191, 230)
    ShockingPink     = base.sRGBColor(255, 110, 255)
    UltraPink        = base.sRGBColor(255, 110, 255)
    RazzleDazzleRose = base.sRGBColor(238,  52, 210)
    HotMagenta       = base.sRGBColor(238,  52, 210)
    HotMagenta2      = base.sRGBColor(255,   0, 204)
    PurplePizzazz    = base.sRGBColor(255,   0, 204)

    # Silver Swirls
    AztecGold        = base.sRGBColor(195, 153,  83)
    BurnishedBrown   = base.sRGBColor(161, 122, 116)
    CeruleanFrost    = base.sRGBColor(109, 155, 195)
    CinnamonSatin    = base.sRGBColor(205,  96, 126)
    CopperPenny      = base.sRGBColor(173, 111, 105)
    CosmicCobalt     = base.sRGBColor( 46,  45, 136)
    GlossyGrape      = base.sRGBColor(171, 146, 179)
    GraniteGray      = base.sRGBColor(103, 103, 103)
    GreenSheen       = base.sRGBColor(110, 174, 161)
    LilacLuster      = base.sRGBColor(174, 152, 170)
    MistyMoss        = base.sRGBColor(187, 180, 119)
    MysticMaroon     = base.sRGBColor(173,  67, 121)
    PearlyPurple     = base.sRGBColor(183, 104, 162)
    PewterBlue       = base.sRGBColor(139, 168, 183)
    PolishedPine     = base.sRGBColor( 93, 164, 147)
    QuickSilver      = base.sRGBColor(166, 166, 166)
    RoseDust         = base.sRGBColor(158,  94, 111)
    RustyRed         = base.sRGBColor(218,  44,  67)
    ShadowBlue       = base.sRGBColor(119, 139, 165)
    ShinyShamrock    = base.sRGBColor( 95, 167, 120)
    SteelTeal        = base.sRGBColor( 95, 138, 139)
    SugarPlum        = base.sRGBColor(145,  78, 117)
    TwilightLavender = base.sRGBColor(138,  73, 107)
    WintergreenDream = base.sRGBColor( 86, 136, 125)

    # Magic Scent
    BabyPowder    = base.sRGBColor(255, 255, 255)
    Banana        = base.sRGBColor(254, 216,  93)
    Blueberry     = base.sRGBColor( 69, 112, 230)
    BubbleGum     = base.sRGBColor(252, 128, 165)
    CedarChest    = base.sRGBColor(202,  52,  53)
    Cherry        = base.sRGBColor(195,  33,  72)
    Chocolate     = base.sRGBColor(175,  89,  62)
    Coconut       = base.sRGBColor(255, 255, 255)
    Daffodil      = base.sRGBColor(251, 232, 112)
    Dirt          = base.sRGBColor(158,  91,  64)
    Eucalyptus    = base.sRGBColor( 41, 171, 135)
    FreshAir      = base.sRGBColor(118, 215, 234)
    Grape         = base.sRGBColor(131,  89, 163)
    JellyBean     = base.sRGBColor(255, 136,  51)
    LeatherJacket = base.sRGBColor(  0,   0,   0)
    Lemon         = base.sRGBColor(251, 232, 112)
    Licorice      = base.sRGBColor(  0,   0,   0)
    Lilac         = base.sRGBColor(201, 160, 220)
    Lime          = base.sRGBColor(197, 225, 122)
    Lumber        = base.sRGBColor(253, 213, 177)
    NewCar        = base.sRGBColor(  0, 102, 255)
    Pine          = base.sRGBColor(  1, 120, 111)
    Rose          = base.sRGBColor(237,  10,  63)
    Shampoo       = base.sRGBColor(255, 166, 201)
    Smoke         = base.sRGBColor(139, 134, 128)
    Soap          = base.sRGBColor(195, 205, 230)
    Strawberry    = base.sRGBColor(255,  51, 153)
    Tulip         = base.sRGBColor(255, 136,  51)

    # Gem Tones
    Amethyst    = base.sRGBColor(100,  96, 154)
    Citrine     = base.sRGBColor(147,  55,   9)
    Emerald     = base.sRGBColor( 20, 169, 137)
    Jade        = base.sRGBColor( 70, 154, 132)
    Jasper      = base.sRGBColor(208,  83,  64)
    LapisLazuli = base.sRGBColor( 67, 108, 185)
    Malachite   = base.sRGBColor( 70, 148, 150)
    Moonstone   = base.sRGBColor( 58, 168, 193)
    Onyx        = base.sRGBColor( 53,  56,  57)
    Peridot     = base.sRGBColor(171, 173,  72)
    PinkPearl   = base.sRGBColor(176, 112, 128)
    RoseQuartz  = base.sRGBColor(189,  85, 156)
    Ruby        = base.sRGBColor(170,  64, 105)
    Sapphire    = base.sRGBColor( 45,  93, 161)
    SmokeyTopaz = base.sRGBColor(131,  42,  13)
    TigersEye   = base.sRGBColor(181, 105,  23)

    # Color 'n Smell
    BabysPowder       = base.sRGBColor(255, 255, 255)
    BaseballMitt      = base.sRGBColor(233, 116,  81)
    BubbleBath        = base.sRGBColor(252, 128, 165)
    Earthworm         = base.sRGBColor(198,  45,  66)
    FlowerShop        = base.sRGBColor(201, 160, 220)
    FreshAir          = base.sRGBColor(118, 215, 234)
    GrandmasPerfume   = base.sRGBColor(255, 136,  51)
    KoalaTree         = base.sRGBColor( 41, 171, 135)
    NewSneakers       = base.sRGBColor(  0,   0,   0)
    PetShop           = base.sRGBColor(175,  89,  62)
    PineTree          = base.sRGBColor(  1, 120, 111)
    SawDust           = base.sRGBColor(255, 203, 164)
    SharpeningPencils = base.sRGBColor(252, 214, 103)
    SmellTheRoses     = base.sRGBColor(237,  10,  63)
    SunnyDay          = base.sRGBColor(251, 232, 112)
    WashTheDog        = base.sRGBColor(254, 216,  93)

    # Color Mix-Up
    BabysBlanket        = base.sRGBColor(255, 138, 186)
    BabysBlanket1       = base.sRGBColor( 31, 117, 254)
    BabysBlanket2       = base.sRGBColor( 28, 172, 120)
    BlazingBonfire      = base.sRGBColor(252, 232, 131)
    BlazingBonfire1     = base.sRGBColor(255, 117,  56)
    BlazingBonfire2     = base.sRGBColor(238,  32,  77)
    CoolAndCrazy        = base.sRGBColor(255, 255, 255)
    CoolAndCrazy1       = base.sRGBColor(120,  81, 169)
    CoolAndCrazy2       = base.sRGBColor( 13, 152, 186)
    LemonLimeZing       = base.sRGBColor(252, 232, 131)
    LemonLimeZing1      = base.sRGBColor( 28, 172, 120)
    LemonLimeZing2      = base.sRGBColor( 31, 117, 254)
    MagentaMixUp        = base.sRGBColor(252, 180, 213)
    MagentaMixUp1       = base.sRGBColor( 31, 117, 254)
    MagentaMixUp2       = base.sRGBColor(200,  56,  90)
    MixedVeggies        = base.sRGBColor(182, 182,  80)
    MixedVeggies1       = base.sRGBColor(189,  11,  76)
    MixedVeggies2       = base.sRGBColor(242, 221, 135)
    OffRoad             = base.sRGBColor(222, 170, 136)
    OffRoad1            = base.sRGBColor( 43, 108, 196)
    OffRoad2            = base.sRGBColor(200,  56,  90)
    PeachesNCream       = base.sRGBColor(255, 255, 255)
    PeachesNCream1      = base.sRGBColor(255, 207, 171)
    PeachesNCream2      = base.sRGBColor(252, 232, 131)
    Rainforest          = base.sRGBColor(109, 174, 129)
    Rainforest1         = base.sRGBColor( 93, 118, 203)
    Rainforest2         = base.sRGBColor(120,  81, 169)
    ShrimpCocktail      = base.sRGBColor(255, 255, 255)
    ShrimpCocktail1     = base.sRGBColor(255, 117,  56)
    ShrimpCocktail2     = base.sRGBColor(200,  56,  90)
    Southwest           = base.sRGBColor(255, 255, 255)
    Southwest1          = base.sRGBColor(255, 117,  56)
    Southwest2          = base.sRGBColor( 93, 118, 203)
    StarSpangledBanner  = base.sRGBColor(248, 239, 230)
    StarSpangledBanner1 = base.sRGBColor( 31, 117, 254)
    StarSpangledBanner2 = base.sRGBColor(238,  32,  77)
    Stonewashed         = base.sRGBColor(248, 239, 230)
    Stonewashed1        = base.sRGBColor( 31, 117, 254)
    Stonewashed2        = base.sRGBColor(238,  32,  77)
    SurfsUp             = base.sRGBColor(255, 255, 255)
    SurfsUp1            = base.sRGBColor( 28, 169, 201)
    SurfsUp2            = base.sRGBColor(252, 232, 131)
    Twister             = base.sRGBColor(255, 255, 255)
    Twister1            = base.sRGBColor( 28, 172, 120)
    Twister2            = base.sRGBColor(255, 117,  56)
    WarmAndFuzzy        = base.sRGBColor(255, 138, 186)
    WarmAndFuzzy1       = base.sRGBColor(255, 117,  56)
    WarmAndFuzzy2       = base.sRGBColor( 31, 117, 254)

    # Pearl Brite
    AquaPearl           = base.sRGBColor( 95, 190, 215)
    BlackCoralPearl     = base.sRGBColor( 84,  98, 111)
    CaribbeanGreenPearl = base.sRGBColor(106, 218, 142)
    CulturedPearl       = base.sRGBColor(245, 245, 245)
    KeyLimePearl        = base.sRGBColor(232, 244, 140)
    MandarinPearl       = base.sRGBColor(243, 122,  72)
    MidnightPearl       = base.sRGBColor(112,  38, 112)
    MysticPearl         = base.sRGBColor(214,  82, 130)
    OceanBluePearl      = base.sRGBColor( 79,  66, 181)
    OceanGreenPearl     = base.sRGBColor( 72, 191, 145)
    OrchidPearl         = base.sRGBColor(123,  66,  89)
    RosePearl           = base.sRGBColor(240,  56, 101)
    SalmonPearl         = base.sRGBColor(241,  68,  74)
    SunnyPearl          = base.sRGBColor(242, 242, 122)
    SunsetPearl         = base.sRGBColor(241, 204, 121)
    TurquoisePearl      = base.sRGBColor( 59, 188, 208)
    
    # Metallic FX
    AlloyOrange         = base.sRGBColor(196,  98,  16)
    BdazzledBlue        = base.sRGBColor( 46,  88, 148)
    BigDipORuby         = base.sRGBColor(156,  37,  66)
    BittersweetShimmer  = base.sRGBColor(191,  79,  81)
    BlastOffBronze      = base.sRGBColor(165, 113, 100)
    CyberGrape          = base.sRGBColor( 88,  66, 124)
    DeepSpaceSparkle    = base.sRGBColor( 74, 100, 108)
    GoldFusion          = base.sRGBColor(133, 117,  78)
    IlluminatingEmerald = base.sRGBColor( 49, 145, 119)
    MetallicSeaweed     = base.sRGBColor( 10, 126, 140)
    MetallicSunburst    = base.sRGBColor(156, 124,  56)
    RazzmicBerry        = base.sRGBColor(141,  78, 133)
    SheenGreen          = base.sRGBColor(143, 212,   0)
    ShimmeringBlush     = base.sRGBColor(217, 134, 149)
    SonicSilver         = base.sRGBColor(117, 117, 117)
    SteelBlue           = base.sRGBColor(  0, 129, 171)

    # Silly Scents
    AlienArmpit     = base.sRGBColor(197, 225, 122)
    BigFootFeet     = base.sRGBColor(217, 154, 108)
    BoogerBuster    = base.sRGBColor(236, 235, 189)
    DingyDungeon    = base.sRGBColor(195,  33,  72)
    GargoyleGas     = base.sRGBColor(254, 216,  93)
    GiantsClub      = base.sRGBColor(185,  78,  72)
    MagicPotion     = base.sRGBColor(237,  10,  63)
    MummysTomb      = base.sRGBColor(139, 134, 128)
    OgreOdor        = base.sRGBColor(255, 104,  31)
    PixiePowder     = base.sRGBColor(100,  86, 183)
    PrincessPerfume = base.sRGBColor(252, 128, 165)
    SasquatchSocks  = base.sRGBColor(247,  70, 138)
    SeaSerpent      = base.sRGBColor(  0, 204, 204)
    SmashedPumpkin  = base.sRGBColor(255, 136,  51)
    SunburntCyclops = base.sRGBColor(231, 114,   0)
    WinterWizard    = base.sRGBColor(118, 215, 234)
    
    # Heads 'n Tails
    SizzlingRed    = base.sRGBColor(255,  56,  85)
    RedSalsa       = base.sRGBColor(253,  58,  74)
    TartOrange     = base.sRGBColor(251,  77,  70)
    OrangeSoda     = base.sRGBColor(250,  91,  61)
    BrightYellow   = base.sRGBColor(255, 170,  29)
    YellowSunshine = base.sRGBColor(255, 247,   0)
    SlimyGreen     = base.sRGBColor( 41, 150,  23)
    GreenLizard    = base.sRGBColor(167, 244,  50)
    DenimBlue      = base.sRGBColor( 34,  67, 182)
    BlueJeans      = base.sRGBColor( 93, 173, 236)
    PlumpPurple    = base.sRGBColor( 89,  70, 178)
    PurplePlum     = base.sRGBColor(156,  81, 182)
    SweetBrown     = base.sRGBColor(168,  55,  49)
    BrownSugar     = base.sRGBColor(175, 110,  77)
    EerieBlack     = base.sRGBColor( 27,  27,  27)
    BlackShadows   = base.sRGBColor(191, 175, 178)

    # True to Life
    AmazonForest      = base.sRGBColor(146, 246,  70)
    AmazonForest1     = base.sRGBColor(253, 254,   3)
    AmazonForest2     = base.sRGBColor(203, 251,   7)
    CaribbeanCurrent  = base.sRGBColor( 93, 141, 223)
    CaribbeanCurrent1 = base.sRGBColor(218, 206, 210)
    CaribbeanCurrent2 = base.sRGBColor( 48, 214, 164)
    FloridaSunrise    = base.sRGBColor(255, 179,  41)
    FloridaSunrise1   = base.sRGBColor(255, 216,  44)
    FloridaSunrise2   = base.sRGBColor(255, 204, 107)
    GrandCanyon       = base.sRGBColor(109,  56,  52)
    GrandCanyon1      = base.sRGBColor(179,  96,  88)
    GrandCanyon2      = base.sRGBColor(  0,   0,   0)
    MauiSunset        = base.sRGBColor(142,  89, 159)
    MauiSunset1       = base.sRGBColor(236, 135,  43)
    MauiSunset2       = base.sRGBColor(250, 121, 185)
    MilkyWay          = base.sRGBColor(  7,   7,   7)
    MilkyWay1         = base.sRGBColor(141,  71, 157)
    MilkyWay2         = base.sRGBColor(110, 127, 231)
    SaharaDesert      = base.sRGBColor(245, 203, 189)
    SaharaDesert1     = base.sRGBColor(176, 110,  84)
    SaharaDesert2     = base.sRGBColor(208, 198, 198)
    YosemiteCampfire  = base.sRGBColor(237,  76,  68)
    YosemiteCampfire1 = base.sRGBColor(239, 142,  48)
    YosemiteCampfire2 = base.sRGBColor(169,  94,  52)

    # True to Life
    FieryRose      = base.sRGBColor(255,  84, 112)
    SizzlingSunset = base.sRGBColor(255, 219,   0)
    HeatWave       = base.sRGBColor(255, 122,   0)
    LemonGlacier   = base.sRGBColor(253, 255,   0)
    SpringFrost    = base.sRGBColor(135, 255,  42)
    AbsoluteZero   = base.sRGBColor(  0,  72, 186)
    WinterSky      = base.sRGBColor(255,   0, 124)
    Frostbite      = base.sRGBColor(233,  54, 167)
