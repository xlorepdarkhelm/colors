"""
Encapsulates a simple Pythonic method to translate colors between systems.

Largely designed to make it a little easier to use a color name from a system
like `X11` colors, and have them translate over to the closest corresponding
`xterm` color index.
"""

__all__ = (
    'RGBColor',
    'HSVColor',
    'HSLColor',
    'ANSI',
    'HTML',
    'Web',
    'Xterm',
    'MaterialDesign',
)

from .base import RGBColor, HSVColor, HSLColor
from .ansi import ANSI
from .html import HTML
from .web import Web
from .xterm import Xterm
from .x11 import X11
from .md import MaterialDesign
