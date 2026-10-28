# weather(for:)

**Framework**: WeatherKit  
**Kind**: method  
**Role**: Instance Method

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
final func weather(for location: CLLocation) async throws -> Weather
```

## Return Value

The aggregate weather.

## Discussion

> **Throws**: Weather data error `WeatherError`

## Parameters

- `location`: The requested location.

## See Also

### Obtaining forecasts
- [func weather<T1, T2>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>) async throws -> (T1, T2)](./weather%28for,including,_%29.md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>) async throws -> (T1, T2, T3)](./weather%28for,including,_,_%29.md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3, T4>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>, WeatherQuery<T4>) async throws -> (T1, T2, T3, T4)](./weather%28for,including,_,_,_%29.md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3, T4, T5>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>, WeatherQuery<T4>, WeatherQuery<T5>) async throws -> (T1, T2, T3, T4, T5)](./weather%28for,including,_,_,_,_%29.md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3, T4, T5, T6>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>, WeatherQuery<T4>, WeatherQuery<T5>, WeatherQuery<T6>) async throws -> (T1, T2, T3, T4, T5, T6)](./weather%28for,including,_,_,_,_,_%29.md)
  Returns the weather forecast for the requested location.
- [static let shared: WeatherService](./shared.md)
  A single, shared weather service object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherservice/weather(for:))*