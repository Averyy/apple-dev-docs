# WeatherKit REST API

**Framework**: Weatherkitrestapi  
**Kind**: module

Obtain historical, current, and predictive weather for your app or service.

**Availability**:
- Weather API 1.0.0+

#### Overview

Use the WeatherKit REST API web service to provide weather data to your apps and services that offer both current and forecasted weather information to your users.

To provide weather information to a web app or other platform, like Android, use the WeatherKit REST API. For native iOS, macOS, tvOS, and watchOS apps, use [`WeatherKit`](https://developer.apple.com/documentation/WeatherKit).

> ❗ **Important**:  Using this API requires attribution. See [`WeatherKit - Data Sources`](https://developer.apple.comhttps://developer.apple.com/weatherkit/data-source-attribution/) to learn more.

 Using this API requires attribution. See [`WeatherKit - Data Sources`](https://developer.apple.comhttps://developer.apple.com/weatherkit/data-source-attribution/) to learn more.

## Topics

### Fundamentals
- [Request authentication for WeatherKit REST API](request-authentication-for-weatherkit-rest-api.md)
  Create a developer token to access weather data.
### Obtaining weather information for a location
- [GET /api/v1/availability/{latitude}/{longitude}](get-api-v1-availability-_latitude_-_longitude_.md)
  Determine the data sets available for the specified location.
- [GET /api/v1/weather/{language}/{latitude}/{longitude}](get-api-v1-weather-_language_-_latitude_-_longitude_.md)
  Obtain weather data for the specified location.
- [object Weather](weather.md)
  The collection of all requested weather data.
- [type Latitude](latitude.md)
  A numeric value indicating the latitude of the coordinate between `-90` and `90`.
- [type Longitude](longitude.md)
  A numeric value indicating the longitude of the coordinate between `-180` and `180`.
- [type DataSet](dataset.md)
  The collection of weather information for a location.
### Obtaining current weather information
- [object CurrentWeather](currentweather.md)
  The current weather conditions for the specified location.
- [object Metadata](metadata.md)
  Descriptive information about the weather data.
- [object ProductData](productdata.md)
  A base type for all weather data.
### Obtaining minute-to-minute forecast weather
- [object ForecastPeriodSummary](forecastperiodsummary.md)
  The summary for a specified period in the minute forecast.
- [object ForecastMinute](forecastminute.md)
  The precipitation forecast for a specified minute.
### Obtaining hourly weather information
- [object HourWeatherConditions](hourweatherconditions.md)
  The historical or forecasted weather conditions for a specified hour.
- [object HourlyForecast](hourlyforecast.md)
  A collection of hour forecasts for a specified range of hours.
- [object NextHourForecast](nexthourforecast.md)
  A minute-by-minute forecast for the next hour.
### Obtaining daily weather information
- [object DayWeatherConditions](dayweatherconditions.md)
  The historical or forecasted weather conditions for a specified day.
- [object DayPartForecast](daypartforecast.md)
  A summary forecast for a daytime or overnight period.
- [object DailyForecast](dailyforecast.md)
  A collection of day forecasts for a specified range of days.
### Obtaining weather alerts
- [GET /api/v1/weatherAlert/{language}/{id}](get-api-v1-weatheralert-_language_-_id_.md)
  Receive an active weather alert.
- [object WeatherAlert](weatheralert.md)
  An official message indicating severe weather from a reporting agency.
- [object WeatherAlertCollection](weatheralertcollection.md)
  A collection of severe weather alerts for a specified location.
- [object WeatherAlertSummary](weatheralertsummary.md)
  Detailed information about the weather alert.
- [type ResponseType](responsetype.md)
  The recommended action from a reporting agency.
- [type Severity](severity.md)
  The level of danger to life and property.
- [type Urgency](urgency.md)
  An indication of urgency of action from the reporting agency.
### Identifying weather events
- [type UnitsSystem](unitssystem.md)
  The system of units that the weather data is reported in.
- [type MoonPhase](moonphase.md)
  The shape of the moon as seen by an observer on the ground at a given time.
- [type PrecipitationType](precipitationtype.md)
  The type of precipitation forecasted to occur during the day.
- [type PressureTrend](pressuretrend.md)
  The direction of change of the sea level air pressure.
### Obtaining event information
- [object EventText](eventtext.md)
  The official text describing a severe weather event from the agency.
- [type Certainty](certainty.md)
  How likely the event is to occur.
### Performing attribution
- [GET /attribution/{language}](get-attribution-_language_.md)
  Receive attribution information.
- [object Attribution](attribution.md)
  A list of image asset URLs for attribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WeatherKitRESTAPI)*