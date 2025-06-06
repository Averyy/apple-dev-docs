# hourlyStatistics(for:startHour:endHour:including:)

**Framework**: Weatherkit  
**Kind**: method

Returns hourly weather statistics for the requested location, for each hour from the start hour to the end hour, inclusively.

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
final func hourlyStatistics<each T>(for location: CLLocation, startHour: Int, endHour: Int, including dataSets: repeat HourlyWeatherStatisticsQuery<each T>) async throws -> (repeat HourlyWeatherStatistics<each T>) where repeat each T : Decodable, repeat each T : Encodable, repeat each T : Equatable, repeat each T : Sendable
```

#### Return Value

The requested hourly weather statistics.

#### Discussion

> **Note**: Weather data error `WeatherError`

The statistics returned for each hour are derived from weather data recorded over the past decades, to the present date. Each item returned represents statistics for a particular hour of the year, in UTC.

This is a variadic API in which any combination of data sets can be requested and returned as a tuple. The following example will return statistics for the first 24 hours of the year.

```swift
let hourlyTemperatureStatistics = try await service.hourlyStatistics(for: newYork, startHour: 1, endHour: 24, including: .temperature)
```

If the start hour is greater than the end hour, then a wrap around will occur. This next example will return statistics for hours 8783, 8784, 1, and 2.

```swift
let hourlyTemperatureStatistics = try await service.hourlyStatistics(for: newYork, startHour: 8783, endHour: 2, including: .temperature)
```

> **Note**: `startHour in 1...8784 && endHour in 1...8784`

## Parameters

- `location`: The requested location.
- `startHour`: The first hour of the span, between 1 and 8784.
- `endHour`: The last hour of the span, between 1 and 8784.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherservice/hourlystatistics(for:starthour:endhour:including:))*