# weather(for:including:_:_:_:_:_:)

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
@preconcurrency
final func weather<T1, T2, T3, T4, T5, T6>(for location: CLLocation, including dataSet1: WeatherQuery<T1>, _ dataSet2: WeatherQuery<T2>, _ dataSet3: WeatherQuery<T3>, _ dataSet4: WeatherQuery<T4>, _ dataSet5: WeatherQuery<T5>, _ dataSet6: WeatherQuery<T6>) async throws -> (T1, T2, T3, T4, T5, T6) where T1 : Sendable, T2 : Sendable, T3 : Sendable, T4 : Sendable, T5 : Sendable, T6 : Sendable
```

#### Return Value

The requested weather data set.

#### Discussion

> **Throws**: Weather data error `WeatherError`

This is a variadic API in which any combination of data sets can be requested and returned as a tuple. Here’s an example:

```
`let (current, minute, hourly, daily, alerts) = try await service.weather(for: newYork, including: .current, .minute, .hourly, .daily, .alerts)`
```

## Parameters

- `location`: The requested location.

## See Also

### Obtaining forecasts
- [func weather(for: CLLocation) async throws -> Weather](./weather%28for%29.md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>) async throws -> (T1, T2)](./weather%28for,including,_%29.md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>) async throws -> (T1, T2, T3)](./weather%28for,including,_,_%29.md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3, T4>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>, WeatherQuery<T4>) async throws -> (T1, T2, T3, T4)](./weather%28for,including,_,_,_%29.md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3, T4, T5>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>, WeatherQuery<T4>, WeatherQuery<T5>) async throws -> (T1, T2, T3, T4, T5)](./weather%28for,including,_,_,_,_%29.md)
  Returns the weather forecast for the requested location.
- [static let shared: WeatherService](./shared.md)
  A single, shared weather service object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherservice/weather(for:including:_:_:_:_:_:))*