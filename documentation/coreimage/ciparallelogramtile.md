# CIParallelogramTile

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a parallelogram tile filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIParallelogramTile
```

## Topics

### Instance Properties
- [var acuteAngle: Float](ciparallelogramtile/3228640-acuteangle.md)
  The primary angle for the repeating parallelogram tile.
- [var angle: Float](ciparallelogramtile/3228641-angle.md)
  The angle, in radians, of the tiled pattern.
- [var center: CGPoint](ciparallelogramtile/3228642-center.md)
  The x and y position to use as the center of the effect.
- [var inputImage: CIImage?](ciparallelogramtile/3228643-inputimage.md)
  The image to use as an input image.
- [var width: Float](ciparallelogramtile/3228644-width.md)
  The width of a tile.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func parallelogramTile() -> any CIFilter & CIParallelogramTile](cifilter/3228379-parallelogramtile.md)
  Warps the image to create a parallelogram and tiles the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciparallelogramtile)*