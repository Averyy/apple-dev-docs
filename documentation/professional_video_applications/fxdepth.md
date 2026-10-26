# FxDepth

**Framework**: Professional Video Applications  
**Kind**: typealias  
**Role**: Type Alias

Constants used to identify bit depth.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
typealias FxDepth = Int
```

```c
typedef NSUInteger FxDepth;
```

## Topics

### Constants
- [var kFxDepth_UINT8: Int](./kfxdepth_uint8.md)
  Each component is an 8-bit integer.
- [var kFxDepth_FLOAT16: Int](./kfxdepth_float16.md)
  Each component is a 16-bit float.
- [var kFxDepth_FLOAT32: Int](./kfxdepth_float32.md)
  Each component is a 32-bit float.

## See Also

### Data types
- [typealias FxField](./fxfield.md)
  Constants used to identify a field.
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

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxdepth)*