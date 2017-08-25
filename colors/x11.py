"""Contains the implementation of the X11 X Windows System color group."""
__all__ = (
    'X11',
)

import enum

from colors import base


class X11(base.ColorGroup):
    """
    The X11 color group.

    In computing, on the X Window System, X11 color names are represented in a
    simple text file, which maps certain strings to RGB color values. It is
    shipped with every X11 installation, hence the name, and is usually located
    in <X11root>/lib/X11/rgb.txt. The web colors list is descended from it but
    differs for certain color names.

    Color names are not standardized by Xlib or the X11 protocol. The list does
    not show continuity either in selected color values or in color names, and
    some color triplets have multiple names. Despite this, graphic designers
    and others got used to them, making it practically impossible to introduce
    a different list. In earlier releases of X11 (prior to the introduction of
    Xcms), server implementors were encouraged to modify the RGB values in the
    reference color database to account for gamma correction.

    See Also:
        `Wikipedia <https://en.wikipedia.org/wiki/X11_color_names>`

    """

    AliceBlue    = base.RGBColor(240, 248, 255)
    AntiqueWhite = base.RGBColor(250, 235, 215)
    Aqua         = base.RGBColor(  0, 255, 255)
    Aquamarine   = base.RGBColor(127, 255, 212)
    Azure        = base.RGBColor(240, 255, 255)

    Beige          = base.RGBColor(245, 245, 220)
    Bisque         = base.RGBColor(255, 228, 196)
    Black          = base.RGBColor(  0,   0,   0)
    BlanchedAlmond = base.RGBColor(255, 235, 205)
    Blue           = base.RGBColor(  0,   0, 255)
    BlueViolet     = base.RGBColor(138,  43, 226)
    Brown          = base.RGBColor(165,  42,  42)
    Burlywood      = base.RGBColor(222, 184, 135)

    CadetBlue  = base.RGBColor( 95, 158, 160)
    Chartreuse = base.RGBColor(127, 255,   0)
    Chocolate  = base.RGBColor(210, 105,  30)
    Coral      = base.RGBColor(255, 127,  80)
    Cornflower = base.RGBColor(100, 149, 237)
    Cornsilk   = base.RGBColor(255, 248, 220)
    Crimson    = base.RGBColor(220,  20,  60)
    Cyan       = base.RGBColor(  0, 255, 255)

    DarkBlue       = base.RGBColor(, , )
    DarkCyan       = base.RGBColor(, , )
    DarkGoldenrod  = base.RGBColor(, , )
    DarkGray       = base.RGBColor(, , )
    DarkGreen      = base.RGBColor(, , )
    DarkKhaki      = base.RGBColor(, , )
    DarkMagenta    = base.RGBColor(, , )
    DarkOliveGreen = base.RGBColor(, , )
    DarkOrange     = base.RGBColor(, , )
    DarkOrchid     = base.RGBColor(, , )
    DarkRed        = base.RGBColor(, , )
    DarkSalmon     = base.RGBColor(, , )
    DarkSeaGreen   = base.RGBColor(, , )
    DarkSlateBlue  = base.RGBColor(, , )
    DarkSlateGray  = base.RGBColor(, , )
    DarkTurquoise  = base.RGBColor(, , )
    DarkViolet     = base.RGBColor(, , )
    DeepPink       = base.RGBColor(, , )
    DeepSkyBlue    = base.RGBColor(, , )
    DimGray        = base.RGBColor(, , )
    DodgerBlue     = base.RGBColor(, , )

    Firebrick   = base.RGBColor(, , )
    FloralWhite = base.RGBColor(, , )
    ForestGreen = base.RGBColor(, , )
    Fuchsia     = base.RGBColor(, , )

    Gainsboro   = base.RGBColor(, , )
    GhostWhite  = base.RGBColor(, , )
    Gold        = base.RGBColor(, , )
    Goldenrod   = base.RGBColor(, , )
    Gray        = base.RGBColor(, , )
    WebGray     = base.RGBColor(, , )
    Green       = base.RGBColor(, , )
    WebGreen    = base.RGBColor(, , )
    GreenYellow = base.RGBColor(, , )

    Honeydew = base.RGBColor(, , )
    HotPink  = base.RGBColor(, , )

    IndianRed = base.RGBColor(, , )
    Indigo    = base.RGBColor(, , )
    Ivory     = base.RGBColor(, , )

    Khaki = base.RGBColor(, , )

    Lavender       = base.RGBColor(, , )
    LavenderBlush  = base.RGBColor(, , )
    LawnGreen      = base.RGBColor(, , )
    LemonChiffon   = base.RGBColor(, , )
    LightBlue      = base.RGBColor(, , )
    LightCoral     = base.RGBColor(, , )
    LightCyan      = base.RGBColor(, , )
    LightGoldenrod = base.RGBColor(, , )
    LightGray      = base.RGBColor(, , )
    LightGreen     = base.RGBColor(, , )
    LightPink      = base.RGBColor(, , )
    LightSalmon    = base.RGBColor(, , )
    LightSeaGreen  = base.RGBColor(, , )
    LightSkyBlue   = base.RGBColor(, , )
    LightSlateGray = base.RGBColor(, , )
    LightSteelBlue = base.RGBColor(, , )
    LightYellow    = base.RGBColor(, , )
    Lime           = base.RGBColor(, , )
    Lime Green     = base.RGBColor(, , )
    Linen          = base.RGBColor(, , )

