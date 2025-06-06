# CISixfoldRotatedTile

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a sixfold rotated tile filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CISixfoldRotatedTile
```

## Topics

### Instance Properties
- [var angle: Float](cisixfoldrotatedtile/3228718-angle.md)
  The angle, in radians, of the tiled pattern.
- [var center: CGPoint](cisixfoldrotatedtile/3228719-center.md)
  The x and y position to use as the center of the effect.
- [var inputImage: CIImage?](cisixfoldrotatedtile/3228720-inputimage.md)
  The image to use as an input image.
- [var width: Float](cisixfoldrotatedtile/3228721-width.md)
  The width of a tile.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func sixfoldRotatedTile() -> any CIFilter & CISixfoldRotatedTile](cifilter/3228406-sixfoldrotatedtile.md)
  Creates a tiled image by rotating in increments of 60 degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisixfoldrotatedtile)*