# Table.VisualProperties.StrokePreset

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

One of a table’s stroke presets.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.VisualProperties.StrokePreset
```

## Overview

Applying the preset strokes each edge listed in `visible_edges` and clears every edge not listed. Interior edges take `horizontal_stroke` or `vertical_stroke`, and outer edges take `exterior_stroke`.

## Topics

### Enumerations
- [type Table.VisualProperties.StrokePreset.Edge](./table.visualproperties.strokepreset.edge.md)
  An edge of the stroked range that a stroke preset can turn on.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.visual-properties.stroke-preset`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `horizontal_stroke` (Stroke): The stroke applied to the interior horizontal gridlines this preset turns on.
- `vertical_stroke` (Stroke): The stroke applied to the interior vertical gridlines this preset turns on.
- `exterior_stroke` (Stroke): The stroke applied to the outer border edges this preset turns on.
- `visible_edges` ([Table.VisualProperties.StrokePreset.Edge]): The edges this preset strokes; every edge left out is cleared when the preset is applied. Order isn’t meaningful and each edge must appear at most once. An empty list is the *no borders* preset.

## See Also

### Objects
- [object Table.VisualProperties.BodyStrokeProperties](./table.visualproperties.bodystrokeproperties.md)
  The borders and gridlines of a table’s body region, and their visibility.
- [object Table.VisualProperties.HeaderFooterStrokeProperties](./table.visualproperties.headerfooterstrokeproperties.md)
  The borders, gridlines, and visibility toggles of a table’s header or footer region.
- [object Table.VisualProperties.OverallProperties](./table.visualproperties.overallproperties.md)
  The style settings that apply to a whole table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.visualproperties.strokepreset)*