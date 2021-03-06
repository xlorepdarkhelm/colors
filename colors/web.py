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
    Pink            = base.RGBColor(255, 192, 203)
    LightPink       = base.RGBColor(255, 182, 193)
    HotPink         = base.RGBColor(255, 105, 180)
    DeepPink        = base.RGBColor(255,  20, 147)
    PaleVioletRed   = base.RGBColor(219, 112, 147)
    MediumVioletRed = base.RGBColor(199,  21, 133)

    # Red colors
    LightSalmon = base.RGBColor(255, 160, 122)
    Salmon      = base.RGBColor(250, 128, 114)
    DarkSalmon  = base.RGBColor(233, 150, 122)
    LightCoral  = base.RGBColor(240, 128, 128)
    IndianRed   = base.RGBColor(205,  92,  92)
    Crimson     = base.RGBColor(220,  20,  60)
    FireBrick   = base.RGBColor(178,  34,  34)
    DarkRed     = base.RGBColor(139,   0,   0)
    Red         = base.RGBColor(255,   0,   0)

    # Orange colors
    OrangeRed  = base.RGBColor(255,  69,   0)
    Tomato     = base.RGBColor(255,  99,  71)
    Coral      = base.RGBColor(255, 127,  80)
    DarkOrange = base.RGBColor(255, 140,   0)
    Orange     = base.RGBColor(255, 165,   0)

    # Yellow colors
    Yellow               = base.RGBColor(255, 255,   0)
    LightYellow          = base.RGBColor(255, 255, 224)
    LemonChiffon         = base.RGBColor(255, 250, 205)
    LightGoldenrodYellow = base.RGBColor(250, 250, 210)
    PapayaWhip           = base.RGBColor(255, 239, 213)
    Moccasin             = base.RGBColor(255, 228, 181)
    PeachPuff            = base.RGBColor(255, 218, 185)
    PaleGoldenrod        = base.RGBColor(238, 232, 170)
    Khaki                = base.RGBColor(240, 230, 140)
    DarkKhaki            = base.RGBColor(189, 183, 107)
    Gold                 = base.RGBColor(255, 215,   0)

    # Brown colors
    Cornsilk       = base.RGBColor(255, 248, 220)
    BlanchedAlmond = base.RGBColor(255, 235, 205)
    Bisque         = base.RGBColor(255, 228, 196)
    NavajoWhite    = base.RGBColor(255, 222, 173)
    Wheat          = base.RGBColor(245, 222, 173)
    BurlyWood      = base.RGBColor(222, 184, 135)
    Tan            = base.RGBColor(210, 180, 140)
    RosyBrown      = base.RGBColor(188, 143, 143)
    SandyBrown     = base.RGBColor(244, 164,  96)
    Goldenrod      = base.RGBColor(218, 165,  32)
    DarkGoldenrod  = base.RGBColor(184, 134,  11)
    Peru           = base.RGBColor(205, 133,  63)
    Chocolate      = base.RGBColor(210, 105,  30)
    SaddleBrown    = base.RGBColor(139,  69,  19)
    Sienna         = base.RGBColor(160,  82,  45)
    Brown          = base.RGBColor(165,  42,  42)
    Maroon         = base.RGBColor(128,   0,   0)

    # Green colors
    DarkOliveGreen    = base.RGBColor( 85, 107,  47)
    Olive             = base.RGBColor(128, 128,   0)
    OliveDrab         = base.RGBColor(107, 142,  35)
    YellowGreen       = base.RGBColor(154, 205,  50)
    LimeGreen         = base.RGBColor( 50, 205,  50)
    Lime              = base.RGBColor(  0, 255,   0)
    LawnGreen         = base.RGBColor(124, 252,   0)
    Chartreuse        = base.RGBColor(127, 255,   0)
    GreenYellow       = base.RGBColor(173, 255,  47)
    SpringGreen       = base.RGBColor(  0, 255, 127)
    MediumSpringGreen = base.RGBColor(  0, 250, 154)
    LightGreen        = base.RGBColor(144, 238, 144)
    PaleGreen         = base.RGBColor(152, 251, 152)
    DarkSeaGreen      = base.RGBColor(143, 188, 143)
    MediumSeaGreen    = base.RGBColor( 80, 179, 113)
    SeaGreen          = base.RGBColor( 46, 139,  87)
    ForestGreen       = base.RGBColor( 34, 139,  34)
    Green             = base.RGBColor(  0, 128,   0)
    DarkGreen         = base.RGBColor(  0, 100,   0)

    # Cyan colors
    MediumAquamarine = base.RGBColor(102, 205, 170)
    Aqua             = base.RGBColor(  0, 255, 255)
    Cyan             = base.RGBColor(  0, 255, 255)
    LightCyan        = base.RGBColor(224, 255, 255)
    PaleTurquoise    = base.RGBColor(175, 238, 238)
    Aquamarine       = base.RGBColor(127, 255, 212)
    Turquiose        = base.RGBColor( 64, 224, 208)
    MediumTurquoise  = base.RGBColor( 72, 209, 204)
    DarkTurquoise    = base.RGBColor(  0, 206, 209)
    LightSeaGreen    = base.RGBColor( 32, 178, 170)
    CadetBlue        = base.RGBColor( 95, 158, 160)
    DarkCyan         = base.RGBColor(  0, 139, 139)
    Teal             = base.RGBColor(  0, 128, 128)

    # Blue colors
    LightSteelBlue = base.RGBColor(176, 196, 222)
    PowderBlue     = base.RGBColor(176, 224, 230)
    LightBlue      = base.RGBColor(173, 216, 230)
    SkyBlue        = base.RGBColor(135, 206, 235)
    LightSkyBlue   = base.RGBColor(135, 206, 250)
    DeepSkyBlue    = base.RGBColor(  0, 191, 255)
    DodgerBlue     = base.RGBColor( 30, 144, 255)
    CornflowerBlue = base.RGBColor(100, 149, 237)
    SteelBlue      = base.RGBColor( 70, 130, 180)
    RoyalBlue      = base.RGBColor( 65, 105, 225)
    Blue           = base.RGBColor(  0,   0, 255)
    MediumBlue     = base.RGBColor(  0,   0, 205)
    DarkBlue       = base.RGBColor(  0,   0, 139)
    Navy           = base.RGBColor(  0,   0, 128)
    MidnightBlue   = base.RGBColor( 25,  25, 112)

    # Purple colors
    Lavender        = base.RGBColor(230, 230, 250)
    Thistle         = base.RGBColor(216, 191, 216)
    Plum            = base.RGBColor(221, 160, 221)
    Violet          = base.RGBColor(238, 130, 238)
    Orchid          = base.RGBColor(218, 112, 214)
    Fuchsia         = base.RGBColor(255,   0, 255)
    Magenta         = base.RGBColor(255,   0, 255)
    MediumOrchid    = base.RGBColor(186,  85, 211)
    MediumPurple    = base.RGBColor(147, 112, 219)
    BlueViolet      = base.RGBColor(138,  43, 226)
    DarkViolet      = base.RGBColor(148,   0, 211)
    DarkOrchid      = base.RGBColor(153,  50, 204)
    DarkMagenta     = base.RGBColor(139,   0, 139)
    Purple          = base.RGBColor(128,   0, 128)
    Indigo          = base.RGBColor( 75,   0, 130)
    DarkSlateBlue   = base.RGBColor( 72,  61, 139)
    RebeccaPurple   = base.RGBColor(102,  51, 153)
    SlateBlue       = base.RGBColor(106,  90, 205)
    MediumSlateBlue = base.RGBColor(123, 104, 238)

    # White colors
    White         = base.RGBColor(255, 255, 255)
    Snow          = base.RGBColor(255, 250, 250)
    Honeydew      = base.RGBColor(240, 255, 240)
    MintCream     = base.RGBColor(245, 255, 250)
    Azure         = base.RGBColor(240, 255, 255)
    AliceBlue     = base.RGBColor(240, 248, 255)
    GhostWhite    = base.RGBColor(248, 248, 255)
    WhiteSmoke    = base.RGBColor(245, 245, 245)
    SeaShell      = base.RGBColor(255, 245, 220)
    Beige         = base.RGBColor(245, 245, 220)
    OldLace       = base.RGBColor(253, 245, 230)
    FloralWhite   = base.RGBColor(255, 250, 240)
    Ivory         = base.RGBColor(255, 255, 240)
    AntiqueWhite  = base.RGBColor(250, 235, 215)
    Linen         = base.RGBColor(250, 240, 230)
    LavenderBlush = base.RGBColor(255, 240, 245)
    MistyRose     = base.RGBColor(255, 228, 225)

    # Gray/Black colors
    Gainsboro      = base.RGBColor(220, 220, 220)
    LightGray      = base.RGBColor(211, 211, 211)
    Silver         = base.RGBColor(192, 192, 192)
    DarkGray       = base.RGBColor(169, 169, 169)
    Gray           = base.RGBColor(128, 128, 128)
    DimGray        = base.RGBColor(105, 105, 105)
    LightSlateGray = base.RGBColor(119, 136, 153)
    SlateGray      = base.RGBColor(112, 128, 144)
    DarkSlateGray  = base.RGBColor( 47,  79,  79)
    Black          = base.RGBColor(  0,   0,   0)
