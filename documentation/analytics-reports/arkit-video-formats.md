# ARKit Video Formats

**Framework**: Analytics Reports

Review information  about ARKit video formats and high-resolution frames.

#### Overview

The data in this report details information about video formats in your application and how many high-resolution frames are captured per session.

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
| Capture Device Position | Position of the capture device | `string` |
| AR Configuration Class | The class of the ARConfiguration, for example, ARWorldTrackingConfiguration or ARFaceTrackingConfiguration | `string` |
| Frame Rate | The configured capturing frame rate | `integer` |
| Frame Resolution | Resolution of the camera stream | `string` |
| Format Binning | Whether the format is nonbinned or binned | `boolean` |
| Video HDR Support | Whether the video format supports high dynamic range (HDR) streaming | `boolean` |
| High-Resolution Frames Captured | The number of captured high-resolution frames in the current session | `integer` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Capture Device Position | Front | Front facing camera |
| Capture Device Position | Back | Back facing camera |
| Capture Device Position | Unknown | Orientation unknown |
| AR Configuration Class | ARWorldTrackingConfiguration | ARWorldTracking Configuration |
| AR Configuration Class | ARFaceTrackingConfiguration | ARFaceTracking Configuration |
| AR Configuration Class | ARGeoTrackingConfiguration | ARGeoTracking Configuration |
| AR Configuration Class | ARPositionalTrackingConfiguration | ARPositionalTracking Configuration |
| AR Configuration Class | ARImageTrackingConfiguration | ARImageTracking Configuration |
| AR Configuration Class | ARBodyTrackingConfiguration | ARBodyTracking Configuration |
| Frame Resolution | 1280x720 | 1280x720 pixel |
| Frame Resolution | 1440x1080 | 1440x1080 pixel |
| Frame Resolution | 1920x1440 | 1920x1440 pixel |
| Frame Resolution | 3840x2160 | 3840x2160 pixel |
| Frame Resolution | 640x480 | 640x480 pixel |
| High-Resolution Frames Captured | 0 | Represents range from -Infinity to 1 |
| High-Resolution Frames Captured | 1 | Represents range from 1 to 5 |
| High-Resolution Frames Captured | 2 | Represents range from 5 to 10 |
| High-Resolution Frames Captured | 3 | Represents range from 10 to 20 |
| High-Resolution Frames Captured | 4 | Represents range from 20 to 50 |
| High-Resolution Frames Captured | 5 | Represents range from 50 to 100 |
| High-Resolution Frames Captured | 6 | Represents range from 100 to 500 |
| High-Resolution Frames Captured | 7 | Represents range from 500 to 1000 |
| High-Resolution Frames Captured | 8 | Represents range from 1000 to 5000 |
| High-Resolution Frames Captured | 9 | Represents range from 5000 to +Infinity |

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
- [ARKit World Tracking](arkit-world-tracking.md)
  Review the configured settings for world tracking in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/arkit-video-formats)*