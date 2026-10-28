# CMEnableMatchingComment

**Framework**: Application Services  
**Kind**: func

Inserts a comment into the currently open picture to turn matching on or off. 

## Declaration

```c
void CMEnableMatchingComment (
   Boolean enableIt
);
```

## Overview

If you call this function when no picture is open, it will have no effect. 

## Parameters

- `enableIt`: A flag that directs the ColorSync Manager to generate a `cmEnableMatchingPicComment` comment if `true`, or a `cmDisbleMatchingPicComment` comment if `false`. 

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
- [NCMUseProfileComment](./api-1805229-ncmuseprofilecomment.md)
  Automatically embeds a profile or a profile identifier into an open picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805227-cmenablematchingcomment)*