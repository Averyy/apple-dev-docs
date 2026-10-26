# Color Packing for Color Spaces

**Framework**: Application Services  
**Kind**: enum  
**Role**: Enumeration

Specify how color values are stored.

**Availability**:
- macOS 10.0+

## Declaration

```c
enum : unsigned int {
    ...
};
```

## Topics

### Constants
- [cmNoColorPacking](./api-1560270-color_packing_for_color_spaces/cmnocolorpacking.md)
  This constant is not used for ColorSync bitmaps.
- [cmWord5ColorPacking](./api-1560270-color_packing_for_color_spaces/cmword5colorpacking.md)
  The color values for three 5-bit color channels are stored consecutively in 16-bits, with the highest order bit unused.
- [cmWord565ColorPacking](./api-1560270-color_packing_for_color_spaces/cmword565colorpacking.md)
- [cmLong8ColorPacking](./api-1560270-color_packing_for_color_spaces/cmlong8colorpacking.md)
- [cmLong10ColorPacking](./api-1560270-color_packing_for_color_spaces/cmlong10colorpacking.md)
  The color values for three 10-bit color channels are stored consecutively in a 32-bit long, with the two highest order bits unused.
- [cmAlphaFirstPacking](./api-1560270-color_packing_for_color_spaces/cmalphafirstpacking.md)
  An alpha channel is added to the color value as its first component.
- [cmOneBitDirectPacking](./api-1560270-color_packing_for_color_spaces/cmonebitdirectpacking.md)
  One bit is used as the pixel format. This storage format is used by the resulting bitmap pointed to by the `resultBitMap` field of the function [CWMatchColors](./colorsync_manager/api-1805108-cwmatchcolors.md); the bitmap must be only 1 bit deep.
- [cmAlphaLastPacking](./api-1560270-color_packing_for_color_spaces/cmalphalastpacking.md)
- [cm8_8ColorPacking](./api-1560270-color_packing_for_color_spaces/cm8_8colorpacking.md)
- [cm16_8ColorPacking](./api-1560270-color_packing_for_color_spaces/cm16_8colorpacking.md)
- [cm24_8ColorPacking](./api-1560270-color_packing_for_color_spaces/cm24_8colorpacking.md)
  The color values for three 8-bit color channels are stored in consecutive bytes, for a total of 24 bits.
- [cm32_8ColorPacking](./api-1560270-color_packing_for_color_spaces/cm32_8colorpacking.md)
  The color values for four 8-bit color channels are stored in consecutive bytes, for a total of 32 bits.
- [cm40_8ColorPacking](./api-1560270-color_packing_for_color_spaces/cm40_8colorpacking.md)
  The color values for five 8-bit color channels are stored in consecutive bytes, for a total of 40 bits.
- [cm48_8ColorPacking](./api-1560270-color_packing_for_color_spaces/cm48_8colorpacking.md)
  The color values for six 8-bit color channels are stored in consecutive bytes, for a total of 48 bits.
- [cm56_8ColorPacking](./api-1560270-color_packing_for_color_spaces/cm56_8colorpacking.md)
  The color values for seven 8-bit color channels are stored in consecutive bytes, for a total of 56 bits.
- [cm64_8ColorPacking](./api-1560270-color_packing_for_color_spaces/cm64_8colorpacking.md)
  The color values for eight 8-bit color channels are stored in consecutive bytes, for a total of 64 bits.
- [cm32_16ColorPacking](./api-1560270-color_packing_for_color_spaces/cm32_16colorpacking.md)
  The color values for two 16-bit color channels are stored in a 32-bit word.
- [cm48_16ColorPacking](./api-1560270-color_packing_for_color_spaces/cm48_16colorpacking.md)
  The color values for three 16-bit color channels are stored in 48 consecutive bits.
- [cm64_16ColorPacking](./api-1560270-color_packing_for_color_spaces/cm64_16colorpacking.md)
  The color values for four 16-bit color channels are stored in 64 consecutive bits.
- [cm32_32ColorPacking](./api-1560270-color_packing_for_color_spaces/cm32_32colorpacking.md)
  The color value for a 32-bit color channel is stored in a 32-bit word.
- [cmLittleEndianPacking](./api-1560270-color_packing_for_color_spaces/cmlittleendianpacking.md)
- [cmReverseChannelPacking](./api-1560270-color_packing_for_color_spaces/cmreversechannelpacking.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces)*