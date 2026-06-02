# App Store Subscription State

**Framework**: Analytics Reports

Analyze your App Store subscription performance.

#### Overview

The Subscription State report includes the count of active and churned subscriptions on the App Store. You can use this report to understand the total number of paid subscriptions, free trials, paid offers, subscriptions in billing issues, and more. Subscription data in this report is enriched with app download source and referrer information, enabling you to understand which acquisition channels help you acquire subscribers.

- Territories: Worldwide
- Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
- Availability: - Daily: Every day
- Completeness: Within 3 days.
- History: On request, data is available beginning from January 1, 2025.
- Privacy: Data is available in two reports: standard and detailed. Standard reports include fields not easily related to uniquely identifiable user data. Detailed reports include all fields and also include additional privacy measures for the data, to help protect uniquely identifiable information for individuals. Download the standard report unless you need to analyze the unique fields in the detailed report. To learn more, see [`Protecting user privacy in report data`](privacy.md).

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections. To learn more, see [`Data Completeness and Corrections`](data-completeness-corrections.md).

#### Report Fields

| Report Field | Description | Data Type | Standard Report | Detailed Report |
| --- | --- | --- | --- | --- |
| Date | Date for which the subscription snapshot has been generated for. | `date` | ✔ | ✔ |
| App Name | The name of the app provided by you during app setup in App Store Connect. | `string` | ✔ | ✔ |
| App Apple Identifier | Your app’s Apple ID. | `integer` | ✔ | ✔ |
| State Metric | The subscription state metric. | `string` | ✔ | ✔ |
| State Metric Grouping | Subscription state group that the subscription metric belongs to. | `string` | ✔ | ✔ |
| Subscription Name | The name of the subscription that the user has subscribed to. Subscription name appears as provided by you during setup in App Store Connect. | `string` | ✔ | ✔ |
| Subscription Identifier | The unique identifier assigned to the subscription by Apple. | `integer` | ✔ | ✔ |
| Subscription Duration | Standard duration of the subscription. | `string` | ✔ | ✔ |
| Billing Frequency | The frequency at which a user is charged for their subscription. | `string` | ✔ | ✔ |
| Billing Period | The current installment period within a 12-month commitment, ranging from the 1st through the 12th period. This dimension applies exclusively to [`Monthly Subscriptions with a 12-Month Commitment`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-subscriptions/set-availability-for-an-auto-renewable-subscription). | `string` | ✔ | ✔ |
| Subscription Group | The group that the subscription belongs to. Subscription group name appears as provided by you during setup in App Store Connect. | `string` | ✔ | ✔ |
| Subscription Group Identifier | The unique identifier assigned to the subscription group by Apple. | `integer` | ✔ | ✔ |
| Offer Type | Type of subscription offer the user has redeemed. | `string` | ✔ | ✔ |
| Offer Name | Name of the subscription offer redeemed by the user. | `string` | ✔ | ✔ |
| Offer ID | Offer ID of the subscription offer redeemed by the user. | `string` | ✔ | ✔ |
| Vanity Code | Vanity code associated with the subscription offer. | `string` | ✔ | ✔ |
| Offer Pricing | The pricing mechanism associated with the offer redeemed by the user. | `string` | ✔ | ✔ |
| Offer Duration | The duration of the subscription offer. | `string` | ✔ | ✔ |
| Family Sharing | Indicates whether users are sharing the subscription with their iCloud family. | `string` | ✔ | ✔ |
| Cancellation Reason | The reason why the subscription was canceled. | `string` | ✔ | ✔ |
| App Download Source Type | The name of the source type that led to the app being downloaded. | `string` | ✔ | ✔ |
| App Download Source Info | Referring app or domain | `string` |  | ✔ |
| Campaign | Campaign name as set by the developer in App Analytics. | `string` |  | ✔ |
| Page Type | Product page type from where the app was downloaded | `string` | ✔ | ✔ |
| Page Title | Name of the product page or in-app event page, as configured by the developer, which led the user to download the app | `string` |  | ✔ |
| Pre-Order | Fulfilled pre-orders / pre-order downloads | `string` | ✔ | ✔ |
| Original Purchase Device | The device on which the subscription was purchased for the very first time. | `string` | ✔ | ✔ |
| Territory | The territory associated with the account that purchased the subscription. | `string` | ✔ | ✔ |
| Counts | Number of subscriptions | `integer` | ✔ | ✔ |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| State Metric | Free trials | The number of active free trial subscriptions. |
| State Metric | Paid offers | The number of active pay-up-front or pay-as-you-go offers. |
| State Metric | Full price | The number of active full price subscriptions. |
| State Metric | Preserved price | The number of active preserved price subscriptions. |
| State Metric | Contingent price | The number of active contingent price subscriptions. |
| State Metric | Grace period | The number of subscriptions with a billing issue that are in a grace period. |
| State Metric | Billing retry | The number of subscriptions with a billing issue that are in billing retry. |
| State Metric | Suspended | The number of commitment-based subscriptions that have missed their payments. |
| State Metric | Voluntarily churned | The number of subscriptions that churned within the last 2 years because the user chose to cancel. |
| State Metric | Involuntarily churned | The number of subscriptions that churned within the last 2 years due to a billing issue and weren’t recovered by Apple within the 60-day retry window. |
| State Metric Grouping | Subscription offers | The number of active free trials and paid offers. |
| State Metric Grouping | Paid plans | The number of active full price, preserved price, and contingent price subscriptions. |
| State Metric Grouping | Billing issue | The number of subscriptions that failed to renew due to a billing issue, and Apple is attempting to recover them. |
| State Metric Grouping | Churned | The number of subscriptions that churned or became inactive within the last 2 years. |
| Family Sharing | Individual | The user is not sharing the subscription with their family. |
| Family Sharing | Shared with family | The user is sharing their subscription with their family. |
| Cancel Reason | Billing issue | The subscriber could not be billed, and the subscription was automatically canceled after the 60-day billing retry period. |
| Cancel Reason | Turned off auto-renew | Subscriber canceled their subscription. |
| Cancel Reason | Price increase | Subscription automatically ended because the price of the subscription increased and the subscriber did not consent. |
| Cancel Reason | Removed from Sale | The subscription was removed from sale, and the subscription was automatically canceled at the end of the entitlement period. |
| Cancel Reason | Unavailable | The cancelation reason is not available. |
| Source Type | App Store search | Users who discovered your app within search results on the App Store. Includes Search Ads results. Doesn’t include the Suggested section of the search landing page. |
| Source Type | App Store browse | Users who viewed your app or tapped to download it while browsing the App Store (for example, in the Today, Games, or Apps tabs, and results in the Suggested section of the search landing page). |
| Source Type | App referrer | Users who discovered your app from within another app. Includes downloads of your app from within a [`store sheet`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/skstoreproductviewcontroller). |
| Source Type | Web referrer | Users who tapped a link from a website that brought them to your App Store product page. If a chain of redirects in Safari leads to your App Store product page, the referring website will be the last URL in the chain. For iOS apps, taps from websites in non-Safari web browsers, such as Chrome, are attributed as that web browser app in App Referrers. For macOS apps, taps from non-Safari web browsers are attributed to Web Referrers. |
| Source Type | App Clip | Users who discovered your app from within an App Clip. |
| Source Type | Unavailable | The source from which the user downloaded your app is unavailable. |
| Source Type | Institutional purchase | The user who downloaded your app from [`Apple Business Manager`](https://developer.apple.comhttps://support.apple.com/guide/apple-business-manager/welcome/web) or [`Apple School Manager`](https://developer.apple.comhttps://support.apple.com/guide/apple-school-manager/welcome/web). |
| Page Type | Product page | Users who downloaded your app from your app’s product page. |
| Page Type | In-App event | Users who downloaded your app from an in-app event page. |
| Page Type | Store sheet | Users who downloaded your app from a store sheet in the App Store. |
| Page Type | No Page | Your app was presented in a list view to the user and there was no page title associated with the download. |

## See Also

- [App Store Downloads](app-download.md)
  Analyze how many times people download your app on the App Store.
- [App Store Pre-orders](app-store-pre-order.md)
  Analyze details on the number of pre-orders that people place and cancel for your app on the App Store.
- [App Store Purchases](app-store-purchase.md)
  Analyze total revenue generated by your apps on the App Store.
- [App Store Subscription Event](subscription-event.md)
  Analyze and track changes throughout your users’ subscription lifecycle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/subscription-state)*