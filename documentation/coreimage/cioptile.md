# CIOpTile

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure an optical tile filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIOpTile
```

## Topics

### Instance Properties
- [var angle: Float](cioptile/3228599-angle.md)
  The angle of a tile.
- [var center: CGPoint](cioptile/3228600-center.md)
  The x and y position to use as the center of the effect.
- [var inputImage: CIImage?](cioptile/3228601-inputimage.md)
  The image to use as an input image.
- [var scale: Float](cioptile/3228602-scale.md)
  A value that determines the number of tiles in the effect.
- [var width: Float](cioptile/3228603-width.md)
  The width of a tile.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func opTile() -> any CIFilter & CIOpTile](cifilter/3228373-optile.md)
  Produces an effect that mimics a style of visual art that uses optical illusions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cioptile)*