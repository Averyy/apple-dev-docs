# CWCheckBitmap

**Framework**: Application Services  
**Kind**: func

Tests the colors of the pixel data of a bitmap to determine whether the colors map to the gamut of the destination device.

## Declaration

```c
CMError CWCheckBitmap (
   CMWorldRef cw,
   const CMBitmap *bitmap,
   CMBitmapCallBackUPP progressProc,
   void *refCon,
   CMBitmap *resultBitmap
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

When your application calls the `CWCheckBitMap` function, the ColorSync Manager dispatches the function to the preferred CMM. The ColorSync Manager determines the preferred CMM based on the color world configuration. If the color world you pass in was created by the `CWConcatColorWorld` function, then the `keyIndex` field of the `CMConcatProfileSet` data structure identifies the preferred CMM. If the preferred CMM is not available, the default CMM is used to perform the color matching.

For the `CWCheckBitMap` function to execute successfully, the source profile’s `dataColorSpace` field value and the `space` field value of the source bitmap pointed to by the `bitMap` parameter must specify the same data color space. `CWCheckBitMap` is not supported if the color world was initialized with a named color space profile. 

## Parameters

- `cw`: A reference to the color world of type [`CMWorldRef`](../cmworldref.md) to use for the color check.

  The functions [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md) and [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md) both allocate color world references of type [`CMWorldRef`](../cmworldref.md).
- `bitmap`: A pointer to a bitmap of type [`CMBitmap`](../cmbitmap.md) whose colors are to be checked. 
- `progressProc`: A calling program–supplied callback function that allows your application to monitor progress or abort the operation as the bitmap’s colors are checked against the gamut of the destination device. The default CMM calls your function approximately every half-second unless color checking occurs in less time this happens when there is a small amount of data to be checked. If the function returns a result of `true`, the operation is aborted. Specify `NULL` for this parameter if your application will not monitor the bitmap color checking. For information on the callback function and its type definition, see the function [`CMBitmapCallBackProcPtr`](../cmbitmapcallbackprocptr.md). 
- `refCon`: A pointer to a reference constant for application data passed as a parameter to calls to `progressProc`. 
- `resultBitmap`: A pointer to a bitmap. On return, contains the results of the color check. The bitmap must have bounds equal to the parameter of the source bitmap pointed to by `bitMap`. You must allocate the pixel buffer pointed to by the `image` field of the structure [`CMBitmap`](../cmbitmap.md) and initialize the buffer to zeroes. Pixels are set to 1 if the corresponding pixel of the source bitmap indicated by `bitMap` is out of gamut. You must set the `space` field of the `CMBitMap` structure to `cmGamutResult1Space` color space storage format, as described in [Abstract Color Space Constants](../api-1560701-abstract_color_space_constants.md).

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
- [CWMatchBitmap](./api-1805116-cwmatchbitmap.md)
  Matches the colors of a bitmap to the gamut of a destination device using the profiles specified by a color world.
- [CWFillLookupTexture](./api-1805126-cwfilllookuptexture.md)
  Fills a 3-D lookup texture from a color world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805121-cwcheckbitmap)*