# Insets

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

Space reserved along each edge of an area, in points.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Insets
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.insets`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `top` (number): The top inset, in points, in the range `0` to `50000000`. Validation: minimum value `0`, maximum value `50000000`.

  **Default**: `0`; **Minimum**: `0`; **Maximum**: `50000000`
- `bottom` (number): The bottom inset, in points, in the range `0` to `50000000`. Validation: minimum value `0`, maximum value `50000000`.

  **Default**: `0`; **Minimum**: `0`; **Maximum**: `50000000`
- `left` (number): The left inset, in points, in the range `0` to `50000000`. Validation: minimum value `0`, maximum value `50000000`.

  **Default**: `0`; **Minimum**: `0`; **Maximum**: `50000000`
- `right` (number): The right inset, in points, in the range `0` to `50000000`. Validation: minimum value `0`, maximum value `50000000`.

  **Default**: `0`; **Minimum**: `0`; **Maximum**: `50000000`

## See Also

### Positions
- [object Geometry](./geometry.md)
  The bounding box in which an object is positioned.
- [object Offset](./offset.md)
  A horizontal and vertical displacement, in points.
- [object Position](./position.md)
  A point, in points, in whichever coordinate space the property using it defines, measured downward from that space’s top-left corner.
- [object TabStopType](./tabstoptype.md)
  A tab stop.
- [type VerticalAlignmentType](./verticalalignmenttype.md)
  Vertical alignment of text within a container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/insets)*