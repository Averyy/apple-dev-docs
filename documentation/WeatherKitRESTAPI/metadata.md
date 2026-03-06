# Metadata

**Framework**: WeatherKit REST API  
**Kind**: dictionary

Descriptive information about the weather data.

**Availability**:
- Weather API 1.0.0+

## Declaration

```swift
object Metadata
```

## Properties

- `attributionURL` (string): The URL of the legal attribution for the data source.
- `expireTime` (date-time) *(required)*: The time when the weather data is no longer valid.
- `language` (string): The ISO language code for localizable fields.
- `latitude` (number) *(required)*: The latitude of the relevant location.
- `longitude` (number) *(required)*: The longitude of the relevant location.
- `providerLogo` (string): The URL of a logo for the data provider.
- `providerName` (string): The name of the data provider.
- `readTime` (date-time) *(required)*: The time the weather data was procured.
- `reportedTime` (date-time): The time the provider reported the weather data.
- `temporarilyUnavailable` (boolean): The weather data is temporarily unavailable from the provider.
- `units` (UnitsSystem): The system of units that the weather data is reported in. This is set to metric.
- `version` (integer) *(required)*: The data format version.

## See Also

- [object CurrentWeather](currentweather.md)
  The current weather conditions for the specified location.
- [object ProductData](productdata.md)
  A base type for all weather data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkitrestapi/metadata)*