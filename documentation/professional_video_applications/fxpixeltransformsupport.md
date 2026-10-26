# FxPixelTransformSupport

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

Constants that define the support for pixel transforms.

**Availability**:
- FxPlug 3.1+ - Deprecated in 4.0

> **Deprecated**: FxPlug 4 must support pixel transforms.

## Declaration

```swift
typealias FxPixelTransformSupport = Int
```

```c
typedef NSUInteger FxPixelTransformSupport;
```

## Topics

### Constants
- [var kFxPixelTransform_Scale: Int](./kfxpixeltransform_scale.md)
  Handles only (non-uniform) scaling - this is the minimum required.
- [var kFxPixelTransform_ScaleTranslate: Int](./kfxpixeltransform_scaletranslate.md)
  Handles non-uniform scaling, and arbitrary translation.
- [var kFxPixelTransform_Full: Int](./kfxpixeltransform_full.md)
  Handles full perspective transformation.

## See Also

### Data Types
- [typealias FxImageOrigin](./fximageorigin.md)
  These constants define the orientation of an image’s coordinate system. Images in Motion have a bottom-left origin. Images in Final Cut have a top-left origin.
- [typealias FxPathStyle](./fxpathstyle.md)
  The style of the path, which is linear, bezier, or b-spline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxpixeltransformsupport)*