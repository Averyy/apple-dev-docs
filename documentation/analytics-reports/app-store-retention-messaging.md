# App Store Retention Messaging

**Framework**: Analytics Reports

Analyze how users interact with retention messages during the subscription cancellation flow.

#### Overview

The Retention Messaging report shows how users respond to retention messages displayed during the subscription cancellation flow. Use it to understand how often retention messages are seen, what actions users take — like redeeming an offer, switching plans, choosing to cancel, or continue their subscription — and which message types are most effective at keeping subscribers. The report captures every page view and user interaction, with breakdowns by subscription tier, message type, device, territory, and platform version, so you can optimize your retention strategy and reduce churn.

- Territories: Worldwide
- Platforms: iOS, iPadOS, visionOS
- Availability: - Daily: Every day.
- Completeness: Within 3 days.
- History: On request, data is available beginning from April 20, 2026.
- Privacy: No privacy measures are applied as the report does not include fields related to uniquely identifiable user data.

The Analytics Reports framework delivers new portions of report content as instances. Each instance can contain one or more batches of data, to accommodate late-arriving events, or in rare cases, data corrections.  To learn more, see [`Data Completeness and Corrections`](data-completeness-corrections.md).

#### Report Fields

| Report Field | Description | Data Type |
| --- | --- | --- |
| Date | Date for which the event has been generated for. | `date` |
| App Name | Name of app as set in App Store Connect. | `string` |
| App Apple Identifier | The unique identifier assigned to the app by Apple. | `integer` |
| Current Group Subscription | Name of the subscription group the user most recently subscribed to. | `string` |
| Current Subscription Group Identifier | The unique identifier assigned to the subscription group by Apple. | `string` |
| Current Subscription | Name of the subscription that the user most recently subscribed to. | `string` |
| Current Subscription Identifier | The unique identifier assigned to the subscription by Apple. | `integer` |
| Event | Type of engagement event. | `string` |
| Page | Page associated with the engagement event. | `string` |
| Retention Message Type | Type of message displayed on the cancel sheet. | `string` |
| Message Selection Type | Indicates if the default message was displayed or if a real-time message selection was made. Applicable for developers using the Retention Messaging API. | `string` |
| Save Type | The type of save interaction on the page. | `string` |
| Device | Type of device on which the event occurred. | `string` |
| Platform Version | OS version on the device on which the event occurred. | `string` |
| Territory | App Store country in which the event occurred. | `string` |
| Counts | Aggregated count of events. | `integer` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Event | Page views | Users were presented with the cancel sheet, and at least 50% of the page loaded. |
| Event | Cancels | Users chose to cancel their subscription after viewing the cancel sheet. |
| Event | Saves | Users chose not to cancel their subscription after viewing the cancel sheet. |
| Retention Message Type | No retention message | The cancel sheet did not include a retention message. |
| Retention Message Type | Text message with optional image | The cancel sheet included the retention message provided, along with the optional image if you had provided one. |
| Retention Message Type | Text message with switch plan | The cancel sheet included the retention message provided and a recommendation to switch to an alternative plan. |
| Retention Message Type | Text message with offer | The cancel sheet included the retention message and a retention offer. |
| Message Selection Type | Default | The default retention message was displayed. |
| Message Selection Type | Real-time | The retention message displayed was based on your real-time selection. |
| Save Type | Switch plan | Users clicked on the “Subscribe” button on the cancel sheet. |
| Save Type | Redeem offer | Users clicked on the “Redeem” button on the cancel sheet. |
| Save Type | Don’t cancel | Users clicked on the “Don’t Cancel” button on the cancel sheet or dismissed the sheet taking no action. |

## See Also

- [App Store Discovery and Engagement](app-store-discovery-and-engagement.md)
  Analyze how users interact with your app on the App Store.
- [App Store Web Preview](app-store-web-preview.md)
  Analyze how people engage with your app’s product pages and in-app events on web browsers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/app-store-retention-messaging)*