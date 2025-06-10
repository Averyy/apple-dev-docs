# HourlyWeatherStatisticsQuery

**Framework**: WeatherKit  
**Kind**: struct

A structure that encapsulates a generic hourly weather statistics dataset request.

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
struct HourlyWeatherStatisticsQuery<T> where T : Decodable, T : Encodable, T : Equatable, T : Sendable
```

#### Overview

Use the properties of this structure to create an hourly weather statistics query. You can combine multiple queries into a single `WeatherService` request.

Here’s how to get hourly weather statistics for New York City:

```None
let (hourlyTemperatureStatistics) = try await service.hourlyStatistics(for: newYork, spanning: timeInterval, including: .temperature)
```

## Topics

### Type Properties
- [static var temperature: HourlyWeatherStatisticsQuery<HourTemperatureStatistics>](hourlyweatherstatisticsquery/temperature.md)
  The hourly temperature statistics query.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/hourlyweatherstatisticsquery)*