#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# This script demonstrates how to iterate through glyphs in a GlyphsApp *.glyphs source file
# and parse glyph-specific color metadata that is used to highlight the glyph in font
# editors
#
# Dependencies for this script can be installed with:
#
#    $ pip3 install --upgrade glyphsLib
#

from glyphsLib import GSFont

SOURCE_PATH = "../glyphs_source/GenericSans-GreenHighlight.glyphs"

font = GSFont(SOURCE_PATH)

for glyph in font.glyphs:
    # integer for GlyphsApp color if present
    # None if color is absent
    glyph_color = glyph.color

    # string
    glyph_name = glyph.name
    # list of strings
    glyph_unicode = glyph.unicode

    print("{} - {} - {}".format(glyph_name, glyph_unicode, glyph_color))
