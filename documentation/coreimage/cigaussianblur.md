# CIGaussianBlur

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a Gaussian blur filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIGaussianBlur
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cigaussianblur/3228464-inputimage.md)
  The image to use as an input image.
- [var radius: Float](cigaussianblur/3228465-radius.md)
  The radius of the blur, in pixels.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func gaussianBlur() -> any CIFilter & CIGaussianBlur](cifilter/3228331-gaussianblur.md)
  Blurs an image with a Gaussian distribution pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cigaussianblur)*