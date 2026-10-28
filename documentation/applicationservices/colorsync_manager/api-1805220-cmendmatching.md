# CMEndMatching

**Framework**: Application Services  
**Kind**: func

Concludes a QuickDraw-specific ColorSync matching session initiated by a previous call to the `NCMBeginMatching` function. 

## Declaration

```c
void CMEndMatching (
   CMMatchRef myRef
);
```

## Overview

The `CMEndMatching` function releases private memory allocated for the QuickDraw-specific matching session. 

After you call the `NCMBeginMatching` function and before you call `CMEndMatching` to end the matching session, embedded color-matching picture comments, such as `cmEnableMatching` and `cmDisableMatching`, are not acknowledged. 

## Parameters

- `myRef`: A reference to the matching session to end. This reference was previously created and returned by a call to `NCMBeginMatching` function. See the QuickDraw Reference for a description of the PixMap data type.

## See Also

### Working With QuickDraw
- [CWMatchPixMap](./api-1805211-cwmatchpixmap.md)
  Matches a pixel map in place based on a specified color world. 
- [CWCheckPixMap](./api-1805214-cwcheckpixmap.md)
  Checks the colors of a pixel map using the profiles of a specified color world to determine whether the colors are in the gamut of the destination device. 
- [NCMBeginMatching](./api-1805216-ncmbeginmatching.md)
  Sets up a QuickDraw-specific ColorSync matching session, using the specified source and destination profiles. 
- [NCMDrawMatchedPicture](./api-1805223-ncmdrawmatchedpicture.md)
  Matches a picture’s colors to a destination device’s color gamut, as the picture is drawn, using the specified destination profile.
- [CMEnableMatchingComment](./api-1805227-cmenablematchingcomment.md)
  Inserts a comment into the currently open picture to turn matching on or off. 
- [NCMUseProfileComment](./api-1805229-ncmuseprofilecomment.md)
  Automatically embeds a profile or a profile identifier into an open picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805220-cmendmatching)*