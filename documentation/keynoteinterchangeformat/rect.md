# Rect

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An axis-aligned rectangle in whichever coordinate space the property using it defines.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Rect
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.rect`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `position` (Position) *(required)*: The top-left corner of the rectangle.
- `size` (Size) *(required)*: The width and height of the rectangle.

## See Also

### Shapes
- [object Shape](./shape.md)
  A path with a fill and a stroke.
- [object Path](./path.md)
  A path that traces the outline of a shape or of an image’s mask.
- [type Stroke](./stroke.md)
  A stroke drawn along a path, such as a border around an object.
- [object ConnectionLine](./connectionline.md)
  A line drawn from its tail end to its head end, each of which can attach to another object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/rect)*