"""Base module containing the core components for the colors system."""

import enum
import functools
import inspect
import typing

import colormath
import colormath.color_objects
import colormath.color_conversions


class ColorMeta(type):
    __class_registry: typing.Dict[str, type] = {}

    @property
    def instances(cls):
        try:
            return cls.__instances
        except AttributeError:
            cls.__instances = {}
            return cls.__instances

    @staticmethod
    def get_conversion(self, attr_name):
        cls = type(self)
        metacls = type(cls)
        if attr_name in metacls.__class_registry:
            attrs = vars(self)
            try:
                return attrs[attr_name]
            except KeyError:
                attr_class = metacls.__class_registry[attr_name]
                color_class = getattr(
                    colormath.color_objects,
                    attr_class.__name__
                )
                color_val = colormath.color_conversions.convert_color(
                    self._color,
                    color_class
                )
                attrs[attr_name] = attr_class(color_val)
                return attrs[attr_name]
        else:
            return super(cls, self).__getattribute__(attr_name)

    def __new__(metacls, name, bases, ns, attr_name, **kwds):
        try:
            return metacls.__class_registry[attr_name]
        except KeyError:
            ns[f'_{metacls.__name__}__color_registry'] = {}
            ns['__getattribute__'] = metacls.get_conversion
            metacls.__class_registry[attr_name] = super().__new__(
                metacls,
                name,
                bases,
                ns
            )
            return metacls.__class_registry[attr_name]

    def __call__(cls, *args, **kwargs):
        sig = inspect.signature(cls.__new__)
        ba = sig.bind(*args, **kwargs)
        ba.apply_defaults()
        arguments = ba.args + tuple(ba.kwargs.items())
        try:
            return cls.instances[arguments]
        except KeyError:
            cls.instances[arguments] = super(type(cls), cls).__call__(
                *args,
                **kwargs
            )
            return cls.instances[arguments]


class BaseColor:
    def __init__(self, color: colormath.color_objects.ColorBase) -> None:
        self.__color = color
        self.__values: typing.Dict[str, typing.Any] = {}

    @property
    def _color(self) -> colormath.color_objects.ColorBase:
        return self.__color

    def _get_value(self, name, function=False) -> typing.Any:
        try:
            return self.__values[name]
        except KeyError:
            orig = getattr(self._color, name)
            if function:
                self.__values[name] = orig()
            else:
                self.__values[name] = orig
            return self.__values[name]


class sRGBColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='srgb'
):
    """Class that defines a red/green/blue (RGB) color."""

    @property
    def red(self) -> int:
        self.__red: int
        try:
            return self.__red
        except AttributeError:
            self.__red = int(self.clamped_red * 255)
            return self.__red

    @property
    def r(self) -> int:
        self.__red: int
        try:
            return self.__red
        except AttributeError:
            self.__red = int(self.clamped_red * 255)
            return self.__red

    @property
    def green(self) -> int:
        self.__green: int
        try:
            return self.__green
        except AttributeError:
            self.__green = int(self.clamped_green * 255)
            return self.__green

    @property
    def g(self) -> int:
        self.__green: int
        try:
            return self.__green
        except AttributeError:
            self.__green = int(self.clamped_green * 255)
            return self.__green

    @property
    def blue(self) -> int:
        self.__blue: int
        try:
            return self.__blue
        except AttributeError:
            self.__blue = int(self.clamped_blue * 255)
            return self.__blue

    @property
    def b(self) -> int:
        self.__blue: int
        try:
            return self.__blue
        except AttributeError:
            self.__blue = int(self.clamped_blue * 255)
            return self.__blue

    @property
    def hex(self) -> str:
        return self._get_value('get_rgb_hex', function=True)

    @property
    def value_tuple(self) -> typing.Tuple[int, int, int]:
        return self._get_value('get_upscaled_value_tuple', function=True)

    @property
    def clamped_value_tuple(self) -> typing.Tuple[float, float, float]:
        return self._get_value('get_value_tuple', function=True)

    @classmethod
    def from_hex(cls, hex_str: str) -> 'sRGBColor':
        return cls(
            colormath.color_objects.sRGBColor.new_from_rgb_hex(hex_str)
        )

    @property
    def clamped_red(self) -> float:
        return self._get_value('rgb_r')

    @property
    def clamped_green(self) -> float:
        return self._get_value('rgb_g')

    @property
    def clamped_blue(self) -> float:
        return self._get_value('rgb_b')

    @property
    def native_illuminant(self) -> str:
        return self._get_value('native_illuminant')

    @property
    def gamma(self) -> float:
        return self._get_value('rgb_gamma')

    def __repr__(self) -> str:
        return ', '.join((
            f'<sRGBColor(red={self.red}',
            f'green={self.green}',
            f'blue={self.blue})>'
        ))


def RGBColor(red: int, green: int, blue: int) -> sRGBColor:
    return sRGBColor(
        colormath.color_objects.sRGBColor(red, green, blue, is_upscaled=True)
    )


class HSVColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='hsv'
):
    """Class that defines a hue/saturation/value (HSV) color."""

    @property
    def hue(self) -> int:
        self.__hue: int
        try:
            return self.__hue
        except AttributeError:
            self.__hue = int(self.clamped_hue * 360)
            return self.__hue

    @property
    def h(self) -> int:
        self.__hue: int
        try:
            return self.__hue
        except AttributeError:
            self.__hue = int(self.clamped_hue * 360)
            return self.__hue

    @property
    def saturation(self) -> int:
        self.__saturation: int
        try:
            return self.__saturation
        except AttributeError:
            self.__saturation = int(self.clamped_saturation * 100)
            return self.__saturation

    @property
    def s(self) -> int:
        self.__saturation: int
        try:
            return self.__saturation
        except AttributeError:
            self.__saturation = int(self.clamped_saturation * 100)
            return self.__saturation

    @property
    def value(self) -> int:
        self.__value: int
        try:
            return self.__value
        except AttributeError:
            self.__value = int(self.clamped_value * 100)
            return self.__value

    @property
    def v(self) -> int:
        self.__value: int
        try:
            return self.__value
        except AttributeError:
            self.__value = int(self.clamped_value * 100)
            return self.__value

    @property
    def value_tuple(self) -> typing.Tuple[int, int, int]:
        self.__value_tuple: typing.Tuple[int, int, int]
        try:
            return self.__value_tuple
        except AttributeError:
            self.__value_tuple = (self.hue, self.saturation, self.value)
            return self.__value_tuple

    @property
    def clamped_value_tuple(self) -> typing.Tuple[float, float, float]:
        return self._get_value('get_value_tuple', function=True)

    @property
    def clamped_hue(self) -> float:
        return self._get_value('hsv_h')

    @property
    def clamped_saturation(self) -> float:
        return self._get_value('hsv_s')

    @property
    def clamped_value(self) -> float:
        return self._get_value('hsv_v')

    def __repr__(self) -> str:
        return ', '.join((
            f'<HSVColor(hue={self.hue}',
            f'saturation={self.saturation}',
            f'value={self.value})>'
        ))


class HSLColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='hsl'
):
    """Class that defines a hue/saturation/lightness (HSL) color."""

    @property
    def hue(self) -> int:
        self.__hue: int
        try:
            return self.__hue
        except AttributeError:
            self.__hue = int(self.clamped_hue * 360)
            return self.__hue

    @property
    def saturation(self) -> int:
        self.__saturation: int
        try:
            return self.__saturation
        except AttributeError:
            self.__saturation = int(self.clamped_saturation * 100)
            return self.__saturation

    @property
    def lightness(self) -> int:
        self.__lightness: int
        try:
            return self.__lightness
        except AttributeError:
            self.__lightness = int(self.clamped_lightness * 100)
            return self.__lightness

    @property
    def value_tuple(self) -> typing.Tuple[int, int, int]:
        self.__value_tuple: typing.Tuple[int, int, int]
        try:
            return self.__value_tuple
        except AttributeError:
            self.__value_tuple = (self.hue, self.saturation, self.lightness)
            return self.__value_tuple

    @property
    def clamped_value_tuple(self) -> typing.Tuple[float, float, float]:
        return self._get_value('get_value_tuple', function=True)

    @property
    def clamped_hue(self) -> float:
        return self._get_value('hsl_h')

    @property
    def clamped_saturation(self) -> float:
        return self._get_value('hsl_s')

    @property
    def clamped_lightness(self) -> float:
        return self._get_value('hsl_l')

    def __repr__(self) -> str:
        return ', '.join((
            f'<HSLColor(hue={self.hue}',
            f'saturation={self.saturation}',
            f'lightness={self.lightness})>'
        ))


# class LabColor(
#     colormath.color_objects.LabColor,
#     metaclass=ColorMeta,
#     attr_name='lab'
# ):
#     """Class that represents a CIE Lab color."""
#     pass


# class LCHabColor(
#     colormath.color_objects.LCHabColor,
#     metaclass=ColorMeta,
#     attr_name='lchab'
# ):
    """Class that represents a CIE LCH color converted through CIE Lab."""
    pass


class ColorGroupMeta(enum.EnumMeta):
    @staticmethod
    def get_conv_attr(self, name):
        return getattr(self.value, name)

    def __new__(metacls, name, bases, ns):
        for attr_name in ColorMeta._ColorMeta__class_registry:
            ns[attr_name] = property(
                functools.partial(
                    ColorGroupMeta.get_conv_attr,
                    name=attr_name
                )
            )
        return super().__new__(
            metacls,
            name,
            bases,
            ns
        )


class ColorGroup(enum.Enum, metaclass=ColorGroupMeta):
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

    @property
    def red(self) -> int:
        return self.value.red

    @property
    def r(self) -> int:
        return self.value.r

    @property
    def green(self) -> int:
        return self.value.green

    @property
    def g(self) -> int:
        return self.value.g

    @property
    def blue(self) -> int:
        return self.value.blue

    @property
    def b(self) -> int:
        return self.value.b

    @property
    def hex(self) -> str:
        return self.value.hex

    @property
    def value_tuple(self) -> typing.Tuple[int, int, int]:
        return self.value.value_tuple

    @property
    def clamped_value_tuple(self) -> typing.Tuple[float, float, float]:
        return self.value.clamped_value_tuple

    @property
    def clamped_red(self) -> float:
        return self.value.clamped_red

    @property
    def clamped_green(self) -> float:
        return self.value.clamped_green

    @property
    def clamped_blue(self) -> float:
        return self.value.clamped_blue

    @property
    def native_illuminant(self) -> str:
        return self.value.native_illuminant

    @property
    def gamma(self) -> float:
        return self.value.gamma
