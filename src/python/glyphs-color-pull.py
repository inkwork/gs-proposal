#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2019 Font Bakery Reporter Authors and Contributors

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -----------------------------------------------------------------------------------------
# This script demonstrates how to iterate through glyphs in a GlyphsApp
# *.glyphs source file and parse glyph-specific color highlighting data,
# then map the color to definitions that are defined in a separate newline-
# delimited definitions file that uses a `KEY:VALUE` definition format
#
# Dependencies for this script can be installed with:
#
#    $ pip3 install --upgrade glyphsLib
#
# ------------------------------------------------------------------------------------------

import os
import sys
from enum import Enum

from glyphsLib import GSFont


SOURCE_PATH = "../glyphs_source/GenericSans-MultiHighlight.glyphs"
KEY_PATH = "colordefs.txt"


class Color(Enum):
    RED = 0
    ORANGE = 1
    BROWN = 2
    YELLOW = 3
    LTGREEN = 4
    DKGREEN = 5
    LTBLUE = 6
    DKBLUE = 7
    PURPLE = 8
    PINK = 9
    LTGREY = 10
    DKGREY = 11
    WHITE = 12  # this is an uncolored glyph


class ColorDefinitions(object):
    def __init__(self):
        self.red = {"hex": "", "rgba": "", "value": None}
        self.orange = {"hex": "", "rgba": "", "value": None}
        self.brown = {"hex": "", "rgba": "", "value": None}
        self.yellow = {"hex": "", "rgba": "", "value": None}
        self.ltgreen = {"hex": "", "rgba": "", "value": None}
        self.dkgreen = {"hex": "", "rgba": "", "value": None}
        self.ltblue = {"hex": "", "rgba": "", "value": None}
        self.dkblue = {"hex": "", "rgba": "", "value": None}
        self.purple = {"hex": "", "rgba": "", "value": None}
        self.pink = {"hex": "", "rgba": "", "value": None}
        self.ltgrey = {"hex": "", "rgba": "", "value": None}
        self.dkgrey = {"hex": "", "rgba": "", "value": None}
        # define default state for white?
        self.white = {"hex": "", "rgba": "", "value": None}


class GlyphColorObj(object):
    def __init__(self, name, unicode_hex, color, color_definitions):
        self.name = name
        self.unicode_hex = unicode_hex
        self.color = color
        self.color_name = color.name
        self.color_index = color.value

        if self.color_name == "RED":
            self.hex = color_definitions.red["hex"]
            self.rgba = color_definitions.red["rgba"]
            self.value = color_definitions.red["value"]
        elif self.color_name == "ORANGE":
            self.hex = color_definitions.orange["hex"]
            self.rgba = color_definitions.orange["rgba"]
            self.value = color_definitions.orange["value"]
        elif self.color_name == "BROWN":
            self.hex = color_definitions.brown["hex"]
            self.rgba = color_definitions.brown["rgba"]
            self.value = color_definitions.brown["value"]
        elif self.color_name == "YELLOW":
            self.hex = color_definitions.yellow["hex"]
            self.rgba = color_definitions.yellow["rgba"]
            self.value = color_definitions.yellow["value"]
        elif self.color_name == "LTGREEN":
            self.hex = color_definitions.ltgreen["hex"]
            self.rgba = color_definitions.ltgreen["rgba"]
            self.value = color_definitions.ltgreen["value"]
        elif self.color_name == "DKGREEN":
            self.hex = color_definitions.dkgreen["hex"]
            self.rgba = color_definitions.dkgreen["rgba"]
            self.value = color_definitions.dkgreen["value"]
        elif self.color_name == "LTBLUE":
            self.hex = color_definitions.ltblue["hex"]
            self.rgba = color_definitions.ltblue["rgba"]
            self.value = color_definitions.ltblue["value"]
        elif self.color_name == "DKBLUE":
            self.hex = color_definitions.dkblue["hex"]
            self.rgba = color_definitions.dkblue["rgba"]
            self.value = color_definitions.dkblue["value"]
        elif self.color_name == "PURPLE":
            self.hex = color_definitions.purple["hex"]
            self.rgba = color_definitions.purple["rgba"]
            self.value = color_definitions.purple["value"]
        elif self.color_name == "PINK":
            self.hex = color_definitions.pink["hex"]
            self.rgba = color_definitions.pink["rgba"]
            self.value = color_definitions.pink["value"]
        elif self.color_name == "LTGREY":
            self.hex = color_definitions.ltgrey["hex"]
            self.rgba = color_definitions.ltgrey["rgba"]
            self.value = color_definitions.ltgrey["value"]
        elif self.color_name == "DKGREY":
            self.hex = color_definitions.dkgrey["hex"]
            self.rgba = color_definitions.dkgrey["rgba"]
            self.value = color_definitions.dkgrey["value"]
        elif self.color_name == "WHITE":
            self.hex = color_definitions.white["hex"]
            self.rgba = color_definitions.white["rgba"]
            self.value = color_definitions.white["value"]


class ColorFileParser(object):
    def __init__(self, definition_path):
        self.definition_path = definition_path
        self.color_definitions = ColorDefinitions()

    def parse(self):
        valid_colors = [member.name for name, member in Color.__members__.items()]
        try:
            with open(self.definition_path, "r") as f:
                for line in f:
                    def_list = self._parse_colon_delimited_line(line.strip())
                    if def_list is not None:
                        color_name = def_list[0]
                        color_value = def_list[1]
                        if color_name in valid_colors:
                            self._define_colordefinitions(color_name, color_value)

            return self.color_definitions
        except Exception as e:
            sys.stderr.write(
                "[ERROR] Error during definition file parsing attempt: {}{}".format(
                    str(e), os.linesep
                )
            )

    def _parse_colon_delimited_line(self, line):
        # allow for empty lines
        # allow for "#" delimiter comment lines
        test_line = line.strip()
        if len(line) > 0 and test_line.startswith("#") is False:
            definition_list = line.split(":")
            if len(definition_list) == 2:
                return [definition_list[0].strip(), definition_list[1].strip()]
            else:
                return None
        else:
            return None

    def _define_colordefinitions(self, colorname, definition_value):
        if colorname == "RED":
            self.color_definitions.red["value"] = definition_value
        elif colorname == "ORANGE":
            self.color_definitions.orange["value"] = definition_value
        elif colorname == "BROWN":
            self.color_definitions.brown["value"] = definition_value
        elif colorname == "YELLOW":
            self.color_definitions.yellow["value"] = definition_value
        elif colorname == "LTGREEN":
            self.color_definitions.ltgreen["value"] = definition_value
        elif colorname == "DKGREEN":
            self.color_definitions.dkgreen["value"] = definition_value
        elif colorname == "LTBLUE":
            self.color_definitions.ltblue["value"] = definition_value
        elif colorname == "DKBLUE":
            self.color_definitions.dkblue["value"] = definition_value
        elif colorname == "PURPLE":
            self.color_definitions.purple["value"] = definition_value
        elif colorname == "PINK":
            self.color_definitions.pink["value"] = definition_value
        elif colorname == "LTGREY":
            self.color_definitions.ltgrey["value"] = definition_value
        elif colorname == "DKGREY":
            self.color_definitions.dkgrey["value"] = definition_value
        elif colorname == "WHITE":
            self.color_definitions.white["value"] = definition_value


def main():
    font = GSFont(SOURCE_PATH)
    glyph_list = []

    # parse definitions file, define ColorDefinitions object
    cfp = ColorFileParser(KEY_PATH)
    color_defs = cfp.parse()

    # parse source code for color settings
    # and create GlyphObj objects with color attributes
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
        # glyph_changetime = glyph.lastChange

        if glyph_color is not None:
            color = Color(glyph_color)
            gco = GlyphColorObj(glyph_name, glyph_unicode, color, color_defs)
        else:
            # default state if no color detected is WHITE
            gco = GlyphColorObj(glyph_name, glyph_unicode, Color.WHITE, color_defs)

        glyph_list.append(gco)

    for glyphobj in glyph_list:
        print(
            "[{} {}] : {} {}".format(
                glyphobj.name, glyphobj.unicode_hex, glyphobj.color_name, glyphobj.value
            )
        )


if __name__ == "__main__":
    main()
