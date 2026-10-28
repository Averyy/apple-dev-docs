# CMBitmapCallBackProcPtr

**Framework**: Application Services  
**Kind**: tdef  
**Role**: Type Alias

Defines a pointer to a bitmap callback function that function reports on the progress of a color-matching or color-checking session being performed for a bitmap or a pixel map.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

## Declaration

```c
typedef Boolean (*CMBitmapCallBackProcPtr)(SInt32 progress, void *refCon);
```

## Return Value

F`alse` indicates the color-matching or color-checking session should continue. T`rue` indicates the session should be aborted—for example, the user may be holding down the Command–period keys. 

## Discussion

Your `MyCMBitmapCallBack` function allows your application to monitor the progress of a color-matching or color-checking session for a bitmap or a pixel map. Your function can also terminate the matching or checking operation. 

Your callback function is called by the CMM performing the matching or checking process if your application passes a pointer to your callback function in the `progressProc` parameter when it calls one of the following functions:  [CWCheckBitmap](./colorsync_manager/api-1805121-cwcheckbitmap.md) ,  [CWMatchBitmap](./colorsync_manager/api-1805116-cwmatchbitmap.md) ,  [CWCheckPixMap](./colorsync_manager/api-1805214-cwcheckpixmap.md) , and [CWMatchPixMap](./colorsync_manager/api-1805211-cwmatchpixmap.md). Note that your callback function may not be called at all if the operation completes in a very short period.

The CMM used for the color-matching session calls your function at regular intervals. For example, the default CMM calls your function approximately every half-second unless the color matching or checking occurs in less time; this happens when there is a small amount of data to match or check. 

Each time the ColorSync Manager calls your function, it passes to the function any data stored in the reference constant. This is the data that your application specified in the `refCon` parameter when it called one of the color-matching or checking functions. 

For large bitmaps and pixel maps, your application can display a progress bar or other indicator to show how much of the operation has been completed. You might, for example, use the reference constant to pass to the callback function a window reference to a dialog box. You obtain information on how much of the operation has completed from the `progress` parameter. The first time your callback is called, this parameter contains an arbitrary byte count. On each subsequent call, the value is decremented by an amount that can vary from call to call, but that reflects how much of the matching process has completed since the previous call. Using the current value and the original value, you can determine the percentage that has completed. If the callback function is called at all, it will be called a final time with a byte count of 0 when the matching is complete.

To terminate the matching or checking operation, your function should return a value of `true`. Because pixel-map matching is done in place, an application that allows the user to terminate the process should revert to the prematched image to avoid partial mapping.

For bitmap matching, if the `matchedBitMap` parameter of the `CWMatchBitmap` function specifies `NULL`, to indicate that the source bitmap is to be matched in place, and the application allows the user to abort the process, you should also revert to the prematched bitmap if the user terminates the operation. 

Each time the ColorSync Manager calls your progress function, it passes a byte count in the `progress` parameter. The last time the ColorSync Manager calls your progress function, it passes a byte count of 0 to indicate the completion of the matching or checking process. You should use the 0 byte count as a signal to perform any cleanup operations your function requires, such as filling the progress bar to completion to indicate to the user the end of the checking or matching session, and then removing the dialog box used for the display.  

## Parameters

- `progress`: A byte count that begins at an arbitrary value when the function is first called. On each subsequent call, the value is decremented by an amount that can vary from call to call, but that reflects how much of the matching process has completed since the previous call. If the function is called at all, it will be called a final time with a byte count of 0 when the matching is complete. 
- `refCon`: The pointer to a reference constant passed to your `MyCMBitmapCallBack` function each time the color management module (CMM) calls your function. 

## See Also

### Callbacks
- [CMConcatCallBackProcPtr](./cmconcatcallbackprocptr.md)
  Defines a pointer to a progress-monitoring function that the ColorSync Manager calls during lengthy color world processing.
- [CMCountImageProfilesProcPtr](./colorsync_manager/cmcountimageprofilesprocptr.md)
  Defines a pointer to a function that obtains a count of the number of embedded profiles for a given image.
- [CMEmbedImageProcPtr](./colorsync_manager/cmembedimageprocptr.md)
  Defines a pointer to a function that embeds an image with an ICC profile.
- [CMFlattenProcPtr](./cmflattenprocptr.md)
  Defines a pointer to a data transfer callback function that transfers profile data from the format for embedded profiles to disk file format or vice versa.
- [CMGetImageSpaceProcPtr](./colorsync_manager/cmgetimagespaceprocptr.md)
  Defines a pointer to a function that obtains the signature of the data color space in which the color values of colors in an image are expressed.
- [CMGetIndImageProfileProcPtr](./colorsync_manager/cmgetindimageprofileprocptr.md)
  Defines a pointer to a function that obtains a specific embedded profile for a given image.
- [CMIterateDeviceInfoProcPtr](./cmiteratedeviceinfoprocptr.md)
  Defines a pointer to a function that iterates through device information available on the system.
- [CMIterateDeviceProfileProcPtr](./cmiteratedeviceprofileprocptr.md)
  Defines a pointer to a function that iterates through the device profiles available on the system.
- [CMLinkImageProcPtr](./colorsync_manager/cmlinkimageprocptr.md)
  Defines a pointer to a function that matches an image file with a device link profile.
- [CMMatchImageProcPtr](./colorsync_manager/cmmatchimageprocptr.md)
  Defines a pointer to a function that color matches an image file.
- [CMMIterateProcPtr](./cmmiterateprocptr.md)
  Defines a pointer to a function that iterates through color management modules installed on the system.
- [CMProofImageProcPtr](./colorsync_manager/cmproofimageprocptr.md)
  Defines a pointer to a function that proofs an image.
- [CMProfileIterateProcPtr](./cmprofileiterateprocptr.md)
  Defines a pointer to a profile iteration callback function that the ColorSync Manager calls for each found profile file as it iterates over the available profiles.
- [CMSetIndImageProfileProcPtr](./colorsync_manager/cmsetindimageprofileprocptr.md)
  Defines a pointer to a function that sets a specific embedded profile for a given image.
- [CMUnembedImageProcPtr](./colorsync_manager/cmunembedimageprocptr.md)
  Defines a pointer to a function that umembeds an ICC profile from an image.
- [CMValidImageProcPtr](./colorsync_manager/cmvalidimageprocptr.md)
  Defines a pointer to a function that validates a specified image file.
- [CountImageProfilesProcPtr](./colorsync_manager/countimageprofilesprocptr.md)
  Defines a pointer to a function that counts the number of embedded profiles for a given image. 
- [EmbedImageProcPtr](./colorsync_manager/embedimageprocptr.md)
  Defines a pointer to an embed-image function.
- [GetImageSpaceProcPtr](./colorsync_manager/getimagespaceprocptr.md)
  Defines a pointer to a get-image-space function.
- [GetIndImageProfileProcPtr](./colorsync_manager/getindimageprofileprocptr.md)
  Defines a pointer to a function that obtains a color profile for an individual image.
- [MatchImageProcPtr](./colorsync_manager/matchimageprocptr.md)
  Defines a pointer to a match-image function.
- [SetIndImageProfileProcPtr](./colorsync_manager/setindimageprofileprocptr.md)
  Defines a pointer to a function that sets a color profile for an individual image.
- [UnembedImageProcPtr](./colorsync_manager/unembedimageprocptr.md)
  Defines a pointer to an umembed-image function.
- [ValidateImageProcPtr](./colorsync_manager/validateimageprocptr.md)
  Defines a pointer to a validate-image function.
- [ValidateSpaceProcPtr](./colorsync_manager/validatespaceprocptr.md)
  Defines a pointer to a validate-space function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/cmbitmapcallbackprocptr)*