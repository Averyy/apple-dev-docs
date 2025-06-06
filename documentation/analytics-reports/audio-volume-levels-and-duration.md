# Audio Volume Levels and Duration

**Framework**: Analytics Reports

Review how your app uses volume and duration for output audio.

#### Overview

The data in this report contains aggregate information about volume and duration for output audio in your app. Duration is binned into increasing bin sizes to keep resolution on shorter audio sessions. Volume is binned into 16 steps from 0 to 1.

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
| Duration | Index of duration values in seconds | `float` |
| Volume Level | Index of volume levels | `float` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Duration | 0 | Represents range from -Infinity to 1 |
| Duration | 1 | Represents range from 1 to 5 |
| Duration | 2 | Represents range from 5 to 10 |
| Duration | 3 | Represents range from 10 to 30 |
| Duration | 4 | Represents range from 30 to 60 |
| Duration | 5 | Represents range from 60 to 300 |
| Duration | 6 | Represents range from 300 to 1800 |
| Duration | 7 | Represents range from 1800 to 3600 |
| Duration | 8 | Represents range from 3600 to 7200 |
| Duration | 9 | Represents range from 7200 to 18000 |
| Duration | 10 | Represents range from 18000 to 36000 |
| Duration | 11 | Represents range from 36000 to +Infinity |
| Volume Level | 0 | Represents range from -Infinity to 0 |
| Volume Level | 1 | Represents range from 0 to 0.0625 |
| Volume Level | 2 | Represents range from 0.0625 to 0.125 |
| Volume Level | 3 | Represents range from 0.125 to 0.1875 |
| Volume Level | 4 | Represents range from 0.1875 to 0.25 |
| Volume Level | 5 | Represents range from 0.25 to 0.3125 |
| Volume Level | 6 | Represents range from 0.3125 to 0.375 |
| Volume Level | 7 | Represents range from 0.375 to 0.4375 |
| Volume Level | 8 | Represents range from 0.4375 to 0.5 |
| Volume Level | 9 | Represents range from 0.5 to 0.5625 |
| Volume Level | 10 | Represents range from 0.5625 to 0.625 |
| Volume Level | 11 | Represents range from 0.625 to 0.6875 |
| Volume Level | 12 | Represents range from 0.6875 to 0.75 |
| Volume Level | 13 | Represents range from 0.75 to 0.8125 |
| Volume Level | 14 | Represents range from 0.8125 to 0.875 |
| Volume Level | 15 | Represents range from 0.875 to 0.9375 |
| Volume Level | 16 | Represents range from 0.9375 to 1 |
| Volume Level | 17 | Represents range from 1 to +Infinity |

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

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/audio-volume-levels-and-duration)*