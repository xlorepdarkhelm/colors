import collections.abc
import colorsys
import enum
import functools
import typing


class RGBColor(
    typing.NamedTuple(
        'RGBColor',
        (
            ('red', int),
            ('green', int),
            ('blue', int),
        )
    )
):
    def __new__(cls, red: int, green: int, blue: int) -> 'RGBColor':
        red, green, blue = int(red), int(green), int(blue)
        red_good = 0 <= red <= 255
        green_good = 0 <= green <= 255
        blue_good = 0 <= blue <= 255
        if all((red_good, green_good, blue_good)):
            return super().__new__(cls, red, green, blue)
        else:
            raise ValueError(
                'Red, green, and blue must be in the range 0 -> 255.'
            )

    @property
    def hsv(self) -> 'HSVColor':
        try:
            return self.__hsv
        except AttributeError:
            self.__hsv = HSVColor.from_rgb(self)
            return self.__hsv

    @property
    def hsl(self) -> 'HSLColor':
        try:
            return self.__hsl
        except AttributeError:
            self.__hsl = HSLColor.from_rgb(self)
            return self.__hsl

    @classmethod
    @functools.lru_cache(maxsize=128)
    def from_hsv(cls, hsv: 'HSVColor') -> 'RGBColor':
        red, green, blue = colorsys.hsv_to_rgb(
            hsv.hue / 360,
            hsv.saturation / 100,
            hsv.value / 100,
        )
        return cls(int(red * 255), int(green * 255), int(blue * 255))

    @classmethod
    @functools.lru_cache(maxsize=128)
    def from_hsl(cls, hsl: 'HSLColor') -> 'RGBColor':
        red, green, blue = colorsys.hls_to_rgb(
            hsl.hue / 360,
            hsl.lightness / 100,
            hsl.saturation / 100,
        )
        return cls(int(red * 255), int(green * 255), int(blue * 255))

    def __str__(self) -> str:
        try:
            return self.__str
        except AttributeError:
            self.__str = f'#{self.red:02X}{self.green:02X}{self.blue:02X}'
            return self.__str

    @classmethod
    @functools.lru_cache(maxsize=128)
    def from_str(cls, web_str: str) -> 'RGBColor':
        try:
            if web_str[0] == '#':
                web_str = web_str[1:]
        except IndexError:
            raise ValueError('Cannot process empty strings.')
        if len(web_str) not in {3, 6}:
            raise ValueError('String must either be 3 or 6 characters long.')
        elif len(web_str) == 6:
            red, green, blue = tuple(
                int(web_str[ndx:ndx+2], 16)
                for ndx in range(0, 5, 2)
            )
            return cls(red, green, blue)
        else:
            red, green, blue = tuple(int(value, 16) << 4 for value in web_str)
            return cls(red, green, blue)


class HSVColor(
    typing.NamedTuple(
        'HSVColor',
        (
            ('hue', int),
            ('saturation', int),
            ('value', int),
        )
    )
):
    def __new__(cls, hue: int, saturation: int, value: int) -> 'HSVColor':
        hue, saturation, value = int(hue), int(saturation), int(value)
        while hue >= 360:
            hue -= 360
        while hue < 0:
            hue += 360
        saturation_good = 0 <= saturation <= 100
        value_good = 0 <= value <= 100
        if all((saturation_good, value_good)):
            return super().__new__(cls, hue, saturation, value)
        else:
            raise ValueError(
                'Saturation and value must be in the range 0 -> 100.'
            )

    @property
    def rgb(self) -> 'RGBColor':
        try:
            return self.__rgb
        except AttributeError:
            self.__rgb = RGBColor.from_hsv(self)
            return self.__rgb

    @property
    def hsl(self) -> 'HSLColor':
        try:
            return self.__hsl
        except AttributeError:
            self.__hsl = self.rgb.hsl
            return self.__hsl

    @classmethod
    @functools.lru_cache(maxsize=128)
    def from_rgb(cls, rgb: 'RGBColor') -> 'HSVColor':
        hue, saturation, value = colorsys.rgb_to_hsv(
            rgb.red / 255,
            rgb.green / 255,
            rgb.blue / 255,
        )
        return cls(int(hue * 360), int(saturation * 100), int(value * 100))


class HSLColor(
    typing.NamedTuple(
        'HSLColor',
        (
            ('hue', int),
            ('saturation', int),
            ('lightness', int),
        )
    )
):
    def __new__(cls, hue: int, saturation: int, lightness: int) -> 'HSLColor':
        hue, saturation, lightness = int(hue), int(saturation), int(lightness)
        while hue >= 360:
            hue -= 360
        while hue < 0:
            hue += 360
        saturation_good = 0 <= saturation <= 100
        lightness_good = 0 <= lightness <= 100
        if all((saturation_good, lightness_good)):
            return super().__new__(cls, hue, saturation, lightness)
        else:
            raise ValueError(
                'Saturation and lightness must be in the range 0 -> 100.'
            )
    @property
    def rgb(self) -> 'RGBColor':
        try:
            return self.__rgb
        except AttributeError:
            self.__rgb = RGBColor.from_hsl(self)
            return self.__rgb

    @property
    def hsv(self) -> 'HSVColor':
        try:
            return self.__hsv
        except AttributeError:
            self.__hsv = self.rgb.hsv
            return self.__hsv

    @classmethod
    @functools.lru_cache(maxsize=128)
    def from_rgb(cls, rgb: 'RGBColor') -> 'HSLColor':
        hue, lightness, saturation = colorsys.rgb_to_hls(
            rgb.red / 255,
            rgb.green / 255,
            rgb.blue / 255,
        )
        return cls(int(hue * 360), int(saturation * 100), int(lightness * 100))


class ANSI(enum.Enum):
    Normal = (
        RGBColor(  0,   0,   0),  # Black
        RGBColor(128,   0,   0),  # Red
        RGBColor(  0, 128,   0),  # Green
        RGBColor(128, 128,   0),  # Brown
        RGBColor(  0,   0, 128),  # Blue
        RGBColor(128,   0, 128),  # Magenta
        RGBColor(  0, 128, 128),  # Cyan
        RGBColor(192, 192, 192),  # Gray
    )

    Bright = (
        RGBColor(128, 128, 128),  # Darkgray
        RGBColor(255,   0,   0),  # Red
        RGBColor(  0, 255,   0),  # Green
        RGBColor(255, 255,   0),  # Yellow
        RGBColor(  0,   0, 255),  # Blue
        RGBColor(255,   0, 255),  # Magenta
        RGBColor(  0, 255, 255),  # Cyan
        RGBColor(255, 255, 255),  # White
    )

    def __getitem__(self, index: int) -> RGBColor:
        return self.value[index]

    def __len__(self) -> int:
        return len(self.value)

    def __contains__(self, value: RGBColor) -> bool:
        return value in self.value

    def __iter__(self) -> typing.Iterator[RGBColor]:
        return iter(self.value)

    def __reversed__(self) -> typing.Iterator[RGBColor]:
        return reversed(self.value)

    def index(self, value: RGBColor) -> int:
        return self.value.index(value)

    def count(self, value: RGBColor) -> int:
        return self.value.count(value)

# http://en.wikipedia.org/wiki/Web_colors#X11_color_names
class X11Colors(enum.Enum):
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

class MaterialDesign(enum.Enum):
    Red_50   = RGBColor(255, 235, 238)
    Red_100  = RGBColor(255, 205, 210)
    Red_200  = RGBColor(239, 154, 154)
    Red_300  = RGBColor(229, 115, 115)
    Red_400  = RGBColor(239,  83,  80)
    Red_500  = RGBColor(244,  67,  54)
    Red_600  = RGBColor(229,  57,  53)
    Red_700  = RGBColor(211,  47,  47)
    Red_800  = RGBColor(198,  40,  40)
    Red_900  = RGBColor(183,  28,  28)
    Red_A100 = RGBColor(255, 138, 128)
    Red_A200 = RGBColor(255,  82,  82)
    Red_A400 = RGBColor(255,  23,  68)
    Red_A700 = RGBColor(213,   0,   0)

    Pink_50   = RGBColor(252, 228, 236)
    Pink_100  = RGBColor(248, 187, 208)
    Pink_200  = RGBColor(244, 143, 177)
    Pink_300  = RGBColor(240,  98, 146)
    Pink_400  = RGBColor(236,  64, 122)
    Pink_500  = RGBColor(233,  30,  99)
    Pink_600  = RGBColor(216,  27,  96)
    Pink_700  = RGBColor(194,  24,  91)
    Pink_800  = RGBColor(173,  20,  87)
    Pink_900  = RGBColor(136,  14,  79)
    Pink_A100 = RGBColor(255, 128, 171)
    Pink_A200 = RGBColor(255,  64, 129)
    Pink_A400 = RGBColor(245,   0,  87)
    Pink_A700 = RGBColor(197,  17,  98)

    Purple_50   = RGBColor(243, 229, 245)
    Purple_100  = RGBColor(225, 190, 231)
    Purple_200  = RGBColor(206, 147, 216)
    Purple_300  = RGBColor(186, 104, 200)
    Purple_400  = RGBColor(171,  71, 188)
    Purple_500  = RGBColor(156,  39, 176)
    Purple_600  = RGBColor(142,  36, 170)
    Purple_700  = RGBColor(123,  31, 162)
    Purple_800  = RGBColor(106,  27, 154)
    Purple_900  = RGBColor( 74,  20, 140)
    Purple_A100 = RGBColor(234, 128, 252)
    Purple_A200 = RGBColor(224,  64, 251)
    Purple_A400 = RGBColor(213,   0, 249)
    Purple_A700 = RGBColor(170,   0, 255)

    DeepPurple_50   = RGBColor(237, 231, 246)
    DeepPurple_100  = RGBColor(209, 196, 233)
    DeepPurple_200  = RGBColor(179, 157, 219)
    DeepPurple_300  = RGBColor(149, 117, 205)
    DeepPurple_400  = RGBColor(126,  87, 194)
    DeepPurple_500  = RGBColor(103,  58, 183)
    DeepPurple_600  = RGBColor( 94,  53, 177)
    DeepPurple_700  = RGBColor( 81,  45, 168)
    DeepPurple_800  = RGBColor( 69,  39, 160)
    DeepPurple_900  = RGBColor( 49,  27, 146)
    DeepPurple_A100 = RGBColor(179, 136, 255)
    DeepPurple_A200 = RGBColor(124,  77, 255)
    DeepPurple_A400 = RGBColor(101,  31, 255)
    DeepPurple_A700 = RGBColor( 98,   0, 234)

    Indigo_50   = RGBColor(232, 234, 246)
    Indigo_100  = RGBColor(197, 202, 233)
    Indigo_200  = RGBColor(159, 168, 218)
    Indigo_300  = RGBColor(121, 134, 203)
    Indigo_400  = RGBColor( 92, 107, 192)
    Indigo_500  = RGBColor( 63,  81, 181)
    Indigo_600  = RGBColor( 57,  73, 171)
    Indigo_700  = RGBColor( 48,  63, 159)
    Indigo_800  = RGBColor( 40,  53, 147)
    Indigo_900  = RGBColor( 26,  35, 126)
    Indigo_A100 = RGBColor(140, 158, 255)
    Indigo_A200 = RGBColor( 83, 109, 254)
    Indigo_A400 = RGBColor( 61,  90, 254)
    Indigo_A700 = RGBColor( 48,  79, 254)

    Blue_50   = RGBColor(227, 242, 253)
    Blue_100  = RGBColor(187, 222, 251)
    Blue_200  = RGBColor(144, 202, 249)
    Blue_300  = RGBColor(100, 181, 246)
    Blue_400  = RGBColor( 66, 165, 245)
    Blue_500  = RGBColor( 33, 150, 243)
    Blue_600  = RGBColor( 30, 136, 229)
    Blue_700  = RGBColor( 25, 118, 210)
    Blue_800  = RGBColor( 21, 101, 192)
    Blue_900  = RGBColor( 13,  71, 161)
    Blue_A100 = RGBColor(130, 177, 255)
    Blue_A200 = RGBColor( 68, 138, 255)
    Blue_A400 = RGBColor( 41, 121, 255)
    Blue_A700 = RGBColor( 41,  98, 255)

    LightBlue_50   = RGBColor(, , )
    LightBlue_100  = RGBColor(, , )
    LightBlue_200  = RGBColor(, , )
    LightBlue_300  = RGBColor(, , )
    LightBlue_400  = RGBColor(, , )
    LightBlue_500  = RGBColor(, , )
    LightBlue_600  = RGBColor(, , )
    LightBlue_700  = RGBColor(, , )
    LightBlue_800  = RGBColor(, , )
    LightBlue_900  = RGBColor(, , )
    LightBlue_A100 = RGBColor(, , )
    LightBlue_A200 = RGBColor(, , )
    LightBlue_A400 = RGBColor(, , )
    LightBlue_A700 = RGBColor(, , )

    Cyan_50   = RGBColor(, , )
    Cyan_100  = RGBColor(, , )
    Cyan_200  = RGBColor(, , )
    Cyan_300  = RGBColor(, , )
    Cyan_400  = RGBColor(, , )
    Cyan_500  = RGBColor(, , )
    Cyan_600  = RGBColor(, , )
    Cyan_700  = RGBColor(, , )
    Cyan_800  = RGBColor(, , )
    Cyan_900  = RGBColor(, , )
    Cyan_A100 = RGBColor(, , )
    Cyan_A200 = RGBColor(, , )
    Cyan_A400 = RGBColor(, , )
    Cyan_A700 = RGBColor(, , )

    Teal_50   = RGBColor(, , )
    Teal_100  = RGBColor(, , )
    Teal_200  = RGBColor(, , )
    Teal_300  = RGBColor(, , )
    Teal_400  = RGBColor(, , )
    Teal_500  = RGBColor(, , )
    Teal_600  = RGBColor(, , )
    Teal_700  = RGBColor(, , )
    Teal_800  = RGBColor(, , )
    Teal_900  = RGBColor(, , )
    Teal_A100 = RGBColor(, , )
    Teal_A200 = RGBColor(, , )
    Teal_A400 = RGBColor(, , )
    Teal_A700 = RGBColor(, , )

    Green_50   = RGBColor(, , )
    Green_100  = RGBColor(, , )
    Green_200  = RGBColor(, , )
    Green_300  = RGBColor(, , )
    Green_400  = RGBColor(, , )
    Green_500  = RGBColor(, , )
    Green_600  = RGBColor(, , )
    Green_700  = RGBColor(, , )
    Green_800  = RGBColor(, , )
    Green_900  = RGBColor(, , )
    Green_A100 = RGBColor(, , )
    Green_A200 = RGBColor(, , )
    Green_A400 = RGBColor(, , )
    Green_A700 = RGBColor(, , )

    LightGreen_50   = RGBColor(, , )
    LightGreen_100  = RGBColor(, , )
    LightGreen_200  = RGBColor(, , )
    LightGreen_300  = RGBColor(, , )
    LightGreen_400  = RGBColor(, , )
    LightGreen_500  = RGBColor(, , )
    LightGreen_600  = RGBColor(, , )
    LightGreen_700  = RGBColor(, , )
    LightGreen_800  = RGBColor(, , )
    LightGreen_900  = RGBColor(, , )
    LightGreen_A100 = RGBColor(, , )
    LightGreen_A200 = RGBColor(, , )
    LightGreen_A400 = RGBColor(, , )
    LightGreen_A700 = RGBColor(, , )

    Lime_50   = RGBColor(, , )
    Lime_100  = RGBColor(, , )
    Lime_200  = RGBColor(, , )
    Lime_300  = RGBColor(, , )
    Lime_400  = RGBColor(, , )
    Lime_500  = RGBColor(, , )
    Lime_600  = RGBColor(, , )
    Lime_700  = RGBColor(, , )
    Lime_800  = RGBColor(, , )
    Lime_900  = RGBColor(, , )
    Lime_A100 = RGBColor(, , )
    Lime_A200 = RGBColor(, , )
    Lime_A400 = RGBColor(, , )
    Lime_A700 = RGBColor(, , )

    Yellow_50   = RGBColor(, , )
    Yellow_100  = RGBColor(, , )
    Yellow_200  = RGBColor(, , )
    Yellow_300  = RGBColor(, , )
    Yellow_400  = RGBColor(, , )
    Yellow_500  = RGBColor(, , )
    Yellow_600  = RGBColor(, , )
    Yellow_700  = RGBColor(, , )
    Yellow_800  = RGBColor(, , )
    Yellow_900  = RGBColor(, , )
    Yellow_A100 = RGBColor(, , )
    Yellow_A200 = RGBColor(, , )
    Yellow_A400 = RGBColor(, , )
    Yellow_A700 = RGBColor(, , )

    Amber_50   = RGBColor(, , )
    Amber_100  = RGBColor(, , )
    Amber_200  = RGBColor(, , )
    Amber_300  = RGBColor(, , )
    Amber_400  = RGBColor(, , )
    Amber_500  = RGBColor(, , )
    Amber_600  = RGBColor(, , )
    Amber_700  = RGBColor(, , )
    Amber_800  = RGBColor(, , )
    Amber_900  = RGBColor(, , )
    Amber_A100 = RGBColor(, , )
    Amber_A200 = RGBColor(, , )
    Amber_A400 = RGBColor(, , )
    Amber_A700 = RGBColor(, , )

    Orange_50   = RGBColor(, , )
    Orange_100  = RGBColor(, , )
    Orange_200  = RGBColor(, , )
    Orange_300  = RGBColor(, , )
    Orange_400  = RGBColor(, , )
    Orange_500  = RGBColor(, , )
    Orange_600  = RGBColor(, , )
    Orange_700  = RGBColor(, , )
    Orange_800  = RGBColor(, , )
    Orange_900  = RGBColor(, , )
    Orange_A100 = RGBColor(, , )
    Orange_A200 = RGBColor(, , )
    Orange_A400 = RGBColor(, , )
    Orange_A700 = RGBColor(, , )

    DeepOrange_50   = RGBColor(, , )
    DeepOrange_100  = RGBColor(, , )
    DeepOrange_200  = RGBColor(, , )
    DeepOrange_300  = RGBColor(, , )
    DeepOrange_400  = RGBColor(, , )
    DeepOrange_500  = RGBColor(, , )
    DeepOrange_600  = RGBColor(, , )
    DeepOrange_700  = RGBColor(, , )
    DeepOrange_800  = RGBColor(, , )
    DeepOrange_900  = RGBColor(, , )
    DeepOrange_A100 = RGBColor(, , )
    DeepOrange_A200 = RGBColor(, , )
    DeepOrange_A400 = RGBColor(, , )
    DeepOrange_A700 = RGBColor(, , )

    Brown_50  = RGBColor(, , )
    Brown_100 = RGBColor(, , )
    Brown_200 = RGBColor(, , )
    Brown_300 = RGBColor(, , )
    Brown_400 = RGBColor(, , )
    Brown_500 = RGBColor(, , )
    Brown_600 = RGBColor(, , )
    Brown_700 = RGBColor(, , )
    Brown_800 = RGBColor(, , )
    Brown_900 = RGBColor(, , )

    Grey_50  = RGBColor(, , )
    Grey_100 = RGBColor(, , )
    Grey_200 = RGBColor(, , )
    Grey_300 = RGBColor(, , )
    Grey_400 = RGBColor(, , )
    Grey_500 = RGBColor(, , )
    Grey_600 = RGBColor(, , )
    Grey_700 = RGBColor(, , )
    Grey_800 = RGBColor(, , )
    Grey_900 = RGBColor(, , )

    BlueGrey_50  = RGBColor(, , )
    BlueGrey_100 = RGBColor(, , )
    BlueGrey_200 = RGBColor(, , )
    BlueGrey_300 = RGBColor(, , )
    BlueGrey_400 = RGBColor(, , )
    BlueGrey_500 = RGBColor(, , )
    BlueGrey_600 = RGBColor(, , )
    BlueGrey_700 = RGBColor(, , )
    BlueGrey_800 = RGBColor(, , )
    BlueGrey_900 = RGBColor(, , )

    Black = RGBColor(  0,   0,   0)
    White = RGBColor(255, 255, 255)
