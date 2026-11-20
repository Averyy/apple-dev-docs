# Stylesheet.ShapeStyle.ShapeProperties

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The appearance that a shape style applies.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Stylesheet.ShapeStyle.ShapeProperties
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.stylesheet.shape-style.shape-properties`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `stroke` ((Stroke | null)): The stroke or border drawn around the shape or, for a line or connection line, the stroke drawn along the line itself.

  **Allowed Types**: `Stroke`, `null`
- `opacity` ((number | null)): The opacity of the shape, in the range `0` to `1`.

  **Allowed Types**: `number`, `null`
- `reflection` ((Reflection | null)): The reflection of the shape.

  **Allowed Types**: `Reflection`, `null`
- `shadow` ((Shadow | null)): The shadow cast behind the shape.

  **Allowed Types**: `Shadow`, `null`
- `fill` ((Fill | null)): The fill used to decorate the interior of the shape. `null` clears the fill; if the key is omitted, the fill is inherited, and with no fill to inherit, the shape is unfilled.

  **Allowed Types**: `Fill`, `null`
- `head` ((LineEnd | null)): The head end of a line or connection line, drawn at its end point.

  **Allowed Types**: `LineEnd`, `null`
- `tail` ((LineEnd | null)): The tail end of a line or connection line, drawn at its start point.

  **Allowed Types**: `LineEnd`, `null`
- `layout_properties` (LayoutProperties): A set of properties defining how text is laid out inside the shape: padding, columns, and vertical alignment. It’s absent when the style sets none of these.
- `paragraph_properties` (ParagraphProperties): A set of properties that define the default paragraph formatting for text inside the shape. It’s absent when the style carries no default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/stylesheet.shapestyle.shapeproperties)*