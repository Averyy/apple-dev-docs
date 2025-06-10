# DailyWeatherStatisticsQuery

**Framework**: WeatherKit  
**Kind**: struct

A structure that encapsulates a generic daily weather statistics dataset request.

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
struct DailyWeatherStatisticsQuery<T> where T : Decodable, T : Encodable, T : Equatable, T : Sendable
```

#### Overview

Use the properties of this structure to create a daily weather statistics query. You can combine multiple queries into a single `WeatherService` request.

Here’s how to get daily weather statistics for New York City:

```swift
let (dailyPrecipitationStatistics, dailyTemperatureStatistics) = try await service.dailyStatistics(for: newYork, spanning: timeInterval, including: .precipitation, .temperature)
```

## Topics

### Type Properties
- [static var precipitation: DailyWeatherStatisticsQuery<DayPrecipitationStatistics>](dailyweatherstatisticsquery/precipitation.md)
  The daily precipitation statistics query.
- [static var temperature: DailyWeatherStatisticsQuery<DayTemperatureStatistics>](dailyweatherstatisticsquery/temperature.md)
  The daily temperature statistics query.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dailyweatherstatisticsquery)*