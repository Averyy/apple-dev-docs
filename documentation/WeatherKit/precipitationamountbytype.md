# PrecipitationAmountByType

**Framework**: WeatherKit  
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

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/precipitationamountbytype)*