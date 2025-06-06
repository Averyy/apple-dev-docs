# CIExposureAdjust

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure an exposure adjust filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIExposureAdjust
```

## Topics

### Instance Properties
- [var ev: Float](ciexposureadjust/3228253-ev.md)
  The amount to adjust the exposure of the image by.
- [var inputImage: CIImage?](ciexposureadjust/3228254-inputimage.md)
  The image to use as an input image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func exposureAdjust() -> any CIFilter & CIExposureAdjust](cifilter/3228324-exposureadjust.md)
  Adjusts an image’s exposure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciexposureadjust)*