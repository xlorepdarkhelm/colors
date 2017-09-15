"""Base module containing the core components for the colors system."""

import enum
import functools
import typing

import colormath


class ColorMeta(type):
    @property
    def instances(cls):
        try:
            return cls.__instances
        except AttributeError:
            cls.__instances = {}
            return cls.__instances
        
    def __call__(cls, *args, **kwargs):
        sig = inspect.signature(cls.__init__)
        ba = sig.bind(*args, **kwargs)
        ba.apply_defaults()
        arg_dict = ba.arguments()
        arguments = tuple(arg_dict.items())
        try:
            return cls.instances[arguments]
        except KeyError:
            cls.instances[arguments] = super().__call__(*args, **kwargs)
            return cls.instances[arguments]


class sRGBColor(colormath.color_objects.sRGBColor, metaclass=ColorMeta):
    """Class that defines a red/green/blue (RGB) color."""
    @property
    def hsv(self) -> 'HSVColor':
        """HSV translation of this color."""
        self.__hsv: HSVColor
        try:
            return self.__hsv
        except AttributeError:
            self.__hsv = colormath.color_conversions.convert_color(self, HSVColor)
            return self.__hsv

    @property
    def hsl(self) -> 'HSLColor':
        """HSL translation of this color."""
        self.__hsl: HSLColor
        try:
            return self.__hsl
        except AttributeError:
            self.__hsl = colormath.color_conversions.convert_color(self, HSLColor)
            return self.__hsl
        
    @property
    def lab(self) -> 'LabColor':
        """CIE Lab translation of this color."""
        self.__lab: LabColor
        try:
            return self.__lab
        except AttributeError:
            self.__lab = colormath.color_conversions.convert_color(self, LabColor)
            return self.__lab

        
class HSVColor(colormath.color_objects.HSVColor, metaclass=ColorMeta):
    """Class that defines a hue/saturation/value (HSV) color."""

    @property
    def srgb(self) -> 'sRGBColor':
        """RGB translation of this color."""
        self.__srgb: sRGBColor
        try:
            return self.__srgb
        except AttributeError:
            self.__srgb = colormath.color_conversions.convert_color(self, sRGBColor)
            return self.__srgb

    @property
    def hsl(self) -> 'HSLColor':
        """HSL translation of this color."""
        self.__hsl: HSLColor
        try:
            return self.__hsl
        except AttributeError:
            self.__hsl = colormath.color_conversions.convert_color(self, HSLColor)
            return self.__hsl
        
    @property
    def lab(self) -> 'LabColor':
        """CIE Lab translation of this color."""
        self.__lab: LabColor
        try:
            return self.__lab
        except AttributeError:
            self.__lab = colormath.color_conversions.convert_color(self, LabColor)
            return self.__lab

        
class HSLColor(colormath.color_objects.HSLColor, metaclass=ColorMeta):
    """Class that defines a hue/saturation/lightness (HSL) color."""
    @property
    def srgb(self) -> 'sRGBColor':
        """sRGB translation of this color."""
        self.__srgb: sRGBColor
        try:
            return self.__srgb
        except AttributeError:
            self.__srgb = colormath.color_conversions.convert_color(self, sRGBColor)
            return self.__srgb

    @property
    def hsv(self) -> 'HSVColor':
        """HSV translation of this color."""
        self.__hsv: HSVColor
        try:
            return self.__hsv
        except AttributeError:
            self.__hsv = colormath.color_conversions.convert_color(self, HSVColor)
            return self.__hsv
        
    @property
    def lab(self) -> 'LabColor':
        """CIE Lab translation of this color."""
        self.__lab: LabColor
        try:
            return self.__lab
        except AttributeError:
            self.__lab = colormath.color_conversions.convert_color(self, LabColor)
            return self.__lab
        
class LabColor(colormath.color_objects.LabColor, metaclass=ColorMeta):
    """Class that represents a CIE Lab color."""
    @property
    def srgb(self) -> 'sRGBColor':
        """sRGB translation of this color."""
        self.__srgb: sRGBColor
        try:
            return self.__srgb
        except AttributeError:
            self.__srgb = colormath.color_conversions.convert_color(self, sRGBColor)
            return self.__srgb

    @property
    def hsv(self) -> 'HSVColor':
        """HSV translation of this color."""
        self.__hsv: HSVColor
        try:
            return self.__hsv
        except AttributeError:
            self.__hsv = colormath.color_conversions.convert_color(self, HSVColor)
            return self.__hsv
        
    @property
    def hsl(self) -> 'HSLColor':
        """HSL translation of this color."""
        self.__hsl: HSLColor
        try:
            return self.__hsl
        except AttributeError:
            self.__hsl = colormath.color_conversions.convert_color(self, HSLColor)
            return self.__hsl


class ColorGroup(enum.Enum):
    """
    Base class used to implement color groups.

    Color groups are defined as Enums of named :py:class:`sRGBColor` values.
    The purpose of these is to logically manage colors more easily, as well
    as provide a mechanism to convert a color from one system to the closest
    color of another system in a simple way.
    """

    @classmethod
    @functools.lru_cache(maxsize=128)
    def closest(
        cls,
        color: typing.Union['ColorGroup', sRGBColor]
    ) -> 'ColorGroup':
        """Find the closest match in this color group to the given color."""
        try:
            rgb = color.value  # type: ignore
        except AttributeError:
            rgb = color
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
