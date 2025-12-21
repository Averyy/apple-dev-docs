# App Store Web Preview

**Framework**: Analytics Reports

Analyze how people engage with your app’s product pages and in-app events on web browsers.

#### Overview

The App Store Web Preview Report allows you to analyze how people are engaging with your app’s product pages and in-app events on the web version of the App Store.

- Territories: Worldwide
- Platforms: iOS, iPadOS, macOS, tvOS, visionOS
- Availability: - Daily: Every day.
- Weekly: Every Friday for the previous week (Monday to Sunday).
- Monthly: On the fifth day of the following month.
- History: On request, data is available beginning on January 1, 2024
- Completeness: Within three days. Weekly and monthly reports are complete by default.
- Privacy: Data is available in two reports: standard and detailed.  reports include fields not easily related to uniquely identifiable data.  reports include all fields and also include additional privacy measures for the data, to help protect uniquely identifiable information for individuals. Download the standard report unless you need to analyze the unique fields in the detailed report. To learn more, see [`Protecting user privacy in report data`](privacy.md).

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections.  To learn more, see [`Data Completeness and Corrections`](data-completeness-corrections.md).

#### Report Fields

| Report Field | Description | Data Type | Summary Report | Detail Report |
| --- | --- | --- | --- | --- |
| Date | Date on which the event occurred. For weekly and monthly instances, this column represents the first day of the week and month, respectively. | `date` | x | ✔ |
| App Name | The name of the app provided by you during app setup in App Store Connect. | `string` | ✔ | ✔ |
| App Apple Identifier | Your app’s Apple ID. | `integer` | ✔ | ✔ |
| Event | The type of event that occurred. | `string` | ✔ | ✔ |
| Page Type | The page type associated with the event. | `string` | ✔ | ✔ |
| Page Title | The name of the product page or in-app event page that led someone to discover the app. | `string` |  | ✔ |
| Source Type | Where someone discovered the app. | `string` | ✔ | ✔ |
| Source Info | The app referrer or web referrer that led someone to discover the app. | `string` |  | ✔ |
| Engagement Type | The type of engagement that occurred. | `string` | ✔ | ✔ |
| Browser | The browser on which the App Store product page or in-app event was viewed. | `string` | ✔ | ✔ |
| Browser Version | The browser version on which the App Store product page or in-app event was viewed. | `string` | ✔ | ✔ |
| Device | Type of device on which the event occurred. | `string` | ✔ | ✔ |
| Platform Version | The OS version of the device on which the event occurred. | `string` | ✔ | ✔ |
| Territory | App Store country in which the event occurred. | `string` | ✔ | ✔ |
| Counts | The total number of events that occurred. | `integer` | ✔ | ✔ |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Event | Page View | A person was presented with the App Store product page or in-app event. |
| Event | Tap | A person tapped on the buttons, tabs, or links on the App Store product page or in-app event. |
| Page Type | Product page | A product page. |
| Page Type | In-app event | An in-app event page. |
| Page Title | Various | The name of the product page or in-app event page that led someone to download the app. Possible values include the name you set for your page in App Store Connect, default product page, no page, or null. |
| Source Type | Web referrer | A person discovered your app or in-app event after browsing a website in Safari. |
| Source Type | Unavailable | The source type is unavailable. |
| Engagement Type | App Privacy details dialog modal close | A person closed the app privacy details dialog modal. |
| Engagement Type | App Privacy details dialog modal open | A person opened the App Privacy details dialog modal. |
| Engagement Type | Learn more about App Privacy | A person tapped on “Learn More” under App Privacy, which links out to a “Learn More About App Privacy” page. |
| Engagement Type | Customer review dialog modal close | A person closed a customer review dialog modal. |
| Engagement Type | Customer review dialog modal open (“more”) | A person tapped on “more” to view an entire customer review. |
| Engagement Type | Developer event page | A person tapped on a link to the developer event page. |
| Engagement Type | Developer preview page | A person tapped on the developer name hyperlink. |
| Engagement Type | Developer privacy policy link | A person tapped on the link to the developer privacy policy page. |
| Engagement Type | Developer website | A person tapped on the link to the developer website. |
| Engagement Type | License Agreement dialog modal close | A person closed the License Agreement modal. |
| Engagement Type | License Agreement dialog modal open | A person opened the License Agreement modal. |
| Engagement Type | Other | A person tapped a link to a destination not covered in the above Engagement Types. |
| Engagement Type | Privacy Definitions and Examples | A person tapped on “Privacy Definitions and Examples” in the App Privacy dialog modal. |
| Engagement Type | Product screenshots expanded | A person tapped on the down arrow to view all screenshots by platform. |
| Engagement Type | See all apps by developer | A person tapped on “See All” to view all apps by the developer. |
| Engagement Type | Ratings & Reviews expanded | A person tapped on “See All” to view all ratings and reviews. |
| Engagement Type | Story app | A person tapped on a link to “Story”. |
| Engagement Type | Version History dialog modal close | A person closed the Version History dialog modal. |
| Engagement Type | Version History dialog modal open | A person tapped on the “Version History” dialog modal. |
| Engagement Type | View in Mac App Store | A person tapped on the “View” button on your app’s product page or in-app event page. |

## See Also

- [App Store Discovery and Engagement](app-store-discovery-and-engagement.md)
  Analyze how users interact with your app on the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/app-store-web-preview)*