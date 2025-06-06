# DayPartForecast

**Framework**: Weatherkit  
**Kind**: struct

A structure that represents the weather forecast for part of the day.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct DayPartForecast
```

## Topics

### Instance Properties
- [var cloudCover: Double](daypartforecast/cloudcover.md)
  The percentage of the sky covered with clouds.
- [var cloudCoverByAltitude: CloudCoverByAltitude](daypartforecast/cloudcoverbyaltitude.md)
  The fraction of sky obscured by low altitude, medium altitude, and high altitude clouds.
- [var condition: WeatherCondition](daypartforecast/condition.md)
  A description of the weather condition
- [var highTemperature: Measurement<UnitTemperature>](daypartforecast/hightemperature.md)
  The high temperature for the day part.
- [var highWindSpeed: Measurement<UnitSpeed>](daypartforecast/highwindspeed.md)
  The maximum sustained wind speed for the day part.
- [var lowTemperature: Measurement<UnitTemperature>](daypartforecast/lowtemperature.md)
  The overnight low temperature for the day part.
- [var maximumHumidity: Double](daypartforecast/maximumhumidity.md)
  The maximum humidity for the day part. Relative humidity measures the amount of water vapor in the air, compared to the maximum amount that the air can hold at the current temperature.
- [var maximumVisibility: Measurement<UnitLength>](daypartforecast/maximumvisibility.md)
  The maximum visibility for the day part.
- [var minimumHumidity: Double](daypartforecast/minimumhumidity.md)
  The minimum humidity for the day part. Relative humidity measures the amount of water vapor in the air, compared to the maximum amount that the air can hold at the current temperature.
- [var minimumVisibility: Measurement<UnitLength>](daypartforecast/minimumvisibility.md)
  The minimum visibility for the day part.
- [var precipitation: Precipitation](daypartforecast/precipitation.md)
  The description of precipitation for the day part.
- [var precipitationAmountByType: PrecipitationAmountByType](daypartforecast/precipitationamountbytype.md)
  A breakdown of all precipitation forecasted for the day.
- [var precipitationChance: Double](daypartforecast/precipitationchance.md)
  The probability of precipitation for the day part.
- [var wind: Wind](daypartforecast/wind.md)
  Wind data describing the wind speed, direction, and gust.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/daypartforecast)*