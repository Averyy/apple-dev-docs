# WeatherKit

**Framework**: WeatherKit  
**Kind**: module

Deliver weather conditions and alerts to your users.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

#### Overview

WeatherKit provides timely weather information including current conditions, minute precipitation, along with hourly, and daily forecasts. It also provides severe weather alerts.

## Topics

### Fundamentals
- [Fetching weather forecasts with WeatherKit](fetching_weather_forecasts_with_weatherkit.md)
  Request and display weather data for destination airports in a flight-planning app.
- [struct Weather](weather.md)
  A model representing the aggregate weather data the caller requests.
- [class WeatherService](weatherservice.md)
  Provides an interface for obtaining weather data.
### Requests
- [struct WeatherQuery](weatherquery.md)
  A structure that encapsulates a generic weather dataset request.
- [struct CurrentWeather](currentweather.md)
  A structure that describes the current conditions observed at a location.
- [struct WeatherAttribution](weatherattribution.md)
  A structure that  defines the necessary information for attributing a weather data provider.
- [struct WeatherMetadata](weathermetadata.md)
  A structure that provides additional weather information.
- [enum WeatherSeverity](weatherseverity.md)
  A description of the severity of the severe weather event.
### Characteristics
- [enum Precipitation](precipitation.md)
  The form of precipitation.
- [enum PressureTrend](pressuretrend.md)
  The atmospheric pressure change over time.
- [struct UVIndex](uvindex.md)
  The expected intensity of ultraviolet radiation from the sun.
- [struct Wind](wind.md)
  Contains wind data of speed, direction, and gust.
- [enum WeatherCondition](weathercondition.md)
  A description of the current weather condition.
### Alerts and forecasts
- [struct WeatherAlert](weatheralert.md)
  A weather alert issued for the requested  location by a governmental authority.
- [struct WeatherAvailability](weatheravailability.md)
  A structure that indicates the availability of data at the requested location.
- [struct Forecast](forecast.md)
  A forecast collection for minute, hourly, and daily forecasts.
- [struct MinuteWeather](minuteweather.md)
  A structure that represents the next hour minute forecasts.
- [struct HourWeather](hourweather.md)
  A structure that represents the weather conditions for the hour.
- [struct DayWeather](dayweather.md)
  A structure that represents the weather conditions for the day.
### Celestial information
- [struct SunEvents](sunevents.md)
  An enumeration that represents dates of solar events, including sunrise, sunset, dawn, and dusk.
- [struct MoonEvents](moonevents.md)
  A structure that represents lunar events.
- [enum MoonPhase](moonphase.md)
  An enumeration that specifies the moon phase kind.
### Errors
- [enum WeatherError](weathererror.md)
  An error WeatherKit returns.
### Structures
- [struct CloudCoverByAltitude](cloudcoverbyaltitude.md)
  Contains the percentage of sky covered by low, medium and high altitude cloud.
- [struct DailyWeatherStatistics](dailyweatherstatistics.md)
  A structure that holds a collection of day weather statistics data.
- [struct DailyWeatherStatisticsQuery](dailyweatherstatisticsquery.md)
  A structure that encapsulates a generic daily weather statistics dataset request.
- [struct DailyWeatherSummary](dailyweathersummary.md)
  A structure that holds a collection of day weather summaries.
- [struct DailyWeatherSummaryQuery](dailyweathersummaryquery.md)
  A structure that encapsulates a generic daily weather summary dataset request.
- [struct DayPartForecast](daypartforecast.md)
  A structure that represents the weather forecast for part of the day.
- [struct DayPrecipitationStatistics](dayprecipitationstatistics.md)
  A structure that describes precipitation statistics for a day.
- [struct DayPrecipitationSummary](dayprecipitationsummary.md)
  A structure that describes the precipitation summary for a day.
- [struct DayTemperatureStatistics](daytemperaturestatistics.md)
  A structure that describes temperature statistics for a day.
- [struct DayTemperatureSummary](daytemperaturesummary.md)
  A structure that describes the temperature summary for a day.
- [struct HistoricalComparisons](historicalcomparisons.md)
  A structure that represents the weather condition comparisons for a specific location. It’s a list of comparisons between current readings and historical averages. The list is ordered by significance of deviation.
- [struct HourTemperatureStatistics](hourtemperaturestatistics.md)
  A structure that describes temperature statistics for a specific hour.
- [struct HourlyWeatherStatistics](hourlyweatherstatistics.md)
  A structure that holds a collection of hour weather statistics data.
- [struct HourlyWeatherStatisticsQuery](hourlyweatherstatisticsquery.md)
  A structure that encapsulates a generic hourly weather statistics dataset request.
- [struct MonthPrecipitationStatistics](monthprecipitationstatistics.md)
  A structure that describes precipitation statistics for a specific month.
- [struct MonthTemperatureStatistics](monthtemperaturestatistics.md)
  A structure that describes temperature statistics for a specific month.
- [struct MonthlyWeatherStatistics](monthlyweatherstatistics.md)
  A structure that holds a collection of month weather statistics data.
- [struct MonthlyWeatherStatisticsQuery](monthlyweatherstatisticsquery.md)
  A structure that encapsulates a generic monthly weather statistics dataset request.
- [struct Percentiles](percentiles.md)
  A structure that describes probability distributions for a measurable weather condition.
- [struct PrecipitationAmountByType](precipitationamountbytype.md)
  A structure that provides a breakdown of amounts of all forms of precipitation that is expected to occur over a period of time.
- [struct SnowfallAmount](snowfallamount.md)
  A structure that describes the snowfall amount over a period of time.
- [struct Trend](trend.md)
  A structure describing an observed pattern in the data for weather at a location for a specific condition.
- [struct TrendBaseline](trendbaseline.md)
  A type encapsulating everything there is to know about what a trend baseline is.
- [struct WeatherChange](weatherchange.md)
  A structure that informs how certain measurable weather aspects are expected to change relative to before.
- [struct WeatherChanges](weatherchanges.md)
  A structure that represents the Weather Change forecast. It provides a qualitative assessment of whether upcoming weather is significantly different from prior conditions.
### Enumerations
- [enum Deviation](deviation.md)
  Describes a comparison between two values in a trend.
- [enum HistoricalComparison](historicalcomparison.md)
  An enum that represents a recognized comparison in the statistical analysis of a location’s historical weather data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WeatherKit)*