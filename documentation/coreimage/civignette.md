# CIVignette

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a vignette filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIVignette
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](civignette/3228826-inputimage.md)
  The image to use as an input image.
- [var intensity: Float](civignette/3228827-intensity.md)
  The intensity of the effect.
- [var radius: Float](civignette/3228828-radius.md)
  The distance from the center of the effect.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func vignette() -> any CIFilter & CIVignette](cifilter/3228431-vignette.md)
  Gradually darkens an image’s edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/civignette)*