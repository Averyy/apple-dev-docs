# App Store Opt-in

**Framework**: Analytics Reports

Analyze the percentage of first-time app downloaders who choose to share their data with you.

#### Overview

The App Store provides an option for users to share diagnostic and usage data with developers. Utilize the App Store Opt-In Report to determine the percentage of first-time app downloaders who have chosen to share their data with you.

- Territories: Worldwide
- Platforms: iOS, iPadOS, macOS, tvOS, visionOS
- Availability: - Daily: Every day.
- History: On request, data is available beginning on January 1, 2024
- Completeness: Within three days.

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections.  To learn more, see [`Data Completeness and Corrections`](data-completeness-corrections.md).

#### Report Fields

| Report Field | Description | Data Type |
| --- | --- | --- |
| Date | Date on which the event occurred. | `date` |
| App Name | The name of the app provided by you during app setup in App Store Connect. | `string` |
| App Apple Identifier | Your app’s Apple ID. | `integer` |
| Downloading Users | Daily count of users who downloaded the app for the first time. | `integer` |
| Users Opting-In | Daily count of users who downloaded the app for the first time and opted to share their usage and diagnostic data with the developer. | `integer` |

## See Also

- [App Clip Usage](app-clip-usage.md)
  Analyze how users engage with your App Clips.
- [App Crashes](app-crashes.md)
  Review crashes for your App Store apps based on app version and device type.
- [App Store Installations and Deletions](app-installs.md)
  Analyze details on the number of times users install and delete your apps.
- [App Sessions](app-sessions.md)
  Analyze how often people open your App Store apps, and the average session duration.
- [CarPlay App Usage](carplay-app-usage.md)
  Review how people use CarPlay in your app.
- [Platform App Installs](platform-app-installs.md)
  Analyze your app’s install data by date, install type, channel, device, platform version, and territory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/app-store-opt-in)*