# CILanczosScaleTransform

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a Lanczos scale transform filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CILanczosScaleTransform
```

## Topics

### Instance Properties
- [var aspectRatio: Float](cilanczosscaletransform/3228516-aspectratio.md)
  The additional horizontal scaling factor to use on the image.
- [var inputImage: CIImage?](cilanczosscaletransform/3228517-inputimage.md)
  The image to use as an input image.
- [var scale: Float](cilanczosscaletransform/3228518-scale.md)
  The scaling factor to use on the image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func lanczosScaleTransform() -> any CIFilter & CILanczosScaleTransform](cifilter/3228344-lanczosscaletransform.md)
  Creates a high-quality, scaled version of a source image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cilanczosscaletransform)*