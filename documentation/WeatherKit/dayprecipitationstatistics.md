# DayPrecipitationStatistics

**Framework**: WeatherKit  
**Kind**: struct

A structure that describes precipitation statistics for a day.

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
struct DayPrecipitationStatistics
```

## Topics

### Instance Properties
- [var averagePrecipitationAmount: Measurement<UnitLength>](dayprecipitationstatistics/averageprecipitationamount.md)
  The average amount of liquid precipitation for the day.
- [var averagePrecipitationProbability: Double](dayprecipitationstatistics/averageprecipitationprobability.md)
  The average percentage probability of precipitation (0.0 = 0%, 1.0 = 100%) for the day.
- [var averageSnowfallAmount: Measurement<UnitLength>](dayprecipitationstatistics/averagesnowfallamount.md)
  The average amount of snowfall as depth of snow crystals for the day.
- [var day: Int](dayprecipitationstatistics/day.md)
  The day of the year, in UTC.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dayprecipitationstatistics)*