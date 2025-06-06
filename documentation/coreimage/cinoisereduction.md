# CINoiseReduction

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a noise reduction filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CINoiseReduction
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cinoisereduction/3228595-inputimage.md)
  The image to use as an input image.
- [var noiseLevel: Float](cinoisereduction/3228596-noiselevel.md)
  The amount of noise reduction.
- [var sharpness: Float](cinoisereduction/3228597-sharpness.md)
  The sharpness of the final image.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func noiseReduction() -> any CIFilter & CINoiseReduction](cifilter/3228372-noisereduction.md)
  Reduces noise by sharpening the edges of objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cinoisereduction)*