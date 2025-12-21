# CIConvolution

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a convolution filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIConvolution : CIFilterProtocol
```

## Topics

### Instance Properties
- [var bias: Float](ciconvolution/bias.md)
  A value that’s added to each output pixel.
- [var inputImage: CIImage?](ciconvolution/inputimage.md)
  The image to use as an input image.
- [var weights: CIVector](ciconvolution/weights.md)
  The convolution kernel.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func convolution3X3() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution3x3.md)
  Applies a convolution 3 x 3 filter to the `RGBA` components of an image.
- [class func convolution5X5() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution5x5.md)
  Applies a convolution 5 x 5 filter to the `RGBA` components image.
- [class func convolution7X7() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution7x7.md)
  Applies a convolution 7 x 7 filter to the `RGBA` color components of an image.
- [class func convolution9Horizontal() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution9horizontal.md)
  Applies a convolution-9 horizontal filter to the `RGBA` components of an image.
- [class func convolution9Vertical() -> any CIFilter & CIConvolution](cifilter-swift.class/convolution9vertical.md)
  Applies a convolution-9 vertical filter to the `RGBA` components of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciconvolution)*