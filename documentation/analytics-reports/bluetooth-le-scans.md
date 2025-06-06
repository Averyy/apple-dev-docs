# Bluetooth LE Scans

**Framework**: Analytics Reports

Review how your app uses Bluetooth Low Energy (LE) scans.

#### Overview

This report contains information about LE Scan duration and time spent in foreground and background.

- Territories: Worldwide
- Platforms: iOS, iPadOS.  For more information about iOS and iPadOS, see the Platforms section in [`Data Completeness and Corrections`](data-completeness-corrections.md).
- Availability: - Daily: Every day.
- History: On request, data is available beginning with iOS 17.4 and iPadOS 17.4.
- Completeness: Data from devices that contribute to this report can arrive as late as 8 days after the date it generates on device. You can download recent data daily, but it might be incomplete, and data updates incrementally daily, until all late-arriving events are available.
- Privacy: - Includes data from users who have opted to share their data with Apple and developers.
- Individual rows will only appear if they have a value of 5 or more.
- Data Context: You can analyze your data with additional context by comparing it with the data in the [`App Sessions Context`](app-sessions-context.md) report, which provides a count of unique devices that use your app on a specific day. For example, if your app performed an action detailed in this report on 10 unique devices on a specific day, and the App Sessions Context report shows there were 100 unique devices running your app that day, then you can approximate that 10% of the devices running your app performed that action.

#### Report Fields

| Report Field | Description | Data Type |
| --- | --- | --- |
| Count | Number of times the event occurred | `integer` |
| Territory | Country or region in which the event occurred | `string` |
| Date | Date when the event occurred | `string` |
| Platform | OS version on the device on which the event occurred | `string` |
| Device | Type of device on which the event occurred | `string` |
| Build | Build of device on which event occurred | `string` |
| Unique Devices | The count of unique devices | `integer` |
| Release Type | Type of software release | `string` |
| Allowed In Background | Whether app can run in background | `boolean` |
| App In Foreground At Start | App in foreground at start | `boolean` |
| App In Foreground At Stop | App in foreground at stop | `boolean` |
| Total time spent | Total time spent scanning in milliseconds | `integer` |
| Time Spent In Background | Time spent scanning in background in milliseconds | `integer` |
| Time Spent In Foreground | Time spent scanning in foreground in milliseconds | `integer` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Total time spent | 0 | Represents range from -Infinity to 0 |
| Total time spent | 1 | Represents range from 0 to 5 |
| Total time spent | 2 | Represents range from 5 to 10 |
| Total time spent | 3 | Represents range from 10 to 20 |
| Total time spent | 4 | Represents range from 20 to 30 |
| Total time spent | 5 | Represents range from 30 to 40 |
| Total time spent | 6 | Represents range from 40 to 50 |
| Total time spent | 7 | Represents range from 50 to 75 |
| Total time spent | 8 | Represents range from 75 to 100 |
| Total time spent | 9 | Represents range from 100 to 200 |
| Total time spent | 10 | Represents range from 200 to 300 |
| Total time spent | 11 | Represents range from 300 to 400 |
| Total time spent | 12 | Represents range from 400 to 500 |
| Total time spent | 13 | Represents range from 500 to 600 |
| Total time spent | 14 | Represents range from 600 to 700 |
| Total time spent | 15 | Represents range from 700 to 800 |
| Total time spent | 16 | Represents range from 800 to 900 |
| Total time spent | 17 | Represents range from 900 to 1000 |
| Total time spent | 18 | Represents range from 1000 to 1500 |
| Total time spent | 19 | Represents range from 1500 to 2000 |
| Total time spent | 20 | Represents range from 2000 to 2500 |
| Total time spent | 21 | Represents range from 2500 to 3000 |
| Total time spent | 22 | Represents range from 3000 to 3500 |
| Total time spent | 23 | Represents range from 3500 to 4000 |
| Total time spent | 24 | Represents range from 4000 to 5000 |
| Total time spent | 25 | Represents range from 5000 to 7500 |
| Total time spent | 26 | Represents range from 7500 to 10000 |
| Total time spent | 27 | Represents range from 10000 to 30000 |
| Total time spent | 28 | Represents range from 30000 to 60000 |
| Total time spent | 29 | Represents range from 60000 to 90000 |
| Total time spent | 30 | Represents range from 90000 to 120000 |
| Total time spent | 31 | Represents range from 120000 to 180000 |
| Total time spent | 32 | Represents range from 180000 to +Infinity |
| Time Spent In Background | 0 | Represents range from -Infinity to 0 |
| Time Spent In Background | 1 | Represents range from 0 to 5 |
| Time Spent In Background | 2 | Represents range from 5 to 10 |
| Time Spent In Background | 3 | Represents range from 10 to 20 |
| Time Spent In Background | 4 | Represents range from 20 to 30 |
| Time Spent In Background | 5 | Represents range from 30 to 40 |
| Time Spent In Background | 6 | Represents range from 40 to 50 |
| Time Spent In Background | 7 | Represents range from 50 to 75 |
| Time Spent In Background | 8 | Represents range from 75 to 100 |
| Time Spent In Background | 9 | Represents range from 100 to 200 |
| Time Spent In Background | 10 | Represents range from 200 to 300 |
| Time Spent In Background | 11 | Represents range from 300 to 400 |
| Time Spent In Background | 12 | Represents range from 400 to 500 |
| Time Spent In Background | 13 | Represents range from 500 to 600 |
| Time Spent In Background | 14 | Represents range from 600 to 700 |
| Time Spent In Background | 15 | Represents range from 700 to 800 |
| Time Spent In Background | 16 | Represents range from 800 to 900 |
| Time Spent In Background | 17 | Represents range from 900 to 1000 |
| Time Spent In Background | 18 | Represents range from 1000 to 1500 |
| Time Spent In Background | 19 | Represents range from 1500 to 2000 |
| Time Spent In Background | 20 | Represents range from 2000 to 2500 |
| Time Spent In Background | 21 | Represents range from 2500 to 3000 |
| Time Spent In Background | 22 | Represents range from 3000 to 3500 |
| Time Spent In Background | 23 | Represents range from 3500 to 4000 |
| Time Spent In Background | 24 | Represents range from 4000 to 5000 |
| Time Spent In Background | 25 | Represents range from 5000 to 7500 |
| Time Spent In Background | 26 | Represents range from 7500 to 10000 |
| Time Spent In Background | 27 | Represents range from 10000 to 30000 |
| Time Spent In Background | 28 | Represents range from 30000 to 60000 |
| Time Spent In Background | 29 | Represents range from 60000 to 90000 |
| Time Spent In Background | 30 | Represents range from 90000 to 120000 |
| Time Spent In Background | 31 | Represents range from 120000 to 180000 |
| Time Spent In Background | 32 | Represents range from 180000 to +Infinity |
| Time Spent In Foreground | 0 | Represents range from -Infinity to 0 |
| Time Spent In Foreground | 1 | Represents range from 0 to 5 |
| Time Spent In Foreground | 2 | Represents range from 5 to 10 |
| Time Spent In Foreground | 3 | Represents range from 10 to 20 |
| Time Spent In Foreground | 4 | Represents range from 20 to 30 |
| Time Spent In Foreground | 5 | Represents range from 30 to 40 |
| Time Spent In Foreground | 6 | Represents range from 40 to 50 |
| Time Spent In Foreground | 7 | Represents range from 50 to 75 |
| Time Spent In Foreground | 8 | Represents range from 75 to 100 |
| Time Spent In Foreground | 9 | Represents range from 100 to 200 |
| Time Spent In Foreground | 10 | Represents range from 200 to 300 |
| Time Spent In Foreground | 11 | Represents range from 300 to 400 |
| Time Spent In Foreground | 12 | Represents range from 400 to 500 |
| Time Spent In Foreground | 13 | Represents range from 500 to 600 |
| Time Spent In Foreground | 14 | Represents range from 600 to 700 |
| Time Spent In Foreground | 15 | Represents range from 700 to 800 |
| Time Spent In Foreground | 16 | Represents range from 800 to 900 |
| Time Spent In Foreground | 17 | Represents range from 900 to 1000 |
| Time Spent In Foreground | 18 | Represents range from 1000 to 1500 |
| Time Spent In Foreground | 19 | Represents range from 1500 to 2000 |
| Time Spent In Foreground | 20 | Represents range from 2000 to 2500 |
| Time Spent In Foreground | 21 | Represents range from 2500 to 3000 |
| Time Spent In Foreground | 22 | Represents range from 3000 to 3500 |
| Time Spent In Foreground | 23 | Represents range from 3500 to 4000 |
| Time Spent In Foreground | 24 | Represents range from 4000 to 5000 |
| Time Spent In Foreground | 25 | Represents range from 5000 to 7500 |
| Time Spent In Foreground | 26 | Represents range from 7500 to 10000 |
| Time Spent In Foreground | 27 | Represents range from 10000 to 30000 |
| Time Spent In Foreground | 28 | Represents range from 30000 to 60000 |
| Time Spent In Foreground | 29 | Represents range from 60000 to 90000 |
| Time Spent In Foreground | 30 | Represents range from 90000 to 120000 |
| Time Spent In Foreground | 31 | Represents range from 120000 to 180000 |
| Time Spent In Foreground | 32 | Represents range from 180000 to +Infinity |

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

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/bluetooth-le-scans)*