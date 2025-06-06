# App Store Downloads

**Framework**: Analytics Reports

Analyze how many times people download your app on the App Store.

#### Overview

The App Downloads Report includes download data generated on the App Store. You can use this report to understand your total number of downloads, including first-time downloads, redownloads, updates, and more.

- Territories: Worldwide
- Platforms: iOS, iPadOS, macOS, tvOS, visionOS
- Availability: - Daily: Every day
- Weekly (detailed report only): Every Friday for the previous week (Monday to Sunday).
- Monthly (detailed report only): On the fifth day of the following month.
- Completeness: Within two days. Weekly and monthly reports are complete by default.
- History: On request, data is available beginning from January 1, 2024.
- Privacy: Data is available in two reports: standard and detailed.  reports include fields not easily related to uniquely identifiable user data.  reports include all fields and also include additional privacy measures for the data, to help protect uniquely identifiable information for individuals. Download the standard report unless you need to analyze the unique fields in the detailed report. To learn more, see see [`Protecting user privacy in report data`](privacy.md).

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections.  To learn more, see [`Data Completeness and Corrections`](data-completeness-corrections.md).

#### Report Fields

| Report Field | Description | Data Type | Standard Report | Detailed Report |
| --- | --- | --- | --- | --- |
| Date | Date on which the event occurred. For weekly and monthly instances, this column represents the first day of the week and month, respectively. | `date` | ✔ | ✔ |
| App Name | The name of the app provided by you during app setup in App Store Connect. | `string` | ✔ | ✔ |
| App Apple Identifier | Your app’s Apple ID. | `integer` | ✔ | ✔ |
| Download Type | The type of download event that occured. | `string` | ✔ | ✔ |
| App Version | The app version being downloaded. | `string` | ✔ | ✔ |
| Device | The device on which the app was downloaded. | `string` | ✔ | ✔ |
| Platform Version | The OS version of the device on which the download occured. | `string` | ✔ | ✔ |
| Source Type | The source from where the user discovered the app. | `string` | ✔ | ✔ |
| Source Info | The app referrer or web referrer that led the user to discover the app. | `string` |  | ✔ |
| Campaign | The Campaign Token of the campaign created in  App Analytics. Column available starting November 19, 2024. | `string` |  | ✔ |
| Page Type | The page type from where the app was downloaded. | `string` | ✔ | ✔ |
| Page Title | The name of the product page or in-app event page that led the user to download the app. | `string` |  | ✔ |
| Pre-Order | A flag indicating whether the download came from a pre-order. | `string` | ✔ | ✔ |
| Territory | The App Store country or region where the download occured. | `string` | ✔ | ✔ |
| Counts | The total number of downloads. | `integer` | ✔ | ✔ |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Download Type | First-time Download | The first time a user downloaded your app. Based on the user’s Apple ID account. Counted when a user taps the “Buy” or “Get” button on the App Store. |
| Download Type | Redownload | A subsequent installation of an app onto a device by an Apple ID account. Counted when a user taps the redownload button on the App Store. |
| Download Type | Manual update | The process of manually replacing an app on a device with another version of the same app. Counted when a user taps the “Update” button on the App Store. |
| Download Type | Auto-update | The process of automatically replacing an app on a device with another version of the same app. Controlled by the device’s settings. |
| Download Type | Restore | The process of restoring an app onto a user’s device from iCloud Backup. |
| Source Type | App Store search | Users who discovered your app within search results on the App Store. Includes Search Ads results. Doesn’t include the Suggested section of the search landing page. |
| Source Type | App Store browse | Users who viewed your app or tapped to download it while browsing the App Store (for example, in the Today, Games, or Apps tabs, and results in the Suggested section of the search landing page). |
| Source Type | App referrer | Users who discovered your app from within another app. Includes downloads of your app from within a [`store sheet`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/skstoreproductviewcontroller). |
| Source Type | Web referrer | Users who tapped a link from a website that brought them to your App Store product page. If a chain of redirects in Safari leads to your App Store product page, the referring website will be the last URL in the chain. For iOS apps, taps from websites in non-Safari web browsers, such as Chrome, are attributed as that web browser app in App Referrers. For macOS apps, taps from non-Safari web browsers are attributed to Web Referrers. |
| Source Type | App Clip | Users who discovered your app from within an App Clip. |
| Source Type | Unavailable | The source from which the user downloaded your app is unavailable. |
| Source Type | Institutional purchase | The user who downloaded your app from [`Apple Business Manager`](https://developer.apple.comhttps://support.apple.com/guide/apple-business-manager/welcome/web) or [`Apple School Manager`](https://developer.apple.comhttps://support.apple.com/guide/apple-school-manager/welcome/web). |
| Page Type | Product page | Users who downloaded your app from your app’s product page. |
| Page Type | In-App event | Users who downloaded your app from an in-app event page. |
| Page Type | Store sheet | Users who downloaded your app from a store sheet in the App Store. |
| Page Type | No Page | Your app was presented in a list view to the user and there was no page title associated with the download. |

## See Also

- [App Store Pre-orders](app-store-pre-order.md)
  Analyze details on the number of pre-orders that people place and cancel for your app on the App Store.
- [App Store Purchases](app-store-purchase.md)
  Analyze total revenue generated by your apps on the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/app-download)*