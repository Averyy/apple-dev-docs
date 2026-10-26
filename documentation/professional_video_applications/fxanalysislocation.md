# FxAnalysisLocation

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

Indicates the type of hardware to use for analysis, either CPU or GPU.

**Availability**:
- FxPlug 4.1+

## Declaration

```swift
typealias FxAnalysisLocation = Int
```

```c
typedef NSInteger FxAnalysisLocation;
```

## Topics

### Constants
- [var kFxAnalysisLocation_CPU: FxAnalysisLocation](./kfxanalysislocation_cpu.md)
  Use a bitmap in main memory for analysis images.
- [var kFxAnalysisLocation_GPU: FxAnalysisLocation](./kfxanalysislocation_gpu.md)
  Use a texture on the GPU for analysis images.

## See Also

### Enumerations
- [typealias FxImageColorInfo](./fximagecolorinfo.md)
  Identifies some color properties of an FxImage instance. These include the color space, gamma level, and, in the case of `YCbCr` images, the color matrix for conversion to RGB.
- [typealias FxPixelTransformSupport](./fxpixeltransformsupport.md)
  Constants that define the support for pixel transforms.
- [typealias FxImageOrigin](./fximageorigin.md)
  These constants define the orientation of an image’s coordinate system. Images in Motion have a bottom-left origin. Images in Final Cut have a top-left origin.
- [typealias FxModifierKeys](./fxmodifierkeys.md)
  Specifies flags that identify modifier keys held down while an event is generated.
- [typealias FxLightType](./fxlighttype.md)
  The type of lighting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxanalysislocation)*