# PrecipitationAmountByType

**Framework**: Weatherkit  
**Kind**: struct

A structure that provides a breakdown of amounts of all forms of precipitation that is expected to occur over a period of time.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct PrecipitationAmountByType
```

## Topics

### Operators
- [static func == (PrecipitationAmountByType, PrecipitationAmountByType) -> Bool](precipitationamountbytype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](precipitationamountbytype/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hail: Measurement<UnitLength>](precipitationamountbytype/hail.md)
  The amount of hail for the period.
- [var mixed: Measurement<UnitLength>](precipitationamountbytype/mixed.md)
  The amount of wintry mix for the period.
- [var precipitation: Measurement<UnitLength>](precipitationamountbytype/precipitation.md)
  The amount of liquid equivalent of all precipitation for the period.
- [var rainfall: Measurement<UnitLength>](precipitationamountbytype/rainfall.md)
  The amount of rainfall for the period.
- [var sleet: Measurement<UnitLength>](precipitationamountbytype/sleet.md)
  The amount of sleet for the period.
- [var snowfallAmount: SnowfallAmount](precipitationamountbytype/snowfallamount.md)
  Describes the amount of snowfall for the period.
### Instance Methods
- [func encode(to: any Encoder) throws](precipitationamountbytype/encode(to:).md)
  Encodes this value into the given encoder.
### Default Implementations
- [Equatable Implementations](precipitationamountbytype/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/precipitationamountbytype)*