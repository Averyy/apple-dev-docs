# FxField

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

Constants used to identify a field.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
typealias FxField = Int
```

```c
typedef NSUInteger FxField;
```

## Discussion

Prior to FxPlug 1.2, this type was used to identify field order. As of FxPlug 1.2, it is used to identify the field of an image.

## Topics

### Constants
- [var kFxField_NONE: Int](./kfxfield_none.md)
  Full frame, progressive (no fields).
- [var kFxField_UPPER: Int](./kfxfield_upper.md)
  Upper field.
- [var kFxField_LOWER: Int](./kfxfield_lower.md)
  Lower field.

## See Also

### Data types
- [typealias FxDepth](./fxdepth.md)
  Constants used to identify bit depth.
- [typealias FxFieldOrder](./fxfieldorder.md)
  Constants used to identify the field order of an image stream.
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

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxfield)*