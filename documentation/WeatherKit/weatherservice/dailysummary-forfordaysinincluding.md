# dailySummary(for:forDaysIn:including:)

**Framework**: Weatherkit  
**Kind**: method

Returns day weather summaries for the requested location, for each day within the provided date interval.

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
final func dailySummary<each T>(for location: CLLocation, forDaysIn interval: DateInterval, including dataSets: repeat DailyWeatherSummaryQuery<each T>) async throws -> (repeat DailyWeatherSummary<each T>) where repeat each T : Decodable, repeat each T : Encodable, repeat each T : Equatable, repeat each T : Sendable
```

#### Return Value

The requested day weather summaries.

#### Discussion

> **Note**: Weather data error `WeatherError`

Weather data error `WeatherError`

This is a variadic API in which any combination of data sets can be requested and returned as a tuple. The following example will get a daily weather summary for New York City.

```swift
let (dailyPrecipitationSummary, dailyTemperatureSummary) = try await service.dailySummary(for: newYork, forDaysIn: timeInterval, including: .precipitation, .temperature)
```

## Parameters

- `location`: The requested location.
- `interval`: The date interval for which to obtain day weather summaries. The end date of the interval will be capped at 1 year after the start date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherservice/dailysummary(for:fordaysin:including:))*