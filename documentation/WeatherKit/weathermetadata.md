# WeatherMetadata

**Framework**: WeatherKit  
**Kind**: struct

A structure that provides additional weather information.

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
struct WeatherMetadata
```

#### Overview

Metadata information includes the location, date of the request, the date the data will expire, and required provider attribution.

## Topics

### Getting the properties
- [var date: Date](weathermetadata/date.md)
  The time of the weather data request.
- [var expirationDate: Date](weathermetadata/expirationdate.md)
  The time the weather data expires.
- [var location: CLLocation](weathermetadata/location.md)
  The location of the request.
### Default Implementations
- [Decodable Implementations](weathermetadata/decodable-implementations.md)
- [Encodable Implementations](weathermetadata/encodable-implementations.md)
- [Equatable Implementations](weathermetadata/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WeatherQuery](weatherquery.md)
  A structure that encapsulates a generic weather dataset request.
- [struct CurrentWeather](currentweather.md)
  A structure that describes the current conditions observed at a location.
- [struct WeatherAttribution](weatherattribution.md)
  A structure that  defines the necessary information for attributing a weather data provider.
- [enum WeatherSeverity](weatherseverity.md)
  A description of the severity of the severe weather event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weathermetadata)*