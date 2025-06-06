# Browser Choice Screen Engagement (iOS versions before 18.2)

**Framework**: Analytics Reports

Measure how often your web browser app is being selected as the default from the browser choice screen  on iOS.

#### Overview

The Browser Choice Screen Engagement Report provides details about users’ selection of a default web browser from the browser choice screen, displayed the first time an EU user opens Safari on their iPhone. Use this report to understand the number of times your app was downloaded, launched, and selected from the browser choice screen.

- Territories: European Union (EU) only.
- Platforms: iOS (before 18.2)
- Availability: - Daily: Every day.
- Weekly: Every Friday for the previous week (Monday to Sunday).
- Monthly: On the fifth day of the following month.
- History: On request, data is available beginning from March 5, 2024.
- Privacy: The Browser Choice Screen Engagement Report does not include sensitive fields easily relatable to user data.
- Completeness: Due to late arriving events, you may expect to see updates in the daily, weekly, and monthly report instances for past dates on an ongoing basis. To learn more, see [`Data Completeness and Corrections`](data-completeness-corrections.md).

#### Report Fields

| Report Field | Description | Data Type |
| --- | --- | --- |
| Date | Date on which the event occurred. For weekly and monthly instances, this column represents the first day of the week and month, respectively. | `date` |
| App Name | The name of the app provided by you during app setup in App Store Connect. | `string` |
| App Apple Identifier | Your app’s Apple ID. | `integer` |
| Event | The type of event that occurred. | `string` |
| Device | The device on which the event occurred. | `string` |
| Platform Version | The OS version of the device on which the event occurred. | `string` |
| Territory | The App Store country or region in which the event occurred. | `string` |
| Counts | The total number of events that occurred. | `integer` |
| Unique Devices | The count of unique devices on which the event occurred. | `integer` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Event | Page view | Your app’s product page was viewed in the browser choice screen. |
| Event | First-time download | Your app was downloaded for the first time on the device and set as the default browser through the browser choice screen. |
| Event | Redownload | Your app was redownloaded on the device and set as the default browser through the browser choice screen. |
| Event | Open | Your app was opened and set as the default browser on the device through the browser choice screen. |
| Event | Update | Your app was updated and set as the default browser on the device through the browser choice screen. |

> **Note**: The user size of “Page view” events is different from that of “First-time download”, “Redownload”, “Open” and “Update” events. For the latter, the data is from users for whom Apple has data about their full journey through the choice screen. Those are a subset of the users for whom Apple has data about “Page view” events.

## See Also

- [AccessorySetupKit Accessory Picker Sessions](accessorysetupkit-accessory-picker-sessions.md)
  Analyze how many people use your app to set up accessories by using AccessorySetupKit.
- [AccessorySetupKit Usage](accessorysetupkit-usage.md)
  Analyze how often your app uses AccessorySetupKit.
- [AirPlay Discovery Sessions](airplay-discovery-sessions.md)
  Review information about AirPlay discovery sessions.
- [Animoji Stickers Sent](animoji-stickers-sent.md)
  Analyze how many times people use Memoji stickers in your app.
- [App Added to Focus](app-added-to-focus.md)
  Review information about your app’s relationship to Focus modes.
- [App Disk Space Usage](app-disk-space-usage.md)
  Analyze your app’s disk space use.
- [App Runtime Usage](app-runtime-usage.md)
  Analyze how often your app executes specific symbols of different dynamic libraries.
- [App Sessions Context](app-sessions-context.md)
  Analyze how many people use your app and for how long.
- [Application Preferred Language Settings](application-preferred-language-settings.md)
  Review how people use language preference settings in your app.
- [ARKit ARSession Duration](arkit-arsession-duration.md)
  Review information  about ARKit ARSession duration.
- [ARKit ARSession Failures](arkit-arsession-failures.md)
  Analyze details about ARKit ARSession failures.
- [ARKit Capture Frame Rate Throttling](arkit-capture-frame-rate-throttling.md)
  Analyze how long it takes for ARKit to throttle the camera frame rate.
- [ARKit Collaborative Session Features](arkit-collaborative-session-features.md)
  Review how your app uses ARKit collaborative session features.
- [ARKit Face Tracking](arkit-face-tracking.md)
  Analyze how often your app uses ARKit face tracking.
- [ARKit Video Formats](arkit-video-formats.md)
  Review information  about ARKit video formats and high-resolution frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/browser-choice-screen-engagement)*