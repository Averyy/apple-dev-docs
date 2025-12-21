# WeatherChange

**Framework**: WeatherKit  
**Kind**: struct

A structure that informs how certain measurable weather aspects are expected to change relative to before.

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
struct WeatherChange
```

## Topics

### Instance Properties
- [var date: Date](weatherchange/date.md)
  The date at which this change record becomes effective.
- [var dayPrecipitationAmount: WeatherChange.Direction](weatherchange/dayprecipitationamount.md)
  How the forecasted precipitation amount for this day, during daylight hours, compares to that of before.
- [var highTemperature: WeatherChange.Direction](weatherchange/hightemperature.md)
  How the high temperature for this day compares to that of before.
- [var lowTemperature: WeatherChange.Direction](weatherchange/lowtemperature.md)
  How the low temperature for this day compares to that of before.
- [var nightPrecipitationAmount: WeatherChange.Direction](weatherchange/nightprecipitationamount.md)
  How the forecasted precipitation amount, during the night of this day, compares to that of before.
### Enumerations
- [WeatherChange.Direction](weatherchange/direction.md)
  An enum that specifies the direction in which a measurable aspect of the weather is expected to change.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherchange)*