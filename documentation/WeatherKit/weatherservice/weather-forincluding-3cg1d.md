# weather(for:including:)

**Framework**: Weatherkit  
**Kind**: method

Returns the weather forecast for the requested location.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
final func weather<T>(for location: CLLocation, including dataSet: WeatherQuery<T>) async throws -> T
```

#### Return Value

The requested weather data set.

#### Discussion

> **Note**: Weather data error `WeatherError`

This is a variadic API in which any combination of data sets can be requested and returned as a tuple. Here’s an example:

```None
let current = try await service.weather(for: newYork, including: .current)
```

## Parameters

- `location`: The requested location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherservice/weather(for:including:)-3cg1d)*