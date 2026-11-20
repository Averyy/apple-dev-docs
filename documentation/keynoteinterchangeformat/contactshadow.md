# ContactShadow

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A shadow whose silhouette pools under the object’s bottom edge as though the object were standing on a ground plane.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object ContactShadow
```

## Overview

The shadow is anchored to that edge, and `height` controls how far it’s foreshortened.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.contact-shadow`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `opacity` (number): The opacity of the cast shadow, in the range `0` to `1`. Validation: minimum value `0`, maximum value `1`.

  **Default**: `1`; **Minimum**: `0`; **Maximum**: `1`
- `color` (Color): The color of the cast shadow. If absent, the shadow is black.
- `offset` (number): The vertical distance, in points, between the bottom edge of the object and the point at which the imaginary ground plane is positioned. Positive values move the shadow farther down, and negative values move it up behind the object. Validation: minimum value `-75`, maximum value `75`.

  **Default**: `0`; **Minimum**: `-75`; **Maximum**: `75`
- `radius` (number): The radius (size) of the cast shadow’s blur, in the range `10` to `100`. Validation: minimum value `10`, maximum value `100`.

  **Default**: `28`; **Minimum**: `10`; **Maximum**: `100`
- `height` (number): The apparent height of the cast shadow, given as the sine of the viewing angle between the imaginary ground plane and the eye, in the range sin(5°) to sin(35°); it controls how much the contact shadow is foreshortened. The default is sin(10°). Validation: minimum value `0.08715574`, maximum value `0.57357644`.

  **Default**: `0.17364818`; **Minimum**: `0.08715574`; **Maximum**: `0.57357644`

## See Also

### Shadows
- [type Shadow](./shadow.md)
  The kind of shadow cast by an object, or `none` for no shadow.
- [object CurvedShadow](./curvedshadow.md)
  A shadow whose silhouette curls away from the object, as if it were a page lifting off the surface rather than lying flat.
- [object DropShadow](./dropshadow.md)
  A shadow whose silhouette appears as though cast by a light source facing down toward the plane of the object.
- [object Reflection](./reflection.md)
  A mirrored copy of the object that the reader drew directly below it on a ground plane aligned to the horizontal axis, fading out with distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/contactshadow)*