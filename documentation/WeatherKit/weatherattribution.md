# WeatherAttribution

**Framework**: WeatherKit  
**Kind**: struct

A structure that  defines the necessary information for attributing a weather data provider.

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
struct WeatherAttribution
```

#### Overview

Attribution is required for publishing software using WeatherKit.

## Topics

### Getting the properties
- [var combinedMarkDarkURL: URL](weatherattribution/combinedmarkdarkurl.md)
  A URL for the combined “ Apple Weather” mark, in dark variant.
- [var combinedMarkLightURL: URL](weatherattribution/combinedmarklighturl.md)
  A URL for the combined “ Apple Weather” mark, in light variant.
- [var legalPageURL: URL](weatherattribution/legalpageurl.md)
  A link to the legal attribution page that contains copyright information about the weather data sources.
- [var serviceName: String](weatherattribution/servicename.md)
  The weather data provider name.
- [var squareMarkURL: URL](weatherattribution/squaremarkurl.md)
  A URL for the square Apple Weather mark.
### Instance Properties
- [var legalAttributionText: String](weatherattribution/legalattributiontext.md)
  This property returns text that should be made available to users for apps that cannot display the attributionURL contents in a Safari view. It contains language that outlines the weather data sources attribution and is a legal requirement of using WeatherKit.

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
- [struct WeatherMetadata](weathermetadata.md)
  A structure that provides additional weather information.
- [enum WeatherSeverity](weatherseverity.md)
  A description of the severity of the severe weather event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/weatherattribution)*