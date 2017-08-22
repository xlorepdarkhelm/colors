import enum

from colors.base import RGBColor


# http://en.wikipedia.org/wiki/Web_colors#X11_color_names
class X11(enum.Enum):
    # Pink colors
    Pink            = RGBColor(255, 192, 203)
    LightPink       = RGBColor(255, 182, 193)
    HotPink         = RGBColor(255, 105, 180)
    DeepPink        = RGBColor(255,  20, 147)
    PaleVioletRed   = RGBColor(219, 112, 147)
    MediumVioletRed = RGBColor(199,  21, 133)

    # Red colors
    LightSalmon = RGBColor(255, 160, 122)
    Salmon      = RGBColor(250, 128, 114)
    DarkSalmon  = RGBColor(233, 150, 122)
    LightCoral  = RGBColor(240, 128, 128)
    IndianRed   = RGBColor(205,  92,  92)
    Crimson     = RGBColor(220,  20,  60)
    FireBrick   = RGBColor(178,  34,  34)
    DarkRed     = RGBColor(139,   0,   0)
    Red         = RGBColor(255,   0,   0)

    # Orange colors
    OrangeRed  = RGBColor(255,  69,   0)
    Tomato     = RGBColor(255,  99,  71)
    Coral      = RGBColor(255, 127,  80)
    DarkOrange = RGBColor(255, 140,   0)
    Orange     = RGBColor(255, 165,   0)

    # Yellow colors
    Yellow               = RGBColor(255, 255,   0)
    LightYellow          = RGBColor(255, 255, 224)
    LemonChiffon         = RGBColor(255, 250, 205)
    LightGoldenrodYellow = RGBColor(250, 250, 210)
    PapayaWhip           = RGBColor(255, 239, 213)
    Moccasin             = RGBColor(255, 228, 181)
    PeachPuff            = RGBColor(255, 218, 185)
    PaleGoldenrod        = RGBColor(238, 232, 170)
    Khaki                = RGBColor(240, 230, 140)
    DarkKhaki            = RGBColor(189, 183, 107)
    Gold                 = RGBColor(255, 215,   0)

    # Brown colors
    Cornsilk       = RGBColor(255, 248, 220)
    BlanchedAlmond = RGBColor(255, 235, 205)
    Bisque         = RGBColor(255, 228, 196)
    NavajoWhite    = RGBColor(255, 222, 173)
    Wheat          = RGBColor(245, 222, 173)
    BurlyWood      = RGBColor(222, 184, 135)
    Tan            = RGBColor(210, 180, 140)
    RosyBrown      = RGBColor(188, 143, 143)
    SandyBrown     = RGBColor(244, 164,  96)
    Goldenrod      = RGBColor(218, 165,  32)
    DarkGoldenrod  = RGBColor(184, 134,  11)
    Peru           = RGBColor(205, 133,  63)
    Chocolate      = RGBColor(210, 105,  30)
    SaddleBrown    = RGBColor(139,  69,  19)
    Sienna         = RGBColor(160,  82,  45)
    Brown          = RGBColor(165,  42,  42)
    Maroon         = RGBColor(128,   0,   0)

    # Green colors
    DarkOliveGreen    = RGBColor( 85, 107,  47)
    Olive             = RGBColor(128, 128,   0)
    OliveDrab         = RGBColor(107, 142,  35)
    YellowGreen       = RGBColor(154, 205,  50)
    LimeGreen         = RGBColor( 50, 205,  50)
    Lime              = RGBColor(  0, 255,   0)
    LawnGreen         = RGBColor(124, 252,   0)
    Chartreuse        = RGBColor(127, 255,   0)
    GreenYellow       = RGBColor(173, 255,  47)
    SpringGreen       = RGBColor(  0, 255, 127)
    MediumSpringGreen = RGBColor(  0, 250, 154)
    LightGreen        = RGBColor(144, 238, 144)
    PaleGreen         = RGBColor(152, 251, 152)
    DarkSeaGreen      = RGBColor(143, 188, 143)
    MediumSeaGreen    = RGBColor( 80, 179, 113)
    SeaGreen          = RGBColor( 46, 139,  87)
    ForestGreen       = RGBColor( 34, 139,  34)
    Green             = RGBColor(  0, 128,   0)
    DarkGreen         = RGBColor(  0, 100,   0)

    # Cyan colors
    MediumAquamarine = RGBColor(102, 205, 170)
    Aqua             = RGBColor(  0, 255, 255)
    Cyan             = RGBColor(  0, 255, 255)
    LightCyan        = RGBColor(224, 255, 255)
    PaleTurquoise    = RGBColor(175, 238, 238)
    Aquamarine       = RGBColor(127, 255, 212)
    Turquiose        = RGBColor( 64, 224, 208)
    MediumTurquoise  = RGBColor( 72, 209, 204)
    DarkTurquoise    = RGBColor(  0, 206, 209)
    LightSeaGreen    = RGBColor( 32, 178, 170)
    CadetBlue        = RGBColor( 95, 158, 160)
    DarkCyan         = RGBColor(  0, 139, 139)
    Teal             = RGBColor(  0, 128, 128)

    # Blue colors
    LightSteelBlue = RGBColor(176, 196, 222)
    PowderBlue     = RGBColor(176, 224, 230)
    LightBlue      = RGBColor(173, 216, 230)
    SkyBlue        = RGBColor(135, 206, 235)
    LightSkyBlue   = RGBColor(135, 206, 250)
    DeepSkyBlue    = RGBColor(  0, 191, 255)
    DodgerBlue     = RGBColor( 30, 144, 255)
    CornflowerBlue = RGBColor(100, 149, 237)
    SteelBlue      = RGBColor( 70, 130, 180)
    RoyalBlue      = RGBColor( 65, 105, 225)
    Blue           = RGBColor(  0,   0, 255)
    MediumBlue     = RGBColor(  0,   0, 205)
    DarkBlue       = RGBColor(  0,   0, 139)
    Navy           = RGBColor(  0,   0, 128)
    MidnightBlue   = RGBColor( 25,  25, 112)

    # Purple colors
    Lavender        = RGBColor(230, 230, 250)
    Thistle         = RGBColor(216, 191, 216)
    Plum            = RGBColor(221, 160, 221)
    Violet          = RGBColor(238, 130, 238)
    Orchid          = RGBColor(218, 112, 214)
    Fuchsia         = RGBColor(255,   0, 255)
    Magenta         = RGBColor(255,   0, 255)
    MediumOrchid    = RGBColor(186,  85, 211)
    MediumPurple    = RGBColor(147, 112, 219)
    BlueViolet      = RGBColor(138,  43, 226)
    DarkViolet      = RGBColor(148,   0, 211)
    DarkOrchid      = RGBColor(153,  50, 204)
    DarkMagenta     = RGBColor(139,   0, 139)
    Purple          = RGBColor(128,   0, 128)
    Indigo          = RGBColor( 75,   0, 130)
    DarkSlateBlue   = RGBColor( 72,  61, 139)
    RebeccaPurple   = RGBColor(102,  51, 153)
    SlateBlue       = RGBColor(106,  90, 205)
    MediumSlateBlue = RGBColor(123, 104, 238)

    # White colors
    White         = RGBColor(255, 255, 255)
    Snow          = RGBColor(255, 250, 250)
    Honeydew      = RGBColor(240, 255, 240)
    MintCream     = RGBColor(245, 255, 250)
    Azure         = RGBColor(240, 255, 255)
    AliceBlue     = RGBColor(240, 248, 255)
    GhostWhite    = RGBColor(248, 248, 255)
    WhiteSmoke    = RGBColor(245, 245, 245)
    SeaShell      = RGBColor(255, 245, 220)
    Beige         = RGBColor(245, 245, 220)
    OldLace       = RGBColor(253, 245, 230)
    FloralWhite   = RGBColor(255, 250, 240)
    Ivory         = RGBColor(255, 255, 240)
    AntiqueWhite  = RGBColor(250, 235, 215)
    Linen         = RGBColor(250, 240, 230)
    LavenderBlush = RGBColor(255, 240, 245)
    MistyRose     = RGBColor(255, 228, 225)

    # Gray/Black colors
    Gainsboro      = RGBColor(220, 220, 220)
    LightGray      = RGBColor(211, 211, 211)
    Silver         = RGBColor(192, 192, 192)
    DarkGray       = RGBColor(169, 169, 169)
    Gray           = RGBColor(128, 128, 128)
    DimGray        = RGBColor(105, 105, 105)
    LightSlateGray = RGBColor(119, 136, 153)
    SlateGray      = RGBColor(112, 128, 144)
    DarkSlateGray  = RGBColor( 47,  79,  79)
    Black          = RGBColor(  0,   0,   0)
