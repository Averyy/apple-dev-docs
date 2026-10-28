# CWCheckColors

**Framework**: Application Services  
**Kind**: func

Tests a list of colors using a specified color world to see if they fall within the gamut of a destination device.

## Declaration

```c
CMError CWCheckColors (
   CMWorldRef cw,
   CMColor *myColors,
   size_t count,
   UInt8 *result
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

The color test provides a preview of color matching using the specified color world.

All CMMs must support the `CWCheckColors` function. 

If you have set a profile’s gamut-checking mask so that no gamut information is included—see [Flag Mask Definitions for Version 2.x Profiles](../api-1560699-x_profiles.md) — `CWCheckColors` returns the `cmCantGamutCheckError` error.

The `CWCheckColors` function supports matching sessions set up with one of the multichannel color data types. `CWCheckColors` is not supported if the color world was initialized with a named color space profile. 

## Parameters

- `cw`: A reference to the color world of type [`CMWorldRef`](../cmworldref.md) describing how the test is to occur.

  The functions [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md) and [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md) both allocate color world references of type [`CMWorldRef`](../cmworldref.md).
- `myColors`: A pointer to an array containing a list of colors of type [`CMColor`](../api-1560453-cmcolor.md) to be checked`.`This function assumes the color values are specified in the data color space of the source profile. 
- `count`: The number of colors in the array. This is a one-based count. 
- `result`: A pointer to a buffer of packed bits. On return, each bit value is interpreted as a bit field with each bit representing a color in the array pointed to by `myColors`. You allocate enough memory to allow for 1 bit to represent each color in the `myColors` array. Bits in the `result` field are set to 1 if the corresponding color is out of gamut for the destination device. Ensure that the buffer you allocate is zeroed out before you call this function. 

  To access the packed bit-array, use code similar to the following:

  ```occ
  inline bool GetNthBit (UInt8* result, int n)
  {
      return ( 0 != (result[n/8] & (128>>(n%8))) );
  }
  ```

  The `result` bit array indicates whether the colors in the list are in or out of gamut for the destination profile. If a bit is set, its corresponding color falls out of gamut for the destination device. The leftmost bit in the field corresponds to the first color in the list.

## See Also

### Working With ColorWorlds
- [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md)
  Creates a color world for color matching based on the specified source and destination profiles. 
- [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md)
  Sets up a color world that includes a set of profiles for various color transformations among devices in a sequence.
- [NCWConcatColorWorld](./api-1805091-ncwconcatcolorworld.md)
  Defines a color world for color transformations among a series of concatenated profiles. 
- [CMGetCWInfo](./api-1805097-cmgetcwinfo.md)
  Obtains information about the color management modules (CMMs) used for a specific color world.
- [CWDisposeColorWorld](./api-1805102-cwdisposecolorworld.md)
  Releases the private storage associated with a color world when your application has finished using the color world. 
- [CWMatchColors](./api-1805108-cwmatchcolors.md)
  Matches colors in a color list, using the specified color world.
- [CWMatchBitmap](./api-1805116-cwmatchbitmap.md)
  Matches the colors of a bitmap to the gamut of a destination device using the profiles specified by a color world.
- [CWCheckBitmap](./api-1805121-cwcheckbitmap.md)
  Tests the colors of the pixel data of a bitmap to determine whether the colors map to the gamut of the destination device.
- [CWFillLookupTexture](./api-1805126-cwfilllookuptexture.md)
  Fills a 3-D lookup texture from a color world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805111-cwcheckcolors)*