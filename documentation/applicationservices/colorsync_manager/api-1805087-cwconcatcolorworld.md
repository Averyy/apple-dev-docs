# CWConcatColorWorld

**Framework**: Application Services  
**Kind**: func

Sets up a color world that includes a set of profiles for various color transformations among devices in a sequence.

## Declaration

```c
CMError CWConcatColorWorld (
   CMWorldRef *cw,
   CMConcatProfileSet *profileSet
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `CWConcatColorWorld` function sets up a session for color processing that includes a set of profiles. The array of profiles is in processing order—source through destination. Your application passes the function a pointer to a data structure of type `CMConcatProfileSet` to identify the profile array. 

The quality flag setting—indicating normal mode, draft mode, or best mode—specified by the first profile prevails for the entire session the quality flags of following profiles in the sequence are ignored. The quality flag setting is stored in the `flags` field of the profile header. See [`CM2Header`](../cm2header.md) and [Flag Mask Definitions for Version 2.x Profiles](../api-1560699-x_profiles.md) for more information on the use of flags. 

The rendering intent specified by the first profile is used to color match to the second profile, the rendering intent for the second profile is used to color match to the third profile, and so on through the series of concatenated profiles. 

The following rules govern the profiles you can specify in the profile array pointed to by the `profileSet` parameter for use with the `CWConcatColorWorld` function: 

-  In the profile array, you can pass in one or more profiles, but you must specify at least one profile. If you specify only one profile, it must be a device link profile. If you specify a device link profile, you cannot specify any other profiles in the profiles array; a device link profile must be used alone. 
-  In the profile array, you can specify an abstract profile anywhere in the sequence other than as the first or last profile. 
-  For the first and last profiles, you can specify device profiles or color space conversion profiles. However, when you set up a color-matching session with a named color space profile and other profiles, the named color profile must be first or the last profile in the color world—it cannot be in the middle. 
-  You cannot specify `NULL` to indicate the system profile. Note that starting with version 2.5, use of the system profile has changed. 
-  If you specify a color space profile in the middle of the profile sequence, it is ignored by the default CMM. 
-  If you specify a named color profile, it must be the first or the last profile. Otherwise, `CWConcatColorWorld` returns the value `cmCantConcatenateError`. 

A after executing the `CWConcatColorWorld` function, you should call the function [CMCloseProfile](./api-1804861-cmcloseprofile.md) for each profile to dispose of its reference. 

Instead of passing in an array of profiles, you can specify a device link profile. For information on how to create a device link profile, see the `CWNewLinkProfile` function, which is described next. 

##### Version-Notes

The parameter description for `profileSet` includes changes in how this function is used starting with ColorSync version 2.5.

Note also that starting with version 2.5, use of the system profile has changed.

## Parameters

- `cw`: A pointer to a color world. On return, a reference to a color world of type [`CMWorldRef`](../cmworldref.md). You pass the returned reference to other functions that use the color world for color-matching and color-checking sessions. 
- `profileSet`: A pointer of type [`CMConcatProfileSet`](../cmconcatprofileset.md) to an array of profiles describing the processing to carry out. You create the array and initialize it in processing order—source through destination.

  You set the `keyIndex` field of the `CMConcatProfileSet` data structure to specify the zero-based index of the profile within the profile array whose specified CMM should be used for the entire color-matching or color-checking session. The profile header’s `CMMType` field specifies the CMM. This CMM will fetch the profile elements necessary for the session.

  Note that starting with ColorSync 2.5, the user can set a preferred CMM with the ColorSync control panel. If that CMM is available, ColorSync will use that CMM for all color conversion and matching operations the CMM is capable of performing.

## See Also

### Working With ColorWorlds
- [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md)
  Creates a color world for color matching based on the specified source and destination profiles. 
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805087-cwconcatcolorworld)*