# CMGetCWInfo

**Framework**: Application Services  
**Kind**: func

Obtains information about the color management modules (CMMs) used for a specific color world.

## Declaration

```c
CMError CMGetCWInfo (
   CMWorldRef cw,
   CMCWInfoRecord *info
);
```

## Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

## Overview

This discussion is accurate for versions of ColorSync prior to 2.5. See the version notes below for changes starting with version 2.5.

To learn whether one or two CMMs are used for color matching and color checking in a given color world and to obtain the CMM type and version number of each CMM used, your application must first obtain a reference to the color world. To obtain a reference to a ColorSync color world, you (or some other process) must have created the color world using the function [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md) or the function [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md).

The source and destination profiles you specify when you create a color world identify their preferred CMMs, and you explicitly identify the profile whose CMM is used for a device link profile or a concatenated color world. However, you cannot be certain if the specified CMM will actually be used until the ColorSync Manager determines internally if the CMM is available and able to perform the requested function. For example, when the specified CMM is not available, the default CMM is used.

The `CMGetCWInfo` function identifies the CMM or CMMs to use. Your application must allocate a data structure of type `CMCWInfoRecord` and pass a pointer to it in the `info` parameter. The `CMGetCWInfo` function returns the color world information in this structure. The structure includes a `cmmCount` field identifying the number of CMMs that will be used and an array of two members containing structures of type `CMMInfoRecord`. The `CMGetCWInfo` function returns information in one or both of the CMM information records depending on whether one or two CMMs are used. 

### Version-Notes

Starting with ColorSync 2.5, a user can select a preferred CMM with the ColorSync control panel. If the user has selected a preferred CMM, and if it is available, then it will be used for all color conversion and matching operations.

## Parameters

- `cw`: A reference to the color world of type [`CMWorldRef`](../cmworldref.md) about which you want information.

  The functions [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md) and [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md) both allocate color world references of type [`CMWorldRef`](../cmworldref.md).
- `info`: A pointer to a color world information record of type `CMCWInfoRecord` that your application supplies. On return, the ColorSync Manager returns information in this structure describing the number of CMMs involved in the matching session and the CMM type and version of each CMM used. 

## See Also

### Working With ColorWorlds
- [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md)
  Creates a color world for color matching based on the specified source and destination profiles. 
- [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md)
  Sets up a color world that includes a set of profiles for various color transformations among devices in a sequence.
- [NCWConcatColorWorld](./api-1805091-ncwconcatcolorworld.md)
  Defines a color world for color transformations among a series of concatenated profiles. 
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
- [CWFillLookupTexture](./api-1805126-cwfilllookuptexture.md)
  Fills a 3-D lookup texture from a color world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805097-cmgetcwinfo)*