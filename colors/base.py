"""Base module containing the core components for the colors system."""

import enum
import functools
import typing

import colormath


class sRGBColor(colormath.color_objects.sRGBColor):
    """
    Class that defines a red/green/blue (RGB) color.

    This is a namedtuple that simply contains 3 8-bit (0-255) values that
    represent red, green, and blue values for the color. It is possible to
    convert this to :py:class:`HSVColor` or :py:class:`HSLColor` through
    conversion properties (:py:meth:`hsv` & :py:meth:`hsl` respectively).

    Attributes:
        red (int): An integer value from 0-255 representing the red level for
            the color.
        green (int): An integer value from 0-255 representing the green level
            for the color.
        blue (int): An integer value from 0-255 representing the blue level
            for the color.

    """
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

    @classmethod
    @functools.lru_cache(maxsize=128)
    def from_str(cls, hex_str: str) -> 'sRGBColor':
        """Convert the web/hex notation string into sRGBColor."""
        return cls.new_from_rgb_hex(hex_str)
    
    def __str__(self):
        return self.get_rgb_hex()


class HSVColor(colormath.color_objects.HSVColor):
    """
    Class that defines a hue/saturation/value (HSV) color.

    HSV is a common cylendrical-coordinate representation of colors. This
    form for colors is an attempt to make it easier to perceive the colors
    in a more three-dimensional model, often used by color pickers and
    television broadcasts. It is possible to convert this to
    :py:class:`sRGBColor` or :py:class:`HSLColor` through conversion
    properties (:py:meth:`srgb` & :py:meth:`hsl` respectively).

    Attributes:
        hue (int): An integer value from 0-359 representing an angle of
            rotation in the color cylender. Each value represents a different
            color hue. If the colors go below 0, they are automatically
            wrapped around (add 360 to the value) to know the true value.
            Likewise, if they exceed 359, they are wrapped (subtract 360 from
            the value) to know the true value.
        saturation (int): An integer value from 0-100 representing the color
            saturation for the given hue. A lower value results in less color
            (more gray), while a higher value results in more color (less
            gray) being shown.
        value (int): An integer value from 0-100 representing the brightness
            of the color. Lower values approach black, while higher values
            approach the brightest color.

    """

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

class HSLColor(colormath.color_objects.HSLColor):
    """
    Class that defines a hue/saturation/lightness (HSL) color.

    HSL is a common cylendrical-coordinate representation of colors. This
    form for colors is an attempt to make it easier to perceive the colors
    in a more three-dimensional model, often used by color pickers and
    television broadcasts. It is possible to convert this to
    :py:class:`sRGBColor` or :py:class:`HSVColor` through conversion
    properties (:py:meth:`rgb` & :py:meth:`hsv` respectively).

    Attributes:
        hue (int): An integer value from 0-359 representing an angle of
            rotation in the color cylender. Each value represents a different
            color hue. If the colors go below 0, they are automatically
            wrapped around (add 360 to the value) to know the true value.
            Likewise, if they exceed 359, they are wrapped (subtract 360 from
            the value) to know the true value.
        saturation (int): An integer value from 0-100 representing the color
            saturation for the given hue. A lower value results in less color
            (more gray), while a higher value results in more color (less
            gray) being shown.
        lightness (int): An integer value from 0-100 representing the
            lightness of the color. Lower values approach black, while higher
            values approach white.

    """
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
