# CMBitmapColorSpace

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

Specifies bitmap spaces with a wide range of data formats appropriate for multiple platforms.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef UInt32 CMBitmapColorSpace;
```

## Discussion

This enumeration defines constants for color spaces which can specify color values for a bitmap image. As a rule, these constants include a packing format, defined in [Color Packing for Color Spaces](./api-1560270-color_packing_for_color_spaces.md). You can use these constants to set the `space` field of the `CMBitmap` type definition identifies the color space in which the colors of the bitmap image are specified, as described in [Abstract Color Space Constants](./api-1560701-abstract_color_space_constants.md).

### Version-Notes

The constants `cmRGBASpace` and `cmGrayASpace` were moved to [Abstract Color Space Constants](./api-1560701-abstract_color_space_constants.md) in ColorSync version 2.5.

The constants `cmGray16Space`, `cmGrayA32Space`, `cmRGB48Space`, `cmCMYK64Space`, and `cmLAB48Space` were added in ColorSync version 2.5.

## Topics

### Constants
- [cmGray8Space](./api-1560256-anonymous/cmgray8space.md)
- [cmGray16Space](./api-1560256-anonymous/cmgray16space.md)
  A luminance color space with a single 16-bit component, gray.
- [cmGray16LSpace](./api-1560256-anonymous/cmgray16lspace.md)
- [cmGrayA16Space](./api-1560256-anonymous/cmgraya16space.md)
- [cmGrayA32Space](./api-1560256-anonymous/cmgraya32space.md)
  A luminance color space with two components, a gray component followed by an alpha channel component. Each component value is 16 bits.
- [cmGrayA32LSpace](./api-1560256-anonymous/cmgraya32lspace.md)
- [cmGrayA16PmulSpace](./api-1560256-anonymous/cmgraya16pmulspace.md)
- [cmGrayA32PmulSpace](./api-1560256-anonymous/cmgraya32pmulspace.md)
- [cmGrayA32LPmulSpace](./api-1560256-anonymous/cmgraya32lpmulspace.md)
- [cmRGB16Space](./api-1560256-anonymous/cmrgb16space.md)
  An RGB color space composed of red, green, and blue components whose values are packed with 5 bits of storage per component. The storage size for a color value expressed in this color space is 16 bits, with the high-order bit not used.
- [cmRGB16LSpace](./api-1560256-anonymous/cmrgb16lspace.md)
- [cmRGB565Space](./api-1560256-anonymous/cmrgb565space.md)
- [cmRGB565LSpace](./api-1560256-anonymous/cmrgb565lspace.md)
- [cmRGB24Space](./api-1560256-anonymous/cmrgb24space.md)
  An RGB color space composed of red, green, and blue components whose values are packed with 8 bits of storage per component. The storage size for a color value expressed in this color space is 24 bits.
- [cmRGB32Space](./api-1560256-anonymous/cmrgb32space.md)
  An RGB color space composed of red, green, and blue components whose values are packed with 8 bits of storage per component. The storage size for a color value expressed in this color space is 32 bits, with bits 24-31 not used.
- [cmRGB48Space](./api-1560256-anonymous/cmrgb48space.md)
  An RGB color space composed of red, green, and blue components whose values are packed with 16 bits of storage per component. The storage size for a color value expressed in this color space is 48 bits.
- [cmRGB48LSpace](./api-1560256-anonymous/cmrgb48lspace.md)
- [cmARGB32Space](./api-1560256-anonymous/cmargb32space.md)
- [cmARGB64Space](./api-1560256-anonymous/cmargb64space.md)
- [cmARGB64LSpace](./api-1560256-anonymous/cmargb64lspace.md)
- [cmRGBA32Space](./api-1560256-anonymous/cmrgba32space.md)
  An RGB color space composed of red, green, and blue color value components, followed by an alpha channel component. Values are packed with 8 bits of storage per component. The storage size for a color value expressed in this color space is 32 bits.
- [cmRGBA64Space](./api-1560256-anonymous/cmrgba64space.md)
- [cmRGBA64LSpace](./api-1560256-anonymous/cmrgba64lspace.md)
- [cmARGB32PmulSpace](./api-1560256-anonymous/cmargb32pmulspace.md)
- [cmARGB64PmulSpace](./api-1560256-anonymous/cmargb64pmulspace.md)
- [cmARGB64LPmulSpace](./api-1560256-anonymous/cmargb64lpmulspace.md)
- [cmRGBA32PmulSpace](./api-1560256-anonymous/cmrgba32pmulspace.md)
- [cmRGBA64PmulSpace](./api-1560256-anonymous/cmrgba64pmulspace.md)
- [cmRGBA64LPmulSpace](./api-1560256-anonymous/cmrgba64lpmulspace.md)
- [cmCMYK32Space](./api-1560256-anonymous/cmcmyk32space.md)
  A CMYK color space composed of cyan, magenta, yellow, and black components whose values are packed with 8 bits of storage per component. The storage size for a color value expressed in this color space is 32 bits.
- [cmCMYK64Space](./api-1560256-anonymous/cmcmyk64space.md)
  A CMYK color space composed of cyan, magenta, yellow, and black components whose values are packed with 16 bits of storage per component. The storage size for a color value expressed in this color space is 64 bits.
- [cmCMYK64LSpace](./api-1560256-anonymous/cmcmyk64lspace.md)
- [cmHSV32Space](./api-1560256-anonymous/cmhsv32space.md)
  An HSV color space composed of hue, saturation, and value components whose values are packed with 10 bits of storage per component. The storage size for a color value expressed in this color space is 32 bits, with the high-order 2 bits not used.
- [cmHLS32Space](./api-1560256-anonymous/cmhls32space.md)
  An HLS color space composed of hue, lightness, and saturation components whose values are packed with 10 bits of storage per component. The storage size for a color value expressed in this color space is 32 bits, with the high-order 2 bits not used.
- [cmYXY32Space](./api-1560256-anonymous/cmyxy32space.md)
  A Yxy color space composed of Y, x, and y components whose values are packed with 10 bits of storage per component. The storage size for a color value expressed in this color space is 32 bits, with the high-order 2 bits not used.
- [cmXYZ24Space](./api-1560256-anonymous/cmxyz24space.md)
- [cmXYZ32Space](./api-1560256-anonymous/cmxyz32space.md)
  An XYZ color space composed of X, Y, and Z components whose values are packed with 10 bits per component. The storage size for a color value expressed in this color space is 32 bits, with the high-order 2 bits not used.
- [cmXYZ48Space](./api-1560256-anonymous/cmxyz48space.md)
- [cmXYZ48LSpace](./api-1560256-anonymous/cmxyz48lspace.md)
- [cmLUV32Space](./api-1560256-anonymous/cmluv32space.md)
  An L*u*v* color space composed of L*, u*, and v* components whose values are packed with 10 bits per component. The storage size for a color value expressed in this color space is 32 bits, with the high-order 2 bits not used.
- [cmLAB24Space](./api-1560256-anonymous/cmlab24space.md)
- [cmLAB32Space](./api-1560256-anonymous/cmlab32space.md)
- [cmLAB48Space](./api-1560256-anonymous/cmlab48space.md)
- [cmLAB48LSpace](./api-1560256-anonymous/cmlab48lspace.md)
- [cmGamutResult1Space](./api-1560256-anonymous/cmgamutresult1space.md)
- [cmNamedIndexed32Space](./api-1560256-anonymous/cmnamedindexed32space.md)
  A color space where each color is stored as a single 32-bit value, specifying an index into a named color space. The storage size for a color value expressed in this color space is 32 bits.
- [cmNamedIndexed32LSpace](./api-1560256-anonymous/cmnamedindexed32lspace.md)
- [cmMCFive8Space](./api-1560256-anonymous/cmmcfive8space.md)
  A five-channel multichannel (HiFi) data color space, whose values are packed with 8 bits per component. The storage size for a color value expressed in this color space is 40 bits.
- [cmMCSix8Space](./api-1560256-anonymous/cmmcsix8space.md)
  A six-channel multichannel (HiFi) data color space, whose values are packed with 8 bits per component. The storage size for a color value expressed in this color space is 48 bits.
- [cmMCSeven8Space](./api-1560256-anonymous/cmmcseven8space.md)
  A seven-channel multichannel (HiFi) data color space, whose values are packed with 8 bits per component. The storage size for a color value expressed in this color space is 56 bits.
- [cmMCEight8Space](./api-1560256-anonymous/cmmceight8space.md)
  An eight-channel multichannel (HiFi) data color space, whose values are packed with 8 bits per component. The storage size for a color value expressed in this color space is 64 bits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmbitmapcolorspace)*