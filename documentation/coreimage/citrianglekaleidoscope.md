# CITriangleKaleidoscope

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a triangle kaleidoscope filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CITriangleKaleidoscope
```

## Topics

### Instance Properties
- [var decay: Float](citrianglekaleidoscope/3228803-decay.md)
  A value that determines how fast the color fades from the center triangle.
- [var inputImage: CIImage?](citrianglekaleidoscope/3228804-inputimage.md)
  The image to use as an input image.
- [var point: CGPoint](citrianglekaleidoscope/3228805-point.md)
  The x and y position to use as the center of the triangular area in the input image.
- [var rotation: Float](citrianglekaleidoscope/3228806-rotation.md)
  The rotation angle of the triangle.
- [var size: Float](citrianglekaleidoscope/3228807-size.md)
  The size, in pixels, of the triangle.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func triangleKaleidoscope() -> any CIFilter & CITriangleKaleidoscope](cifilter/3228425-trianglekaleidoscope.md)
  Create a triangular kaleidoscope effect and then tiles the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/citrianglekaleidoscope)*