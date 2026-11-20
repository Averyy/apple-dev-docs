# Fill.Gradient.Flavor.Radial

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A gradient that spreads its stops outward from a center point, with a second point fixing the radius and the direction of the outer edge.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Fill.Gradient.Flavor.Radial
```

## Overview

Both points are in the filled shape’s untransformed space, in points with y increasing downward; `base_natural_size` is the size that space was captured at, so the gradient rescales when the object’s size differs from it.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.fill.gradient.flavor.radial`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `start_point` (Position) *(required)*: The center point of the radial gradient, relative to a rectangle defined by `base_natural_size`.
- `end_point` (Position) *(required)*: A point on the outer edge of the radial gradient, relative to a rectangle defined by `base_natural_size`. Together with `start_point`, it sets the gradient’s radius and direction.
- `base_natural_size` (Size) *(required)*: The size of the rectangle that `start_point` and `end_point` are relative to. When filling an area, the gradient’s start and end points are transformed so that this size covers the filled area.

## See Also

### Objects
- [object Fill.Gradient.Flavor.Linear](./fill.gradient.flavor.linear.md)
  A gradient that lays out its stops along a straight line.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/fill.gradient.flavor.radial)*