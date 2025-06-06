# App Store Discovery and Engagement

**Framework**: Analytics Reports

Analyze how users interact with your app on the App Store.

#### Overview

The App Store Discovery and Engagement report provides details about how users engage with your apps on the App Store itself. This includes data about user engagement with your app’s icons, product pages, in-app event pages, and [`other install sheets`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/skstoreproductviewcontroller).

- Territories: Worldwide
- Platforms: iOS, iPadOS, macOS, tvOS, visionOS
- Availability: - Daily: Every day.
- Weekly: Every Friday for the previous week (Monday to Sunday).
- Monthly: On the fifth day of the following month.
- History: On request, data is available beginning from January 1, 2024.
- Completeness: Within three days. Weekly and monthly reports are complete by default.
- Privacy: Data is available in two reports: standard and detailed.  reports include fields not easily related to uniquely identifiable user data.  reports include all fields and also include additional privacy measures for the data, to help protect uniquely identifiable information for individuals. Download the standard report unless you need to analyze the unique fields in the detailed report. To learn more, see [`Protecting user privacy in report data`](privacy.md).

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections.  To learn more, see [`Data Completeness and Corrections`](data-completeness-corrections.md).

#### Report Fields

| Report Field | Description | Data Type | Standard Report | Detailed Report |
| --- | --- | --- | --- | --- |
| Date | Date on which the event occurred. For weekly and monthly instances, this column represents the first day of the week and month, respectively. | `date` | ✔ | ✔ |
| App Name | The name of the app provided by you during app setup in App Store Connect. | `string` | ✔ | ✔ |
| App Apple Identifier | Your app’s Apple ID. | `integer` | ✔ | ✔ |
| Event | The type of event that occurred. | `string` | ✔ | ✔ |
| Page Type | The page type associated with the event. | `string` | ✔ | ✔ |
| Page Title | The name of the product page or in-app event page that led the user to discover the app. | `string` |  | ✔ |
| Source Type | Where the user discovered the app. | `string` | ✔ | ✔ |
| Source Info | The app referrer or web referrer that led the user to discover the app. | `string` |  | ✔ |
| Campaign | The Campaign Token of the campaign created in  App Analytics. Column available starting November 19, 2024. | `string` |  | ✔ |
| Engagement Type | User action, if any, on the impression or page. | `string` | ✔ | ✔ |
| Device | The device on which the event occurred. | `string` | ✔ | ✔ |
| Platform Version | The OS version of the device on which the event occurred. | `string` | ✔ | ✔ |
| Territory | The App Store country or region in which the event occurred. | `string` | ✔ | ✔ |
| Counts | The total number of events that occurred. | `integer` | ✔ | ✔ |
| Unique Counts | The total number of unique users that performed the event. | `integer` | ✔ | ✔ |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Event | Impression | A user viewed your app icon in a list alongside other apps, including in search results, charts, and the Today, Apps, and Games tabs. Page views are not included in these counts. |
| Event | Page view | The user was presented with a dedicated page for your app or in-app event. |
| Event | Tap | The user tapped on an impression or page for your app or in-app event. |
| Page Type | No page | Your app was presented to the user outside of a dedicated page, such as in a list alongside other apps. |
| Page Type | In-app event | An in-app Event page. |
| Page Type | Notification | An App Store notification. |
| Page Type | Product page | A product page. |
| Page Type | Store sheet | An App Store [`other install sheets`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/skstoreproductviewcontroller). |
| Page Type | App version history | Your app’s version history page. |
| Page Type | App privacy | Your app’s privacy detail page. |
| Page Type | Developer page | Your developer page. |
| Page Type | Media view | Pages containing your app’s media (such as screenshots and previews). |
| Page Title | Various | The name of the product page or in-app event page that led the user to download the app. Possible values include the name you set for your page in App Store Connect, default product page, no page, or null. |
| Source Type | App Store search | Users who discovered your app within search results on the App Store. Includes Search Ads results. Doesn’t include the Suggested section of the search landing page. |
| Source Type | App Store browse | Users who discovered your app while browsing the App Store. Includes results in the Suggested section of the search landing page. |
| Source Type | App referrer | Users who discovered your app from within another app. Includes impressions and page views loaded in a [`other install sheets`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/skstoreproductviewcontroller). Includes Apple apps, such as Messages, except Safari. |
| Source Type | Web referrer | Users who discovered your app after browsing a website in Safari. |
| Source Type | App Clip | Users who discovered your app from within an App Clip. |
| Source Type | Notification | Users who were presented with your app from within an App Store generated notification. |
| Source Type | Unavailable | The source type is unavailable. Includes apps downloaded using App Store gift cards, promotional codes, or Mobile Device Management software. |
| Engagement Type | Get | The number of taps on the Get, Buy, or Pre-order button. To differentiate between these values, view the App Store Download and App Store Pre-Order reports. |
| Engagement Type | Update | The number of taps on the Update button. |
| Engagement Type | Redownload | The number of taps on the Download button. |
| Engagement Type | Open | The number of taps on the Open button. |
| Engagement Type | IAE reminder | The number of times a user activates a reminder for your in-app event. |
| Engagement Type | IAE reminder deactivated | The number of times a user de-activates a reminder for your in-app event. |
| Engagement Type | Notification tap | The number of taps on a notification. |
| Engagement Type | Share | The number of taps on the Share button. |

## See Also

- [App Store Web Preview](app-store-web-preview.md)
  Analyze how users engage with your app’s product pages and in-app events on web browsers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/app-store-discovery-and-engagement)*