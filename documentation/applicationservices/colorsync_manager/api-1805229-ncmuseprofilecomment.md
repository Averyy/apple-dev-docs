# NCMUseProfileComment

**Framework**: Application Services  
**Kind**: func

Automatically embeds a profile or a profile identifier into an open picture.

## Declaration

```c
CMError NCMUseProfileComment (
   CMProfileRef prof,
   UInt32 flags
);
```

#### Return Value

A `CMError` value. See [Result Codes](../colorsync_manager.md#1670295).

#### Overview

The `NCMUseProfileComment` function automatically generates the picture comments required to embed the specified profile or profile identifier into the open picture.

To embed a profile, you use the constant `cmEmbedWholeProfile` to set the `flags` parameter before calling `NCMUseProfileComment`. The `NCMUseProfileComment` function calls the QuickDraw `PicComment` function with a picture comment `kind` value of `cmComment` and a 4-byte selector that describes the type of data in the picture comment: `cmBeginProfileSel` to begin the profile, `cmContinueProfileSel` to continue, and `cmEndProfileSel` to end the profile. These constants are described in `Picture Comment Selectors`.

If the size in bytes of the profile and the 4-byte selector together exceed 32 KB, this function segments the profile data and embeds the multiple segments in consecutive order using selector `cmContinueProfileSel` to embed each segment.

To embed a profile identifier of type `CMProfileIdentifier` , you use the constant `cmEmbedProfileIdentifier` to set the `flags` parameter before calling `NCMUseProfileComment`. The function extracts the necessary information from the profile reference ( `prof`) to embed a profile identifier for the profile. The profile reference can refer to a previously embedded profile, or to a profile on disk in the ColorSync Profiles folder.

You can use this function to embed most types of profiles in an image, including device link profiles, but not abstract profiles. You cannot use this function to embed ColorSync 1.0 profiles in an image.

The `NCMUseProfileComment` function precedes the profile it embeds with a picture comment of kind `cmBeginProfile`. For embedding to work correctly, the currently effective profile must be terminated by a picture comment of kind `cmEndProfile` after drawing operations using that profile are performed. You are responsible for adding the picture comment of kind `cmEndProfile`. If a picture comment was not specified to end the profile following the drawing operations to which the profile applies, the profile will remain in effect until the next embedded profile is introduced with a picture comment of kind `cmBeginProfile`. However, use of the next profile might not be the intended action. Always pair use of the `cmBeginProfile` and `cmEndProfile` picture comments. When the ColorSync Manager encounters a `cmEndProfile` picture comment, it restores use of the system profile for matching until it encounters another `cmBeginProfile` picture comment. 

##### Version-Notes

In ColorSync 2.0, the `flags` parameter was ignored and the routine always embedded the entire profile.

In ColorSync 2.0, if the `prof` parameter refers to a version 1.0 profile, the profile is not embedded into the picture correctly. In ColorSync versions starting with 2.1, this bug has been fixed. One possible workaround for this problem in ColorSync 2.0 is to call `CMCopyProfile` to copy the 1.0 profile reference into a handle. The handle can then be embedded into the picture using `CMUseProfileComment`.

## Parameters

- `prof`: A profile reference of type [`CMProfileRef`](../cmprofileref.md) to the profile to embed. See the QuickDraw Reference for a description of the PixMap data type.
- `flags`: A flag value in which individual bits determine settings. `Embedded Profile Identifiers` describes constants for use with this parameter. For example, you pass `cmEmbedWholeProfile` to embed a whole profile or `cmEmbedProfileIdentifier` to embed a profile identifier. No other values are currently defined; all other bits are reserved for future use. 

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
- [NCMDrawMatchedPicture](./api-1805223-ncmdrawmatchedpicture.md)
  Matches a picture’s colors to a destination device’s color gamut, as the picture is drawn, using the specified destination profile.
- [CMEnableMatchingComment](./api-1805227-cmenablematchingcomment.md)
  Inserts a comment into the currently open picture to turn matching on or off. 


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805229-ncmuseprofilecomment)*