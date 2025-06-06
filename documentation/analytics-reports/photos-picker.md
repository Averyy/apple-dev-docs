# Photos Picker

**Framework**: Analytics Reports

Analyze how people use Photos in your app.

#### Overview

The data in this report details usage of the out-of-process picker provided by Photos.

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
| Did Select Items | Boolean that determines whether items are selected when Photos picker is finished | `boolean` |
| Is Limited Library Picker | Boolean that determines whether the Photos picker is presented as the Limited Library Picker or not | `boolean` |
| Is Single Selection | Boolean that determines whether the Photos picker is in single-selection or multiple-selection mode | `boolean` |
| Accessory Visibility | Accessory visibility of the Photos picker. Accessories include anything between the content and the edge, for example, the navigation bar or the sidebar. | `string` |
| Style | Value that determines the style of the Photos picker | `string` |
| Encoding Policy | Policy that determines the encoding to use given a content type, if multiple encodings are available | `string` |
| Selection Behavior | Value that determines how the Photos picker handles user selection | `string` |
| Has Photo Library Access | Boolean that determines whether the app has library access or not when the Photos picker is presented | `boolean` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Accessory Visibility | none | None |
| Accessory Visibility | top | Top |
| Accessory Visibility | leading | Leading |
| Accessory Visibility | top + leading | Top + Leading |
| Accessory Visibility | bottom | Bottom |
| Accessory Visibility | top + bottom | Top + Bottom |
| Accessory Visibility | leading + bottom | Leading + Bottom |
| Accessory Visibility | top + leading + bottom | Top + Leading + Bottom |
| Accessory Visibility | trailing | Trailing |
| Accessory Visibility | top + trailing | Top + Trailing |
| Accessory Visibility | leading + trailing | Leading + Trailing |
| Accessory Visibility | top + leading + trailing | Top + Leading + Trailing |
| Accessory Visibility | bottom + trailing | Bottom + Trailing |
| Accessory Visibility | top + bottom + trailing | Top + Bottom + Trailing |
| Accessory Visibility | leading + bottom + trailing | Leading + Bottom + Trailing |
| Accessory Visibility | top + leading + bottom + trailing | Top + Leading + Bottom |
| Style | default | Default picker style. |
| Style | compact | Compact picker style (single row). |
| Encoding Policy | automatic | Uses the best encoding determined by the system. |
| Encoding Policy | current | Uses the current encoding to avoid transcoding if possible. |
| Encoding Policy | compatible | Uses the most compatible encoding if possible, even if transcoding is required. |
| Selection Behavior | default | Uses the default selection behavior. |
| Selection Behavior | ordered | Uses the selection order made by the user. Selected items are numbered. |
| Selection Behavior | continuous | Selection can be delivered continuously. |
| Selection Behavior | continuous and ordered | Selection can be delivered continuously and uses the selection order made by the user. Selected assets are numbered. |

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

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/photos-picker)*