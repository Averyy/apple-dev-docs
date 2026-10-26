# FxPoint3D

**Framework**: Professional Video Applications  
**Kind**: struct  
**Role**: Structure

A 3D point representation

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
struct FxPoint3D
```

```c
typedef struct FxPoint3D { ... } FxPoint3D;
```

## Topics

### Constants
- [init()](./fxpoint3d/init%28%29.md)
- [init(x: CGFloat, y: CGFloat, z: CGFloat)](./fxpoint3d/init%28x,y,z%29.md)
### Instance Properties
- [var x: CGFloat](./fxpoint3d/x.md)
  The value for the X-axis.
- [var y: CGFloat](./fxpoint3d/y.md)
  The value for the Y-axis.
- [var z: CGFloat](./fxpoint3d/z.md)
  The value for the Z-axis.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Data types
- [typealias FxDepth](./fxdepth.md)
  Constants used to identify bit depth.
- [typealias FxField](./fxfield.md)
  Constants used to identify a field.
- [typealias FxFieldOrder](./fxfieldorder.md)
  Constants used to identify the field order of an image stream.
- [typealias FxPoint2D](./fxpoint2d.md)
  A 2D point representation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxpoint3d)*