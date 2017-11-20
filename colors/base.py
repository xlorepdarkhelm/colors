"""Base module containing the core components for the colors system."""

import enum
import functools
import inspect
import typing

import colormath
import colormath.color_conversions
import colormath.color_diff
import colormath.color_objects


class ColorMeta(type):
    """
    Metaclass for colors that sets up class and instance registries.

    This provides needed components for simple translation properties for
    colors.
    """

    __class_registry: typing.Dict[str, type] = {}

    @property
    def instances(cls):
        """Class-specific instance registry to flywheel instances."""
        try:
            return cls.__instances
        except AttributeError:
            cls.__instances = {}
            return cls.__instances

    @staticmethod
    def get_conversion(self, attr_name):
        """Handle conversions as necessary otherwise get attribute."""
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
                    self._BaseColor__color,
                    color_class
                )
                attrs[attr_name] = attr_class(color_val)
                return attrs[attr_name]
        else:
            return super(cls, self).__getattribute__(attr_name)

    def __new__(metacls, name, bases, ns, attr_name, **kwds):
        """Create new class definition."""
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
        """Hijack instance creation for flywheeling."""
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
    """Base class for color classes."""

    def __init__(self, color: colormath.color_objects.ColorBase) -> None:
        """Initialize with a given colormath object instance."""
        self.__color = color
        self.__values: typing.Dict[str, typing.Any] = {}

    def _get_value(self, name, function=False) -> typing.Any:
        """Get a specific value from the colormath object."""
        try:
            return self.__values[name]
        except KeyError:
            orig = getattr(self.__color, name)
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
        """Get the red color level (0-255)."""
        self.__red: int
        try:
            return self.__red
        except AttributeError:
            self.__red = int(self._get_value('rgb_r') * 255)
            return self.__red

    @property
    def r(self) -> int:
        """Get the red color level (0-255)."""
        self.__red: int
        try:
            return self.__red
        except AttributeError:
            self.__red = int(self._get_value('rgb_r') * 255)
            return self.__red

    @property
    def green(self) -> int:
        """Get the green color level (0-255)."""
        self.__green: int
        try:
            return self.__green
        except AttributeError:
            self.__green = int(self._get_value('rgb_g') * 255)
            return self.__green

    @property
    def g(self) -> int:
        """Get the green color level (0-255)."""
        self.__green: int
        try:
            return self.__green
        except AttributeError:
            self.__green = int(self._get_value('rgb_g') * 255)
            return self.__green

    @property
    def blue(self) -> int:
        """Get the blue color level (0-255)."""
        self.__blue: int
        try:
            return self.__blue
        except AttributeError:
            self.__blue = int(self._get_value('rgb_b') * 255)
            return self.__blue

    @property
    def b(self) -> int:
        """Get the blue color level (0-255)."""
        self.__blue: int
        try:
            return self.__blue
        except AttributeError:
            self.__blue = int(self._get_value('rgb_b') * 255)
            return self.__blue

    @property
    def hex(self) -> str:
        """Get the html 6-digit hex code (#rrggbb)."""
        return self._get_value('get_rgb_hex', function=True)

    @property
    def value_tuple(self) -> typing.Tuple[int, int, int]:
        """Get the tuple containing (red, green, blue)."""
        return self._get_value('get_upscaled_value_tuple', function=True)

    @classmethod
    def from_hex(cls, hex_str: str) -> 'sRGBColor':
        """Convert a 6-digit hex code into a new sRGBColor object."""
        return cls(
            colormath.color_objects.sRGBColor.new_from_rgb_hex(hex_str)
        )

    def __repr__(self) -> str:
        """Get the string representation of the sRGBColor instance."""
        return f'<sRGBColor(r={self.r}, g={self.g}, b={self.b})>'


def RGBColor(red: int, green: int, blue: int) -> sRGBColor:
    """Create sRGBColor instance for use in a Color Group."""
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
        """Get the color's hue angle (0-360)."""
        self.__hue: int
        try:
            return self.__hue
        except AttributeError:
            self.__hue = int(self._get_value('hsv_h'))
            return self.__hue

    @property
    def h(self) -> int:
        """Get the color's hue angle (0-360)."""
        self.__hue: int
        try:
            return self.__hue
        except AttributeError:
            self.__hue = int(self._get_value('hsv_h'))
            return self.__hue

    @property
    def saturation(self) -> int:
        """Get the color's saturation level (0-100)."""
        self.__saturation: int
        try:
            return self.__saturation
        except AttributeError:
            self.__saturation = int(self._get_value('hsv_s') * 100)
            return self.__saturation

    @property
    def s(self) -> int:
        """Get the color's saturation level (0-100)."""
        self.__saturation: int
        try:
            return self.__saturation
        except AttributeError:
            self.__saturation = int(self._get_value('hsv_s') * 100)
            return self.__saturation

    @property
    def value(self) -> int:
        """Get the color's value level (0-100)."""
        self.__value: int
        try:
            return self.__value
        except AttributeError:
            self.__value = int(self._get_value('hsv_v') * 100)
            return self.__value

    @property
    def v(self) -> int:
        """Get the color's value level (0-100)."""
        self.__value: int
        try:
            return self.__value
        except AttributeError:
            self.__value = int(self._get_value('hsv_v') * 100)
            return self.__value

    @property
    def value_tuple(self) -> typing.Tuple[int, int, int]:
        """Get the tuple containing (hue, saturation, value)."""
        self.__value_tuple: typing.Tuple[int, int, int]
        try:
            return self.__value_tuple
        except AttributeError:
            self.__value_tuple = (self.hue, self.saturation, self.value)
            return self.__value_tuple

    def __repr__(self) -> str:
        """Get the string representation of the HSVColor instance."""
        return f'<HSVColor(h={self.h}, s={self.s}, v={self.v})>'


class HSLColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='hsl'
):
    """Class that defines a hue/saturation/lightness (HSL) color."""

    @property
    def hue(self) -> int:
        """Get the color's hue angle (0-360)."""
        self.__hue: int
        try:
            return self.__hue
        except AttributeError:
            self.__hue = int(self._get_value('hsl_h'))
            return self.__hue

    @property
    def h(self) -> int:
        """Get the color's hue angle (0-360)."""
        self.__hue: int
        try:
            return self.__hue
        except AttributeError:
            self.__hue = int(self._get_value('hsl_h'))
            return self.__hue

    @property
    def saturation(self) -> int:
        """Get the color's saturation level (0-100)."""
        self.__saturation: int
        try:
            return self.__saturation
        except AttributeError:
            self.__saturation = int(self._get_value('hsl_s') * 100)
            return self.__saturation

    @property
    def s(self) -> int:
        """Get the color's saturation level (0-100)."""
        self.__saturation: int
        try:
            return self.__saturation
        except AttributeError:
            self.__saturation = int(self._get_value('hsl_s') * 100)
            return self.__saturation

    @property
    def lightness(self) -> int:
        """Get the color's lighness level (0-100)."""
        self.__lightness: int
        try:
            return self.__lightness
        except AttributeError:
            self.__lightness = int(self._get_value('hsl_l') * 100)
            return self.__lightness

    @property
    def l_(self) -> int:
        """Get the color's lighness level (0-100)."""
        self.__lightness: int
        try:
            return self.__lightness
        except AttributeError:
            self.__lightness = int(self._get_value('hsl_l') * 100)
            return self.__lightness

    @property
    def value_tuple(self) -> typing.Tuple[int, int, int]:
        """Get the tuple containing (hue, saturation, lightness)."""
        self.__value_tuple: typing.Tuple[int, int, int]
        try:
            return self.__value_tuple
        except AttributeError:
            self.__value_tuple = (self.hue, self.saturation, self.lightness)
            return self.__value_tuple

    def __repr__(self) -> str:
        """Get the string representation of the HSLColor instance."""
        return f'<HSLColor(h={self.h}, s={self.s}, l={self.l_})>'


class LabColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='lab'
):
    """Class that represents a CIE Lab color."""

    @property
    def lightness(self) -> float:
        """Get the color's lighness level (0-100)."""
        self.__lightness: float
        try:
            return self.__lightness
        except AttributeError:
            self.__lightness = self._get_value('lab_l')
            return self.__lightness

    @property
    def l_(self) -> float:
        """Get the color's lighness level (0-100)."""
        self.__lightness: float
        try:
            return self.__lightness
        except AttributeError:
            self.__lightness = self._get_value('lab_l')
            return self.__lightness

    @property
    def magenta_green(self) -> float:
        """Get the color's magenta [+] / green [-] axis position."""
        self.__magenta_green: float
        try:
            return self.__magenta_green
        except AttributeError:
            self.__magenta_green = self._get_value('lab_a')
            return self.__magenta_green

    @property
    def a(self) -> float:
        """Get the color's magenta [+] / green [-] axis position."""
        self.__magenta_green: float
        try:
            return self.__magenta_green
        except AttributeError:
            self.__magenta_green = self._get_value('lab_a')
            return self.__magenta_green

    @property
    def yellow_blue(self) -> float:
        """Get the color's yellow [+] / blue [-] axis position."""
        self.__yellow_blue: float
        try:
            return self.__yellow_blue
        except AttributeError:
            self.__yellow_blue = self._get_value('lab_b')
            return self.__yellow_blue

    @property
    def b(self) -> float:
        """Get the color's yellow [+] / blue [-] axis position."""
        self.__yellow_blue: float
        try:
            return self.__yellow_blue
        except AttributeError:
            self.__yellow_blue = self._get_value('lab_b')
            return self.__yellow_blue

    @property
    def value_tuple(self) -> typing.Tuple[float, float, float]:
        """Get the tuple containing (lightness, magenta_green, yellow_blue)."""
        self.__value_tuple: typing.Tuple[float, float, float]
        try:
            return self.__value_tuple
        except AttributeError:
            self.__value_tuple = self._get_value(
                'get_value_tuple',
                function=True
            )
            return self.__value_tuple

    def __repr__(self) -> str:
        """Get the string representation of the LabColor instance."""
        return f'<LabColor(l={self.l_}, a={self.a}, b={self.b})>'


class LuvColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='luv'
):
    """Class that represents a CIE Luv color."""

    @property
    def lightness(self) -> float:
        """Get the color's lighness level (0-100)."""
        self.__lightness: float
        try:
            return self.__lightness
        except AttributeError:
            self.__lightness = self._get_value('luv_l')
            return self.__lightness

    @property
    def l_(self) -> float:
        """Get the color's lighness level (0-100)."""
        self.__lightness: float
        try:
            return self.__lightness
        except AttributeError:
            self.__lightness = self._get_value('luv_l')
            return self.__lightness

    @property
    def u_axis(self) -> float:
        """Get the color's u axis position (-100 - 100)."""
        self.__u_axis: float
        try:
            return self.__u_axis
        except AttributeError:
            self.__u_axis = self._get_value('luv_u')
            return self.__u_axis

    @property
    def u(self) -> float:
        """Get the color's u axis position (-100 - 100)."""
        self.__u_axis: float
        try:
            return self.__u_axis
        except AttributeError:
            self.__u_axis = self._get_value('luv_u')
            return self.__u_axis

    @property
    def v_axis(self) -> float:
        """Get the color's v axis position (-100 - 100)."""
        self.__v_axis: float
        try:
            return self.__v_axis
        except AttributeError:
            self.__v_axis = self._get_value('luv_v')
            return self.__v_axis

    @property
    def v(self) -> float:
        """Get the color's v axis position (-100 - 100)."""
        self.__v_axis: float
        try:
            return self.__v_axis
        except AttributeError:
            self.__v_axis = self._get_value('luv_v')
            return self.__v_axis

    @property
    def value_tuple(self) -> typing.Tuple[float, float, float]:
        """Get the tuple containing (lightness, u_axis, yellow_blue)."""
        self.__value_tuple: typing.Tuple[float, float, float]
        try:
            return self.__value_tuple
        except AttributeError:
            self.__value_tuple = self._get_value(
                'get_value_tuple',
                function=True
            )
            return self.__value_tuple

    def __repr__(self) -> str:
        """Get the string representation of the LuvColor instance."""
        return f'<LuvColor(l={self.l_}, u={self.u}, v={self.v})>'


class LCHabColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='lchab'
):
    """Class that represents a CIE LCH color converted through CIE Lab."""

    @property
    def lightness(self) -> float:
        """Get the color's lighness level (0-100)."""
        self.__lightness: float
        try:
            return self.__lightness
        except AttributeError:
            self.__lightness = self._get_value('lch_l')
            return self.__lightness

    @property
    def l_(self) -> float:
        """Get the color's lighness level (0-100)."""
        self.__lightness: float
        try:
            return self.__lightness
        except AttributeError:
            self.__lightness = self._get_value('lch_l')
            return self.__lightness

    @property
    def chroma(self) -> float:
        """Get the color's chroma level (0-100)."""
        self.__chroma: float
        try:
            return self.__chroma
        except AttributeError:
            self.__chroma = self._get_value('lch_c')
            return self.__chroma

    @property
    def c(self) -> float:
        """Get the color's chroma level (0-100)."""
        self.__chroma: float
        try:
            return self.__chroma
        except AttributeError:
            self.__chroma = self._get_value('lch_c')
            return self.__chroma

    @property
    def hue(self) -> float:
        """Get the color's hue angle (0-360)."""
        self.__hue: float
        try:
            return self.__hue
        except AttributeError:
            self.__hue = self._get_value('lch_h')
            return self.__hue

    @property
    def h(self) -> float:
        """Get the color's hue angle (0-360)."""
        self.__hue: float
        try:
            return self.__hue
        except AttributeError:
            self.__hue = self._get_value('lch_h')
            return self.__hue

    @property
    def value_tuple(self) -> typing.Tuple[float, float, float]:
        """Get the tuple containing (lightness, chroma, hue)."""
        self.__value_tuple: typing.Tuple[float, float, float]
        try:
            return self.__value_tuple
        except AttributeError:
            self.__value_tuple = self._get_value(
                'get_value_tuple',
                function=True
            )
            return self.__value_tuple

    def __repr__(self) -> str:
        """Get the string representation of the LCHabColor instance."""
        return f'<LCHabColor(l={self.l_}, c={self.c}, h={self.h})>'


class LCHuvColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='lchuv'
):
    """Class that represents a CIE LCH color converted through CIE Luv."""

    @property
    def lightness(self) -> float:
        """Get the color's lighness level (0-100)."""
        self.__lightness: float
        try:
            return self.__lightness
        except AttributeError:
            self.__lightness = self._get_value('lch_l')
            return self.__lightness

    @property
    def l_(self) -> float:
        """Get the color's lighness level (0-100)."""
        self.__lightness: float
        try:
            return self.__lightness
        except AttributeError:
            self.__lightness = self._get_value('lch_l')
            return self.__lightness

    @property
    def chroma(self) -> float:
        """Get the color's chroma level (0-100)."""
        self.__chroma: float
        try:
            return self.__chroma
        except AttributeError:
            self.__chroma = self._get_value('lch_c')
            return self.__chroma

    @property
    def c(self) -> float:
        """Get the color's chroma level (0-100)."""
        self.__chroma: float
        try:
            return self.__chroma
        except AttributeError:
            self.__chroma = self._get_value('lch_c')
            return self.__chroma

    @property
    def hue(self) -> float:
        """Get the color's hue angle (0-360)."""
        self.__hue: float
        try:
            return self.__hue
        except AttributeError:
            self.__hue = self._get_value('lch_h')
            return self.__hue

    @property
    def h(self) -> float:
        """Get the color's hue angle (0-360)."""
        self.__hue: float
        try:
            return self.__hue
        except AttributeError:
            self.__hue = self._get_value('lch_h')
            return self.__hue

    @property
    def value_tuple(self) -> typing.Tuple[float, float, float]:
        """Get the tuple containing (lightness, chroma, hue)."""
        self.__value_tuple: typing.Tuple[float, float, float]
        try:
            return self.__value_tuple
        except AttributeError:
            self.__value_tuple = self._get_value(
                'get_value_tuple',
                function=True
            )
            return self.__value_tuple

    def __repr__(self) -> str:
        """Get the string representation of the LCHuvColor instance."""
        return f'<LCHuvColor(l={self.l_}, c={self.c}, h={self.h})>'


class XYZColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='xyz'
):
    """Class that represents an XYZ color."""

    @property
    def x_coordinate(self) -> float:
        """Get the color's x coordinate."""
        self.__x_coordinate: float
        try:
            return self.__x_coordinate
        except AttributeError:
            self.__x_coordinate = self._get_value('xyz_x')
            return self.__x_coordinate

    @property
    def x(self) -> float:
        """Get the color's x coordinate."""
        self.__x_coordinate: float
        try:
            return self.__x_coordinate
        except AttributeError:
            self.__x_coordinate = self._get_value('xyz_x')
            return self.__x_coordinate

    @property
    def y_coordinate(self) -> float:
        """Get the color's y coordinate."""
        self.__y_coordinate: float
        try:
            return self.__y_coordinate
        except AttributeError:
            self.__y_coordinate = self._get_value('xyz_y')
            return self.__y_coordinate

    @property
    def y(self) -> float:
        """Get the color's y coordinate."""
        self.__y_coordinate: float
        try:
            return self.__y_coordinate
        except AttributeError:
            self.__y_coordinate = self._get_value('xyz_y')
            return self.__y_coordinate

    @property
    def z_coordinate(self) -> float:
        """Get the color's z coordinate."""
        self.__z_coordinate: float
        try:
            return self.__z_coordinate
        except AttributeError:
            self.__z_coordinate = self._get_value('xyz_z')
            return self.__z_coordinate

    @property
    def z(self) -> float:
        """Get the color's z coordinate."""
        self.__z_coordinate: float
        try:
            return self.__z_coordinate
        except AttributeError:
            self.__z_coordinate = self._get_value('xyz_z')
            return self.__z_coordinate

    @property
    def value_tuple(self) -> typing.Tuple[float, float, float]:
        """Get the tuple containing the (x, y, z) coordinates."""
        self.__value_tuple: typing.Tuple[float, float, float]
        try:
            return self.__value_tuple
        except AttributeError:
            self.__value_tuple = self._get_value(
                'get_value_tuple',
                function=True
            )
            return self.__value_tuple

    def __repr__(self) -> str:
        """Get the string representation of the XYZColor instance."""
        return f'<XYZColor(x={self.x}, y={self.y}, z={self.z})>'


class xyYColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='xyy'
):
    """Class that represents a CIE xyY color."""

    @property
    def x_coordinate(self) -> float:
        """Get the color's x coordinate."""
        self.__x_coordinate: float
        try:
            return self.__x_coordinate
        except AttributeError:
            self.__x_coordinate = self._get_value('xyy_x')
            return self.__x_coordinate

    @property
    def x(self) -> float:
        """Get the color's x coordinate."""
        self.__x_coordinate: float
        try:
            return self.__x_coordinate
        except AttributeError:
            self.__x_coordinate = self._get_value('xyy_x')
            return self.__x_coordinate

    @property
    def y_coordinate(self) -> float:
        """Get the color's y coordinate."""
        self.__y_coordinate: float
        try:
            return self.__y_coordinate
        except AttributeError:
            self.__y_coordinate = self._get_value('xyy_y')
            return self.__y_coordinate

    @property
    def y(self) -> float:
        """Get the color's y coordinate."""
        self.__y_coordinate: float
        try:
            return self.__y_coordinate
        except AttributeError:
            self.__y_coordinate = self._get_value('xyy_y')
            return self.__y_coordinate

    @property
    def luminance(self) -> float:
        """Get the color's luminance level."""
        self.__luminance: float
        try:
            return self.__luminance
        except AttributeError:
            self.__luminance = self._get_value('xyy_Y')
            return self.__luminance

    @property
    def Y(self) -> float:
        """Get the color's luminance level."""
        self.__luminance: float
        try:
            return self.__luminance
        except AttributeError:
            self.__luminance = self._get_value('xyy_Y')
            return self.__luminance

    @property
    def value_tuple(self) -> typing.Tuple[float, float, float]:
        """Get the tuple containing the (x coord, y coord, luminance)."""
        self.__value_tuple: typing.Tuple[float, float, float]
        try:
            return self.__value_tuple
        except AttributeError:
            self.__value_tuple = self._get_value(
                'get_value_tuple',
                function=True
            )
            return self.__value_tuple

    def __repr__(self) -> str:
        """Get the string representation of the xyYColor instance."""
        return f'<xyYColor(x={self.x}, y={self.y}, Y={self.Y})>'


class AdobeRGBColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='adobe'
):
    """Class that represents an Adobe RGB color."""

    @property
    def red(self) -> int:
        """Get the red color level (0-255)."""
        self.__red: int
        try:
            return self.__red
        except AttributeError:
            self.__red = int(self._get_value('rgb_r') * 255)
            return self.__red

    @property
    def r(self) -> int:
        """Get the red color level (0-255)."""
        self.__red: int
        try:
            return self.__red
        except AttributeError:
            self.__red = int(self._get_value('rgb_r') * 255)
            return self.__red

    @property
    def green(self) -> int:
        """Get the green color level (0-255)."""
        self.__green: int
        try:
            return self.__green
        except AttributeError:
            self.__green = int(self._get_value('rgb_g') * 255)
            return self.__green

    @property
    def g(self) -> int:
        """Get the green color level (0-255)."""
        self.__green: int
        try:
            return self.__green
        except AttributeError:
            self.__green = int(self._get_value('rgb_g') * 255)
            return self.__green

    @property
    def blue(self) -> int:
        """Get the blue color level (0-255)."""
        self.__blue: int
        try:
            return self.__blue
        except AttributeError:
            self.__blue = int(self._get_value('rgb_b') * 255)
            return self.__blue

    @property
    def b(self) -> int:
        """Get the blue color level (0-255)."""
        self.__blue: int
        try:
            return self.__blue
        except AttributeError:
            self.__blue = int(self._get_value('rgb_b') * 255)
            return self.__blue

    @property
    def hex(self) -> str:
        """Get the html 6-digit hex code (#rrggbb)."""
        return self._get_value('get_rgb_hex', function=True)

    @property
    def value_tuple(self) -> typing.Tuple[int, int, int]:
        """Get the tuple containing (red, green, blue)."""
        return self._get_value('get_upscaled_value_tuple', function=True)

    @classmethod
    def from_hex(cls, hex_str: str) -> 'AdobeRGBColor':
        """Convert a 6-digit hex code into a new AdobeRGBColor object."""
        return cls(
            colormath.color_objects.AdobeRGBColor.new_from_rgb_hex(hex_str)
        )

    def __repr__(self) -> str:
        """Get the string representation of the AdobeRGBColor instance."""
        return f'<AdobeRGBColor(r={self.r}, g={self.g}, b={self.b})>'


class AppleRGBColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='apple'
):
    """Class that represents an Adobe RGB color."""

    @property
    def red(self) -> int:
        """Get the red color level (0-255)."""
        self.__red: int
        try:
            return self.__red
        except AttributeError:
            self.__red = int(self._get_value('rgb_r') * 255)
            return self.__red

    @property
    def r(self) -> int:
        """Get the red color level (0-255)."""
        self.__red: int
        try:
            return self.__red
        except AttributeError:
            self.__red = int(self._get_value('rgb_r') * 255)
            return self.__red

    @property
    def green(self) -> int:
        """Get the green color level (0-255)."""
        self.__green: int
        try:
            return self.__green
        except AttributeError:
            self.__green = int(self._get_value('rgb_g') * 255)
            return self.__green

    @property
    def g(self) -> int:
        """Get the green color level (0-255)."""
        self.__green: int
        try:
            return self.__green
        except AttributeError:
            self.__green = int(self._get_value('rgb_g') * 255)
            return self.__green

    @property
    def blue(self) -> int:
        """Get the blue color level (0-255)."""
        self.__blue: int
        try:
            return self.__blue
        except AttributeError:
            self.__blue = int(self._get_value('rgb_b') * 255)
            return self.__blue

    @property
    def b(self) -> int:
        """Get the blue color level (0-255)."""
        self.__blue: int
        try:
            return self.__blue
        except AttributeError:
            self.__blue = int(self._get_value('rgb_b') * 255)
            return self.__blue

    @property
    def hex(self) -> str:
        """Get the html 6-digit hex code (#rrggbb)."""
        return self._get_value('get_rgb_hex', function=True)

    @property
    def value_tuple(self) -> typing.Tuple[int, int, int]:
        """Get the tuple containing (red, green, blue)."""
        return self._get_value('get_upscaled_value_tuple', function=True)

    @classmethod
    def from_hex(cls, hex_str: str) -> 'AppleRGBColor':
        """Convert a 6-digit hex code into a new AppleRGBColor object."""
        return cls(
            colormath.color_objects.AppleRGBColor.new_from_rgb_hex(hex_str)
        )

    def __repr__(self) -> str:
        """Get the string representation of the AppleRGBColor instance."""
        return f'<AppleRGBColor(r={self.r}, g={self.g}, b={self.b})>'


class CMYColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='cmy'
):
    """Class that represents a CMY color."""

    @property
    def cyan(self) -> float:
        """Get the cyan color level."""
        self.__cyan: float
        try:
            return self.__cyan
        except AttributeError:
            self.__cyan = self._get_value('cmy_c')
            return self.__cyan

    @property
    def c(self) -> float:
        """Get the cyan color level."""
        self.__cyan: float
        try:
            return self.__cyan
        except AttributeError:
            self.__cyan = self._get_value('cmy_c')
            return self.__cyan

    @property
    def magenta(self) -> float:
        """Get the magenta color level."""
        self.__magenta: float
        try:
            return self.__magenta
        except AttributeError:
            self.__magenta = self._get_value('cmy_m')
            return self.__magenta

    @property
    def m(self) -> float:
        """Get the magenta color level."""
        self.__magenta: float
        try:
            return self.__magenta
        except AttributeError:
            self.__magenta = self._get_value('cmy_m')
            return self.__magenta

    @property
    def yellow(self) -> float:
        """Get the yellow color level."""
        self.__yellow: float
        try:
            return self.__yellow
        except AttributeError:
            self.__yellow = self._get_value('cmy_y')
            return self.__yellow

    @property
    def y(self) -> float:
        """Get the yellow color level."""
        self.__yellow: float
        try:
            return self.__yellow
        except AttributeError:
            self.__yellow = self._get_value('cmy_y')
            return self.__yellow

    @property
    def value_tuple(self) -> typing.Tuple[float, float, float]:
        """Get the tuple containing (cyan, magenta, yellow)."""
        self.__value_tuple: typing.Tuple[float, float, float]
        try:
            return self.__value_tuple
        except AttributeError:
            self.__value_tuple = self._get_value(
                'get_value_tuple',
                function=True
            )
            return self.__value_tuple

    def __repr__(self) -> str:
        """Get the string representation of the CMYColor instance."""
        return f'<CMYColor(c={self.c}, m={self.m}, y={self.y})>'


class CMYKColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='cmyk'
):
    """Class that represents a CMYK color."""

    @property
    def cyan(self) -> float:
        """Get the cyan color level."""
        self.__cyan: float
        try:
            return self.__cyan
        except AttributeError:
            self.__cyan = self._get_value('cmyk_c')
            return self.__cyan

    @property
    def c(self) -> float:
        """Get the cyan color level."""
        self.__cyan: float
        try:
            return self.__cyan
        except AttributeError:
            self.__cyan = self._get_value('cmyk_c')
            return self.__cyan

    @property
    def magenta(self) -> float:
        """Get the magenta color level."""
        self.__magenta: float
        try:
            return self.__magenta
        except AttributeError:
            self.__magenta = self._get_value('cmyk_m')
            return self.__magenta

    @property
    def m(self) -> float:
        """Get the magenta color level."""
        self.__magenta: float
        try:
            return self.__magenta
        except AttributeError:
            self.__magenta = self._get_value('cmyk_m')
            return self.__magenta

    @property
    def yellow(self) -> float:
        """Get the yellow color level."""
        self.__yellow: float
        try:
            return self.__yellow
        except AttributeError:
            self.__yellow = self._get_value('cmyk_y')
            return self.__yellow

    @property
    def y(self) -> float:
        """Get the yellow color level."""
        self.__yellow: float
        try:
            return self.__yellow
        except AttributeError:
            self.__yellow = self._get_value('cmyk_y')
            return self.__yellow

    @property
    def black(self) -> float:
        """Get the black color level."""
        self.__black: float
        try:
            return self.__black
        except AttributeError:
            self.__black = self._get_value('cmyk_k')
            return self.__black

    @property
    def k(self) -> float:
        """Get the black color level."""
        self.__black: float
        try:
            return self.__black
        except AttributeError:
            self.__black = self._get_value('cmyk_k')
            return self.__black

    @property
    def value_tuple(self) -> typing.Tuple[float, float, float, float]:
        """Get the tuple containing (cyan, magenta, yellow, black)."""
        self.__value_tuple: typing.Tuple[float, float, float, float]
        try:
            return self.__value_tuple
        except AttributeError:
            self.__value_tuple = self._get_value(
                'get_value_tuple',
                function=True
            )
            return self.__value_tuple

    def __repr__(self) -> str:
        """Get the string representation of the CMYKColor instance."""
        return f'<CMYKColor(c={self.c}, m={self.m}, y={self.y}, k={self.k})>'


class IPTColor(
    BaseColor,
    metaclass=ColorMeta,
    attr_name='ipt'
):
    """Class that represents an IPT color."""

    @property
    def i_coordinate(self) -> float:
        """Get the color's i coordinate."""
        self.__i_coordinate: float
        try:
            return self.__i_coordinate
        except AttributeError:
            self.__i_coordinate = self._get_value('ipt_i')
            return self.__i_coordinate

    @property
    def i(self) -> float:
        """Get the color's i coordinate."""
        self.__i_coordinate: float
        try:
            return self.__i_coordinate
        except AttributeError:
            self.__i_coordinate = self._get_value('ipt_i')
            return self.__i_coordinate

    @property
    def p_coordinate(self) -> float:
        """Get the color's p coordinate."""
        self.__p_coordinate: float
        try:
            return self.__p_coordinate
        except AttributeError:
            self.__p_coordinate = self._get_value('ipt_p')
            return self.__p_coordinate

    @property
    def p(self) -> float:
        """Get the color's p coordinate."""
        self.__p_coordinate: float
        try:
            return self.__p_coordinate
        except AttributeError:
            self.__p_coordinate = self._get_value('ipt_p')
            return self.__p_coordinate

    @property
    def t_coordinate(self) -> float:
        """Get the color's t coordinate."""
        self.__t_coordinate: float
        try:
            return self.__t_coordinate
        except AttributeError:
            self.__t_coordinate = self._get_value('ipt_t')
            return self.__t_coordinate

    @property
    def t(self) -> float:
        """Get the color's t coordinate."""
        self.__t_coordinate: float
        try:
            return self.__t_coordinate
        except AttributeError:
            self.__t_coordinate = self._get_value('ipt_t')
            return self.__t_coordinate

    @property
    def value_tuple(self) -> typing.Tuple[float, float, float]:
        """Get the tuple containing the (i, p, t) coordinates."""
        self.__value_tuple: typing.Tuple[float, float, float]
        try:
            return self.__value_tuple
        except AttributeError:
            self.__value_tuple = self._get_value(
                'get_value_tuple',
                function=True
            )
            return self.__value_tuple

    def __repr__(self) -> str:
        """Get the string representation of the IPTColor instance."""
        return f'<IPTColor(i={self.i}, p={self.p}, t={self.t})>'


class ColorGroupMeta(enum.EnumMeta):
    """Metaclass for Color Groups."""

    @staticmethod
    def get_conv_attr(self, name):
        """Get attribute for conversion from the enum value."""
        return getattr(self.value, name)

    def __new__(metacls, name, bases, ns):
        """Add all conversion properties to the new instance."""
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
        color: typing.Union['ColorGroup', 'BaseColor']
    ) -> 'ColorGroup':
        """Find the closest match in this color group to the given color."""
        color_object = color.lab._BaseColor__color  # type: ignore

        distances = {
            colormath.color_diff.delta_e_cmc(
                color_object,
                item.lab._BaseColor__color  # type: ignore
            ): item
            for item in reversed(cls)
        }
        return distances[min(distances.keys())]  # type: ignore

    @property
    def red(self) -> int:
        """Get the red color level (0-255)."""
        return self.value.red

    @property
    def r(self) -> int:
        """Get the red color level (0-255)."""
        return self.value.r

    @property
    def green(self) -> int:
        """Get the green color level (0-255)."""
        return self.value.green

    @property
    def g(self) -> int:
        """Get the green color level (0-255)."""
        return self.value.g

    @property
    def blue(self) -> int:
        """Get the blue color level (0-255)."""
        return self.value.blue

    @property
    def b(self) -> int:
        """Get the blue color level (0-255)."""
        return self.value.b

    @property
    def hex(self) -> str:
        """Get the html 6-digit hex code (#rrggbb)."""
        return self.value.hex

    @property
    def value_tuple(self) -> typing.Tuple[int, int, int]:
        """Get the tuple containing (red, green, blue)."""
        return self.value.value_tuple
