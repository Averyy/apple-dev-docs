# CITriangleTile

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a triangle tile filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CITriangleTile
```

## Topics

### Instance Properties
- [var angle: Float](citriangletile/3228809-angle.md)
  The angle, in radians, of the tiled pattern.
- [var center: CGPoint](citriangletile/3228810-center.md)
  The x and y position to use as the center of the effect.
- [var inputImage: CIImage?](citriangletile/3228811-inputimage.md)
  The image to use as an input image.
- [var width: Float](citriangletile/3228812-width.md)
  The width of a tile.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func triangleTile() -> any CIFilter & CITriangleTile](cifilter/3228426-triangletile.md)
  Tiles a triangular area of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/citriangletile)*