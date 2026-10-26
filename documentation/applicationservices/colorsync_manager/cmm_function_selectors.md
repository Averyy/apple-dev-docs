# CMM Function Selectors

**Framework**: Application Services  
**Kind**: enum

Define selectors used for component-based CMM functions.

## Declaration

```c
enum {
   kCMMOpen = -1,
   kCMMClose = -2,
   kCMMGetInfo = -4,
   kNCMMInit = 6,
   kCMMMatchColors = 1,
   kCMMCheckColors = 2,
   kCMMValidateProfile = 8,
   kCMMMatchBitmap = 9,
   kCMMCheckBitmap = 10,
   kCMMConcatenateProfiles = 5,
   kCMMConcatInit = 7,
   kCMMNewLinkProfile = 16,
   kNCMMConcatInit = 18,
   kNCMMNewLinkProfile = 19,
   kCMMGetPS2ColorSpace = 11,
   kCMMGetPS2ColorRenderingIntent = 12,
   kCMMGetPS2ColorRendering = 13,
   kCMMGetPS2ColorRenderingVMSize = 17,
   kCMMFlattenProfile = 14,
   kCMMUnflattenProfile = 15,
   kCMMInit = 0,
   kCMMGetNamedColorInfo = 70,
   kCMMGetNamedColorValue = 71,
   kCMMGetIndNamedColorValue = 72,
   kCMMGetNamedColorIndex = 73,
   kCMMGetNamedColorName = 74,
   kCMMMatchPixMap = 3,
   kCMMCheckPixMap = 4
};
```

#### Overview

Your CMM must respond to the ColorSync Manager required request codes. When a CMM receives a required request code from the ColorSync Manager, the CMM must determine the nature of the request, perform the appropriate processing, set an error code if necessary, and return an appropriate function result to the Component Manager. The required request codes are:

- `kNCMMInit `
- `kCMMMatchColors `
- `kCMMCheckColors `
- `kCMMInit `

Your CMM should respond to the rest of the ColorSync Manager request codes defined by this enumeration, but it is not required to do so. 

## Topics

### Constants
- [kCMMOpen](./cmm_function_selectors/kcmmopen.md)
  Required.
- [kCMMClose](./cmm_function_selectors/kcmmclose.md)
  Required.
- [kCMMGetInfo](./cmm_function_selectors/kcmmgetinfo.md)
  Required.
- [kNCMMInit](./cmm_function_selectors/kncmminit.md)
  In response to this request code, your CMM should initialize any private data it will need for the color session and for subsequent requests from the calling application or driver. Required.
- [kCMMMatchColors](./cmm_function_selectors/kcmmmatchcolors.md)
  In response to this request code, your CMM should match the colors in the `myColors` parameter to the color gamut of the destination profile and replace the color-list color values with the matched colors. Required.
- [kCMMCheckColors](./cmm_function_selectors/kcmmcheckcolors.md)
- [kCMMValidateProfile](./cmm_function_selectors/kcmmvalidateprofile.md)
- [kCMMMatchBitmap](./cmm_function_selectors/kcmmmatchbitmap.md)
- [kCMMCheckBitmap](./cmm_function_selectors/kcmmcheckbitmap.md)
- [kCMMConcatenateProfiles](./cmm_function_selectors/kcmmconcatenateprofiles.md)
  This request code is for backward compatibility with ColorSync 1.0.
- [kCMMConcatInit](./cmm_function_selectors/kcmmconcatinit.md)
- [kCMMNewLinkProfile](./cmm_function_selectors/kcmmnewlinkprofile.md)
- [kNCMMConcatInit](./cmm_function_selectors/kncmmconcatinit.md)
- [kNCMMNewLinkProfile](./cmm_function_selectors/kncmmnewlinkprofile.md)
- [kCMMGetPS2ColorSpace](./cmm_function_selectors/kcmmgetps2colorspace.md)
- [kCMMGetPS2ColorRenderingIntent](./cmm_function_selectors/kcmmgetps2colorrenderingintent.md)
- [kCMMGetPS2ColorRendering](./cmm_function_selectors/kcmmgetps2colorrendering.md)
- [kCMMGetPS2ColorRenderingVMSize](./cmm_function_selectors/kcmmgetps2colorrenderingvmsize.md)
- [kCMMFlattenProfile](./cmm_function_selectors/kcmmflattenprofile.md)
- [kCMMUnflattenProfile](./cmm_function_selectors/kcmmunflattenprofile.md)
- [kCMMInit](./cmm_function_selectors/kcmminit.md)
- [kCMMGetNamedColorInfo](./cmm_function_selectors/kcmmgetnamedcolorinfo.md)
  In response to this request code, your CMM extracts named color data from the profile whose reference is passed in the `srcProf` parameter. For more information, see the function [CMGetNamedColorInfo](./api-1805047-cmgetnamedcolorinfo.md).
- [kCMMGetNamedColorValue](./cmm_function_selectors/kcmmgetnamedcolorvalue.md)
- [kCMMGetIndNamedColorValue](./cmm_function_selectors/kcmmgetindnamedcolorvalue.md)
  In response to this request code, your CMM extracts device and PCS color values for a specific named color index from the profile whose reference is passed in the `prof` parameter. For more information, see the function [CMGetIndNamedColorValue](./api-1805059-cmgetindnamedcolorvalue.md).
- [kCMMGetNamedColorIndex](./cmm_function_selectors/kcmmgetnamedcolorindex.md)
  In response to this request code, your CMM extracts a named color index for a specific color name from the profile whose reference is passed in the `prof` parameter. For more information, see the function [CMGetNamedColorIndex](./api-1805065-cmgetnamedcolorindex.md).
- [kCMMGetNamedColorName](./cmm_function_selectors/kcmmgetnamedcolorname.md)
  In response to this request code, your CMM extracts a named color name for a specific named color index from the profile whose reference is passed in the `prof` parameter. For more information, see the function [CMGetNamedColorName](./api-1805072-cmgetnamedcolorname.md).
- [kCMMMatchPixMap](./cmm_function_selectors/kcmmmatchpixmap.md)
- [kCMMCheckPixMap](./cmm_function_selectors/kcmmcheckpixmap.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applicationservices/colorsync_manager/cmm_function_selectors)*