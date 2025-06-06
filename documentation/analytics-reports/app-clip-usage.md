# App Clip Usage

**Framework**: Analytics Reports

Analyze how users engage with your App Clips.

#### Overview

The App Clip Usage Report includes App Clip engagement and usage data from users who have opted-in to share their data with Apple and developers. Use these reports to estimate the number of App Clip card views, App Clip installations, App Clip Sessions, and session duration.

Data is available in two reports: standard and detailed. The  reports include all fields that are not easily related to uniquely identifiable user data. to potentially sensitive data, and the  report includes all fields. Detailed reports include additional privacy measures for the data, to help protect uniquely identifiable information for individuals. To learn more, see [`Protecting user privacy in report data`](privacy.md).

- Territories: Worldwide
- Platforms: iOS, iPadOS, macOS, tvOS, visionOS
- Availability: - Daily: Every day
- Weekly: Every Friday for the previous week (Monday to Sunday).
- Monthly: On the fifth day of the following month.
- History: On request, data is available beginning from January 1, 2024.
- Completeness: Within five days. Weekly and monthly reports are complete by default.

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections.  To learn more, see [`Data Completeness and Corrections`](data-completeness-corrections.md).

> **Note**: Download the standard report unless you need to analyze the unique fields in the detailed report.

#### Report Fields

| Report Field | Description | Data Type | Standard Report | Detailed Report |
| --- | --- | --- | --- | --- |
| Date | Date on which the event occurred. For weekly and monthly instances, this column represents the first day of the week and month, respectively. | `date` | ✔ | ✔ |
| App Name | The name of the app provided  by you during app setup in App Store Connect. | `string` | ✔ | ✔ |
| App Apple Identifier | Your app’s Apple ID. App Clips share the same App Apple Identifier as their parent app. | `integer` | ✔ | ✔ |
| App Clip Event Type | The type of App Clip event that occurred. | `string` | ✔ | ✔ |
| Source Type | Where the user discovered the App Clip. | `string` | ✔ | ✔ |
| Source Info | Additional details, if applicable, on the source type. | `string` |  | ✔ |
| Campaign | The Campaign Token of the campaign created in  App Analytics. Column available starting November 19, 2024. | `string` |  | ✔ |
| App Version | The App Clip version on the device. | `string` | ✔ | ✔ |
| Device | The type of device on which the App Clip event occurred. | `string` | ✔ | ✔ |
| Platform Version | OS version on the device on which the App Clip event occurred | `string` | ✔ | ✔ |
| Territory | The App Store country or region in which the App Clip event occurred. | `string` | ✔ | ✔ |
| Counts | The aggregated count of App Clip events. | `integer` | ✔ | ✔ |
| Total Session Duration | Total duration, in seconds, of all sessions being reported. | `integer` | ✔ | ✔ |
| Unique Devices | The count of App Clip events on unique devices. | `integer` | ✔ | ✔ |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Event Type | Views | The total number of times a card for this App Clip was invoked on a device running iOS 14 or later. |
| Event Type | Installations | The number of times your App Clip was installed on a device. |
| Event Type | Sessions | The number of times your App Clip was used for at least one second. |
| Event Type | Crashes | The total number of times your App Clip crashed. |
| Source Type | App Clip code | The user scanned an App Clip code with their device. |
| Source Type | App referrer | Your App Clip card was displayed after a user tapped on a link in another app. |
| Source Type | Web referrer | The user tapped on an invocation URL or Smart App Banner in Safari which invoked the App Clip Card. |
| Source Type | Location-based | Your App Clip card was displayed due to the user’s location. |
| Source Type | Maps | The user tapped on a place card in Apple Maps, and followed the link to your App Clip. |
| Source Type | Messages | Your App Clip Card was displayed after the user tapped a link they received through the Messages app. |
| Source Type | NFC tags | The user held their iPhone near an NFC tag, causing your App Clip card to be displayed. |
| Source Type | QR code | The user scanned a QR code with their device and your App Clip card was displayed. |
| Source Type | Siri | Siri suggested your App Clip in response to a user. |

## See Also

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
- [Platform App Installs](platform-app-installs.md)
  Analyze your app’s install data by date, install type, channel, device, platform version, and territory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/app-clip-usage)*