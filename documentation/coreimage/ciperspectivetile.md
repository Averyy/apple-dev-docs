# CIPerspectiveTile

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a perspective tile filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIPerspectiveTile
```

## Topics

### Instance Properties
- [var bottomLeft: CGPoint](ciperspectivetile/3228653-bottomleft.md)
  The bottom-left coordinate of a tile.
- [var bottomRight: CGPoint](ciperspectivetile/3228654-bottomright.md)
  The bottom-right coordinate of a tile.
- [var inputImage: CIImage?](ciperspectivetile/3228655-inputimage.md)
  The image to use as an input image.
- [var topLeft: CGPoint](ciperspectivetile/3228656-topleft.md)
  The top-left coordinate of a tile.
- [var topRight: CGPoint](ciperspectivetile/3228657-topright.md)
  The top-right coordinate of a tile.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func perspectiveTile() -> any CIFilter & CIPerspectiveTile](cifilter/3228381-perspectivetile.md)
  Tiles an image by adjusting the perspective of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciperspectivetile)*