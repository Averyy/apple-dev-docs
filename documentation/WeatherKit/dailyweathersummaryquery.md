# DailyWeatherSummaryQuery

**Framework**: Weatherkit  
**Kind**: struct

A structure that encapsulates a generic daily weather summary dataset request.

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
struct DailyWeatherSummaryQuery<T> where T : Decodable, T : Encodable, T : Equatable
```

#### Overview

Use the properties of this structure to create a daily weather summary query. You can combine multiple queries into a single `WeatherService` request.

Here’s how to get a daily weather summary for New York City:

```swift
let (dailyPrecipitationSummary, dailyTemperatureSummary) = try await service.dailySummary(for: newYork, spanning: timeInterval, including: .precipitation, .temperature)
```

## Topics

### Type Properties
- [static var precipitation: DailyWeatherSummaryQuery<DayPrecipitationSummary>](dailyweathersummaryquery/precipitation.md)
  The daily precipitation summary query.
- [static var temperature: DailyWeatherSummaryQuery<DayTemperatureSummary>](dailyweathersummaryquery/temperature.md)
  The daily temperature summary query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/dailyweathersummaryquery)*