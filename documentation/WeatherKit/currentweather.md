# CurrentWeather

**Framework**: WeatherKit  
**Kind**: struct

A structure that describes the current conditions observed at a location.

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
struct CurrentWeather
```

#### Overview

The current conditions may not be a literal observation, but rather the result of a mathematical weather model predicting conditions based on real observations.

## Topics

### Getting temperature and humidity
- [var apparentTemperature: Measurement<UnitTemperature>](currentweather/apparenttemperature.md)
  The feels-like temperature when factoring wind and humidity.
- [var dewPoint: Measurement<UnitTemperature>](currentweather/dewpoint.md)
  The temperature at which relative humidity is 100%.
- [var humidity: Double](currentweather/humidity.md)
  The amount of water vapor in the air.
- [var temperature: Measurement<UnitTemperature>](currentweather/temperature.md)
  The current temperature.
### Getting wind and pressure
- [var pressure: Measurement<UnitPressure>](currentweather/pressure.md)
  The sea level air pressure in millibars.
- [var pressureTrend: PressureTrend](currentweather/pressuretrend.md)
  The direction of change of the sea level air pressure.
- [var wind: Wind](currentweather/wind.md)
  The wind speed, direction, and gust.
### Getting conditions
- [var cloudCover: Double](currentweather/cloudcover.md)
  The percentage of the sky covered with clouds.
- [var condition: WeatherCondition](currentweather/condition.md)
  An enumeration value indicating the condition at the time.
### Getting date and validity
- [var date: Date](currentweather/date.md)
  The date of the current weather.
### Getting daylight and visibility
- [var isDaylight: Bool](currentweather/isdaylight.md)
  A Boolean value indicating whether there is daylight.
- [var uvIndex: UVIndex](currentweather/uvindex.md)
  The level of ultraviolet radiation.
- [var visibility: Measurement<UnitLength>](currentweather/visibility.md)
  The distance at which terrain is visible.
### Getting additional information
- [var metadata: WeatherMetadata](currentweather/metadata.md)
  Descriptive information about the current weather data.
- [var symbolName: String](currentweather/symbolname.md)
  The SF Symbol icon that represents the current weather condition and whether it’s daylight at the current date.
### Instance Properties
- [var cloudCoverByAltitude: CloudCoverByAltitude](currentweather/cloudcoverbyaltitude.md)
  The percentage of the sky covered with low-altitude, middle altitude and high-altitude clouds during the period.
- [var precipitationIntensity: Measurement<UnitSpeed>](currentweather/precipitationintensity.md)
  The current precipitation intensity in kilometers per hour.

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
- [struct WeatherAttribution](weatherattribution.md)
  A structure that  defines the necessary information for attributing a weather data provider.
- [struct WeatherMetadata](weathermetadata.md)
  A structure that provides additional weather information.
- [enum WeatherSeverity](weatherseverity.md)
  A description of the severity of the severe weather event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/currentweather)*