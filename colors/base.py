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
        self.__hsv: HSVColor
        try:
            return self.__hsv
        except AttributeError:
            self.__hsv = HSVColor.from_rgb(self)
            return self.__hsv

    @property
    def hsl(self) -> 'HSLColor':
        self.__hsl: HSLColor
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
        self.__str: str
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
        self.__rgb: RGBColor
        try:
            return self.__rgb
        except AttributeError:
            self.__rgb = RGBColor.from_hsv(self)
            return self.__rgb

    @property
    def hsl(self) -> 'HSLColor':
        self.__hsl: HSLColor
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
        self.__rgb: RGBColor
        try:
            return self.__rgb
        except AttributeError:
            self.__rgb = RGBColor.from_hsl(self)
            return self.__rgb

    @property
    def hsv(self) -> 'HSVColor':
        self.__hsv: HSVColor
        try:
            return self.__hsv
        except AttributeError:
            self.__hsv = self.rgb.hsv  # type: ignore
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


class ColorGroup(enum.Enum):
    @classmethod
    @functools.lru_cache(maxsize=128)
    def closest(cls, rgb: RGBColor) -> ColorGroup:
        try:
            return cls(rgb)
        except ValueError:
            distances = {
                sum((
                    abs(item.value.red - rgb.red),
                    abs(item.value.green - rgb.green),
                    abs(item.value.blue - rgb.blue)
                )): item
                for item in reversed(cls)
            }
            return distances[min(distances.keys())]  # type: ignore

    @property
    def index(self):
        try:
            return self.__index
        except AttributeError:
            self.__index = tuple(
                type(self).__members__.keys()
            ).index(self.name)
            return self.__index
