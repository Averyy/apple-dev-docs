# Core Location Geofencing

**Framework**: Analytics Reports

Review how your app uses geo fences.

#### Overview

The data in this report contains information about fence radii use by applications.

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
| Event Type | State change of fence, for example, entry or exit | `integer` |
| Fence Radius | Fence radius in meters | `integer` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Event Type | -1 | Unknown |
| Event Type | 0 | Entry |
| Event Type | 1 | Exit |
| Fence Radius | 0 | Represents range from -Infinity to 0 |
| Fence Radius | 1 | Represents range from 0 to 10 |
| Fence Radius | 2 | Represents range from 10 to 20 |
| Fence Radius | 3 | Represents range from 20 to 30 |
| Fence Radius | 4 | Represents range from 30 to 40 |
| Fence Radius | 5 | Represents range from 40 to 50 |
| Fence Radius | 6 | Represents range from 50 to 60 |
| Fence Radius | 7 | Represents range from 60 to 70 |
| Fence Radius | 8 | Represents range from 70 to 80 |
| Fence Radius | 9 | Represents range from 80 to 90 |
| Fence Radius | 10 | Represents range from 90 to 100 |
| Fence Radius | 11 | Represents range from 100 to 120 |
| Fence Radius | 12 | Represents range from 120 to 140 |
| Fence Radius | 13 | Represents range from 140 to 160 |
| Fence Radius | 14 | Represents range from 160 to 180 |
| Fence Radius | 15 | Represents range from 180 to 200 |
| Fence Radius | 16 | Represents range from 200 to 300 |
| Fence Radius | 17 | Represents range from 300 to 400 |
| Fence Radius | 18 | Represents range from 400 to 500 |
| Fence Radius | 19 | Represents range from 500 to 1000 |
| Fence Radius | 20 | Represents range from 1000 to 5000 |
| Fence Radius | 21 | Represents range from 5000 to 10000 |
| Fence Radius | 22 | Represents range from 10000 to 20000 |
| Fence Radius | 23 | Represents range from 20000 to +Infinity |

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

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/core-location-geofencing)*