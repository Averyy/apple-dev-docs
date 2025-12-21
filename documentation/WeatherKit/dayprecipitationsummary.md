# DayPrecipitationSummary

**Framework**: WeatherKit  
**Kind**: struct

A structure that describes the precipitation summary for a day.

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
struct DayPrecipitationSummary
```

## Topics

### Instance Properties
- [var date: Date](dayprecipitationsummary/date.md)
  The day of the observed precipitation summary
- [var precipitationAmount: Measurement<UnitLength>](dayprecipitationsummary/precipitationamount.md)
  The amount of liquid precipitation for the day.
- [var snowfallAmount: Measurement<UnitLength>](dayprecipitationsummary/snowfallamount.md)
  The snowfall amount as depth of snow crystals for the day.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dayprecipitationsummary)*