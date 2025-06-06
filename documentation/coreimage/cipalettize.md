# CIPalettize

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a palettize filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIPalettize
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cipalettize/3228636-inputimage.md)
  The image to use as an input image.
- [var paletteImage: CIImage?](cipalettize/3228637-paletteimage.md)
  The input color palette, obtained by using a k-means clustering filter.
- [var perceptual: Bool](cipalettize/3228638-perceptual.md)
  A Boolean value that specifies whether the filter applies the color palette in a perceptual color space.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func palettize() -> any CIFilter & CIPalettize](cifilter/3228378-palettize.md)
  Replaces colors with colors from a palette image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cipalettize)*