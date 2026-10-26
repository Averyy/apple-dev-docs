# FxImageColorInfo

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

Identifies some color properties of an FxImage instance. These include the color space, gamma level, and, in the case of `YCbCr` images, the color matrix for conversion to RGB.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
typealias FxImageColorInfo = Int
```

```c
typedef NSUInteger FxImageColorInfo;
```

#### Discussion

This method was introduced in FxImage.

## Topics

### Constants
- [var kFxImageColorInfo_RGB_LINEAR: Int](./kfximagecolorinfo_rgb_linear.md)
  RGB linear (not gamma corrected).
- [var kFxImageColorInfo_RGB_GAMMA_VIDEO: Int](./kfximagecolorinfo_rgb_gamma_video.md)
  RGB at video gamma (2.2).

## See Also

### Enumerations
- [typealias FxPixelTransformSupport](./fxpixeltransformsupport.md)
  Constants that define the support for pixel transforms.
- [typealias FxImageOrigin](./fximageorigin.md)
  These constants define the orientation of an image’s coordinate system. Images in Motion have a bottom-left origin. Images in Final Cut have a top-left origin.
- [typealias FxModifierKeys](./fxmodifierkeys.md)
  Specifies flags that identify modifier keys held down while an event is generated.
- [typealias FxLightType](./fxlighttype.md)
  The type of lighting.
- [typealias FxAnalysisLocation](./fxanalysislocation.md)
  Indicates the type of hardware to use for analysis, either CPU or GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fximagecolorinfo)*