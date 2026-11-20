# Fill.Gradient.Flavor.Linear

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A gradient that lays out its stops along a straight line.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Fill.Gradient.Flavor.Linear
```

## Overview

`angle` alone fits the line to the filled shape’s bounds, so the whole stop range is visible. `start_point`, `end_point`, and `base_natural_size` place it exactly, possibly running past those bounds; the points are in the shape’s untransformed space, in points with y increasing downward, and rescale when the object’s size differs from `base_natural_size`. Those three are read only together: with any of them missing, the gradient falls back to `angle` and discards the points.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.fill.gradient.flavor.linear`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out. The latest version of `Fill.Gradient.Flavor.Linear` is 1.1.

  **Default**: `1.1`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `angle` (number) *(required)*: The angle in degrees at which the gradient runs, in the range `0` to `360` (exclusive) measured counterclockwise with `0` corresponding to horizontal left-to-right. Ignored if `start_point`, `end_point`, and `base_natural_size` are all present; `angle` remains the fallback for version 1.0 readers, which predate those properties. Validation: minimum value `0`, maximum value `360`.

  **Minimum**: `0`; **Maximum**: `360`
- `start_point` (Position): If present, the starting point of the line along which the gradient’s colors change, relative to a rectangle defined by `base_natural_size`. If it’s present, it must be combined with `end_point` and `base_natural_size`; when all three are present, they take precedence over `angle`. Version 1.0 readers ignore it and render from `angle`.
- `end_point` (Position): If present, the end point of the line along which the gradient’s colors change, relative to a rectangle defined by `base_natural_size`. If it’s present, it must be combined with `start_point` and `base_natural_size`. For details, see `start_point`.
- `base_natural_size` (Size): If present, the size of the rectangle that `start_point` and `end_point` are relative to. When filling an area, the gradient’s start and end points are transformed so that this size covers the filled area. For details, see `start_point`.

## See Also

### Objects
- [object Fill.Gradient.Flavor.Radial](./fill.gradient.flavor.radial.md)
  A gradient that spreads its stops outward from a center point, with a second point fixing the radius and the direction of the outer edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/fill.gradient.flavor.linear)*