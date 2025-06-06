# CISixfoldReflectedTile

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a sixfold reflected tile filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CISixfoldReflectedTile
```

## Topics

### Instance Properties
- [var angle: Float](cisixfoldreflectedtile/3228713-angle.md)
  The angle, in radians, of the tiled pattern.
- [var center: CGPoint](cisixfoldreflectedtile/3228714-center.md)
  The x and y position to use as the center of the effect.
- [var inputImage: CIImage?](cisixfoldreflectedtile/3228715-inputimage.md)
  The image to use as an input image.
- [var width: Float](cisixfoldreflectedtile/3228716-width.md)
  The width of a tile.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func sixfoldReflectedTile() -> any CIFilter & CISixfoldReflectedTile](cifilter/3228405-sixfoldreflectedtile.md)
  Produces a tiled image from a source image by applying a six-way reflected symmetry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cisixfoldreflectedtile)*