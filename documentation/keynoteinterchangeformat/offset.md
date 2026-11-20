# Offset

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A horizontal and vertical displacement, in points.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Offset
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.offset`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `dx` (number): The horizontal offset, in points.

  **Default**: `0`
- `dy` (number): The vertical offset, in points.

  **Default**: `0`

## See Also

### Positions
- [object Geometry](./geometry.md)
  The bounding box in which an object is positioned.
- [object Position](./position.md)
  A point, in points, in whichever coordinate space the property using it defines, measured downward from that space’s top-left corner.
- [object Insets](./insets.md)
  Space reserved along each edge of an area, in points.
- [object TabStopType](./tabstoptype.md)
  A tab stop.
- [type VerticalAlignmentType](./verticalalignmenttype.md)
  Vertical alignment of text within a container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/offset)*