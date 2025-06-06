# CIColorMap

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a color map filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIColorMap
```

## Topics

### Instance Properties
- [var gradientImage: CIImage?](cicolormap/3228157-gradientimage.md)
  The image data that transforms the source image values.
- [var inputImage: CIImage?](cicolormap/3228158-inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func colorMap() -> any CIFilter & CIColorMap](cifilter/3228293-colormap.md)
  Performs a transformation of the input image colors to colors from a gradient image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicolormap)*