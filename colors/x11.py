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

    Beige          = base.RGBColor(, , )
    Bisque         = base.RGBColor(, , )
    Black          = base.RGBColor(, , )
    BlanchedAlmond = base.RGBColor(, , )
    Blue           = base.RGBColor(, , )
    BlueViolet     = base.RGBColor(, , )
    Brown          = base.RGBColor(, , )
    Burlywood      = base.RGBColor(, , )

    CadetBlue  = base.RGBColor(, , )
    Chartreuse = base.RGBColor(, , )
    Chocolate  = base.RGBColor(, , )
    Coral      = base.RGBColor(, , )
    Cornflower = base.RGBColor(, , )
    Cornsilk   = base.RGBColor(, , )
    Crimson    = base.RGBColor(, , )
    Cyan       = base.RGBColor(, , )
