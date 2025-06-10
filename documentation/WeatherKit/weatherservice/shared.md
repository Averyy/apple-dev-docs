# shared

**Framework**: WeatherKit  
**Kind**: property

A single, shared weather service object.

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
static let shared: WeatherService
```

#### Discussion

Use this object to interface to weather services in your application. If you need to prioritize weather information, create separate instances with `init`.

## See Also

- [func weather(for: CLLocation) async throws -> Weather](weatherservice/weather(for:).md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>) async throws -> (T1, T2)](weatherservice/weather(for:including:_:).md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>) async throws -> (T1, T2, T3)](weatherservice/weather(for:including:_:_:).md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3, T4>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>, WeatherQuery<T4>) async throws -> (T1, T2, T3, T4)](weatherservice/weather(for:including:_:_:_:).md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3, T4, T5>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>, WeatherQuery<T4>, WeatherQuery<T5>) async throws -> (T1, T2, T3, T4, T5)](weatherservice/weather(for:including:_:_:_:_:).md)
  Returns the weather forecast for the requested location.
- [func weather<T1, T2, T3, T4, T5, T6>(for: CLLocation, including: WeatherQuery<T1>, WeatherQuery<T2>, WeatherQuery<T3>, WeatherQuery<T4>, WeatherQuery<T5>, WeatherQuery<T6>) async throws -> (T1, T2, T3, T4, T5, T6)](weatherservice/weather(for:including:_:_:_:_:_:).md)
  Returns the weather forecast for the requested location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherservice/shared)*