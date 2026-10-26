# CWFillLookupTexture

**Framework**: Application Services  
**Kind**: func

Fills a 3-D lookup texture from a color world.

## Declaration

```c
CMError CWFillLookupTexture (
   CMWorldRef cw,
   UInt32 gridPoints,
   UInt32 format,
   UInt32 dataSize,
   void *data
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295). 

#### Overview

You can use the resulting table in OpenGL to accelerate color management in hardware.

## Parameters

- `cw`: The color world to use.
- `gridPoints`: The number of grid points per channel in the texture.
- `format`: The format of pixels in texture; for example, `cmTextureRGBtoRGBX8`.
- `dataSize`: The size in bytes of texture data to fill.
- `data`: On output, points to the texture data to fill.

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
- [CWCheckBitmap](./api-1805121-cwcheckbitmap.md)
  Tests the colors of the pixel data of a bitmap to determine whether the colors map to the gamut of the destination device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805126-cwfilllookuptexture)*