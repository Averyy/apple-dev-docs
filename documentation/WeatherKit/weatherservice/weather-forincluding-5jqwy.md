# weather(for:including:)

**Framework**: Weatherkit  
**Kind**: method

Returns the weather forecast for the requested location.

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
final func weather<each T>(for location: CLLocation, including dataSet: repeat WeatherQuery<each T>) async throws -> (repeat each T)
```

#### Return Value

The requested weather data set.

#### Discussion

> **Note**: Weather data error `WeatherError`

Weather data error `WeatherError`

This is a variadic API in which any combination of data sets can be requested and returned as a tuple. Here’s an example:

```None
`let (current, minute, hourly, daily, alerts) = try await service.weather(for: newYork, including: .current, .minute, .hourly, .daily, .alerts)`
```

## Parameters

- `location`: The requested location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherservice/weather(for:including:)-5jqwy)*