# VTInt32Size

**Framework**: Video Toolbox  
**Kind**: struct

A structure that represents a 32-bit integer size value.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 10.2+
- visionOS 1.0+

## Declaration

```swift
struct VTInt32Size
```

#### Overview

Use this structure to represent a size with a particular width and height.

## Topics

### Creating a Size
- [init()](vtint32size/init.md)
  Creates a size with a width and height of zero.
- [init(width: Int32, height: Int32)](vtint32size/init(width:height:).md)
  Creates a size with a width and height.
### Accessing the Dimensions
- [var width: Int32](vtint32size/width.md)
  The width of the size.
- [var height: Int32](vtint32size/height.md)
  The height of the size.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [VTSession](vtsession-api-collection.md)
  An abstract object that provides the common interface to configure VideoToolbox session objects.
- [struct VTInt32Point](vtint32point.md)
  A structure that represents a 32-bit integer point value.
- [var VT_SUPPORT_COLORSYNC_PIXEL_TRANSFER: Bool](vt_support_colorsync_pixel_transfer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/videotoolbox/vtint32size)*