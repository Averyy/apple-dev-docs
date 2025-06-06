# CIGlideReflectedTile

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a glide reflected tile filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIGlideReflectedTile
```

## Topics

### Instance Properties
- [var angle: Float](ciglidereflectedtile/3228472-angle.md)
  The angle, in radians, of the tiled pattern.
- [var center: CGPoint](ciglidereflectedtile/3228473-center.md)
  The x and y position to use as the center of the effect.
- [var inputImage: CIImage?](ciglidereflectedtile/3228474-inputimage.md)
  The image to use as an input image.
- [var width: Float](ciglidereflectedtile/3228475-width.md)
  The width of a tile.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func glideReflectedTile() -> any CIFilter & CIGlideReflectedTile](cifilter/3228333-glidereflectedtile.md)
  Tiles an image by rotating and reflecting a tile from the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciglidereflectedtile)*