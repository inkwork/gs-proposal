#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# This script demonstrates how to iterate through glyphs in a GlyphsApp *.glyphs source file
# and parse glyph-specific metadata
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
    # date / time formatted as 2019-01-18 15:04:57 if present
    # None if no edits have been made to the glyph
    glyph_changetime = glyph.lastChange

    print(
        "{} - {} - {} - {}".format(
            glyph_name, glyph_unicode, glyph_color, glyph_changetime
        )
    )
