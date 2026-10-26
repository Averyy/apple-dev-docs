# NCWConcatColorWorld

**Framework**: Application Services  
**Kind**: func

Defines a color world for color transformations among a series of concatenated profiles. 

## Declaration

```c
CMError NCWConcatColorWorld (
   CMWorldRef *cw,
   NCMConcatProfileSet *profileSet,
   CMConcatCallBackUPP proc,
   void *refCon
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The caller can override the color management module (CMM) that would normally be selected by ColorSync by providing a CMM identifier in the `NCMConcatProfileSet` structure, or pass 0 to accept ColorSync's CMM selection (note that this could either be the user's preferred CMM selection or the CMM called for in the profile). The `flags` and k parameters are provided to allow easy customization of such attributes as quality and gamut-checking, while preserving the other settings. Each profile in the set can be customized by overriding the intent, and the selection of the transform tag. Together with other profiles, a custom-rendering environment can be set up to transform to or from device-dependent spaces with a minimum of gamut compression and/or unnecessary transformations to and from connection spaces. This flexibility comes at the price of specific knowledge of the profile contents and how device gamuts overlap. 

Note that for standard input and output device profiles, A2B and B2A tags represent transforms from data space to connection space and from connection space to data space, respectively. Under these circumstances, the caller would not normally be able to use the same transform tags (e.g., `kUseAtoB` ) consecutively, since a connection space would not be the same as the subsequent data space. If the spaces aren't the same, the caller will get `a cmCantConcatenateError` error returned. For profiles of type `cmLinkClass`, `cmAbstractClass`, `cmColorSpaceClass` , and `cmNamedColorClass` , these constants are not always meaningful, and the caller is encouraged to think in terms of the actual tags present in the profiles (e.g., A2B0 or B2A0 ). Under these conditions, it may well be appropriate to specify two transform tags of the same type consecutively, as long as the actual color spaces align in between tags. If this is not the case, a c`mCantConcatenateError` error is returned.

The callback proc is provided as protection against the appearance of a stalled machine during lengthy color world processing. If a CMM takes more than several          seconds to process the information and create a color world, it will call the callback proc, if one is provided, and pass it the `refCon` provided. This is also true for `NCWNewLinkProfile`. 

## Parameters

- `cw`: A reference to a color world that the ColorSync Manager returns if the function completes successfully. You pass this reference to other functions that use the color world for color-matching and color-checking sessions. 
- `profileSet`: An array of profiles describing the processing to be carried out. The array is in processing order source through destination. 
- `proc`: A calling-program-supplied callback function that allows your application to monitor progress or abort the operation. 
- `refCon`: A reference constant containing data specified by the          calling application program. 

## See Also

### Working With ColorWorlds
- [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md)
  Creates a color world for color matching based on the specified source and destination profiles. 
- [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md)
  Sets up a color world that includes a set of profiles for various color transformations among devices in a sequence.
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
- [CWFillLookupTexture](./api-1805126-cwfilllookuptexture.md)
  Fills a 3-D lookup texture from a color world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805091-ncwconcatcolorworld)*