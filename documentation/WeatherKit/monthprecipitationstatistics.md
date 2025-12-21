# MonthPrecipitationStatistics

**Framework**: WeatherKit  
**Kind**: struct

A structure that describes precipitation statistics for a specific month.

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
struct MonthPrecipitationStatistics
```

## Topics

### Instance Properties
- [var averagePrecipitationAmount: Measurement<UnitLength>](monthprecipitationstatistics/averageprecipitationamount.md)
  The average amount of liquid precipitation for the month.
- [var averagePrecipitationProbability: Double](monthprecipitationstatistics/averageprecipitationprobability.md)
  The average percentage probability of precipitation (0.0 = 0%, 1.0 = 100%) for the month.
- [var averageSnowfallAmount: Measurement<UnitLength>](monthprecipitationstatistics/averagesnowfallamount.md)
  The average amount of snowfall as depth of snow crystals for the month.
- [var month: Int](monthprecipitationstatistics/month.md)
  The month of the year, in UTC.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/monthprecipitationstatistics)*