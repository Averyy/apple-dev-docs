# App Store Web Preview

**Framework**: Analytics Reports

Analyze how users engage with your app’s product pages and in-app events on web browsers.

#### Overview

The App Store Web Preview Report allows you to analyze how users are engaging with your app’s product pages and in-app events on the web version of the App Store.

- Territories: Worldwide
- Platforms: iOS, iPadOS, macOS, tvOS, visionOS
- Availability: - Daily: Every day.
- Weekly: Every Friday for the previous week (Monday to Sunday).
- Monthly: On the fifth day of the following month.
- History: On request, data is available beginning on January 1, 2024
- Completeness: Within three days. Weekly and monthly reports are complete by default.
- Privacy: Data is available in two reports: standard and detailed.  reports include fields not easily related to uniquely identifiable user data.  reports include all fields and also include additional privacy measures for the data, to help protect uniquely identifiable information for individuals. Download the standard report unless you need to analyze the unique fields in the detailed report. To learn more, see [`Protecting user privacy in report data`](privacy.md).

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections.  To learn more, see [`Data Completeness and Corrections`](data-completeness-corrections.md).

#### Report Fields

| Report Field | Description | Data Type | Summary Report | Detail Report |
| --- | --- | --- | --- | --- |
| Date | Date on which the event occurred. For weekly and monthly instances, this column represents the first day of the week and month, respectively. | `date` | x | ✔ |
| App Name | The name of the app provided by you during app setup in App Store Connect. | `string` | ✔ | ✔ |
| App Apple Identifier | Your app’s Apple ID. | `integer` | ✔ | ✔ |
| Event | The type of event that occurred. | `string` | ✔ | ✔ |
| Page Type | The page type associated with the event. | `string` | ✔ | ✔ |
| Page Title | The name of the product page or in-app event page that led the user to discover the app. | `string` |  | ✔ |
| Source Type | Where the user discovered the app. | `string` | ✔ | ✔ |
| Source Info | The app referrer or web referrer that led the user to discover the app. | `string` |  | ✔ |
| Engagement Type | The type of engagement that occured. | `string` | ✔ | ✔ |
| Browser | The browser on which the App Store product page or in-app event was viewed. | `string` | ✔ | ✔ |
| Browser Version | The browser version on which the App Store product page or in-app event was viewed. | `string` | ✔ | ✔ |
| Device | Type of device on which the event occured. | `string` | ✔ | ✔ |
| Platform Version | The OS version of the device on which the event occurred. | `string` | ✔ | ✔ |
| Territory | App Store country in which the event occured. | `string` | ✔ | ✔ |
| Counts | The total number of events that occurred. | `integer` | ✔ | ✔ |

#### Glossary

| Dimension | Value | Defintion |
| --- | --- | --- |
| Event | Page View | A user was presented with the App Store product page or in-app event. |
| Event | Tap | A user tapped on the buttons, tabs, or links on the App Store product page or in-app event. |
| Page Type | Product page | A product page. |
| Page Type | In-app event | An in-app event page. |
| Page Title | Various | The name of the product page or in-app event page that led the user to download the app. Possible values include the name you set for your page in App Store Connect, default product page, no page, or null. |
| Source Type | Web referrer | A user discovered your app or in-app event after browsing a website in Safari. |
| Source Type | Unavailable | The source type is unavailable. |
| Engagement Type | App preview page | A user tapped on a card in the app preview page. |
| Engagement Type | App Privacy details module close | A user closed the app privacy details module. |
| Engagement Type | App Privacy details module open (“See Details”) | A user tapped on “See Details” to view app privacy details. |
| Engagement Type | Apple TV screenshots | A user tapped on the Apple TV screenshots tab. |
| Engagement Type | Apple Vision screenshots | A user tapped on the Apple Vision screenshots tab. |
| Engagement Type | Apple Watch screenshots | A user tapped on the Apple Watch screenshots tab. |
| Engagement Type | Customer review module close | A user closed a customer review module. |
| Engagement Type | Customer review module open (“more”) | A user tapped on “more” to view an entire customer review. |
| Engagement Type | Developer app support link | A user tapped on the link to the app support page. |
| Engagement Type | Developer event page | A user tapped on a link to the developer event page. |
| Engagement Type | Developer preview page | A user tapped on the developer name hyperlink. |
| Engagement Type | Developer privacy policy link | A user tapped on the link to the developer privacy policy page. |
| Engagement Type | Developer website | A user tapped on the link to the developer website. |
| Engagement Type | Genre page | A user tapped on a “Genre” page link. |
| Engagement Type | iPad screenshots | A user tapped on the iPad screenshots tab. |
| Engagement Type | iPhone screenshots | A user tapped on the iPhone screenshots tab. |
| Engagement Type | Learn more Arcade app | A user tapped on “Learn More” to view Arcade apps. |
| Engagement Type | License Agreement module close | A user closed the License Agreement module. |
| Engagement Type | License Agreement module open | A user opened the License Agreement module. |
| Engagement Type | Mac screenshots | A user tapped on the Mac screenshots tab. |
| Engagement Type | Messages screenshots | A user tapped on the Messages screenshots tab. |
| Engagement Type | Other | A user tapped a link to a destination not covered in the above Engagement Types. |
| Engagement Type | Other app preview page | A user tapped on a link to another app preview page. |
| Engagement Type | See all app events | A user tapped on “See All” to view all in-app events by the developer. |
| Engagement Type | See all apps by developer | A user tapped on “See All” to view all apps by the developer. |
| Engagement Type | See all in-app purchases | A user tapped on “See All” to view all in-app purchases by the developer. |
| Engagement Type | See all ratings and reviews | A user tapped on “See All” to view all ratings and reivews. |
| Engagement Type | See all recommendations | A user tapped on “See All” to view more apps recommended by Apple. |
| Engagement Type | See all related editorial items | A user tapped See All to view all related editorial items. |
| Engagement Type | See all subscriptions | A user tapped on See All to view all subscriptions by the developer. |
| Engagement Type | Story app | A user tapped on a link to “Story”. |
| Engagement Type | Top Charts | A user tapped on a link to “Top Charts”. |
| Engagement Type | Version History module close | A user closed the Version History module. |
| Engagement Type | Version History module open | A user tapped on the “Version History” link in the What’s New section. |
| Engagement Type | View in Mac App Store | A user tapped on the “View” button on your app’s product page or in-app event page. |

## See Also

- [App Store Discovery and Engagement](app-store-discovery-and-engagement.md)
  Analyze how users interact with your app on the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/app-store-web-preview)*