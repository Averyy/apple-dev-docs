# CWMatchColors

**Framework**: Application Services  
**Kind**: func

Matches colors in a color list, using the specified color world.

## Declaration

```c
CMError CWMatchColors (
   CMWorldRef cw,
   CMColor *myColors,
   size_t count
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

The `CWMatchColors` function matches colors according to the profiles corresponding to the specified color world. On input, the color values in the `myColors` array are assumed to be specified in the data color space of the source profile. On return, the color values in the `myColors` array are transformed to the data color space of the destination profile.

All color management modules (CMM)s must support this function. 

This function supports color-matching sessions set up with one of the multichannel color data types. 

## Parameters

- `cw`: A reference to the color world of type [`CMWorldRef`](../cmworldref.md) that describes how matching is to occur in the color-matching session.

  The functions [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md) and [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md) both allocate color world references of type [`CMWorldRef`](../cmworldref.md).
- `myColors`: A pointer to an array containing a list of colors of type [`CMColor`](../api-1560453-cmcolor.md). On input, contains the list of colors to match. On return, contains the list of matched colors specified in the color data space of the color world’s destination profile. 
- `count`: A one-based count of the number of colors in the color list of the `myColors` array. 

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
- [CWCheckColors](./api-1805111-cwcheckcolors.md)
  Tests a list of colors using a specified color world to see if they fall within the gamut of a destination device.
- [CWMatchBitmap](./api-1805116-cwmatchbitmap.md)
  Matches the colors of a bitmap to the gamut of a destination device using the profiles specified by a color world.
- [CWCheckBitmap](./api-1805121-cwcheckbitmap.md)
  Tests the colors of the pixel data of a bitmap to determine whether the colors map to the gamut of the destination device.
- [CWFillLookupTexture](./api-1805126-cwfilllookuptexture.md)
  Fills a 3-D lookup texture from a color world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805108-cwmatchcolors)*