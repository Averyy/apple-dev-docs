# Path

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A path that traces the outline of a shape or of an image’s mask.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Path
```

## Overview

Only one form is defined so far; later versions of the format can add others without changing how a shape or an image mask refers to its outline.

A path described by an SVG path string. This is the only supported path representation.

## Topics

### Objects
- [object Path.BezierPath](./path.bezierpath.md)
  A path as an SVG path string, together with the coordinate space in which its points are expressed.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.path`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `bezier` (Path.BezierPath) *(required)*: A path described by an SVG path string. This is the only supported path representation.

## See Also

### Shapes
- [object Shape](./shape.md)
  A path with a fill and a stroke.
- [object Rect](./rect.md)
  An axis-aligned rectangle in whichever coordinate space the property using it defines.
- [type Stroke](./stroke.md)
  A stroke drawn along a path, such as a border around an object.
- [object ConnectionLine](./connectionline.md)
  A line drawn from its tail end to its head end, each of which can attach to another object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/path)*