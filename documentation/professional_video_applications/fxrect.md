# FxRect

**Framework**: Professional Video Applications  
**Kind**: struct  
**Role**: Structure

A 2D axis-aligned rectangle with integer coordinates.

**Availability**:
- FxPlug 3.1+

## Declaration

```swift
struct FxRect
```

```c
typedef struct FxRect { ... } FxRect;
```

## Topics

### Constants
- [init()](./fxrect/init%28%29.md)
- [init(left: Int32, bottom: Int32, right: Int32, top: Int32)](./fxrect/init%28left,bottom,right,top%29.md)
### Properties
- [var bottom: Int32](./fxrect/bottom.md)
  The thickness, in pixels, of the bottom-edge processing region of the `edgeWidths` property.
- [var left: Int32](./fxrect/left.md)
  The thickness, in pixels, of the left-edge processing region of the `edgeWidths` property.
- [var right: Int32](./fxrect/right.md)
  The thickness, in pixels, of the right-edge processing region of the `edgeWidths` property.
- [var top: Int32](./fxrect/top.md)
  The thickness, in pixels, of the top-edge processing region of the `edgeWidths` property.

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
- [struct FxPoint3D](./fxpoint3d.md)
  A 3D point representation
- [typealias FxQuality](./fxquality.md)
  Constants used to identify rendering quality.
- [typealias FxSize](./fxsize.md)
  A structure to store width and height values.
- [typealias FxDrawingCoordinates](./fxdrawingcoordinates.md)
  Constants used to identify coordinate spaces.
- [typealias FxError](./fxerror.md)
  Errors returned by plug-in hosts applications.
- [typealias FxImageColorInfo](./fximagecolorinfo.md)
  Identifies some color properties of an FxImage instance. These include the color space, gamma level, and, in the case of `YCbCr` images, the color matrix for conversion to RGB.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxrect)*