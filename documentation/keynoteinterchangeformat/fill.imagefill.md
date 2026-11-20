# Fill.ImageFill

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

An image that the reader uses to fill an area.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Fill.ImageFill
```

## Topics

### Enumerations
- [type Fill.ImageFill.Technique](./fill.imagefill.technique.md)
  The technique the reader uses to fit the image to the fill area.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.fill.image-fill`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out.

  **Default**: `1.0`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `resource` (Resource) *(required)*: The resource containing the image fill’s data.
- `technique` (Fill.ImageFill.Technique) *(required)*: How the image fill covers the filled area.
- `scale_percent` (number): A scale applied to the image resource’s natural size, as a percentage in the range `10` to `200`; a value of 100 shows the image at its natural size. Used only when `technique` is `natural_size` or `tile`. Validation: minimum value `10`, maximum value `200`.

  **Default**: `100`; **Minimum**: `10`; **Maximum**: `200`
- `tint_color` (Color): A color laid over the image, usually with an opacity less than 1. The default is none.

## See Also

### Objects
- [object Fill.Gradient](./fill.gradient.md)
  A fill with a continuous gradient between two or more colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/fill.imagefill)*