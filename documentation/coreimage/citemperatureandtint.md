# CITemperatureAndTint

**Framework**: Core Image  
**Kind**: intf

The properties you use to configure a temperature and tint filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
protocol CITemperatureAndTint
```

## Topics

### Instance Properties
- [var inputImage: CIImage?](citemperatureandtint/3228781-inputimage.md)
  The image to use as an input image.
- [var neutral: CIVector](citemperatureandtint/3228782-neutral.md)
  A vector containing the source white point defined by color temperature and tint.
- [var targetNeutral: CIVector](citemperatureandtint/3228783-targetneutral.md)
  A vector containing the desired white point defined by color temperature and tint.

## Relationships

### Inherits From
- [CIFilterProtocol](cifilterprotocol.md)

## See Also

- [class func temperatureAndTint() -> any CIFilter & CITemperatureAndTint](cifilter/3228421-temperatureandtint.md)
  Alters an image’s temperature and tint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/citemperatureandtint)*