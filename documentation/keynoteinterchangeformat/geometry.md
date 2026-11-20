# Geometry

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

The bounding box in which an object is positioned.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Geometry
```

## Overview

`position` and `size` are in points. `position` is measured after rotation and `size` before it, so the object’s center is the center of the rotated bounding box whose top-left corner is `position`.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.geometry`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `position` (Position) *(required)*: The top-left corner of the object’s axis-aligned bounding box, measured after rotation is applied. Coordinates are absolute within the containing slide, even for an object nested inside a group.
- `size` (Size) *(required)*: The width and height of the object’s bounding box, in points, before rotation and flipping are applied. The width or height may be zero for objects without an intrinsic size, such as audio.
- `angle` (number): The rotation of the object’s bounding box around its center, in degrees measured counterclockwise. It’s written in the range `0` to `360` (exclusive); values outside that range are mapped to the equivalent angle within it.

  **Default**: `0`
- `flip_horizontally` (boolean): Whether the object is mirrored across the vertical axis through its center, before rotation by `angle` is applied. A vertical flip is represented by combining a horizontal flip with a 180-degree rotation.

  **Default**: `false`
- `width_valid` (boolean): Whether the object’s width is valid. When `false` for an object that can compute its own width, the natural width that fits its text is used instead of the width in `size`.

  **Default**: `true`
- `height_valid` (boolean): Whether the object’s height is valid. When `false` for an object that can compute its own height, the natural height that fits its text is used instead of the height in `size`.

  **Default**: `true`

## See Also

### Positions
- [object Offset](./offset.md)
  A horizontal and vertical displacement, in points.
- [object Position](./position.md)
  A point, in points, in whichever coordinate space the property using it defines, measured downward from that space’s top-left corner.
- [object Insets](./insets.md)
  Space reserved along each edge of an area, in points.
- [object TabStopType](./tabstoptype.md)
  A tab stop.
- [type VerticalAlignmentType](./verticalalignmenttype.md)
  Vertical alignment of text within a container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/geometry)*