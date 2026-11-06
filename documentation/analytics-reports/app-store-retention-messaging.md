# App Store Retention Messaging

**Framework**: Analytics Reports  
**Role**: Article

Analyze how users interact with retention messages during the subscription cancellation flow.

## Overview

The Retention Messaging report shows how users respond to retention messages displayed during the subscription cancellation flow. Use it to understand how often retention messages are seen, what actions users take — like redeeming an offer, switching plans, choosing to cancel, or continue their subscription — and which message types are most effective at keeping subscribers. The report captures every page view and user interaction, with breakdowns by subscription tier, message type, device, territory, and platform version, so you can optimize your retention strategy and reduce churn.

- Territories: Worldwide
- Platforms: iOS, iPadOS, macOS, visionOS
- Availability:

  - Daily: Every day.
- Completeness: Within 4 days.
- History: On request, data is available beginning from April 20, 2026.
- Privacy: No privacy measures are applied as the report does not include fields related to uniquely identifiable user data.

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections.  To learn more, see [Data Completeness and Corrections](./data-completeness-corrections.md).

## Report Fields

| Report Field | Description | Data Type |
| --- | --- | --- |
| Date | The date for which the event was generated. | `date` |
| App Name | The name of the app, as set in App Store Connect. | `string` |
| App Apple Identifier | The unique identifier assigned to the app by Apple. | `integer` |
| Current Subscription Group | The name of the subscription group the user most recently subscribed to. | `string` |
| Current Subscription Group Identifier | The unique identifier assigned to the subscription group by Apple. | `integer` |
| Current Subscription | The name of the subscription plan the user most recently subscribed to. | `string` |
| Current Subscription Identifier | The unique identifier assigned to the subscription plan by Apple. | `integer` |
| Event | The type of engagement event. | `string` |
| Page | The page associated with the engagement event. | `string` |
| Retention Message Type | The type of message displayed on the cancel screen. | `string` |
| Retention Message Selection Type | Indicates if the default message was displayed or if a real-time message selection was made. Applicable for developers using the Retention Messaging API. | `string` |
| Retention Message Name | The name of the retention message, as set in App Store Connect. For retention messages configured through the Retention Messaging API, default messages are labeled as “Default” and real-time selected messages are labeled as “Unavailable.” | `string` |
| Retention Message Identifier | The unique identifier for the retention message. For messages configured in App Store Connect, the ID is assigned by Apple. For messages delivered through the Retention Messaging API, the ID is the UUID provided by you. | `string` |
| Offer Name | The name of the retention offer or promotional offer presented to the user. | `string` |
| Offer Identifier | The offer ID of the retention offer or promotional offer presented to the user. | `string` |
| Suggested Subscription | The name of the subscription that was recommended in the retention message for the user to switch to. | `string` |
| Suggested Subscription Identifier | The unique identifier assigned to the recommended subscription by Apple. | `integer` |
| Save Type | The type of save interaction on the page. | `string` |
| Device | The type of device on which the event occurred. | `string` |
| Platform Version | The OS version on the device on which the event occurred. | `string` |
| Territory | The App Store country in which the event occurred. | `string` |
| Counts | The aggregated count of events. | `integer` |

## Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Event | Page views | Users were presented with the cancel screen, and at least 50% of the page loaded. |
| Event | Cancels | Users chose to cancel their subscription after viewing the cancel screen. |
| Event | Saves | Users chose not to cancel their subscription after viewing the cancel screen. |
| Retention Message Type | No Message | The cancel screen did not include a retention message. |
| Retention Message Type | Text message with optional image | The cancel screen included the retention message provided, along with the optional image if you had provided one. This value appears for events prior to November 4, 2026. Starting November 4, 2026, this value is replaced by Text message and Text message with image. |
| Retention Message Type | Text message | The cancel screen included the retention message provided, without an image. This value appears for events starting November 4, 2026. |
| Retention Message Type | Text message with image | The cancel screen included the retention message provided, along with the image you have configured. This value appears for events starting November 4, 2026. |
| Retention Message Type | Text message with switch plan | The cancel screen included the retention message provided and a recommendation to switch to an alternative plan. |
| Retention Message Type | Text message with offer | The cancel screen included the retention message and a retention offer. |
| Retention Message Selection Type | Default | The default retention message configured through the Retention Messaging API was displayed. |
| Retention Message Selection Type | Real - time | The retention message displayed was based on your real-time selection. |
| Retention Message Selection Type | App Store Connect | The retention message displayed was configured in App Store Connect. |
| Save Type | Switch plan | Users tapped the “Subscribe” button on the cancel screen. |
| Save Type | Redeem offer | Users tapped the “Redeem” button on the cancel screen. |
| Save Type | Don’t cancel | Users tapped the “Keep Subscription” button on the cancel screen. |

## See Also

### App Store Engagement
- [App Store Discovery and Engagement](./app-store-discovery-and-engagement.md)
  Analyze how users interact with your app on the App Store.
- [App Store Web Preview](./app-store-web-preview.md)
  Analyze how people engage with your app’s product pages and in-app events on web browsers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/app-store-retention-messaging)*