"""Base module containing the core components for the colors system."""

import collections.abc
import colorsys
import contextlib
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

    def __new__(cls, red: int, green: int, blue: int) -> 'RGBColor':
        """
        Validate red, green, and blue then construct the instance.

        Parameters:
            red (int): Integer value in the range 0-255.
            green (int): Integer value in the range 0-255.
            blue (int): Integer value in the range 0-255.

        Returns:
            RGBColor: The RGBColor instance.

        Raises:
            ValueError: If `red`, `green`, or `blue` are outside of the
            required range.

        """
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
        """HSV translation of this color."""
        self.__hsv: HSVColor
        try:
            return self.__hsv
        except AttributeError:
            self.__hsv = HSVColor.from_rgb(self)
            return self.__hsv

    @property
    def hsl(self) -> 'HSLColor':
        """HSL translation of this color."""
        self.__hsl: HSLColor
        try:
            return self.__hsl
        except AttributeError:
            self.__hsl = HSLColor.from_rgb(self)
            return self.__hsl

    @classmethod
    @functools.lru_cache(maxsize=128)
    def from_hsv(cls, hsv: 'HSVColor') -> 'RGBColor':
        """Convert the HSVColor to RGBColor."""
        red, green, blue = colorsys.hsv_to_rgb(
            hsv.hue / 360,
            hsv.saturation / 100,
            hsv.value / 100,
        )
        return cls(int(red * 255), int(green * 255), int(blue * 255))

    @classmethod
    @functools.lru_cache(maxsize=128)
    def from_hsl(cls, hsl: 'HSLColor') -> 'RGBColor':
        """Convert the HSLColor to RGBColor."""
        red, green, blue = colorsys.hls_to_rgb(
            hsl.hue / 360,
            hsl.lightness / 100,
            hsl.saturation / 100,
        )
        return cls(int(red * 255), int(green * 255), int(blue * 255))

    def __str__(self) -> str:
        """Convert this RGBColor into web/hex notation string format."""
        self.__str: str
        try:
            return self.__str
        except AttributeError:
            self.__str = f'#{self.red:02X}{self.green:02X}{self.blue:02X}'
            return self.__str

    @classmethod
    @functools.lru_cache(maxsize=128)
    def from_str(cls, web_str: str) -> 'RGBColor':
        """Convert the web/hex notation string into RGBColor."""
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
    """
    Class that defines a hue/saturation/value (HSV) color.

    HSV is a common cylendrical-coordinate representation of colors. This
    form for colors is an attempt to make it easier to perceive the colors
    in a more three-dimensional model, often used by color pickers and
    television broadcasts. It is possible to convert this to
    :py:class:`RGBColor` or :py:class:`HSLColor` through conversion
    properties (:py:meth:`rgb` & :py:meth:`hsl` respectively).

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

    def __new__(cls, hue: int, saturation: int, value: int) -> 'HSVColor':
        """
        Validate hue, saturation, and value then construct the instance.

        Parameters:
            hue (int): Integer value in the range 0-359.
            saturation (int): Integer value in the range 0-100.
            value (int): Integer value in the range 0-100.

        Returns:
            HSVColor: The HSVColor instance.

        Raises:
            ValueError: If `saturation` or `value` are outside of the
            required range.

        Notes:
            If `hue` is outside the required range, the value either has 360
            added or subtraced from it until the value is in the required
            range.

        """
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
        """RGB translation of this color."""
        self.__rgb: RGBColor
        try:
            return self.__rgb
        except AttributeError:
            self.__rgb = RGBColor.from_hsv(self)
            return self.__rgb

    @property
    def hsl(self) -> 'HSLColor':
        """HSL translation of this color."""
        self.__hsl: HSLColor
        try:
            return self.__hsl
        except AttributeError:
            self.__hsl = self.rgb.hsl
            return self.__hsl

    @classmethod
    @functools.lru_cache(maxsize=128)
    def from_rgb(cls, rgb: 'RGBColor') -> 'HSVColor':
        """Convert the RGBColor to HSVColor."""
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
    """
    Class that defines a hue/saturation/lightness (HSL) color.

    HSL is a common cylendrical-coordinate representation of colors. This
    form for colors is an attempt to make it easier to perceive the colors
    in a more three-dimensional model, often used by color pickers and
    television broadcasts. It is possible to convert this to
    :py:class:`RGBColor` or :py:class:`HSVColor` through conversion
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

    def __new__(cls, hue: int, saturation: int, lightness: int) -> 'HSLColor':
        """
        Validate hue, saturation, and lightness then construct the instance.

        Parameters:
            hue (int): Integer value in the range 0-359.
            saturation (int): Integer value in the range 0-100.
            lightness (int): Integer value in the range 0-100.

        Returns:
            HSLColor: The HSLColor instance.

        Raises:
            ValueError: If `saturation` or `lightness` are outside of the
            required range.

        Notes:
            If `hue` is outside the required range, the value either has 360
            added or subtraced from it until the value is in the required
            range.

        """
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
        """RGB translation of this color."""
        self.__rgb: RGBColor
        try:
            return self.__rgb
        except AttributeError:
            self.__rgb = RGBColor.from_hsl(self)
            return self.__rgb

    @property
    def hsv(self) -> 'HSVColor':
        """HSV translation of this color."""
        self.__hsv: HSVColor
        try:
            return self.__hsv
        except AttributeError:
            self.__hsv = self.rgb.hsv  # type: ignore
            return self.__hsv

    @classmethod
    @functools.lru_cache(maxsize=128)
    def from_rgb(cls, rgb: 'RGBColor') -> 'HSLColor':
        """Convert the RGBColor to HSLColor."""
        hue, lightness, saturation = colorsys.rgb_to_hls(
            rgb.red / 255,
            rgb.green / 255,
            rgb.blue / 255,
        )
        return cls(int(hue * 360), int(saturation * 100), int(lightness * 100))


class ColorGroup(enum.Enum):
    """
    Base class used to implement color groups.

    Color groups are defined as Enums of named :py:class:`RGBColor` values.
    The purpose of these is to logically manage colors more easily, as well
    as provide a mechanism to convert a color from one system to the closest
    color of another system in a simple way.
    """

    @classmethod
    @functools.lru_cache(maxsize=128)
    def closest(cls, color: typing.Union[ColorGroup, RGBColor]) -> ColorGroup:
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

    @property
    def index(self):
        """Index value for color in this group."""
        try:
            return self.__index
        except AttributeError:
            self.__index = tuple(
                type(self).__members__.keys()
            ).index(self.name)
            return self.__index
