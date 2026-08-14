# MinuteWeather

**Framework**: WeatherKit  
**Kind**: struct

A structure that represents the next hour minute forecasts.

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
struct MinuteWeather
```

## Topics

### Getting the precipitation
- [var precipitation: Precipitation](minuteweather/precipitation.md)
  A description of the precipitation for this minute.
- [var precipitationChance: Double](minuteweather/precipitationchance.md)
  The probability of precipitation in this minute.
- [var precipitationIntensity: Measurement<UnitSpeed>](minuteweather/precipitationintensity.md)
  The forecasted precipitation intensity.
### Getting the date
- [var date: Date](minuteweather/date.md)
  The start time of the minute weather.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct WeatherAlert](weatheralert.md)
  A weather alert issued for the requested  location by a governmental authority.
- [struct WeatherAvailability](weatheravailability.md)
  A structure that indicates the availability of data at the requested location.
- [struct Forecast](forecast.md)
  A forecast collection for minute, hourly, and daily forecasts.
- [struct HourWeather](hourweather.md)
  A structure that represents the weather conditions for the hour.
- [struct DayWeather](dayweather.md)
  A structure that represents the weather conditions for the day.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/minuteweather)*