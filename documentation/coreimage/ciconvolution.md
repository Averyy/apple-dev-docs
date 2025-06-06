# CIConvolution

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a convolution filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIConvolution
```

## Topics

### Instance Properties
- [var bias: Float](ciconvolution/3228185-bias.md)
  A value that’s added to each output pixel.
- [var inputImage: CIImage?](ciconvolution/3228186-inputimage.md)
  The image to use as an input image.
- [var weights: CIVector](ciconvolution/3228187-weights.md)
  The convolution kernel.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func convolution3X3() -> any CIFilter & CIConvolution](cifilter/3228299-convolution3x3.md)
  Applies a convolution 3 x 3 filter to the `RGBA` components of an image.
- [class func convolution5X5() -> any CIFilter & CIConvolution](cifilter/3228300-convolution5x5.md)
  Applies a convolution 5 x 5 filter to the `RGBA` components image.
- [class func convolution7X7() -> any CIFilter & CIConvolution](cifilter/3228301-convolution7x7.md)
  Applies a convolution 7 x 7 filter to the `RGBA` color components of an image.
- [class func convolution9Horizontal() -> any CIFilter & CIConvolution](cifilter/3228302-convolution9horizontal.md)
  Applies a convolution-9 horizontal filter to the `RGBA` components of an image.
- [class func convolution9Vertical() -> any CIFilter & CIConvolution](cifilter/3228303-convolution9vertical.md)
  Applies a convolution-9 vertical filter to the `RGBA` components of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciconvolution)*