# FxPathStyle

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

The style of the path, which is linear, bezier, or b-spline.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
typealias FxPathStyle = Int
```

```c
typedef NSUInteger FxPathStyle;
```

## Discussion

This is used by the `styleOfPath:error:` method and the [`FxVertex`](./fxvertex.md) structure.

## Topics

### Constants
- [var kFxPathStyle_Linear: Int](./kfxpathstyle_linear.md)
  The path is linear style.
- [var kFxPathStyle_Bezier: Int](./kfxpathstyle_bezier.md)
  The path is bezier style.
- [var kFxPathStyle_XSpline: Int](./kfxpathstyle_xspline.md)
  The path is b-spline style.

## See Also

### Data Types
- [typealias FxImageOrigin](./fximageorigin.md)
  These constants define the orientation of an image’s coordinate system. Images in Motion have a bottom-left origin. Images in Final Cut have a top-left origin.
- [typealias FxPixelTransformSupport](./fxpixeltransformsupport.md)
  Constants that define the support for pixel transforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxpathstyle)*