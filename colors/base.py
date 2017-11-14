"""Base module containing the core components for the colors system."""

import enum
import functools
import inspect
import sys
import typing

import colormath
import colormath.color_objects


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
        try:
            return self.__color_registry[attr_name]
        except KeyError:
            cls = type(self)
            metacls = type(cls)
            try:
                class_name = metacls.__class_registry[attr_name]
            except KeyError:
                return getattr(
                    super(cls, self),
                    '__getattr__',
                    super(cls, self).__getattribute__
                )(attr_name)
            all_classes = dict(
                inspect.getmembers(
                    sys.modules.get(__name__, sys.modules['colors.base']),
                    inspect.isclass
                )
            )
            try:
                color_class = all_classes[class_name]
            except KeyError:
                return super().__getattr__(attr_name)
            self.__color_registry[attr_name] = \
                colormath.color_conversions.convert_color(
                    self,
                    color_class
                )
            return self.__color_registry[attr_name]

    def __new__(metacls, name, bases, ns, attr_name, **kwds):
        try:
            return metacls.__class_registry[attr_name]
        except KeyError:
            ns[f'_{metacls.__name__}__color_registry'] = {}
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
            cls.instances[arguments] = cls.__new__(cls, *args, **kwargs)
            return cls.instances[arguments]


class sRGBColor(
    colormath.color_objects.sRGBColor,
    metaclass=ColorMeta,
    attr_name='srgb'
):
    """Class that defines a red/green/blue (RGB) color."""
    pass


class HSVColor(
    colormath.color_objects.HSVColor,
    metaclass=ColorMeta,
    attr_name='hsv'
):
    """Class that defines a hue/saturation/value (HSV) color."""
    pass


class HSLColor(
    colormath.color_objects.HSLColor,
    metaclass=ColorMeta,
    attr_name='hsl'
):
    """Class that defines a hue/saturation/lightness (HSL) color."""
    pass


class LabColor(
    colormath.color_objects.LabColor,
    metaclass=ColorMeta,
    attr_name='lab'
):
    """Class that represents a CIE Lab color."""
    pass


class LCHabColor(
    colormath.color_objects.LCHabColor,
    metaclass=ColorMeta,
    attr_name='lchab'
):
    """Class that represents a CIE LCH color converted through CIE Lab."""
    pass


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
