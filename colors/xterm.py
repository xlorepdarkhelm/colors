import collections.abc
import colorsys
import enum
import functools
import typing

from colors import RGBColor


XtermColors = (
    # ANSI colors
    RGBColor(  0,   0,   0),  # Black
    RGBColor(128,   0,   0),  # Maroon
    RGBColor(  0, 128,   0),  # Green
    RGBColor(128, 128,   0),  # Olive
    RGBColor(  0,   0, 128),  # Navy
    RGBColor(128,   0, 128),  # Purple
    RGBColor(  0, 128, 128),  # Teal
    RGBColor(192, 192, 192),  # Silver
    RGBColor(128, 128, 128),  # Gray
    RGBColor(255,   0,   0),  # Red
    RGBColor(  0, 255,   0),  # Lime
    RGBColor(255, 255,   0),  # Yellow
    RGBColor(  0,   0, 255),  # Blue
    RGBColor(255,   0, 255),  # Magenta
    RGBColor(  0, 255, 255),  # Cyan
    RGBColor(255, 255, 255),  # White

    # 6x6x6 Cube
    RGBColor(  0,   0,   0),  # Gray0
    RGBColor(  0,   0,  95),  # NavyBlue
    RGBColor(  0,   0, 135),  # DarkBlue
    RGBColor(  0,   0, 175),  # Blue3
    RGBColor(  0,   0, 215),  # Blue3
    RGBColor(  0,   0, 255),  # Blue1
    RGBColor(  0,  95,   0),  # DarkGreen
    RGBColor(  0,  95,  95),  # DeepSkyBlue4
    RGBColor(  0,  95, 135),  # DeepSkyBlue4
    RGBColor(  0,  95, 175),  # DeepSkyBlue4
    RGBColor(  0,  95, 215),  # DodgerBlue3
    RGBColor(  0,  95, 255),  # DodgetBlue2
    RGBColor(  0, 135,   0),  # Green4
    RGBColor(  0, 135,  95),  # SpringGreen4
    RGBColor(  0, 135, 135),  # Turquoise4
    RGBColor(  0, 135, 175),  # DeepSkyBlue3
    RGBColor(  0, 135, 215),  # DeepSkyBlue3
    RGBColor(  0, 135, 255),  # DodgerBlue1
    RGBColor(  0, 175,   0),  # Green3
    RGBColor(  0, 175,  95),  # SpringGreen3
    RGBColor(  0, 175, 135),  # DarkCyan
    RGBColor(  0, 175, 175),  # LightSeaGreen
    RGBColor(  0, 175, 215),  # DeepSkyBlue2
    RGBColor(  0, 175, 255),  # DeepSkyBlue1
    RGBColor(  0, 215,   0),  # Green3
    RGBColor(  0, 215,  95),  # SpringGreen3
    RGBColor(  0, 215, 135),  # SpringGreen2
    RGBColor(  0, 215, 175),  # Cyan3
    RGBColor(  0, 215, 215),  # DarkTurquoise
    RGBColor(  0, 215, 255),  # Turquoise2
    RGBColor(  0, 255,   0),  # Green1
    RGBColor(  0, 255,  95),  # SpringGreen2
    RGBColor(  0, 255, 135),  # SpringGreen1
    RGBColor(  0, 255, 175),  # MediumSpringGreen
    RGBColor(  0, 255, 215),  # Cyan2
    RGBColor(  0, 255, 255),  # Cyan1
    RGBColor( 95,   0,   0),  # DarkRed
    RGBColor( 95,   0,  95),  # DeepPink4
    RGBColor( 95,   0, 135),  # Purple4
    RGBColor( 95,   0, 175),  # Purple4
    RGBColor( 95,   0, 215),  # Purple3
    RGBColor( 95,   0, 255),  # BlueViolet
    RGBColor( 95,  95,   0),  # Orange4
    RGBColor( 95,  95,  95),  # Gray37
    RGBColor( 95,  95, 135),  # MediumPurple4
    RGBColor( 95,  95, 175),  # SlateBlue3
    RGBColor( 95,  95, 215),  # SlateBlue3
    RGBColor( 95,  95, 255),  # RoyalBlue1
    RGBColor( 95, 135,   0),  # Chartreuse4
    RGBColor( 95, 135,  95),  # DarkSeaGreen4
    RGBColor( 95, 135, 135),  # PaleTurquoise4
    RGBColor( 95, 135, 175),  # SteelBlue
    RGBColor( 95, 135, 215),  # SteelBlue3
    RGBColor( 95, 135, 255),  # CornflowerBlue
    RGBColor( 95, 175,   0),  # Chartreuse3
    RGBColor( 95, 175,  95),  # DarkSeaGreen4
    RGBColor( 95, 175, 135),  # CadetBlue
    RGBColor( 95, 175, 175),  # CadetBlue
    RGBColor( 95, 175, 215),  # SkyBlue3
    RGBColor( 95, 175, 255),  # SteelBlue1
    RGBColor( 95, 215,   0),  # Cartreuse3
    RGBColor( 95, 215,  95),  # PaleGreen3
    RGBColor( 95, 215, 135),  # SeaGreen3
    RGBColor( 95, 215, 175),  # Aquamarine3
    RGBColor( 95, 215, 215),  # MediumTurquoise
    RGBColor( 95, 215, 255),  # SteelBlue1
    RGBColor( 95, 255,   0),  # Chartreuse2
    RGBColor( 95, 255,  95),  # SeaGreen2
    RGBColor( 95, 255, 135),  # SeaGreen1
    RGBColor( 95, 255, 175),  # SeaGreen1
    RGBColor( 95, 255, 215),  # Aquamarine1
    RGBColor( 95, 255, 255),  # DarkSlateGray2
    RGBColor(135,   0,   0),  # DarkRed
    RGBColor(135,   0,  95),  # DeepPink4
    RGBColor(135,   0, 135),  # DarkMagenta
    RGBColor(135,   0, 175),  # DarkMagenta
    RGBColor(135,   0, 215),  # DarkViolet
    RGBColor(135,   0, 255),  # Purple
    RGBColor(135,  95,   0),  # Orange4
    RGBColor(135,  95,  95),  # LightPink4
    RGBColor(135,  95, 135),  # Plum4
    RGBColor(135,  95, 175),  # MediumPurple3
    RGBColor(135,  95, 215),  # MediumPurple3
    RGBColor(135,  95, 255),  # SlateBlue1
    RGBColor(135, 135,   0),  # Yellow4
    RGBColor(135, 135,  95),  # Wheat4
    RGBColor(135, 135, 135),  # Gray53
    RGBColor(135, 135, 175),  # LightSlateGray
    RGBColor(135, 135, 215),  # MediumPurple
    RGBColor(135, 135, 255),  # LightSlateBlue
    RGBColor(135, 175,   0),  # Yellow4
    RGBColor(135, 175,  95),  # DarkOliveGreen3
    RGBColor(135, 175, 135),  # DarkSeaGreen
    RGBColor(135, 175, 175),  # LightSkyBlue3
    RGBColor(135, 175, 215),  # LightSkyBlue3
    RGBColor(135, 175, 255),  # SkyBlue2
    RGBColor(135, 215,   0),  # Chartreuse2
    RGBColor(135, 215,  95),  # DarkOliveGreen3
    RGBColor(135, 215, 135),  # PaleGreen3
    RGBColor(135, 215, 175),  # DarkSeaGreen3
    RGBColor(135, 215, 215),  # DarkSlateGray3
    RGBColor(135, 215, 255),  # SkyBlue1
    RGBColor(135, 255,   0),  # Chartreuse1
    RGBColor(135, 255,  95),  # LightGreen
    RGBColor(135, 255, 135),  # LightGreen
    RGBColor(135, 255, 175),  # PaleGreen1
    RGBColor(135, 255, 215),  # Aquamarine1
    RGBColor(135, 255, 255),  # DarkSlateGray1
    RGBColor(175,   0,   0),  # Red3
    RGBColor(175,   0,  95),  # DeepPink4
    RGBColor(175,   0, 135),  # MediumVioletRed
    RGBColor(175,   0, 175),  # Magenta3
    RGBColor(175,   0, 215),  # DarkViolet
    RGBColor(175,   0, 255),  # Purple
    RGBColor(175,  95,   0),  # DarkOrange3
    RGBColor(175,  95,  95),  # IndianRed
    RGBColor(175,  95, 135),  # HotPink3
    RGBColor(175,  95, 175),  # MediumOrchid3
    RGBColor(175,  95, 215),  # MediumOrchid
    RGBColor(175,  95, 255),  # MediumPurple2
    RGBColor(175, 135,   0),  # DarkGoldenrod
    RGBColor(175, 135,  95),  # LightSalmon3
    RGBColor(175, 135, 135),  # RosyBrown
    RGBColor(175, 135, 175),  # Gray63
    RGBColor(175, 135, 215),  # MediumPurple2
    RGBColor(175, 135, 255),  # MediumPurple1
    RGBColor(175, 175,   0),  # Gold3
    RGBColor(175, 175,  95),  # DarkKhaki
    RGBColor(175, 175, 135),  # NavajoWhite
    RGBColor(175, 175, 175),  # Gray69
    RGBColor(175, 175, 215),  # LightSteelBlue3
    RGBColor(175, 175, 255),  # LightSteelBlue
    RGBColor(175, 215,   0),  # Yellow3
    RGBColor(175, 215,  95),  # DarkOliveGreen3
    RGBColor(175, 215, 135),  # DarkSeaGreen3
    RGBColor(175, 215, 175),  # DarkSeaGreen2
    RGBColor(175, 215, 215),  # LightCyan3
    RGBColor(175, 215, 255),  # LightSkyBlue1
    RGBColor(175, 255,   0),  # GreenYellow
    RGBColor(175, 255,  95),  # DarkOliveGreen2
    RGBColor(175, 255, 135),  # PaleGreen1
    RGBColor(175, 255, 175),  # DarkSeaGreen2
    RGBColor(175, 255, 215),  # DarkSeaGreen1
    RGBColor(175, 255, 255),  # PaleTurquoise1
    RGBColor(215,   0,   0),  # Red3
    RGBColor(215,   0,  95),  # DeepPink3
    RGBColor(215,   0, 135),  # DeepPink3
    RGBColor(215,   0, 175),  # Magenta3
    RGBColor(215,   0, 215),  # Magenta3
    RGBColor(215,   0, 255),  # Magenta2
    RGBColor(215,  95,   0),  # DarkOrange3
    RGBColor(215,  95,  95),  # IndianRed
    RGBColor(215,  95, 135),  # HotPink3
    RGBColor(215,  95, 175),  # HotPink2
    RGBColor(215,  95, 215),  # Orchid
    RGBColor(215,  95, 255),  # MediumOrchid1
    RGBColor(215, 135,   0),  # Orange3
    RGBColor(215, 135,  95),  # LightSalmon3
    RGBColor(215, 135, 135),  # LightPink3
    RGBColor(215, 135, 175),  # Pink3
    RGBColor(215, 135, 215),  # Plum3
    RGBColor(215, 135, 255),  # Violet
    RGBColor(215, 175,   0),  # Gold3
    RGBColor(215, 175,  95),  # LightGoldenrod3
    RGBColor(215, 175, 135),  # Tan
    RGBColor(215, 175, 175),  # MistyRose3
    RGBColor(215, 175, 215),  # Thistle3
    RGBColor(215, 175, 255),  # Plum2
    RGBColor(215, 215,   0),  # Yellow3
    RGBColor(215, 215,  95),  # Khaki3
    RGBColor(215, 215, 135),  # LightGoldenrod2
    RGBColor(215, 215, 175),  # LightYellow3
    RGBColor(215, 215, 215),  # Gray84
    RGBColor(215, 215, 255),  # LightSteelBlue1
    RGBColor(215, 255,   0),  # Yellow2
    RGBColor(215, 255,  95),  # DarkOliveGreen1
    RGBColor(215, 255, 135),  # DarkOliveGreen1
    RGBColor(215, 255, 175),  # DarkSeaGreen1
    RGBColor(215, 255, 215),  # Honeydew2
    RGBColor(215, 255, 255),  # LightCyan
    RGBColor(255,   0,   0),  # Red1
    RGBColor(255,   0,  95),  # DeepPink2
    RGBColor(255,   0, 135),  # DeepPink1
    RGBColor(255,   0, 175),  # DeepPink1
    RGBColor(255,   0, 215),  # Magenta2
    RGBColor(255,   0, 255),  # Magenta1
    RGBColor(255,  95,   0),  # OrangeRed1
    RGBColor(255,  95,  95),  # IndianRed1
    RGBColor(255,  95, 135),  # IndianRed1
    RGBColor(255,  95, 175),  # HotPink
    RGBColor(255,  95, 215),  # HotPink
    RGBColor(255,  95, 255),  # MediumOrchid1
    RGBColor(255, 135,   0),  # DarkOrange
    RGBColor(255, 135,  95),  # Salmon1
    RGBColor(255, 135, 135),  # LightCoral
    RGBColor(255, 135, 175),  # PaleVioletRed1
    RGBColor(255, 135, 215),  # Orchid2
    RGBColor(255, 135, 255),  # Orchid1
    RGBColor(255, 175,   0),  # Orange1
    RGBColor(255, 175,  95),  # SandyBrown
    RGBColor(255, 175, 135),  # LightSalmon1
    RGBColor(255, 175, 175),  # LightPink1
    RGBColor(255, 175, 215),  # Pink1
    RGBColor(255, 175, 255),  # Plum1
    RGBColor(255, 215,   0),  # Gold1
    RGBColor(255, 215,  95),  # LightGoldenrod2
    RGBColor(255, 215, 135),  # LightGoldenrod2
    RGBColor(255, 215, 175),  # NavajoWhite1
    RGBColor(255, 215, 215),  # MistyRose1
    RGBColor(255, 215, 255),  # Thistle1
    RGBColor(255, 255,   0),  # Yellow1
    RGBColor(255, 255,  95),  # LightGoldenrod1
    RGBColor(255, 255, 135),  # Khaki1
    RGBColor(255, 255, 175),  # Wheat1
    RGBColor(255, 255, 215),  # Cornsilk1
    RGBColor(255, 255, 255),  # Gray100

    # Grayscale
    RGBColor(  8,   8,   8),  # Gray3
    RGBColor( 18,  18,  18),  # Gray7
    RGBColor( 28,  28,  28),  # Gray11
    RGBColor( 38,  38,  38),  # Gray15
    RGBColor( 48,  48,  48),  # Gray19
    RGBColor( 58,  58,  58),  # Gray23
    RGBColor( 68,  68,  68),  # Gray27
    RGBColor( 78,  78,  78),  # Gray30
    RGBColor( 88,  88,  88),  # Gray35
    RGBColor( 98,  98,  98),  # Gray39
    RGBColor(108, 108, 108),  # Gray42
    RGBColor(118, 118, 118),  # Gray46
    RGBColor(128, 128, 128),  # Gray50
    RGBColor(138, 138, 138),  # Gray54
    RGBColor(148, 148, 148),  # Gray58
    RGBColor(158, 158, 158),  # Gray62
    RGBColor(168, 168, 168),  # Gray66
    RGBColor(178, 178, 178),  # Gray70
    RGBColor(188, 188, 188),  # Gray74
    RGBColor(198, 198, 198),  # Gray78
    RGBColor(208, 208, 208),  # Gray82
    RGBColor(218, 218, 218),  # Gray85
    RGBColor(228, 228, 228),  # Gray89
    RGBColor(238, 238, 238),  # Gray93
)
