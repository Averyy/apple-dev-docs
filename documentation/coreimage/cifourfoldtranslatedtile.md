# CIFourfoldTranslatedTile

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a fourfold translated tile filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIFourfoldTranslatedTile
```

## Topics

### Instance Properties
- [var acuteAngle: Float](cifourfoldtranslatedtile/3228455-acuteangle.md)
  The primary angle for the repeating translated tile.
- [var angle: Float](cifourfoldtranslatedtile/3228456-angle.md)
  The angle, in radians, of the tiled pattern.
- [var center: CGPoint](cifourfoldtranslatedtile/3228457-center.md)
  The x and y position to use as the center of the effect.
- [var inputImage: CIImage?](cifourfoldtranslatedtile/3228458-inputimage.md)
  The image to use as an input image.
- [var width: Float](cifourfoldtranslatedtile/3228459-width.md)
  The width of a tile.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func fourfoldTranslatedTile() -> any CIFilter & CIFourfoldTranslatedTile](cifilter/3228329-fourfoldtranslatedtile.md)
  Creates a tiled image by applying four translation operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifourfoldtranslatedtile)*