#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# This script demonstrates how to iterate through glyphs in a UFO source directory
# and parse glyph-specific color metadata
#
# Dependencies for this script can be installed with:
#
#    $ pip3 install --upgrade fontTools
#

from fontTools.ufoLib.glifLib import GlyphSet

# this path must be to the `glyphs` subdirectory of the root UFO directory
GLYPH_DIR = "../ufo_source/GenericSans-GreenHighlight.ufo/glyphs"


# dummy object that is used to set glyph-specific attributes
# by fontTools.ufoLib.glifLib.GlyphObject.readGlyph() method
class GlyphObj(object):
    def __init__(self):
        pass


gs = GlyphSet(GLYPH_DIR)
for glif in gs.contents:
    go = GlyphObj()
    gs.readGlyph(glif, glyphObject=go)

    # define useful glyph data fields through read of the glyph object
    # Includes:
    # - name
    # - unicode(s)
    # - glyph highlight color (defined by designer in font editor)
    #      - defined in RGBA format
    #      - defined in sRGB color space (https://en.wikipedia.org/wiki/SRGB)
    #      - returns comma-separated string of these four integer or float values in set [0.0,1.0]
    #      - defined as None if no highlighting used on glyph
    # - last write time/date
    # - note (glyph-specific free text entered by designer in editor)
    #      - Unicode Python str
    #      - defined as None if no free text note is defined for the glyph
    glyph_name = go.name
    glyph_unicode_list = go.unicodes

    if hasattr(go, "lib"):
        glyph_lib = go.lib
        if glyph_lib["public.markColor"] is not None:
            glyph_color = glyph_lib["public.markColor"]
        else:
            glyph_color = None
        # this field seems to be GlyphsApp editor dependent, I do not see this in
        # Robofont modified *.glif files
        if glyph_lib["com.schriftgestaltung.Glyphs.lastChange"] is not None:
            glyph_lastchange = glyph_lib["com.schriftgestaltung.Glyphs.lastChange"]
        else:
            glyph_lastchange = None
    else:
        glyph_color = None
        glyph_lastchange = None

    if hasattr(go, "note"):
        glyph_note = go.note
    else:
        glyph_note = None

    print(
        "{} - {} - {} - {} - {}".format(
            glyph_name, glyph_unicode_list, glyph_color, glyph_lastchange, glyph_note
        )
    )
