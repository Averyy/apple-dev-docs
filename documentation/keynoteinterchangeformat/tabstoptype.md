# TabStopType

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A tab stop.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object TabStopType
```

## Topics

### Enumerations
- [type TabStopType.TabAlignmentKindType](./tabstoptype.tabalignmentkindtype.md)
  The alignment of a tab stop.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.tab-stop-type`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `position` (number) *(required)*: The position of the tab stop, in points. Use a position greater than 0; a tab stop at `0` or less is accepted but is dropped the next time the document is opened.
- `kind` (TabStopType.TabAlignmentKindType): The alignment of the tab stop; the default is `left`.
- `leader` (string): The string shown in the space before the tab stop (for example, a period for a dotted leader). The default is a single space (a plain gap), so a value of `" "` is equivalent to omitting the property.

## See Also

### Positions
- [object Geometry](./geometry.md)
  The bounding box in which an object is positioned.
- [object Offset](./offset.md)
  A horizontal and vertical displacement, in points.
- [object Position](./position.md)
  A point, in points, in whichever coordinate space the property using it defines, measured downward from that space’s top-left corner.
- [object Insets](./insets.md)
  Space reserved along each edge of an area, in points.
- [type VerticalAlignmentType](./verticalalignmenttype.md)
  Vertical alignment of text within a container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/tabstoptype)*