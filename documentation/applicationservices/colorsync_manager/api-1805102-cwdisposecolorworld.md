# CWDisposeColorWorld

**Framework**: Application Services  
**Kind**: func

Releases the private storage associated with a color world when your application has finished using the color world. 

## Declaration

```c
void CWDisposeColorWorld (
   CMWorldRef cw
);
```

#### Overview

The following functions use color worlds. If you create a color world to pass to one of these functions, you must dispose of the color world when your application is finished with it.

- [CWMatchColors](./api-1805108-cwmatchcolors.md)
- [CWCheckColors](./api-1805111-cwcheckcolors.md)
- [CWMatchBitmap](./api-1805116-cwmatchbitmap.md)
- [CWCheckBitmap](./api-1805121-cwcheckbitmap.md)
- [CWMatchPixMap](./api-1805211-cwmatchpixmap.md)
- [CWCheckPixMap](./api-1805214-cwcheckpixmap.md)

## Parameters

- `cw`: A color world reference of type [`CMWorldRef`](../cmworldref.md). 

  The function [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md) and the function [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md) both allocate color world references of type [`CMWorldRef`](../cmworldref.md).

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
- [CWMatchColors](./api-1805108-cwmatchcolors.md)
  Matches colors in a color list, using the specified color world.
- [CWCheckColors](./api-1805111-cwcheckcolors.md)
  Tests a list of colors using a specified color world to see if they fall within the gamut of a destination device.
- [CWMatchBitmap](./api-1805116-cwmatchbitmap.md)
  Matches the colors of a bitmap to the gamut of a destination device using the profiles specified by a color world.
- [CWCheckBitmap](./api-1805121-cwcheckbitmap.md)
  Tests the colors of the pixel data of a bitmap to determine whether the colors map to the gamut of the destination device.
- [CWFillLookupTexture](./api-1805126-cwfilllookuptexture.md)
  Fills a 3-D lookup texture from a color world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805102-cwdisposecolorworld)*