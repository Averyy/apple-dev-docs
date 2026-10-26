# NCWNewColorWorld

**Framework**: Application Services  
**Kind**: func

Creates a color world for color matching based on the specified source and destination profiles. 

## Declaration

```c
CMError NCWNewColorWorld (
   CMWorldRef *cw,
   CMProfileRef src,
   CMProfileRef dst
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

You must set up a color world before your application can perform general purpose color-matching or color-checking operations. To set up a color world for these operations, your application can call `NCWNewColorWorld` after obtaining references to the profiles to use as the source and destination profiles for the color world. The following rules govern the types of profiles allowed:

-  You can specify a device profile or a color space conversion profile for the source and destination profiles. 
-  You can not specify a device link profile or an abstract profile for either the source profile or the destination profile. 
-  Only one profile can be a named color profile. 
-  You can specify the system profile explicitly by reference or by giving `NULL` for either the source profile or the destination profile. 

You should call the function [CMCloseProfile](./api-1804861-cmcloseprofile.md) for both the source and destination profiles to dispose of their references after execution of the `NCWNewColorWorld` function.

The quality flag setting (indicating normal mode, draft mode, or best mode) specified by the source profile prevails for the entire session. The quality flag setting is stored in the `flags` field of the profile header. See [`CM2Header`](../cm2header.md) and [Flag Mask Definitions for Version 2.x Profiles](../api-1560699-x_profiles.md) for more information on the use of flags. The rendering intent specified by the source profile also prevails for the entire session.

The function [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md) also allocates a color world reference of type [`CMWorldRef`](../cmworldref.md). 

##### Version-Notes

The parameter descriptions for `src` and `dst` describe changes in how this functions is used starting with ColorSync version 2.5.

## Parameters

- `cw`: A pointer to a color world. On return, a reference to a matching session color world of type [`CMWorldRef`](../cmworldref.md). You pass this reference to other functions that use the color world. 
- `src`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) that specifies the source profile for the color-matching world. This profile’s `dataColorSpace` element corresponds to the source data type for subsequent calls to functions that use this color world.

  Starting with ColorSync version 2.5, you can call [CMGetDefaultProfileBySpace](./api-1804940-cmgetdefaultprofilebyspace.md) to get the default profile for a specific color space or [CMGetProfileByAVID](./api-1804955-cmgetprofilebyavid.md) to get a profile for a specific display. 

  With any version of ColorSync, you can specify a `NULL` value to indicate the ColorSync system profile. Note, however, that starting with version 2.5, use of the system profile has changed.
- `dst`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) that specifies the destination profile for the color-matching world. This profile’s `dataColorSpace` element corresponds to the destination data type for subsequent calls to functions using this color world.

  Starting with ColorSync version 2.5, you can call [CMGetDefaultProfileBySpace](./api-1804940-cmgetdefaultprofilebyspace.md) to get the default profile for a specific color space or [CMGetProfileByAVID](./api-1804955-cmgetprofilebyavid.md) to get a profile for a specific display.

   With any version of ColorSync, you can specify a `NULL` value to indicate the ColorSync system profile. Note, however, that starting with version 2.5, use of the system profile has changed.

## See Also

### Working With ColorWorlds
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
- [CWFillLookupTexture](./api-1805126-cwfilllookuptexture.md)
  Fills a 3-D lookup texture from a color world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805079-ncwnewcolorworld)*