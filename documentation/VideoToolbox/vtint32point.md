# VTInt32Point

**Framework**: Video Toolbox  
**Kind**: struct

A structure that represents a 32-bit integer point value.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
struct VTInt32Point
```

#### Overview

Use this structure to represent a point at an (x, y) location.

## Topics

### Creating a Point
- [init()](vtint32point/init.md)
  Creates a size with coordinates equal to zero.
- [init(x: Int32, y: Int32)](vtint32point/init(x:y:).md)
  Creates a point with coordinates specified as integer values.
### Accessing the Coordinates
- [var x: Int32](vtint32point/x.md)
  The x-coordinate of the point.
- [var y: Int32](vtint32point/y.md)
  The y-coordinate of the point.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [VTSession](vtsession-api-collection.md)
  An abstract object that provides the common interface to configure VideoToolbox session objects.
- [struct VTInt32Size](vtint32size.md)
  A structure that represents a 32-bit integer size value.
- [var VT_SUPPORT_COLORSYNC_PIXEL_TRANSFER: Bool](vt_support_colorsync_pixel_transfer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtint32point)*