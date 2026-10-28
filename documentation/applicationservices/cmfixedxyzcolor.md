# CMFixedXYZColor

**Framework**: Application Services  
**Kind**: struct  
**Role**: Structure

Contains data that specifies the profile illuminant in the profile header’s `white` field and other profile element values. 

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef struct CMFixedXYZColor {
    ...
} CMFixedXYZColor;
```

## Overview

ColorSync uses the `CMFixedXYZColor` data type to specify the profile illuminant in the profile header’s `white` field and to specify other profile element values. Color component values defined by the `Fixed` type definition can be used to specify a color value in the XYZ color space with greater precision than a color whose components are expressed as `CMXYZComponent` data types. The `Fixed` data type is a signed 32-bit value. A color value expressed in the XYZ color space whose color components are of type `Fixed` is defined by the `CMFixedXYZColor` type definition. 

Your application can convert colors defined in the XYZ color space between `CMXYZColor` data types (in which the color components are expressed as 16-bit unsigned values) and `CMFixedXYZColor` data types (in which the colors are expressed as 32-bit signed values). To convert color values, you use the functions [CMConvertFixedXYZToXYZ](./colorsync_manager/api-1805174-cmconvertfixedxyztoxyz.md) and [CMConvertXYZToFixedXYZ](./colorsync_manager/api-1805169-cmconvertxyztofixedxyz.md).

## Topics

### Instance Properties
- [X](./cmfixedxyzcolor/api-1560683-x.md)
- [Y](./cmfixedxyzcolor/api-1560426-y.md)
- [Z](./cmfixedxyzcolor/api-1560538-z.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmfixedxyzcolor)*