# App Store Subscription Event

**Framework**: Analytics Reports

Analyze and track changes throughout your users’ subscription lifecycle.

#### Overview

The Subscription Event report includes an aggregated count of subscription lifecycle changes. You can use this report to understand the number of offer starts, offer renewals, conversions to paid, paid renewals, voluntary and involuntary churn, and more. Subscription data in this report is enriched with app download source and referrer information, enabling you to understand which acquisition channels help you acquire subscribers.

- Territories: Worldwide
- Platforms: iOS, iPadOS, macOS, tvOS, visionOS, watchOS
- Availability: - Daily: Every day
- Weekly (detailed report only): Every Friday for the previous week (Monday to Sunday).
- Monthly (detailed report only): On the fifth day of the following month.
- Completeness: Within 3 days. Weekly and monthly reports are complete by default.
- History: On request, data is available beginning from January 1, 2025.
- Privacy: Data is available in two reports: standard and detailed. Standard reports include fields not easily related to uniquely identifiable user data. Detailed reports include all fields and also include additional privacy measures for the data, to help protect uniquely identifiable information for individuals. Download the standard report unless you need to analyze the unique fields in the detailed report. To learn more, see [`Protecting user privacy in report data`](privacy.md).

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections. To learn more, see [`Data Completeness and Corrections`](data-completeness-corrections.md).

#### Report Fields

| Report Field | Description | Data Type | Standard | Detailed |
| --- | --- | --- | --- | --- |
| Event Date | Date for which the subscription snapshot has been generated for. | `date` | ✔ | ✔ |
| App Name | Name of app as set in ASC. | `string` | ✔ | ✔ |
| App Apple Identifier | Apple identifier of the app. | `integer` | ✔ | ✔ |
| Event Sub Type | The subscription event metric being reported. | `string` | ✔ | ✔ |
| Event Grouping | Subscription event group that the event metric belongs to. | `string` | ✔ | ✔ |
| Subscription Name | The name of the subscription that the user has subscribed to. Subscription name appears as provided by you during setup in App Store Connect. | `string` | ✔ | ✔ |
| Subscription Identifier | The unique identifier assigned to the subscription by Apple. | `integer` | ✔ | ✔ |
| Subscription Duration | Standard duration of the subscription. | `string` | ✔ | ✔ |
| Subscription Group | The group that the subscription belongs to. Subscription group name appears as provided by you during setup in App Store Connect. | `string` | ✔ | ✔ |
| Subscription Group Identifier | The unique identifier assigned to the subscription group by Apple. | `integer` | ✔ | ✔ |
| Offer Type | Type of subscription offer the user has redeemed. | `string` | ✔ | ✔ |
| Offer Name | Name of the subscription offer redeemed by the user. | `string` | ✔ | ✔ |
| Offer ID | Offer ID of the subscription offer redeemed by the user. | `string` | ✔ | ✔ |
| Vanity Code | Vanity code associated with the subscription offer. | `string` | ✔ | ✔ |
| Offer Pricing | The pricing mechanism associated with the offer redeemed by the user. | `string` | ✔ | ✔ |
| Offer Duration | The duration of the subscription offer. | `string` | ✔ | ✔ |
| Plan Change Type | When users switch plans, this field indicates if it was an upgrade, crossgrade, or a downgrade. | `string` | ✔ | ✔ |
| Previous Subscription Name | When users switch plans, this field is populated with the previous subscription name. | `string` | ✔ | ✔ |
| Previous Subscription Identifier | When users switch plans, this field is populated with the previous subscription id. | `integer` | ✔ | ✔ |
| Family Sharing | Indicates whether users are sharing the subscription with their iCloud family. | `string` | ✔ | ✔ |
| Cancellation Reason | The reason why the subscription was canceled. | `string` | ✔ | ✔ |
| Paid Service Days Recovered | The estimated number of paid service days recovered due to Billing Grace Period. This field will be populated for recovery from grace period events only. | `string` | ✔ | ✔ |
| App Download Source Type | The name of the source type that led to the app being downloaded. | `string` | ✔ | ✔ |
| App Download Source Info | Referring app or domain | `string` |  | ✔ |
| Campaign | Campaign name as set by the developer in App Analytics. | `string` |  | ✔ |
| Page Type | Product page type from where the app was downloaded | `string` | ✔ | ✔ |
| Page Title | Name of the product page or in-app event page, as configured by the developer, which led the user to download the app | `string` |  | ✔ |
| Pre-Order | Fulfilled pre-orders / pre-order downloads | `string` | ✔ | ✔ |
| Original Purchase Device | The device on which the subscription was purchased for the very first time. | `string` | ✔ | ✔ |
| Territory | The territory associated with the account that purchased the subscription. | `string` | ✔ | ✔ |
| Counts | Number of events. | `integer` | ✔ | ✔ |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Event Grouping | Offer Starts | The number of offers that began. |
| Event Grouping | Offer Renewals | The number of free and paid offers that renewed. |
| Event Grouping | Paid Subscriptions from Offers | The number of offers that converted to paid subscriptions. |
| Event Grouping | Paid Subscription Starts | The number of paid subscriptions that began. |
| Event Grouping | Renewals | The total number of subscriptions that renewed. |
| Event Grouping | Entered Billing Issue | The total number of subscriptions that entered a grace period or billing retry due to a billing issue. |
| Event Grouping | Recoveries from Billing Issue | The number of subscriptions that Apple was able to recover following a billing issue. |
| Event Grouping | Involuntary Churn | The number of subscriptions that were canceled at the end of the 60-day billing retry period. |
| Event Grouping | Voluntary Churn | The number of subscriptions that were canceled by the user. |
| Event Grouping | Exits | The total number of subscriptions or offers that ended where another subscription or offer was started. |
| Event Grouping | Extensions | The total number of subscriptions that were provided with a renewal extension. |
| Event Sub Type | Free Trial Starts | The number of free trial subscriptions that began. |
| Event Sub Type | Paid Offer Starts | The number of pay-up-front or pay-as-you-go offers that began. |
| Event Sub Type | Free Trial Renewals | The number of free trials that renewed for another period. |
| Event Sub Type | Paid Offer Renewals | The number of paid offers that renewed for another period. |
| Event Sub Type | Full Price from Free Trial | The number of free trials that converted to full price subscriptions. |
| Event Sub Type | Contingent Price from Free Trial | The number of free trials that converted to contingent price subscriptions. |
| Event Sub Type | Full Price from Paid Offer | The number of paid offers that converted to full price subscriptions. |
| Event Sub Type | Contingent Price from Paid Offer | The number of paid offers that converted to contingent price subscriptions. |
| Event Sub Type | Full Price Subscription Starts | The number of subscriptions that were started or reactivated at full price. |
| Event Sub Type | Contingent Price Subscription Starts | The number of subscriptions that were started or reactivated at a contingent price. |
| Event Sub Type | Full Price Renewals | The number of subscriptions that renewed at full price. |
| Event Sub Type | Preserved Price Renewals | The number of subscriptions that renewed at a preserved price. |
| Event Sub Type | Contingent Price Renewals | The number of subscriptions that renewed at a contingent price. |
| Event Sub Type | Contingent Price Renewal from Full Price | The number of subscriptions that renewed at a contingent price from full price. |
| Event Sub Type | Contingent Price Renewal from Preserved Price | The number of subscriptions that renewed at a contingent price from a preserved price. |
| Event Sub Type | Full Price Renewal from Contingent Price | The number of subscriptions that renewed at full price from a contingent price. |
| Event Sub Type | Preserved Price Renewal from Contingent Price | The number of subscriptions that renewed at a preserved price from a contingent price. |
| Event Sub Type | Preserved Price Renewal from Full Price | The number of subscriptions that renewed at a preserved price instead of the updated full price. |
| Event Sub Type | Full Price Renewal from Preserved Price | The number of subscriptions that renewed at full price instead of a preserved price. |
| Event Sub Type | Entered Grace Period from Full Price | The number of full price subscriptions that entered a grace period due to a billing issue at the time of renewal. |
| Event Sub Type | Entered Grace Period from Contingent Price | The number of contingent price subscriptions that entered a grace period due to a billing issue at the time of renewal. |
| Event Sub Type | Entered Grace Period from Free Trial | The number of free trials that entered a grace period due to a billing issue at the time of renewal. |
| Event Sub Type | Entered Grace Period from Paid Offer | The number of paid offers that entered a grace period due to a billing issue at the time of renewal or conversion. |
| Event Sub Type | Entered Billing Retry from Full Price | The number of full price subscriptions that entered billing retry due to a billing issue at the time of renewal. |
| Event Sub Type | Entered Billing Retry from Contingent Price | The number of contingent price subscriptions that entered billing retry due to a billing issue at the time of renewal. |
| Event Sub Type | Entered Billing Retry from Free Trial | The number of free trials that entered billing retry due to a billing issue at the time of renewal. |
| Event Sub Type | Entered Billing Retry from Paid Offer | The number of paid offers that entered billing retry due to a billing issue at the time of renewal or conversion. |
| Event Sub Type | Entered Billing Retry from Grace Period | The number of subscriptions that didn’t recover from a billing issue during the grace period and moved to billing retry. Apple will continue trying to recover these subscriptions during the billing retry period. |
| Event Sub Type | Full Price Recoveries from Grace Period | The number of subscriptions that were recovered to full price from a grace period. |
| Event Sub Type | Contingent Price Recoveries from Grace Period | The number of subscriptions that were recovered to a contingent price from a grace period. |
| Event Sub Type | Preserved Price Recoveries from Grace Period | The number of subscriptions that were recovered to a preserved price from a grace period. |
| Event Sub Type | Paid Offer Recoveries from Grace Period | The number of paid offers that were started or renewed from a grace period. |
| Event Sub Type | Free Trial Recoveries from Grace Period | The number of free trials that were started during a grace period. |
| Event Sub Type | Full Price Recoveries from Billing Retry | The number of full price subscriptions recovered from billing retry. |
| Event Sub Type | Contingent Price Recoveries from Billing Retry | The number of contingent price subscriptions recovered from billing retry. |
| Event Sub Type | Preserved Price Recoveries from Billing Retry | The number of preserved price subscriptions recovered from billing retry. |
| Event Sub Type | Paid Offer Recoveries from Billing Retry | The number of paid offers that were started or renewed from billing retry. |
| Event Sub Type | Free Trial Recoveries from Billing Retry | The number of free trials that were started from a billing retry. |
| Event Sub Type | Involuntary Churn from Free Trials | The number of free trials that were canceled at the end of the 60-day billing retry period. |
| Event Sub Type | Involuntary Churn from Paid Offers | The number of paid offers that were canceled at the end of the 60-day billing retry period. |
| Event Sub Type | Involuntary Churn from Full Price | The number of full price subscriptions that were canceled at the end of the 60-day billing retry period. |
| Event Sub Type | Involuntary Churn from Contingent Price | The number of contingent price subscriptions that were canceled at the end of the 60-day billing retry period. |
| Event Sub Type | Involuntary Churn from Preserved Price | The number of preserved price subscriptions that were canceled at the end of the 60-day billing retry period. |
| Event Sub Type | Voluntary Churn from Free Trials | The number of free trials that were canceled by the user. |
| Event Sub Type | Voluntary Churn from Paid Offers | The number of paid offers that were canceled by the user. |
| Event Sub Type | Voluntary Churn from Full Price | The number of full price subscriptions that were canceled by the user. |
| Event Sub Type | Voluntary Churn from Contingent Price | The number of contingent price subscriptions that were canceled by the user. |
| Event Sub Type | Voluntary Churn from Preserved Price | The number of preserved price subscriptions that were canceled by the user. |
| Event Sub Type | Refunds from Paid Offers | The number of refunds requested on paid offers. |
| Event Sub Type | Refunds from Full Price | The number of refunds requested on full price subscriptions. |
| Event Sub Type | Refunds from Contingent Price | The number of refunds requested on contingent price subscriptions. |
| Event Sub Type | Refunds from Preserved Price | The number of refunds requested on preserved price subscriptions. |
| Event Sub Type | Plan Changes | The number of subscriptions where the user chose to upgrade, crossgrade, or downgrade to a different subscription. |
| Event Sub Type | Offer to Offer | The number of offers that changed to a different offer. |
| Event Sub Type | Offers from Paid | The number of existing paid subscriptions that changed to an offer. |
| Event Sub Type | Free Trial Extensions | The number of free trials that were provided with a renewal extension. |
| Event Sub Type | Paid Offer Extensions | The number of paid offers that were provided with a renewal extension. |
| Event Sub Type | Contingent Price Extensions | The number of contingent price subscriptions that were provided with a renewal extension. |
| Event Sub Type | Preserved Price Extensions | The number of preserved price subscriptions that were provided with a renewal extension. |
| Family Sharing | Individual | The user is not sharing the subscription with their family. |
| Family Sharing | Shared with family | The user is sharing they subscription with their family. |
| Cancel Reason | Billing Issue | The subscriber could not be billed, and the subscription was automatically canceled after the 60-day billing retry period. |
| Cancel Reason | Turned off auto-renew | Subscriber canceled their subscription. |
| Cancel Reason | Price Increase | Subscription automatically ended because the price of the subscription increased and the subscriber did not consent. |
| Cancel Reason | Removed from Sale | The subscription was removed from sale, and the subscription was automatically canceled at the end of the entitlement period. |
| Cancel Reason | Unavailable | The cancelation reason is not available. |
| Source Type | App Store search | Users who discovered your app within search results on the App Store. Includes Search Ads results. Doesn’t include the Suggested section of the search landing page. |
| Source Type | App Store browse | Users who viewed your app or tapped to download it while browsing the App Store (for example, in the Today, Games, or Apps tabs, and results in the Suggested section of the search landing page). |
| Source Type | App referrer | Users who discovered your app from within another app. Includes downloads of your app from within a [`store sheet`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/skstoreproductviewcontroller). |
| Source Type | Web referrer | Users who tapped a link from a website that brought them to your App Store product page. If a chain of redirects in Safari leads to your App Store product page, the referring website will be the last URL in the chain. For iOS apps, taps from websites in non-Safari web browsers, such as Chrome, are attributed as that web browser app in App Referrers. For macOS apps, taps from non-Safari web browsers are attributed to Web Referrers. |
| Source Type | App Clip | Users who discovered your app from within an App Clip. |
| Source Type | Unavailable | The source from which the user downloaded your app is unavailable. |
| Source Type | Institutional purchase | The user who downloaded your app from [`Apple Business Manager`](https://developer.apple.comhttps://support.apple.com/guide/apple-business-manager/welcome/web) or [`Apple School Manager`](https://developer.apple.comhttps://support.apple.com/guide/apple-school-manager/welcome/web). |
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
- [App Store Subscription State](subscription-state.md)
  Analyze your App Store subscription performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/subscription-event)*