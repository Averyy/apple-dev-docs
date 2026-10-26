# NCMDrawMatchedPicture

**Framework**: Application Services  
**Kind**: func

Matches a picture’s colors to a destination device’s color gamut, as the picture is drawn, using the specified destination profile.

## Declaration

```c
void NCMDrawMatchedPicture (
   PicHandle myPicture,
   CMProfileRef dst,
   Rect *myRect
);
```

#### Return Value

This function does not return an error value. Instead, after calling `NCMDrawMatchedPicture` you call the `QDError` routine to determine if an error has occurred. 

#### Overview

The `NCMDrawMatchedPicture` function operates in the context of the current color graphics port. This function sets up and takes down a color-matching session. It automatically matches all colors in a picture to the destination profile for a destination device as the picture is drawn. It uses the ColorSync system profile as the initial source profile and any embedded profiles as they are encountered thereafter. (Because color-matching picture comments embedded in the picture to be matched are recognized, embedded profiles are used.)

The ColorSync Manager defines five picture comment kinds, as described in `Picture Comment Kinds`. For embedding to work correctly, each embedded profile that is used for matching must be terminated by a picture comment of kind `cmEndProfile`. If a picture comment is not specified to end the profile after drawing operations using that profile are performed, the profile will remain in effect until another embedded profile is introduced that has a picture comment kind of `cmBeginProfile`. To avoid unexpected matching effects, always pair use of the `cmBeginProfile` and `cmEndProfile` picture comments. When the ColorSync Manager encounters a `cmEndProfile` picture comment, it restores use of the system profile for matching until it encounters another `cmBeginProfile` picture comment.

The picture is drawn with matched colors to all screen graphics devices. If the current graphics device is not a screen device, matching occurs for that graphics device only. 

If the current port is not a color graphics port, then calling this function is equivalent to calling `DrawPicture`, in which case no color matching occurs. 

##### Version-Notes

The parameter description for `dst` describes changes in how this function is used starting with ColorSync version 2.5.

## Parameters

- `myPicture`: The QuickDraw picture whose colors are to be matched. See the QuickDraw Reference for a description of the PixMap data type.
- `dst`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile of the destination device. Starting with ColorSync version 2.5, if you know the destination display device, you can call [CMGetProfileByAVID](./api-1804955-cmgetprofilebyavid.md) to get the specific profile for the display, or you can call [CMGetDefaultProfileBySpace](./api-1804940-cmgetdefaultprofilebyspace.md) to get the default profile for the RGB color space,.

  With any version of ColorSync, you can specify a `NULL` value to indicate the ColorSync system profile. Note, however, that starting with version 2.5, use of the system profile has changed.

  See the QuickDraw Reference for a description of the PixMap data type.
- `myRect`: A pointer to a destination rectangle for rendering the picture specified by `myPicture`. 

## See Also

### Working With QuickDraw
- [CWMatchPixMap](./api-1805211-cwmatchpixmap.md)
  Matches a pixel map in place based on a specified color world. 
- [CWCheckPixMap](./api-1805214-cwcheckpixmap.md)
  Checks the colors of a pixel map using the profiles of a specified color world to determine whether the colors are in the gamut of the destination device. 
- [NCMBeginMatching](./api-1805216-ncmbeginmatching.md)
  Sets up a QuickDraw-specific ColorSync matching session, using the specified source and destination profiles. 
- [CMEndMatching](./api-1805220-cmendmatching.md)
  Concludes a QuickDraw-specific ColorSync matching session initiated by a previous call to the `NCMBeginMatching` function. 
- [CMEnableMatchingComment](./api-1805227-cmenablematchingcomment.md)
  Inserts a comment into the currently open picture to turn matching on or off. 
- [NCMUseProfileComment](./api-1805229-ncmuseprofilecomment.md)
  Automatically embeds a profile or a profile identifier into an open picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805223-ncmdrawmatchedpicture)*