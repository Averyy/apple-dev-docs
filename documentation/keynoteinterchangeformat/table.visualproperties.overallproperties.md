# Table.VisualProperties.OverallProperties

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The style settings that apply to a whole table.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.VisualProperties.OverallProperties
```

## Overview

A `preset_identifier` here is matched against the overall style of each table style collection in the document stylesheet by the numeric slot in the identifier rather than by the whole string, so an identifier not in that form resolves to the first slot. When no collection matches, the first table style in the stylesheet is used.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.visual-properties.overall-properties`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `behaves_like_spreadsheet` (boolean): Whether the table uses spreadsheet-style interaction (cell selection, navigation, and fill handles). Keynote writes `false`; when no value is given, `true` is used.
- `auto_resize` (boolean): Whether the table grows and shrinks to fit its content rather than keeping fixed row and column sizes.
- `writing_direction` (WritingDirectionType): The default writing direction for the table (left-to-right, right-to-left, or natural).
- `has_alternating_rows` (boolean): Whether every other body row is filled with `alternating_rows_fill` to produce a banded look.
- `alternating_rows_fill` ((Fill | null)): The fill applied to alternating body rows when `has_alternating_rows` is `true`. If it’s absent, it’s inherited; an explicit `null` leaves the alternating rows unfilled, which isn’t the same as a fill at 0% opacity.

  **Allowed Types**: `Fill`, `null`
- `rounded_corners` (boolean): Whether the table outline uses rounded corners. Keynote always writes `false` and ignores the value when it reads a document.
- `stroke_presets` ([Table.VisualProperties.StrokePreset]): The border and gridline stroke presets available for this table, in order. They are choices that can be applied, not a description of the table’s borders and gridlines. A list shorter than 15 entries is padded with generated presets, and a longer one is truncated.

## See Also

### Objects
- [object Table.VisualProperties.BodyStrokeProperties](./table.visualproperties.bodystrokeproperties.md)
  The borders and gridlines of a table’s body region, and their visibility.
- [object Table.VisualProperties.HeaderFooterStrokeProperties](./table.visualproperties.headerfooterstrokeproperties.md)
  The borders, gridlines, and visibility toggles of a table’s header or footer region.
- [object Table.VisualProperties.StrokePreset](./table.visualproperties.strokepreset.md)
  One of a table’s stroke presets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.visualproperties.overallproperties)*