"""Contains the implementation of the named Web colors used by browsers."""
__all__ = (
    'Web',
)

import enum

from colors import base


class Web(base.ColorGroup):
    """
    The standard named web color group.

    A number of colors are defined by web browsers. A particular browser may
    not recognize all of these colors, but as of 2005 all modern,
    general-use, graphical browsers support the full list of colors. Many of
    these colors are from the list of X11 color names distributed with the X
    Window System. These colors were standardized by SVG 1.0, and are
    accepted by SVG Full user agents. They are not part of SVG Tiny.

    The list of colors shipped with the X11 product varies between
    implementations, and clashes with certain of the HTML names such as
    green. X11 colors are defined as simple RGB (hence, no particular color
    space), rather than sRGB. This means that the list of colors found in X11
    (e.g., in /usr/lib/X11/rgb.txt) should not directly be used to choose
    colors for the web.

    See Also:
        `Wikipedia <http://en.wikipedia.org/wiki/Web_colors#X11_color_names>`

    """

    # Pink colors
    Pink            = base.sRGBColor(255, 192, 203)
    LightPink       = base.sRGBColor(255, 182, 193)
    HotPink         = base.sRGBColor(255, 105, 180)
    DeepPink        = base.sRGBColor(255,  20, 147)
    PaleVioletRed   = base.sRGBColor(219, 112, 147)
    MediumVioletRed = base.sRGBColor(199,  21, 133)

    # Red colors
    LightSalmon = base.sRGBColor(255, 160, 122)
    Salmon      = base.sRGBColor(250, 128, 114)
    DarkSalmon  = base.sRGBColor(233, 150, 122)
    LightCoral  = base.sRGBColor(240, 128, 128)
    IndianRed   = base.sRGBColor(205,  92,  92)
    Crimson     = base.sRGBColor(220,  20,  60)
    FireBrick   = base.sRGBColor(178,  34,  34)
    DarkRed     = base.sRGBColor(139,   0,   0)
    Red         = base.sRGBColor(255,   0,   0)

    # Orange colors
    OrangeRed  = base.sRGBColor(255,  69,   0)
    Tomato     = base.sRGBColor(255,  99,  71)
    Coral      = base.sRGBColor(255, 127,  80)
    DarkOrange = base.sRGBColor(255, 140,   0)
    Orange     = base.sRGBColor(255, 165,   0)

    # Yellow colors
    Yellow               = base.sRGBColor(255, 255,   0)
    LightYellow          = base.sRGBColor(255, 255, 224)
    LemonChiffon         = base.sRGBColor(255, 250, 205)
    LightGoldenrodYellow = base.sRGBColor(250, 250, 210)
    PapayaWhip           = base.sRGBColor(255, 239, 213)
    Moccasin             = base.sRGBColor(255, 228, 181)
    PeachPuff            = base.sRGBColor(255, 218, 185)
    PaleGoldenrod        = base.sRGBColor(238, 232, 170)
    Khaki                = base.sRGBColor(240, 230, 140)
    DarkKhaki            = base.sRGBColor(189, 183, 107)
    Gold                 = base.sRGBColor(255, 215,   0)

    # Brown colors
    Cornsilk       = base.sRGBColor(255, 248, 220)
    BlanchedAlmond = base.sRGBColor(255, 235, 205)
    Bisque         = base.sRGBColor(255, 228, 196)
    NavajoWhite    = base.sRGBColor(255, 222, 173)
    Wheat          = base.sRGBColor(245, 222, 173)
    BurlyWood      = base.sRGBColor(222, 184, 135)
    Tan            = base.sRGBColor(210, 180, 140)
    RosyBrown      = base.sRGBColor(188, 143, 143)
    SandyBrown     = base.sRGBColor(244, 164,  96)
    Goldenrod      = base.sRGBColor(218, 165,  32)
    DarkGoldenrod  = base.sRGBColor(184, 134,  11)
    Peru           = base.sRGBColor(205, 133,  63)
    Chocolate      = base.sRGBColor(210, 105,  30)
    SaddleBrown    = base.sRGBColor(139,  69,  19)
    Sienna         = base.sRGBColor(160,  82,  45)
    Brown          = base.sRGBColor(165,  42,  42)
    Maroon         = base.sRGBColor(128,   0,   0)

    # Green colors
    DarkOliveGreen    = base.sRGBColor( 85, 107,  47)
    Olive             = base.sRGBColor(128, 128,   0)
    OliveDrab         = base.sRGBColor(107, 142,  35)
    YellowGreen       = base.sRGBColor(154, 205,  50)
    LimeGreen         = base.sRGBColor( 50, 205,  50)
    Lime              = base.sRGBColor(  0, 255,   0)
    LawnGreen         = base.sRGBColor(124, 252,   0)
    Chartreuse        = base.sRGBColor(127, 255,   0)
    GreenYellow       = base.sRGBColor(173, 255,  47)
    SpringGreen       = base.sRGBColor(  0, 255, 127)
    MediumSpringGreen = base.sRGBColor(  0, 250, 154)
    LightGreen        = base.sRGBColor(144, 238, 144)
    PaleGreen         = base.sRGBColor(152, 251, 152)
    DarkSeaGreen      = base.sRGBColor(143, 188, 143)
    MediumSeaGreen    = base.sRGBColor( 80, 179, 113)
    SeaGreen          = base.sRGBColor( 46, 139,  87)
    ForestGreen       = base.sRGBColor( 34, 139,  34)
    Green             = base.sRGBColor(  0, 128,   0)
    DarkGreen         = base.sRGBColor(  0, 100,   0)

    # Cyan colors
    MediumAquamarine = base.sRGBColor(102, 205, 170)
    Aqua             = base.sRGBColor(  0, 255, 255)
    Cyan             = base.sRGBColor(  0, 255, 255)
    LightCyan        = base.sRGBColor(224, 255, 255)
    PaleTurquoise    = base.sRGBColor(175, 238, 238)
    Aquamarine       = base.sRGBColor(127, 255, 212)
    Turquiose        = base.sRGBColor( 64, 224, 208)
    MediumTurquoise  = base.sRGBColor( 72, 209, 204)
    DarkTurquoise    = base.sRGBColor(  0, 206, 209)
    LightSeaGreen    = base.sRGBColor( 32, 178, 170)
    CadetBlue        = base.sRGBColor( 95, 158, 160)
    DarkCyan         = base.sRGBColor(  0, 139, 139)
    Teal             = base.sRGBColor(  0, 128, 128)

    # Blue colors
    LightSteelBlue = base.sRGBColor(176, 196, 222)
    PowderBlue     = base.sRGBColor(176, 224, 230)
    LightBlue      = base.sRGBColor(173, 216, 230)
    SkyBlue        = base.sRGBColor(135, 206, 235)
    LightSkyBlue   = base.sRGBColor(135, 206, 250)
    DeepSkyBlue    = base.sRGBColor(  0, 191, 255)
    DodgerBlue     = base.sRGBColor( 30, 144, 255)
    CornflowerBlue = base.sRGBColor(100, 149, 237)
    SteelBlue      = base.sRGBColor( 70, 130, 180)
    RoyalBlue      = base.sRGBColor( 65, 105, 225)
    Blue           = base.sRGBColor(  0,   0, 255)
    MediumBlue     = base.sRGBColor(  0,   0, 205)
    DarkBlue       = base.sRGBColor(  0,   0, 139)
    Navy           = base.sRGBColor(  0,   0, 128)
    MidnightBlue   = base.sRGBColor( 25,  25, 112)

    # Purple colors
    Lavender        = base.sRGBColor(230, 230, 250)
    Thistle         = base.sRGBColor(216, 191, 216)
    Plum            = base.sRGBColor(221, 160, 221)
    Violet          = base.sRGBColor(238, 130, 238)
    Orchid          = base.sRGBColor(218, 112, 214)
    Fuchsia         = base.sRGBColor(255,   0, 255)
    Magenta         = base.sRGBColor(255,   0, 255)
    MediumOrchid    = base.sRGBColor(186,  85, 211)
    MediumPurple    = base.sRGBColor(147, 112, 219)
    BlueViolet      = base.sRGBColor(138,  43, 226)
    DarkViolet      = base.sRGBColor(148,   0, 211)
    DarkOrchid      = base.sRGBColor(153,  50, 204)
    DarkMagenta     = base.sRGBColor(139,   0, 139)
    Purple          = base.sRGBColor(128,   0, 128)
    Indigo          = base.sRGBColor( 75,   0, 130)
    DarkSlateBlue   = base.sRGBColor( 72,  61, 139)
    RebeccaPurple   = base.sRGBColor(102,  51, 153)
    SlateBlue       = base.sRGBColor(106,  90, 205)
    MediumSlateBlue = base.sRGBColor(123, 104, 238)

    # White colors
    White         = base.sRGBColor(255, 255, 255)
    Snow          = base.sRGBColor(255, 250, 250)
    Honeydew      = base.sRGBColor(240, 255, 240)
    MintCream     = base.sRGBColor(245, 255, 250)
    Azure         = base.sRGBColor(240, 255, 255)
    AliceBlue     = base.sRGBColor(240, 248, 255)
    GhostWhite    = base.sRGBColor(248, 248, 255)
    WhiteSmoke    = base.sRGBColor(245, 245, 245)
    SeaShell      = base.sRGBColor(255, 245, 220)
    Beige         = base.sRGBColor(245, 245, 220)
    OldLace       = base.sRGBColor(253, 245, 230)
    FloralWhite   = base.sRGBColor(255, 250, 240)
    Ivory         = base.sRGBColor(255, 255, 240)
    AntiqueWhite  = base.sRGBColor(250, 235, 215)
    Linen         = base.sRGBColor(250, 240, 230)
    LavenderBlush = base.sRGBColor(255, 240, 245)
    MistyRose     = base.sRGBColor(255, 228, 225)

    # Gray/Black colors
    Gainsboro      = base.sRGBColor(220, 220, 220)
    LightGray      = base.sRGBColor(211, 211, 211)
    Silver         = base.sRGBColor(192, 192, 192)
    DarkGray       = base.sRGBColor(169, 169, 169)
    Gray           = base.sRGBColor(128, 128, 128)
    DimGray        = base.sRGBColor(105, 105, 105)
    LightSlateGray = base.sRGBColor(119, 136, 153)
    SlateGray      = base.sRGBColor(112, 128, 144)
    DarkSlateGray  = base.sRGBColor( 47,  79,  79)
    Black          = base.sRGBColor(  0,   0,   0)
