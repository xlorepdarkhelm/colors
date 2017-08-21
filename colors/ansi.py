import collections.abc
import colorsys
import enum
import functools
import typing

from colors import RGBColor

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
