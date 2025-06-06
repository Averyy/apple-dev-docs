# CIFourfoldRotatedTile

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a fourfold rotated tile filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIFourfoldRotatedTile
```

## Topics

### Instance Properties
- [var angle: Float](cifourfoldrotatedtile/3228450-angle.md)
  The angle, in radians, of the tiled pattern.
- [var center: CGPoint](cifourfoldrotatedtile/3228451-center.md)
  The x and y position to use as the center of the effect.
- [var inputImage: CIImage?](cifourfoldrotatedtile/3228452-inputimage.md)
  The image to use as an input image.
- [var width: Float](cifourfoldrotatedtile/3228453-width.md)
  The width of a tile.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func fourfoldRotatedTile() -> any CIFilter & CIFourfoldRotatedTile](cifilter/3228328-fourfoldrotatedtile.md)
  Creates a tiled image by rotating a tile in increments of 90 degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifourfoldrotatedtile)*