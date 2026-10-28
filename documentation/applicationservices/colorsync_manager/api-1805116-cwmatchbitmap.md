# CWMatchBitmap

**Framework**: Application Services  
**Kind**: func

Matches the colors of a bitmap to the gamut of a destination device using the profiles specified by a color world.

## Declaration

```c
CMError CWMatchBitmap (
   CMWorldRef cw,
   CMBitmap *bitmap,
   CMBitmapCallBackUPP progressProc,
   void *refCon,
   CMBitmap *matchedBitmap
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

The `CWMatchBitmap` function matches a bitmap using the profiles specified by the given color world.

You should ensure that the buffer pointed to by the `image` field of the bitmap passed in the `bitMap` parameter is zeroed out before you call this function.

The ColorSync Manager does not explicitly support a CMY color space. However, for printers that have a CMY color space, you can use either of the following circumventions to make the adjustment:

-  You can use a CMY profile, which the ColorSync Manager does support, with a CMYK color space. If you specify a CMYK color space in this case, the ColorSync Manager zeroes out the K channel to simulate a CMY color space. 
-  You can use an RGB color space and pass in the bitmap along with an RGB profile, then perform the conversion from RGB to CMY yourself. 

For this function to execute successfully, the source profile’s `dataColorSpace` field value and the `space` field value of the source bitmap pointed to by the `bitMap` parameter must specify the same data color space. Additionally, the destination profile’s `dataColorSpace` field value and the `space` field value of the resulting bitmap pointed to by the `matchedBitMap` parameter must specify the same data color space, unless the destination profile is a named color space profile.

If you set `matchedBitMap` to `NULL` to specify in-place matching, you must be sure the space required by the destination bitmap is less than or equal to the size of the source bitmap. 

### Version-Notes

The color spaces currently supported for the CWMatchBitmap function are defined in [`CMBitmapColorSpace`](../cmbitmapcolorspace.md). Support for the following color space constants, was added with ColorSync version 2.5:

- `cmGray16Space`
- `cmGrayA32Space`
- `cmRGB48Space`.
- `cmCMYK64Space`
- `cmLAB48Space`

## Parameters

- `cw`: A reference to a color world of type [`CMWorldRef`](../cmworldref.md) in which matching is to occur.

  The functions [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md) and [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md) both allocate color world references of type [`CMWorldRef`](../cmworldref.md).
- `bitmap`: A pointer to a bitmap of type [`CMBitmap`](../cmbitmap.md) whose colors are to be matched. 
- `progressProc`: A calling program–supplied universal procedure pointer to a callback function that allows your application to monitor progress or abort the operation as the bitmap colors are matched. The default CMM calls your function approximately every half-second unless color matching occurs in less time this happens when there is a small amount of data to be matched. If the function returns a result of `true`, the operation is aborted. To match colors without monitoring the process, specify `NULL` for this parameter. For a description of the function your application supplies, see the function [`CMBitmapCallBackProcPtr`](../cmbitmapcallbackprocptr.md). 
- `refCon`: A pointer to a reference constant for application data passed through as a parameter to calls to the `progressProc` function. 
- `matchedBitmap`: A pointer to a bitmap. On return, contains the color-matched image. You must allocate the pixel buffer pointed to by the `image` field of the structure [`CMBitmap`](../cmbitmap.md). If you specify `NULL` for `matchedBitMap`, then the source bitmap is matched in place.

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
- [CWCheckColors](./api-1805111-cwcheckcolors.md)
  Tests a list of colors using a specified color world to see if they fall within the gamut of a destination device.
- [CWCheckBitmap](./api-1805121-cwcheckbitmap.md)
  Tests the colors of the pixel data of a bitmap to determine whether the colors map to the gamut of the destination device.
- [CWFillLookupTexture](./api-1805126-cwfilllookuptexture.md)
  Fills a 3-D lookup texture from a color world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805116-cwmatchbitmap)*