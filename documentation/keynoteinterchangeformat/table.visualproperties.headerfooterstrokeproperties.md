# Table.VisualProperties.HeaderFooterStrokeProperties

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The borders, gridlines, and visibility toggles of a table’s header or footer region.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.VisualProperties.HeaderFooterStrokeProperties
```

## Overview

The same type is used for header rows, header columns, and footer rows; the region it describes depends on which of the table’s visual properties holds it.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.visual-properties.header-footer-stroke-properties`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `border_stroke` (Stroke): The outer border around the region.
- `separator_stroke` (Stroke): The stroke that separates this region from the adjacent body.
- `horizontal_stroke` (Stroke): The horizontal gridlines between cells inside the region.
- `vertical_stroke` (Stroke): The vertical gridlines between cells inside the region.
- `separator_visible` (boolean): Whether `separator_stroke` is visible.
- `across_strokes_visible` (boolean): Whether the strokes that run across the region are visible: the vertical strokes for header and footer rows, and the horizontal strokes for header columns.

## See Also

### Objects
- [object Table.VisualProperties.BodyStrokeProperties](./table.visualproperties.bodystrokeproperties.md)
  The borders and gridlines of a table’s body region, and their visibility.
- [object Table.VisualProperties.OverallProperties](./table.visualproperties.overallproperties.md)
  The style settings that apply to a whole table.
- [object Table.VisualProperties.StrokePreset](./table.visualproperties.strokepreset.md)
  One of a table’s stroke presets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.visualproperties.headerfooterstrokeproperties)*