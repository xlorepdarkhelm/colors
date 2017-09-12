# colors
Python module for manipulating and generating color codes.

The primary concept for this is to be able to use a named color defined from something like the X11 Color Codes, and then be able to translate it to the closest color in another color set, like the xterm-256 colors. More features will be added as necessary. I am attempting to make this as flexible and expansive as possible, to be a handy API for Python developers to use.

I am relying on the colormath module to provide the color types, which also then provides me a convenient better distance (delta E) calculation to use for the color conversions.

I tend to write code in Python 3.6. There might be some parts of the code that do not work in Python versions lower than that without tweaks I may eventually make it more universal.... or not. Not sure yet.
