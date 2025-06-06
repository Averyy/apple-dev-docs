# Location Sessions

**Framework**: Analytics Reports

Review how your app uses Core Location APIs.

#### Overview

The data in this report shows the location usage histogram of apps. The information is made up of multiple dimensions including the daily total of location sessions, counts of delivered locations, durations of the location requests, the desired accuracy the app specified in CoreLocation API, and the achieved accuracy of the delivered locations.

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
| Pauses Location Updates Automatically | The flag describing whether a session allows automatic pausing | `boolean` |
| Duration | The duration of the location session in seconds | `float` |
| Desired Accuracy | The desired accuracy that the app requests | `float` |
| Delivered Locations | The count of locations delivered to the app during the location session | `integer` |
| Session Count | The number of location sessions | `integer` |
| Achieved Accuracy | The location accuracy achieved by the location session | `float` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Desired Accuracy | 0 | Represents range from -Infinity to -3 |
| Desired Accuracy | 1 | Represents range from -3 to -2 |
| Desired Accuracy | 2 | Represents range from -2 to -1 |
| Desired Accuracy | 3 | Represents range from -1 to 0 |
| Desired Accuracy | 4 | Represents range from 0 to 1 |
| Desired Accuracy | 5 | Represents range from 1 to 2 |
| Desired Accuracy | 6 | Represents range from 2 to 3 |
| Desired Accuracy | 7 | Represents range from 3 to 4 |
| Desired Accuracy | 8 | Represents range from 4 to 5 |
| Desired Accuracy | 9 | Represents range from 5 to 6 |
| Desired Accuracy | 10 | Represents range from 6 to 7 |
| Desired Accuracy | 11 | Represents range from 7 to 8 |
| Desired Accuracy | 12 | Represents range from 8 to 9 |
| Desired Accuracy | 13 | Represents range from 9 to 10 |
| Desired Accuracy | 14 | Represents range from 10 to 11 |
| Desired Accuracy | 15 | Represents range from 11 to 12 |
| Desired Accuracy | 16 | Represents range from 12 to 13 |
| Desired Accuracy | 17 | Represents range from 13 to 14 |
| Desired Accuracy | 18 | Represents range from 14 to 15 |
| Desired Accuracy | 19 | Represents range from 15 to 16 |
| Desired Accuracy | 20 | Represents range from 16 to 17 |
| Desired Accuracy | 21 | Represents range from 17 to 18 |
| Desired Accuracy | 22 | Represents range from 18 to 19 |
| Desired Accuracy | 23 | Represents range from 19 to 20 |
| Desired Accuracy | 24 | Represents range from 20 to 21 |
| Desired Accuracy | 25 | Represents range from 21 to 22 |
| Desired Accuracy | 26 | Represents range from 22 to 23 |
| Desired Accuracy | 27 | Represents range from 23 to 24 |
| Desired Accuracy | 28 | Represents range from 24 to 25 |
| Desired Accuracy | 29 | Represents range from 25 to 26 |
| Desired Accuracy | 30 | Represents range from 26 to 27 |
| Desired Accuracy | 31 | Represents range from 27 to 28 |
| Desired Accuracy | 32 | Represents range from 28 to 29 |
| Desired Accuracy | 33 | Represents range from 29 to 30 |
| Desired Accuracy | 34 | Represents range from 30 to 31 |
| Desired Accuracy | 35 | Represents range from 31 to 32 |
| Desired Accuracy | 36 | Represents range from 32 to 33 |
| Desired Accuracy | 37 | Represents range from 33 to 34 |
| Desired Accuracy | 38 | Represents range from 34 to 35 |
| Desired Accuracy | 39 | Represents range from 35 to 36 |
| Desired Accuracy | 40 | Represents range from 36 to 37 |
| Desired Accuracy | 41 | Represents range from 37 to 100 |
| Desired Accuracy | 42 | Represents range from 100 to 200 |
| Desired Accuracy | 43 | Represents range from 200 to 1000 |
| Desired Accuracy | 44 | Represents range from 1000 to 3000 |
| Desired Accuracy | 45 | Represents range from 3000 to 638000 |
| Desired Accuracy | 46 | Represents range from 638000 to 2147483644 |
| Desired Accuracy | 47 | Represents range from 2147483644 to 2147483645 |
| Desired Accuracy | 48 | Represents range from 2147483645 to 2147483646 |
| Desired Accuracy | 49 | Represents range from 2147483646 to 2147483647 |
| Desired Accuracy | 50 | Represents range from 2147483647 to +Infinity |
| Achieved Accuracy | 0 | Represents range from -Infinity to 0 |
| Achieved Accuracy | 1 | Represents range from 0 to 1 |
| Achieved Accuracy | 2 | Represents range from 1 to 2 |
| Achieved Accuracy | 3 | Represents range from 2 to 3 |
| Achieved Accuracy | 4 | Represents range from 3 to 4 |
| Achieved Accuracy | 5 | Represents range from 4 to 5 |
| Achieved Accuracy | 6 | Represents range from 5 to 6 |
| Achieved Accuracy | 7 | Represents range from 6 to 7 |
| Achieved Accuracy | 8 | Represents range from 7 to 8 |
| Achieved Accuracy | 9 | Represents range from 8 to 9 |
| Achieved Accuracy | 10 | Represents range from 9 to 10 |
| Achieved Accuracy | 11 | Represents range from 10 to 11 |
| Achieved Accuracy | 12 | Represents range from 11 to 12 |
| Achieved Accuracy | 13 | Represents range from 12 to 13 |
| Achieved Accuracy | 14 | Represents range from 13 to 14 |
| Achieved Accuracy | 15 | Represents range from 14 to 15 |
| Achieved Accuracy | 16 | Represents range from 15 to 16 |
| Achieved Accuracy | 17 | Represents range from 16 to 17 |
| Achieved Accuracy | 18 | Represents range from 17 to 18 |
| Achieved Accuracy | 19 | Represents range from 18 to 19 |
| Achieved Accuracy | 20 | Represents range from 19 to 20 |
| Achieved Accuracy | 21 | Represents range from 20 to 21 |
| Achieved Accuracy | 22 | Represents range from 21 to 22 |
| Achieved Accuracy | 23 | Represents range from 22 to 23 |
| Achieved Accuracy | 24 | Represents range from 23 to 24 |
| Achieved Accuracy | 25 | Represents range from 24 to 25 |
| Achieved Accuracy | 26 | Represents range from 25 to 26 |
| Achieved Accuracy | 27 | Represents range from 26 to 27 |
| Achieved Accuracy | 28 | Represents range from 27 to 28 |
| Achieved Accuracy | 29 | Represents range from 28 to 29 |
| Achieved Accuracy | 30 | Represents range from 29 to 30 |
| Achieved Accuracy | 31 | Represents range from 30 to 31 |
| Achieved Accuracy | 32 | Represents range from 31 to 32 |
| Achieved Accuracy | 33 | Represents range from 32 to 33 |
| Achieved Accuracy | 34 | Represents range from 33 to 34 |
| Achieved Accuracy | 35 | Represents range from 34 to 35 |
| Achieved Accuracy | 36 | Represents range from 35 to 36 |
| Achieved Accuracy | 37 | Represents range from 36 to 37 |
| Achieved Accuracy | 38 | Represents range from 37 to 100 |
| Achieved Accuracy | 39 | Represents range from 100 to 200 |
| Achieved Accuracy | 40 | Represents range from 200 to 300 |
| Achieved Accuracy | 41 | Represents range from 300 to 500 |
| Achieved Accuracy | 42 | Represents range from 500 to 700 |
| Achieved Accuracy | 43 | Represents range from 700 to 1000 |
| Achieved Accuracy | 44 | Represents range from 1000 to 3000 |
| Achieved Accuracy | 45 | Represents range from 3000 to 638000 |
| Achieved Accuracy | 46 | Represents range from 638000 to 2147483644 |
| Achieved Accuracy | 47 | Represents range from 2147483644 to 2147483645 |
| Achieved Accuracy | 48 | Represents range from 2147483645 to 2147483646 |
| Achieved Accuracy | 49 | Represents range from 2147483646 to 2147483647 |
| Achieved Accuracy | 50 | Represents range from 2147483647 to +Infinity |

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

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/location-sessions)*