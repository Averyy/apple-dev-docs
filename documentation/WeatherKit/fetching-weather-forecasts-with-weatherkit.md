# Fetching weather forecasts with WeatherKit

**Framework**: Weatherkit

Request and display weather data for destination airports in a flight-planning app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Xcode 14.0+

#### Overview

> **Note**: This sample code project is associated with WWDC22 session [`10003: Meet WeatherKit`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10003/).

This sample code project is associated with WWDC22 session [`10003: Meet WeatherKit`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10003/).

##### 4039215

Before you run the sample code project in Xcode:

1. Download, install, and launch the latest version of Xcode.
2. In Safari, visit the [`Certificates, Identifiers, and Profiles`](https://developer.apple.comhttps://developer.apple.com/account/resources) section of the developer website.
3. Select Identifiers and click the Add button to create a new App ID for `FlightPlanner`. Follow the steps until you reach the Register an App ID page.
4. For the Bundle ID, select Explicit, and enter a unique bundle identifier. Use a reverse-DNS format for your identifier, as [`Preparing your app for distribution`](https://developer.apple.com/documentation/xcode/preparing-your-app-for-distribution) describes.
5. Click the App Services tab, and select the WeatherKit checkbox.
6. Complete the App ID creation process.
7. Wait 30 minutes while the service registers your app’s bundle ID.
8. In Xcode, from the Project navigator, select the `FlightPlanner` project and click the Signing & Capabilities tab.
9. Enter the unique bundle ID from step 4 in the Bundle Identifier field of the `FlightPlanner` target.
10. From the scheme pop-up menu, select a run destination.
11. If necessary, click Register Device on the Signing & Capabilities tab to create the provisioning profile.
12. On the toolbar, click Run, or choose Product > Run.

## See Also

- [struct Weather](weather.md)
  A model representing the aggregate weather data the caller requests.
- [class WeatherService](weatherservice.md)
  Provides an interface for obtaining weather data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/weatherkit/fetching_weather_forecasts_with_weatherkit)*