# WeatherSeverity

**Framework**: WeatherKit  
**Kind**: enum

A description of the severity of the severe weather event.

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
enum WeatherSeverity
```

## Topics

### Getting the properties
- [WeatherSeverity.minor](weatherseverity/minor.md)
  Minimal or no known threat.
- [WeatherSeverity.moderate](weatherseverity/moderate.md)
  Possible threat.
- [WeatherSeverity.severe](weatherseverity/severe.md)
  Significant threat.
- [WeatherSeverity.extreme](weatherseverity/extreme.md)
  Extraordinary threat.
- [WeatherSeverity.unknown](weatherseverity/unknown.md)
  Unknown threat.
### Describing the weather severity
- [var accessibilityDescription: String](weatherseverity/accessibilitydescription.md)
  A localized accessibility description describing the weather severity.
- [var description: String](weatherseverity/description.md)
  A localized string describing the weather severity.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct WeatherQuery](weatherquery.md)
  A structure that encapsulates a generic weather dataset request.
- [struct CurrentWeather](currentweather.md)
  A structure that describes the current conditions observed at a location.
- [struct WeatherAttribution](weatherattribution.md)
  A structure that  defines the necessary information for attributing a weather data provider.
- [struct WeatherMetadata](weathermetadata.md)
  A structure that provides additional weather information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherseverity)*