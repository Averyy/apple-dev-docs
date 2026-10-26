# CWCheckPixMap

**Framework**: Application Services  
**Kind**: func

Checks the colors of a pixel map using the profiles of a specified color world to determine whether the colors are in the gamut of the destination device. 

## Declaration

```c
CMError CWCheckPixMap (
   CMWorldRef cw,
   PixMap *myPixMap,
   CMBitmapCallBackUPP progressProc,
   void *refCon,
   BitMap *resultBitMap
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `CWCheckPixMap` function performs a gamut test of the pixel data of the `myPixMap` pixel map to determine if its colors are within the gamut of the destination device as specified by the destination profile. The gamut test provides a preview of color matching using the specified color world.

The preferred CMM, as determined by the ColorSync Manager based on the profiles of the color world configuration, is called to perform the color matching.

If the preferred CMM is not available, then the ColorSync Manager calls the default CMM to perform the matching. If the preferred CMM is available but does not implement the `CMCheckPixmap` function, then the ColorSync Manager unpacks the colors in the pixel map to create a color list and calls the preferred CMM’s `CMCheckColors` function, passing to this function the list of colors to match. Every CMM must support the `CMCheckColors` function.

For this function to execute successfully, the source and destination profiles’ data color spaces ( `dataColorSpace` field) must be RGB to match the data color space of the pixel map, which is implicitly RGB.

If you specify a pointer to a callback function in the `progressProc` parameter, the CMM performing the color checking calls your function to monitor progress of the session. Each time the CMM calls your function, it passes the function any data you specified in the `CWCheckPixMap` function’s `refCon` parameter.

You can use the reference constant to pass in any kind of data your callback function requires. For example, if your application uses a dialog box with a progress bar to inform the user of the color-checking session’s progress, you can use the reference constant to pass the dialog box’s window reference to the callback routine. For information about the callback function, see the function [`CMBitmapCallBackProcPtr`](../cmbitmapcallbackprocptr.md).

You should ensure that the buffer pointed to by the `baseAddr` field of the bitmap passed in the `resultBitMap` parameter is zeroed out.  

## Parameters

- `cw`: A reference to the color world of type [`CMWorldRef`](../cmworldref.md) in which color checking is to occur.

  The functions [NCWNewColorWorld](./api-1805079-ncwnewcolorworld.md) and [CWConcatColorWorld](./api-1805087-cwconcatcolorworld.md) both return color world references of type [`CMWorldRef`](../cmworldref.md).

  See the QuickDraw Reference for a description of the PixMap data type.
- `myPixMap`: A pointer to the pixel map to check colors for. A pixel map is a QuickDraw structure describing pixel data. The pixel map must be nonrelocatable; to ensure this, you should lock the handle to the pixel map. See the QuickDraw Reference for a description of the PixMap data type.
- `progressProc`: A calling program–supplied callback function that allows your application to monitor progress or abort the operation as the pixel map colors are checked against the gamut of the destination device. 

  The default CMM calls your function approximately every half-second unless color checking occurs in less time; this happens when there is a small amount of data to be checked. If the function returns a result of `true`, the operation is aborted. Specify `NULL` for this parameter if your application will not monitor the pixel map color checking. For information on the callback function and its type definition, see the function [`CMBitmapCallBackProcPtr`](../cmbitmapcallbackprocptr.md).

  See the QuickDraw Reference for a description of the PixMap data type.
- `refCon`: A pointer to a reference constant for application data passed as a parameter to calls to your `CMBitmapCallBack` function pointed to by `progressProc`. 
- `resultBitMap`: A pointer to a QuickDraw bitmap. On return, bits are set to 1 if the corresponding pixel of the pixel map indicated by `myPixMap` is out of gamut. Boundaries of the bitmap indicated by `resultBitMap` must equal the parameter of the pixel map indicated by the `myPixMap`. See the QuickDraw Reference for a description of the PixMap data type.

## See Also

### Working With QuickDraw
- [CWMatchPixMap](./api-1805211-cwmatchpixmap.md)
  Matches a pixel map in place based on a specified color world. 
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

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805214-cwcheckpixmap)*