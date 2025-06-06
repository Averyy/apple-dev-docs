# CIPaletteCentroid

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a palette centroid filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIPaletteCentroid
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cipalettecentroid/3228632-inputimage.md)
  The image to use as an input image.
- [var paletteImage: CIImage?](cipalettecentroid/3228633-paletteimage.md)
  The input color palette, obtained by using a k-means clustering filter.
- [var perceptual: Bool](cipalettecentroid/3228634-perceptual.md)
  A Boolean value that specifies whether the filter applies the color palette in a perceptual color space.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func paletteCentroid() -> any CIFilter & CIPaletteCentroid](cifilter/3228377-palettecentroid.md)
  Calculates the location of an image’s colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipalettecentroid)*