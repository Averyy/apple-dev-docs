# CWMatchPixMap

**Framework**: Application Services  
**Kind**: func

Matches a pixel map in place based on a specified color world. 

## Declaration

```c
CMError CWMatchPixMap (
   CMWorldRef cw,
   PixMap *myPixMap,
   CMBitmapCallBackUPP progressProc,
   void *refCon
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `CWMatchPixMap` function matches a pixel map in place using the profiles specified by the given color world. The preferred CMM, as determined by the ColorSync Manager based on the color world configuration, is called to perform the color matching.

If the preferred CMM is not available, then the ColorSync Manager calls the default CMM to perform the matching. If the preferred CMM is available but it does not implement the `CMMatchPixMap` function, then the ColorSync Manager unpacks the colors in the pixel map to create a color list and calls the preferred CMM’s `CMMatchColors` function, passing to this function the list of colors to match. Every CMM must support the `CMMatchColors` function. 

For this function to execute successfully, the source and destination profiles’ data color spaces ( `dataColorSpace` field) must be RGB to match the data color space of the pixel map, which is implicitly RGB. For color spaces other than RGB, you should use the function [CWMatchBitmap](./api-1805116-cwmatchbitmap.md).

If you specify a pointer to a callback function in the `progressProc` parameter, the CMM performing the color matching calls your function to monitor progress of the session. Each time the CMM calls your function, it passes the function any data you specified in the `CWMatchPixMap` function’s `refCon` parameter. If the ColorSync Manager performs the color matching, it calls your callback monitoring function once every scan line during this process. 

You can use the reference constant to pass in any kind of data your callback function requires. For example, if your application uses a dialog box with a progress bar to inform the user of the color-matching session’s progress, you can use the reference constant to pass the dialog box’s window reference to the callback routine. For information about the callback function, see the function [`CMBitmapCallBackProcPtr`](../cmbitmapcallbackprocptr.md).

Applications do not interact directly with the function [CWMatchColors](./api-1805108-cwmatchcolors.md). 

## Parameters

- `cw`: A reference to the color world of type [`CMWorldRef`](../cmworldref.md) in which matching is to occur.

  The functions [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md) and [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md) both allocate color world references of type [`CMWorldRef`](../cmworldref.md).
- `myPixMap`: A pointer to the pixel map to match. A pixel map is a QuickDraw structure describing pixel data. The pixel map must be nonrelocatable; to ensure this, you should lock the handle to the pixel map before you call this function. See the QuickDraw Reference for a description of the `PixMap` data type.
- `progressProc`: A function supplied by your application to monitor progress or abort the operation as the pixel map colors are matched. The default CMM calls your function approximately every half-second, unless matching is completed in less time.

  If the function returns a result of `true`, the operation is aborted. You specify `NULL` for this parameter if your application will not monitor the pixel map color matching. For information on the callback function and its type definition, refer to the function `CMProfileFilterProcPtr`.
- `refCon`: A pointer to a reference constant for application data that is passed as a parameter to calls to `progressProc`. 

## See Also

### Working With QuickDraw
- [CWCheckPixMap](./api-1805214-cwcheckpixmap.md)
  Checks the colors of a pixel map using the profiles of a specified color world to determine whether the colors are in the gamut of the destination device. 
- [NCMBeginMatching](./api-1805216-ncmbeginmatching.md)
  Sets up a QuickDraw-specific ColorSync matching session, using the specified source and destination profiles. 
- [CMEndMatching](./api-1805220-cmendmatching.md)
  Concludes a QuickDraw-specific ColorSync matching session initiated by a previous call to the `NCMBeginMatching` function. 
- [NCMDrawMatchedPicture](./api-1805223-ncmdrawmatchedpicture.md)
  Matches a picture’s colors to a destination device’s color gamut, as the picture is drawn, using the specified destination profile.
- [CMEnableMatchingComment](./api-1805227-cmenablematchingcomment.md)
  Inserts a comment into the currently open picture to turn matching on or off. 
- [NCMUseProfileComment](./api-1805229-ncmuseprofilecomment.md)
  Automatically embeds a profile or a profile identifier into an open picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805211-cwmatchpixmap)*