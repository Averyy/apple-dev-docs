# FxFieldOrder

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

Constants used to identify the field order of an image stream.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
typealias FxFieldOrder = Int
```

```c
typedef NSUInteger FxFieldOrder;
```

## Topics

### Constants
- [var kFxFieldOrder_PROGRESSIVE: Int](./kfxfieldorder_progressive.md)
  Full frame, progressive (no fields).
- [var kFxFieldOrder_UPPER_FIRST: Int](./kfxfieldorder_upper_first.md)
  Upper field first.
- [var kFxFieldOrder_LOWER_FIRST: Int](./kfxfieldorder_lower_first.md)
  Lower field first.

## See Also

### Data types
- [typealias FxDepth](./fxdepth.md)
  Constants used to identify bit depth.
- [typealias FxField](./fxfield.md)
  Constants used to identify a field.
- [typealias FxPoint2D](./fxpoint2d.md)
  A 2D point representation.
- [struct FxPoint3D](./fxpoint3d.md)
  A 3D point representation
- [typealias FxQuality](./fxquality.md)
  Constants used to identify rendering quality.
- [struct FxRect](./fxrect.md)
  A 2D axis-aligned rectangle with integer coordinates.
- [typealias FxSize](./fxsize.md)
  A structure to store width and height values.
- [typealias FxDrawingCoordinates](./fxdrawingcoordinates.md)
  Constants used to identify coordinate spaces.
- [typealias FxError](./fxerror.md)
  Errors returned by plug-in hosts applications.
- [typealias FxImageColorInfo](./fximagecolorinfo.md)
  Identifies some color properties of an FxImage instance. These include the color space, gamma level, and, in the case of `YCbCr` images, the color matrix for conversion to RGB.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxfieldorder)*