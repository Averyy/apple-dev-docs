# Platform App Installs

**Framework**: Analytics Reports

Analyze your app’s install data by date, install type, channel, device, platform version, and territory.

#### Overview

The Platform App Installs report includes install data from the App Store, TestFlight, and alternative distribution channels. Using the data in this report, you can measure the number of times your app was installed on devices running iOS and iPadOS.

- Territories: European Union only.
- Platforms: iOS, iPadOS
- Availability: - Daily: Every day
- History: On request, data is available beginning on March 5, 2024.
- Completeness: Same day.

#### Report Fields

| Report Field | Description | Data Type |
| --- | --- | --- |
| Install Day | The date on which Apple servers recorded the install event. | `date` |
| App Name | The name of the app as set in the App Store Connect. | `string` |
| App Apple Identifier | Your app’s Apple ID. | `integer` |
| Install Type | The type of install that occurred. | `string` |
| Channel | The channel from which the install was initiated. | `string` |
| Device | The device on which the install occurred. | `string` |
| Platform Version | The OS version of the device on which the install occurred. | `string` |
| Territory | The App Store country or region in which the install occurred. | `string` |
| Installs | The total number of installs. | `integer` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Install Type | First-time install | The first time an app is installed onto a device by an Apple Account. |
| Install Type | Reinstall | A subsequent installation of an app onto a device by an Apple Account. |
| Install Type | Update | The process of replacing an app on a device with the latest version of the same app. Includes manual updates and auto-updates. |
| Install Type | App Clip install | The process of installing an [`App Clip`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/offer-app-clip-experiences/overview-of-app-clips). |
| Install Type | Other install | The process of installing a pre-release version of your app using [`TestFlight`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/test-a-beta-version/testflight-overview). |
| Install Type | Other update | The process of replacing a pre-release version of your app with the latest version using TestFlight. |
| Install Type | User managed install | The process of installing an app using Mobile Device Management software. This includes apps installed with Apple Business Manager, Apple School Manager, and custom apps. |
| Install Type | Device managed install | The process of installing an app on a [`supervised device`](https://developer.apple.comhttps://support.apple.com/guide/deployment/about-device-supervision-dep1d89f0bff/web) using Mobile Device Management software. This includes Apple Business Manager, Apple School Manager, and custom apps. |
| Install Type | Restore | The process of automatically installing an app on a device from an iCloud backup. |
| Install Type | Auto-download | The process of automatically installing an app onto other devices associated with the user’s Apple Account. Controlled by the Apple account’s auto-download setting. |
| Install Type | Web Install | The process of manually installing an app from a web browser. |
| Channel | App Store | The app was installed directly from the App Store. |
| Channel | TestFlight | The app was installed using TestFlight. |
| Channel | Admin managed | The app was installed using Mobile Device Management software. This includes Apple Business Manager, Apple School Manager, and custom apps. |
| Channel | Alternative app marketplace name | The app was installed from a digital marketplace other than the App Store. |
| Channel | Web domain | The app was installed directly from a developer’s website. |

## See Also

- [App Clip Usage](app-clip-usage.md)
  Analyze how users engage with your App Clips.
- [App Crashes](app-crashes.md)
  Review crashes for your App Store apps based on app version and device type.
- [App Store Installations and Deletions](app-installs.md)
  Analyze details on the number of times users install and delete your apps.
- [App Store Opt-in](app-store-opt-in.md)
  Analyze the percentage of first-time app downloaders who choose to share their data with you.
- [App Sessions](app-sessions.md)
  Analyze how often people open your App Store apps, and the average session duration.
- [CarPlay App Usage](carplay-app-usage.md)
  Review how people use CarPlay in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/platform-app-installs)*