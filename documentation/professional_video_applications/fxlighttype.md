# FxLightType

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

The type of lighting.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
typealias FxLightType = Int
```

```c
typedef NSUInteger FxLightType;
```

## Topics

### Constants
- [var kFxLightType_Ambient: Int](./kfxlighttype_ambient.md)
  Light that illuminates all objects in the scene evenly.
- [var kFxLightType_Directional: Int](./kfxlighttype_directional.md)
  Light that comes from a particular direction, but which is infinitely far away.
- [var kFxLightType_Point: Int](./kfxlighttype_point.md)
  Light which exists at a point and illuminates in all directions.
- [var kFxLightType_Spot: Int](./kfxlighttype_spot.md)
  Light which has a limiting cone, and which can be positioned and pointed in a particular direction.

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
- [typealias FxAnalysisLocation](./fxanalysislocation.md)
  Indicates the type of hardware to use for analysis, either CPU or GPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxlighttype)*