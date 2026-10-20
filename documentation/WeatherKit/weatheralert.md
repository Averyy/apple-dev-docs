# WeatherAlert

**Framework**: WeatherKit  
**Kind**: struct  
**Role**: Structure

A weather alert issued for the requested  location by a governmental authority.

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
struct WeatherAlert
```

#### Overview

Weather alerts often contains severe weather information; however, not all alerts are severe. Alerts may or may not contain localized descriptions, depending on what is available from the source. Due to data source restrictions, information contained is served raw.

## Topics

### Getting the properties
- [var metadata: WeatherMetadata](./weatheralert/metadata.md)
  Descriptive information about the weather alert data.
- [var region: String?](./weatheralert/region.md)
  The name of the affected area.
- [var severity: WeatherSeverity](./weatheralert/severity.md)
  The severity of the weather alert.
- [var summary: String](./weatheralert/summary.md)
  The summary of the event type.
### Providing attribution
- [var detailsURL: URL](./weatheralert/detailsurl.md)
  The site for more details about the weather alert.
- [var source: String](./weatheralert/source.md)
  The name of the source issuing the weather alert.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Alerts and forecasts
- [struct WeatherAvailability](./weatheravailability.md)
  A structure that indicates the availability of data at the requested location.
- [struct Forecast](./forecast.md)
  A forecast collection for minute, hourly, and daily forecasts.
- [struct MinuteWeather](./minuteweather.md)
  A structure that represents the next hour minute forecasts.
- [struct HourWeather](./hourweather.md)
  A structure that represents the weather conditions for the hour.
- [struct DayWeather](./dayweather.md)
  A structure that represents the weather conditions for the day.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatheralert)*