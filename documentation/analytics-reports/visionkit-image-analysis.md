# VisionKit Image Analysis

**Framework**: Analytics Reports

Analyze VisionKit analysis requests on images.

#### Overview

The data in this report shows histograms for the quantity of information found when performing a VisionKit analysis request on an image. The information includes the length of text, the number of visual lookup elements, and the time to parse the machine-readable codes in the image.

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
| Had Error | Whether there was an error | `boolean` |
| Machine-Readable Codes Parse Duration | Time in seconds to parse machine-readable codes | `float` |
| Text Length | Character length of the detected text | `integer` |
| Visual Lookup Count | Number of visual lookup elements found | `integer` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Machine-Readable Codes Parse Duration | 0 | Represents range from -Infinity to 0 |
| Machine-Readable Codes Parse Duration | 1 | Represents range from 0 to 0.2 |
| Machine-Readable Codes Parse Duration | 2 | Represents range from 0.2 to 0.4 |
| Machine-Readable Codes Parse Duration | 3 | Represents range from 0.4 to 0.6 |
| Machine-Readable Codes Parse Duration | 4 | Represents range from 0.6 to 0.8 |
| Machine-Readable Codes Parse Duration | 5 | Represents range from 0.8 to 1 |
| Machine-Readable Codes Parse Duration | 6 | Represents range from 1 to 1.2 |
| Machine-Readable Codes Parse Duration | 7 | Represents range from 1.2 to 1.4 |
| Machine-Readable Codes Parse Duration | 8 | Represents range from 1.4 to 1.6 |
| Machine-Readable Codes Parse Duration | 9 | Represents range from 1.6 to 1.8 |
| Machine-Readable Codes Parse Duration | 10 | Represents range from 1.8 to 2 |
| Machine-Readable Codes Parse Duration | 11 | Represents range from 2 to +Infinity |
| Text Length | 0 | Represents range from -Infinity to 0 |
| Text Length | 1 | Represents range from 0 to 10 |
| Text Length | 2 | Represents range from 10 to 20 |
| Text Length | 3 | Represents range from 20 to 50 |
| Text Length | 4 | Represents range from 50 to 100 |
| Text Length | 5 | Represents range from 100 to 200 |
| Text Length | 6 | Represents range from 200 to 400 |
| Text Length | 7 | Represents range from 400 to 800 |
| Text Length | 8 | Represents range from 800 to 1000 |
| Text Length | 9 | Represents range from 1000 to 1500 |
| Text Length | 10 | Represents range from 1500 to +Infinity |
| Visual Lookup Count | 0 | Represents range from -Infinity to 0 |
| Visual Lookup Count | 1 | Represents range from 0 to 1 |
| Visual Lookup Count | 2 | Represents range from 1 to 2 |
| Visual Lookup Count | 3 | Represents range from 2 to 3 |
| Visual Lookup Count | 4 | Represents range from 3 to 4 |
| Visual Lookup Count | 5 | Represents range from 4 to 5 |
| Visual Lookup Count | 6 | Represents range from 5 to 6 |
| Visual Lookup Count | 7 | Represents range from 6 to 7 |
| Visual Lookup Count | 8 | Represents range from 7 to 8 |
| Visual Lookup Count | 9 | Represents range from 8 to 9 |
| Visual Lookup Count | 10 | Represents range from 9 to 10 |
| Visual Lookup Count | 11 | Represents range from 10 to +Infinity |

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

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/visionkit-image-analysis)*