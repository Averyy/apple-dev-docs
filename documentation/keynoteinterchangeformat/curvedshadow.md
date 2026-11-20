# CurvedShadow

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A shadow whose silhouette curls away from the object, as if it were a page lifting off the surface rather than lying flat.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object CurvedShadow
```

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.curved-shadow`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `angle` (number): The angle at which the shadow is offset from its default position, directly below the object. It’s in degrees, in the range `0` to `360`, measured counterclockwise with `0` corresponding to horizontal left-to-right. Validation: minimum value `0`, maximum value `360`.

  **Default**: `270`; **Minimum**: `0`; **Maximum**: `360`
- `opacity` (number): The opacity of the cast shadow, in the range `0` to `1`. Validation: minimum value `0`, maximum value `1`.

  **Default**: `1`; **Minimum**: `0`; **Maximum**: `1`
- `color` (Color): The color of the cast shadow. If absent, the shadow is black.
- `offset` (number): The amount by which the shadow is offset from its default position, in the direction of `angle`, in the range `-50` to `50`. Validation: minimum value `-50`, maximum value `50`.

  **Default**: `1`; **Minimum**: `-50`; **Maximum**: `50`
- `radius` (number): The radius (size) of the cast shadow’s blur, in the range `0` to `100`. Validation: minimum value `0`, maximum value `100`.

  **Default**: `0`; **Minimum**: `0`; **Maximum**: `100`
- `curve` (number): The amount by which the shadow curls away from the object, in the range `-1` to `1`. When `curve` is `0`, the shadow is cast as though the object were lying flat. Negative values of `curve` make the cast shadow appear as though the object were concave, with the left and right edges bulging toward the viewer; positive values make the cast shadow appear as though the object were convex, with the vertical center axis bulging toward the viewer. Validation: minimum value `-1`, maximum value `1`.

  **Default**: `1`; **Minimum**: `-1`; **Maximum**: `1`

## See Also

### Shadows
- [type Shadow](./shadow.md)
  The kind of shadow cast by an object, or `none` for no shadow.
- [object ContactShadow](./contactshadow.md)
  A shadow whose silhouette pools under the object’s bottom edge as though the object were standing on a ground plane.
- [object DropShadow](./dropshadow.md)
  A shadow whose silhouette appears as though cast by a light source facing down toward the plane of the object.
- [object Reflection](./reflection.md)
  A mirrored copy of the object that the reader drew directly below it on a ground plane aligned to the horizontal axis, fading out with distance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/curvedshadow)*