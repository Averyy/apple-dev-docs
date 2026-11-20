# Color.RGBA

**Framework**: Keynote Interchange Format  
**Kind**: dictionary  
**Role**: Object

A color in an RGB-component color space, together with its alpha and an HDR headroom value.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
object Color.RGBA
```

## Topics

### Enumerations
- [type Color.RGBA.ColorSpace](./color.rgba.colorspace.md)
  The RGB primaries, white point, and transfer function used to map a color’s red, green, and blue values to a display.

## Properties

- `type_identifier` (string): The canonical reverse-DNS identifier for this object’s type.

  **Allowed Values**: `com.apple.apps.content-language.color.rgba`
- `version` (string): The version of this object, in major.minor format. An object without one uses the latest version of its type, so you can leave it out. The latest version of `Color.RGBA` is 1.1.

  **Default**: `1.1`; **Allowed Values**: `/^[0-9]+\.[0-9]+$/`
- `preset_identifier` (string): The identifier of the preset that this value adopts. A property that’s absent here uses that preset, then its parent chain, and a property that’s present here takes precedence. An identifier that matches no preset isn’t an error: the properties it might supply fall back to their declared defaults. Declare presets in `presets.json`; a few types look first in the document’s stylesheet, and their descriptions explain this.
- `red` (number): The red component, in the range `0` to `1`, expressed in the color space named by `color_space`. Validation: minimum value `0`, maximum value `1`.

  **Default**: `0`; **Minimum**: `0`; **Maximum**: `1`
- `green` (number): The green component, in the range `0` to `1`, expressed in the color space named by `color_space`. Validation: minimum value `0`, maximum value `1`.

  **Default**: `0`; **Minimum**: `0`; **Maximum**: `1`
- `blue` (number): The blue component, in the range `0` to `1`, expressed in the color space named by `color_space`. Validation: minimum value `0`, maximum value `1`.

  **Default**: `0`; **Minimum**: `0`; **Maximum**: `1`
- `alpha` (number): The alpha (opacity) component, in the range `0` to `1`, where `0` is fully transparent and `1` is fully opaque. Validation: minimum value `0`, maximum value `1`.

  **Default**: `1`; **Minimum**: `0`; **Maximum**: `1`
- `color_space` (Color.RGBA.ColorSpace): The RGB color space that the red, green, and blue components are expressed in.
- `headroom` (number): The color’s own HDR headroom: how many times brighter than standard dynamic range (SDR) white it reaches. A value of `1` means an ordinary SDR color; `red`, `green`, and `blue` always describe its SDR appearance. If HDR can’t be reproduced, this value is ignored and those components can be used unchanged. Validation: minimum value `1`, maximum value `16`.

  **Default**: `1`; **Minimum**: `1`; **Maximum**: `16`


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/color.rgba)*