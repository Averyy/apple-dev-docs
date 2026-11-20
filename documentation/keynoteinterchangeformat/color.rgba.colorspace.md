# Color.RGBA.ColorSpace

**Framework**: Keynote Interchange Format  
**Kind**: typealias  
**Role**: Type

The RGB primaries, white point, and transfer function used to map a color’s red, green, and blue values to a display.

**Availability**:
- Keynote Interchange Format 1.0+ (Beta)

## Declaration

```
string Color.RGBA.ColorSpace
```

## Discussion

The same three numbers denote a different color in each space. Where `p3` can’t be reproduced, the components are used unchanged as `srgb`, which renders a less saturated version of the intended color rather than failing.

This value takes one of the following forms:

- `p3`: Display P3 color space, with a nonlinear transfer function and D65 white point.
- `srgb`: Standard RGB color space, with a nonlinear transfer function and D65 white point, as defined by IEC 61966-2-1.


---

*[View on Apple Developer](https://developer.apple.com/documentation/keynoteinterchangeformat/color.rgba.colorspace)*