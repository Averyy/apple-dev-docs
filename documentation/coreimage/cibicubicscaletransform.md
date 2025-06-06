# CIBicubicScaleTransform

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a bicubic scale transform filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIBicubicScaleTransform
```

## Topics

### Instance Properties
- [var aspectRatio: Float](cibicubicscaletransform/3228074-aspectratio.md)
  The additional horizontal scaling factor to use on the image.
- [var inputImage: CIImage?](cibicubicscaletransform/3228075-inputimage.md)
  The image to use as an input image.
- [var parameterB: Float](cibicubicscaletransform/3228076-parameterb.md)
  The value of B to use for the cubic resampling function.
- [var parameterC: Float](cibicubicscaletransform/3228077-parameterc.md)
  The value of C to use for the cubic resampling function.
- [var scale: Float](cibicubicscaletransform/3228078-scale.md)
  The scaling factor to use on the image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func bicubicScaleTransform() -> any CIFilter & CIBicubicScaleTransform](cifilter/3228271-bicubicscaletransform.md)
  Produces a high-quality scaled version of an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cibicubicscaletransform)*