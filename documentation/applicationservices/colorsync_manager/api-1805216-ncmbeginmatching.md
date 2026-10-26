# NCMBeginMatching

**Framework**: Application Services  
**Kind**: func

Sets up a QuickDraw-specific ColorSync matching session, using the specified source and destination profiles. 

## Declaration

```c
CMError NCMBeginMatching (
   CMProfileRef src,
   CMProfileRef dst,
   CMMatchRef *myRef
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `NCMBeginMatching` function sets up a QuickDraw-specific matching session, telling the ColorSync Manager to match all colors drawn to the current graphics device using the specified source and destination profiles. 

The `NCMBeginMatching` function returns a reference to the color-matching session. You must later pass this reference to the function [CMEndMatching](./api-1805220-cmendmatching.md) to conclude the session.

The source and destination profiles define how the match is to occur. Passing `NULL` for either the source or destination profile is equivalent to passing the system profile. If the current device is a screen device, matching to all screen devices occurs.

The `NCMBeginMatching` and `CMEndMatching` functions can be nested. In such cases, the ColorSync Manager matches to the most recently added profiles first. Therefore, if you want to use the `NCMBeginMatching`– `CMEndMatching` pair to perform a page preview—which typically entails color matching from a source device (scanner) to a destination device (printer) to a preview device (display)— you first call `NCMBeginMatching` with the printer-to-display profiles, and then call `NCMBeginMatching` with the scanner-to-printer profiles. The ColorSync Manager then matches all drawing from the scanner to the printer and then back to the display. The print preview process entails multiprofile transformations. The ColorSync Manager general purpose functions (which include the use of concatenated profiles well suited to print-preview processing) offer an easier and faster way to do this. These functions are described in “Matching Colors Using General Purpose Functions”.

If you call `NCMBeginMatching` before drawing to the screen’s graphics device (as opposed to an offscreen device), you must call `CMEndMatching` to finish a matching session before calling `WaitNextEvent` or any other routine (such as Window Manager routines) that could draw to the screen. Failing to do so will cause unwanted matching to occur. Furthermore, if a device has color matching enabled, you cannot call the `CopyBits` procedure to copy from it to itself unless the source and destination rectangles are the same.

Even if you call the `NCMBeginMatching` function before calling the QuickDraw `DrawPicture` function, the ColorSync picture comments such as `cmEnableMatching` and `cmDisableMatching` are not acknowledged. For the ColorSync Manager to recognize these comments and allow their use, you must call the function [NCMUseProfileComment](./api-1805229-ncmuseprofilecomment.md) for color matching using picture comments.

This function causes matching for the specified devices rather than for the current color graphics port.

The `NCMBeginMatching` function uses QuickDraw and performs color matching in a manner acceptable to most applications. However, if your application needs a finer level of control over color matching, it can use the general purpose functions described in “Matching Colors Using General Purpose Functions”. 

##### Version-Notes

The parameter descriptions for `src` and `dst` describe changes in how this function is used starting with ColorSync version 2.5.

## Parameters

- `src`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) that specifies the source profile for the matching session. Starting with ColorSync version 2.5, you can call [CMGetDefaultProfileBySpace](./api-1804940-cmgetdefaultprofilebyspace.md) to get the default profile for a specific color space or [CMGetProfileByAVID](./api-1804955-cmgetprofilebyavid.md) to get a profile for a specific display.

  With any version of ColorSync, you can specify a `NULL` value to indicate the ColorSync system profile. Note, however, that starting with version 2.5, use of the system profile has changed.

  See the QuickDraw Reference for a description of the PixMap data type.
- `dst`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) that specifies the destination profile for the matching session. Starting with ColorSync version 2.5, you can call [CMGetDefaultProfileBySpace](./api-1804940-cmgetdefaultprofilebyspace.md) to get the default profile for a specific color space or [CMGetProfileByAVID](./api-1804955-cmgetprofilebyavid.md) to get a profile for a specific display.

  With any version of ColorSync, you can specify a `NULL` value to indicate the ColorSync system profile. Note, however, that starting with version 2.5, use of the system profile has changed.See the QuickDraw Reference for a description of the PixMap data type.
- `myRef`: A pointer to a matching session. On return, it specifies the QuickDraw-specific matching session that was set up. See the QuickDraw Reference for a description of the PixMap data type.

## See Also

### Working With QuickDraw
- [CWMatchPixMap](./api-1805211-cwmatchpixmap.md)
  Matches a pixel map in place based on a specified color world. 
- [CWCheckPixMap](./api-1805214-cwcheckpixmap.md)
  Checks the colors of a pixel map using the profiles of a specified color world to determine whether the colors are in the gamut of the destination device. 
- [CMEndMatching](./api-1805220-cmendmatching.md)
  Concludes a QuickDraw-specific ColorSync matching session initiated by a previous call to the `NCMBeginMatching` function. 
- [NCMDrawMatchedPicture](./api-1805223-ncmdrawmatchedpicture.md)
  Matches a picture’s colors to a destination device’s color gamut, as the picture is drawn, using the specified destination profile.
- [CMEnableMatchingComment](./api-1805227-cmenablematchingcomment.md)
  Inserts a comment into the currently open picture to turn matching on or off. 
- [NCMUseProfileComment](./api-1805229-ncmuseprofilecomment.md)
  Automatically embeds a profile or a profile identifier into an open picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805216-ncmbeginmatching)*