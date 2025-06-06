# CIGammaAdjust

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a gamma adjust filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CIGammaAdjust
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](cigammaadjust/3228461-inputimage.md)
  The image to use as an input image.
- [var power: Float](cigammaadjust/3228462-power.md)
  A gamma value to use to correct image brightness.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func gammaAdjust() -> any CIFilter & CIGammaAdjust](cifilter/3228330-gammaadjust.md)
  Alters an image’s transition between black and white.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cigammaadjust)*