# App Store Installations and Deletions

**Framework**: Analytics Reports

Analyze details on the number of times users install and delete your apps.

#### Overview

Use the data in this report to estimate the number of times people install and delete your App Store apps.

- Territories: Worldwide
- Platforms: iOS, iPadOS, macOS, tvOS, visionOS
- Availability: - Daily: Every day
- Weekly: Every Friday for the previous week (Monday to Sunday).
- Monthly: On the fifth day of the following month.
- Completeness: Within five days. Weekly and monthly reports are complete by default.
- History: On request, data is available beginning from January 1, 2024.
- Privacy: - Includes data from users who have opted to share their data with Apple and developers. Data is provided only when events exist from at least five users for the respective report.
- Data is available in two reports: standard and detailed.  reports include fields not easily related to uniquely identifiable user data.  reports include all fields and also include additional privacy measures for the data, to help protect uniquely identifiable information for individuals. Download the standard report unless you need to analyze the unique fields in the detailed report. To learn more, see [`Protecting user privacy in report data`](privacy.md).

App Download Date

- The date on which someone downloaded the app onto the device. This field is only populated if the download occurred in the previous 30 days, otherwise it is null.

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections.  To learn more, see [`Data Completeness and Corrections`](data-completeness-corrections.md).

#### Report Fields

| Report Field | Description | Data Type | Summary Report | Detail Report |
| --- | --- | --- | --- | --- |
| Date | Date on which the event occurred. For weekly and monthly instances, this column represents the first day of the week and month, respectively. | `date` | ✔ | ✔ |
| App Name | The name of the app provided by you during app setup in App Store Connect. | `string` | ✔ | ✔ |
| App Apple Identifier | Your app’s Apple ID. | `integer` | ✔ | ✔ |
| Event | The type of usage event that occurred. | `string` | ✔ | ✔ |
| Download Type | The type of download event that occurred. | `string` | ✔ | ✔ |
| App Version | The version of the app being associated with the instalation or deletion. | `string` | ✔ | ✔ |
| Device | The device on which the app was installed or deleted. | `string` | ✔ | ✔ |
| Platform Version | The OS version of the device on which the app was installed or deleted. | `string` | ✔ | ✔ |
| Source Type | Where the user discovered your app. | `string` | ✔ | ✔ |
| Source Info | The app referrer or web referrer that led the user to discover your app. | `string` |  | ✔ |
| Campaign | The Campaign Token of the campaign created in  App Analytics. Column available starting November 19, 2024. | `string` |  | ✔ |
| Page Type | The page type which led the user to discover your app. | `string` | ✔ | ✔ |
| Page Title | The name of the product page or in-app event page that led the user to discover your app. | `string` |  | ✔ |
| App Download Date | The date on which the app was downloaded onto the device. This field is only populated if the download occurred in the previous 30 days, otherwise it is null. | `date` | ✔ | ✔ |
| Territory | The App Store country or region where the installation or deletion occurred. | `string` | ✔ | ✔ |
| Counts | The total count of events, based on users who have agreed to share their data with Apple and developers. | `integer` | ✔ | ✔ |
| Unique Devices | The number of unique devices on which events were generated,  based on users who have agreed to share their data with Apple and developers. | `integer` | ✔ | ✔ |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Event | Install | Your app was installed on the device. |
| Event | Delete | Your app was deleted from the device. |
| Download Type | First-time download | The first time a user downloaded your app. Based on the user’s Apple ID account. Counted when a user taps the Buy or Get button on the App Store. |
| Download Type | Redownload | A subsequent installation of an app onto a device by an Apple ID account. Counted when a user taps the redownload button on the App Store. |
| Download Type | Manual update | The process of manually replacing an app on a device with another version of the same app. Counted when a user taps the Update button on the App Store. |
| Download Type | Restore | The process of restoring an app onto a user’s device from iCloud Backup. |
| Source Type | App Store search | Users who discovered your app within search results on the App Store. Includes Search Ads results. Doesn’t include the Suggested section of the search landing page. |
| Source Type | App Store browse | The user viewed your app or tapped to download it while browsing the App Store (for example, in the Today, Games, or Apps tabs, and results in the Suggested section of the search landing page). |
| Source Type | App referrer | The users tapped a link in an app that brought them to your App Store product page. Includes apps using the StoreKit API to load your product page. Includes Apple apps, such as Messages, except Safari. |
| Source Type | Web referrer | The user tapped a link from a website that brought them to your App Store product page. If a chain of redirects in Safari leads to your App Store product page, the referring website will be the last URL in the chain. For iOS apps, taps from websites in non-Safari web browsers, such as Chrome, are attributed as that web browser app in App Referrers. For macOS apps, taps from non-Safari web browsers are attributed to Web Referrers. |
| Source Type | App Clip | The user tapped a link in your App Clip that brought them to your App Store product page. |
| Source Type | Unavailable | The source from which the user downloaded your app is unavailable. |
| Source Type | Institutional purchase | The user downloaded your app from [`Apple Business Manager`](https://developer.apple.comhttps://support.apple.com/guide/apple-business-manager/welcome/web) or [`Apple School Manager`](https://developer.apple.comhttps://support.apple.com/guide/apple-school-manager/welcome/web). |
| Page Type | Product page | The user downloaded your app from your app’s product page. |
| Page Type | In-app event | The user downloaded your app from an in-app event page. |
| Page Type | Store sheet | The user downloaded the app from a store sheet in the App Store. |
| Page Type | No page | Your app was presented in a list view to the user and there was no page title associated with the download. |

## See Also

- [App Clip Usage](app-clip-usage.md)
  Analyze how users engage with your App Clips.
- [App Crashes](app-crashes.md)
  Review crashes for your App Store apps based on app version and device type.
- [App Store Opt-in](app-store-opt-in.md)
  Analyze the percentage of first-time app downloaders who choose to share their data with you.
- [App Sessions](app-sessions.md)
  Analyze how often people open your App Store apps, and the average session duration.
- [CarPlay App Usage](carplay-app-usage.md)
  Review how people use CarPlay in your app.
- [Platform App Installs](platform-app-installs.md)
  Analyze your app’s install data by date, install type, channel, device, platform version, and territory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/app-installs)*