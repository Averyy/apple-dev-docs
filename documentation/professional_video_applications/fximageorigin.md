# FxImageOrigin

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

These constants define the orientation of an image’s coordinate system. Images in Motion have a bottom-left origin. Images in Final Cut have a top-left origin.

**Availability**:
- FxPlug 3.1+ - Deprecated in 4.0

> **Deprecated**: Not supported in FxPlug 4. Use [`FxImageTile`](./fximagetile.md).

## Declaration

```swift
typealias FxImageOrigin = Int
```

```c
typedef NSUInteger FxImageOrigin;
```

#### Discussion

This method was introduced in FxImage class 0.0.

## Topics

### Constants
- [var kFxImageOrigin_BOTTOM_LEFT: Int](./kfximageorigin_bottom_left.md)
  Right-handed “bottom-up” coordinate system where Y values increase upwardly.
- [var kFxImageOrigin_TOP_LEFT: Int](./kfximageorigin_top_left.md)
  Left-handed “top-down” coordinate system where Y values increase downwardly.

## See Also

### Data Types
- [typealias FxPathStyle](./fxpathstyle.md)
  The style of the path, which is linear, bezier, or b-spline.
- [typealias FxPixelTransformSupport](./fxpixeltransformsupport.md)
  Constants that define the support for pixel transforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fximageorigin)*