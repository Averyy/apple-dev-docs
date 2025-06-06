# WeatherAvailability

**Framework**: Weatherkit  
**Kind**: struct

A structure that indicates the availability of data at the requested location.

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
struct WeatherAvailability
```

#### Overview

`WeatherAvailability` represents the availability of data at the requested location. Weather alerts, or minute forecast data may be temporarily unavailable from the data provider, or unsupported in some regions. Other data sets are expected to be supported for all geographic locations, for example, current weather, and therefore are not included in `WeatherAvailability`.

## Topics

### Getting the properties
- [var alertAvailability: WeatherAvailability.AvailabilityKind](weatheravailability/alertavailability.md)
  The weather alerts availability.
- [var minuteAvailability: WeatherAvailability.AvailabilityKind](weatheravailability/minuteavailability.md)
  The minute forecast availability.
- [WeatherAvailability.AvailabilityKind](weatheravailability/availabilitykind.md)
  The availability kind.
### Default Implementations
- [Decodable Implementations](weatheravailability/decodable-implementations.md)
- [Encodable Implementations](weatheravailability/encodable-implementations.md)
- [Equatable Implementations](weatheravailability/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct WeatherAlert](weatheralert.md)
  A weather alert issued for the requested  location by a governmental authority.
- [struct Forecast](forecast.md)
  A forecast collection for minute, hourly, and daily forecasts.
- [struct MinuteWeather](minuteweather.md)
  A structure that represents the next hour minute forecasts.
- [struct HourWeather](hourweather.md)
  A structure that represents the weather conditions for the hour.
- [struct DayWeather](dayweather.md)
  A structure that represents the weather conditions for the day.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatheravailability)*