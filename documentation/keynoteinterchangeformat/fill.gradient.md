# Fill.Gradient

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A fill with a continuous gradient between two or more colors.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Fill.Gradient
```

## Topics

### Objects
- [object Fill.Gradient.Stop](./fill.gradient.stop.md)
  One color in the gradient, and its position along it.
### Enumerations
- [type Fill.Gradient.Flavor](./fill.gradient.flavor.md)
  A method for laying out a gradient’s stops over the area being filled.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.fill.gradient`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out. The latest version of `Fill.Gradient` is 1.1.

  **Default**: `1.1`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `is_advanced` (boolean): Whether the gradient is an advanced gradient. It’s independent of the linear or radial `flavor` and doesn’t affect rendering.

  **Default**: `false`
- `stops` ([Fill.Gradient.Stop]) *(required)*: The color stops that define the gradient, ordered from the start of the gradient to its end. A gradient must have at least two stops. An array with fewer than two stops is padded to two on read; an empty one produces a fully transparent gradient. If a stop’s `fraction` isn’t greater than the previous stop’s, it’s shown immediately after the previous stop.
- `opacity` (number): The opacity of the gradient, in the range `0` to `1`. Validation: minimum value `0`, maximum value `1`.

  **Default**: `1`; **Minimum**: `0`; **Maximum**: `1`
- `flavor` (Fill.Gradient.Flavor) *(required)*: The kind of gradient, linear or radial, along with the geometry that positions it.

## See Also

### Objects
- [object Fill.ImageFill](./fill.imagefill.md)
  An image that the reader uses to fill an area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/fill.gradient)*