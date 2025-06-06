# App Store Pre-orders

**Framework**: Analytics Reports

Analyze details on the number of pre-orders that people place and cancel for your app on the App Store.

#### Overview

The App Store Pre-Orders Report includes pre-order data generated on the App Store. Use the data in this report to measure the number of pre-orders that people place and the number of cancelations, as well as attribute pre-orders to acquisition sources and App Store pages.

- Territories: Worldwide
- Platforms: iOS, iPadOS, macOS, tvOS, visionOS
- Availability: - Daily: Every day
- Weekly (detailed report only): Every Friday for the previous week (Monday to Sunday).
- Monthly (detailed report only: On the fifth day of the following month.
- Completeness: Within two days. Weekly and monthly reports are complete by default.
- History: On request, data is available beginning from January 1, 2024.
- Privacy: Data is available in two reports: standard and detailed.  reports include fields not easily related to uniquely identifiable user data.  reports include all fields and also include additional privacy measures for the data, to help protect uniquely identifiable information for individuals. Download the standard report unless you need to analyze the unique fields in the detailed report. To learn more, see [`Protecting user privacy in report data`](privacy.md).

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections.  To learn more, see [`Data Completeness and Corrections`](data-completeness-corrections.md).

#### Report Fields

| Report Field | Description | Data Type | Summary Report | Detail Report |
| --- | --- | --- | --- | --- |
| Date | Date on which the event occurred. For weekly and monthly instances, this column represents the first day of the week and month, respectively. | `date` | ✔ | ✔ |
| App Name | The name of the app provided by you during app setup in App Store Connect. | `string` | ✔ | ✔ |
| App Apple Identifier | Your app’s Apple ID. | `integer` | ✔ | ✔ |
| Device | The type of device on which the app was pre-ordered. | `string` | ✔ | ✔ |
| Platform Verison | The OS version of the device on which the app was pre-ordered. | `string` | ✔ | ✔ |
| Source Type | The source type that led the user to discover your app. | `string` | ✔ | ✔ |
| Source Info | The app referrer or web referrer that led the user to place the pre-order. | `string` |  | ✔ |
| Campaign | The Campaign Token of the campaign created in  App Analytics. Column available starting November 19, 2024. | `string` |  | ✔ |
| Page Type | The page type from which the pre-order was placed. | `string` | ✔ | ✔ |
| Page Title | The name of the product page or in-app event page that led the user to pre-order your app. | `string` |  | ✔ |
| Territory | The App Store country or region in which the pre-order was initiated. | `string` | ✔ | ✔ |
| Pre-Order Start Date | The date the app became available for pre-order. | `date` | ✔ | ✔ |
| Pre-Order End Date | The last date the app is available for pre-order. | `date` | ✔ | ✔ |
| Pre-Orders Placed | The total number of pre-orders placed. | `integer` | ✔ | ✔ |
| Pre-Order Canceled | The total number of pre-orders canceled. | `integer` | ✔ | ✔ |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Source Type | App Store search | The user pre-ordered your app from Search on the App Store. Includes Search Ads in App Store search. |
| Source Type | App Store browse | The user viewed your app or tapped to pre-order it while browsing the App Store (for example, in the Today, Games, or Apps sections). |
| Source Type | App referrer | The user tapped a link in an app that brought them to your App Store product page. Includes apps using the StoreKit API to load your product page. Includes Apple apps, such as Messages, except Safari. |
| Source Type | Web referrer | The user tapped a link from a website that brought them to your App Store product page. If a chain of redirects in Safari leads to your App Store product page, the referring website will be the last URL in the chain. For iOS apps, taps from websites in non-Safari web browsers, such as Chrome, are attributed as that web browser app in App Referrers. For macOS apps, taps from non-Safari web browsers are attributed to Web Referrers. |
| Source Type | App Clip | The user tapped a link in your App Clip that brought them to your App Store product page. |
| Source Type | Unavailable | The source from which the user pre-ordered your app is unavailable. |
| Source Type | Institutional Purchase | The user pre-ordered your app from [`Apple Business Manager`](https://developer.apple.comhttps://support.apple.com/guide/apple-business-manager/welcome/web) or [`Apple School Manager`](https://developer.apple.comhttps://support.apple.com/guide/apple-school-manager/welcome/web). |
| Page Type | Product page | The user pre-ordered your app from your app’s product page. |
| Page Type | In-app event | The user pre-ordered your app from an In-App Event page. |
| Page Type | Store sheet | The user pre-ordered your app from a store sheet in the App Store. |
| Page Type | No page | Your app was presented in a list view to the user and there was no page title associated with the download. |

## See Also

- [App Store Downloads](app-download.md)
  Analyze how many times people download your app on the App Store.
- [App Store Purchases](app-store-purchase.md)
  Analyze total revenue generated by your apps on the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/app-store-pre-order)*