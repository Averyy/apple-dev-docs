# Table.VisualProperties.BodyStrokeProperties

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The borders and gridlines of a table’s body region, and their visibility.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Table.VisualProperties.BodyStrokeProperties
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.table.visual-properties.body-stroke-properties`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `horizontal_border_stroke` (Stroke): The outer top and bottom borders of the body region.
- `vertical_border_stroke` (Stroke): The outer left and right borders of the body region.
- `horizontal_stroke` (Stroke): The horizontal gridlines between body rows (interior only; the outer borders are `horizontal_border_stroke`).
- `vertical_stroke` (Stroke): The vertical gridlines between body columns (interior only; the outer borders are `vertical_border_stroke`).
- `border_strokes_visible` (boolean): Whether the body’s outer border strokes (`horizontal_border_stroke` and `vertical_border_stroke`) are visible. It’s the main visibility setting for both.
- `horizontal_strokes_visible` (boolean): Whether the body’s horizontal gridlines are visible. It’s their main visibility setting.
- `vertical_strokes_visible` (boolean): Whether the body’s vertical gridlines are visible. It’s their main visibility setting.

## See Also

### Objects
- [object Table.VisualProperties.HeaderFooterStrokeProperties](./table.visualproperties.headerfooterstrokeproperties.md)
  The borders, gridlines, and visibility toggles of a table’s header or footer region.
- [object Table.VisualProperties.OverallProperties](./table.visualproperties.overallproperties.md)
  The style settings that apply to a whole table.
- [object Table.VisualProperties.StrokePreset](./table.visualproperties.strokepreset.md)
  One of a table’s stroke presets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/table.visualproperties.bodystrokeproperties)*