# ConnectionLine

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A line drawn from its tail end to its head end, each of which can attach to another object.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ConnectionLine
```

## Overview

The route comes from `tail`, `head`, and (for a curved or corner line) the control position carried by `line_type`. Because the line’s position and size follow from the route, `geometry` only transforms the supplied end points and control position, and is omitted when Keynote writes out a connection line.

This type includes the properties of `CanvasObject`, as does every other type that adopts it.

## Topics

### Objects
- [object ConnectionLine.End](./connectionline.end.md)
  One end of a connection line.
### Enumerations
- [type ConnectionLine.LineType](./connectionline.linetype.md)
  How a connection line is routed between its ends.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.connection-line`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `identifier` (string): An identifier for this object that other objects use to refer to it. This identifier must be unique across the whole document.
- `geometry` (Geometry): The object’s position and size. If this value is absent, Keynote places the object automatically, with a default position and size for its kind.
- `aspect_ratio_locked` (boolean): A Boolean value that indicates whether the object’s width-to-height ratio is locked when the object resizes. The lock doesn’t constrain the `geometry` property. If this property is absent, images, movies, and groups default to `true`, and other objects to `false`.

  **Default**: `false`
- `description` (string): The accessibility description for the object, read aloud by assistive technologies such as VoiceOver.
- `line_type` (ConnectionLine.LineType): The routing style of the connection line.
- `tail` (ConnectionLine.End) *(required)*: The tail end of the connection line.
- `head` (ConnectionLine.End) *(required)*: The head end of the connection line.
- `stroke` (Stroke): The stroke used to draw the connection line.
- `opacity` (number): The opacity of the connection line, in the range `0` to `1`.

  **Default**: `1`
- `shadow` ((Shadow | null)): The shadow shown beneath the connection line.

  **Allowed Types**: `Shadow`, `null`
- `reflection` (Reflection): The reflection shown for the connection line.

## See Also

### Shapes
- [object Shape](./shape.md)
  A path with a fill and a stroke.
- [object Rect](./rect.md)
  An axis-aligned rectangle in whichever coordinate space the property using it defines.
- [object Path](./path.md)
  A path that traces the outline of a shape or of an image’s mask.
- [type Stroke](./stroke.md)
  A stroke drawn along a path, such as a border around an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/connectionline)*