# Reflection

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A mirrored copy of the object that the reader drew directly below it on a ground plane aligned to the horizontal axis, fading out with distance.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Reflection
```

## Overview

It extends down 40% of the object’s height, at most 120 points.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.reflection`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `opacity` (number): The reflection’s opacity where it meets the object, in the range `0` to `1` (`0` is invisible). The reflection fades away from this opacity to zero as it extends farther down, at a rate set by `fade_acceleration`. Validation: minimum value `0`, maximum value `1`.

  **Default**: `1`; **Minimum**: `0`; **Maximum**: `1`
- `fade_acceleration` (number): An exponent, `1` or greater, that sets how quickly the reflection fades from `opacity` to clear. A value of `1` fades linearly to 40% of the object’s height (at most 120 points) when measured from the apparent ground plane, and larger values fade out more quickly. Validation: minimum value `1`.

  **Default**: `1`; **Minimum**: `1`

## See Also

### Shadows
- [type Shadow](./shadow.md)
  The kind of shadow cast by an object, or `none` for no shadow.
- [object ContactShadow](./contactshadow.md)
  A shadow whose silhouette pools under the object’s bottom edge as though the object were standing on a ground plane.
- [object CurvedShadow](./curvedshadow.md)
  A shadow whose silhouette curls away from the object, as if it were a page lifting off the surface rather than lying flat.
- [object DropShadow](./dropshadow.md)
  A shadow whose silhouette appears as though cast by a light source facing down toward the plane of the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/reflection)*