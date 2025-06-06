# App Runtime Usage

**Framework**: Analytics Reports

Analyze how often your app executes specific symbols of different dynamic libraries.

#### Overview

The data in this report contains aggregated information about the symbols and dynamic library version (dylib) that your app executes.

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
| App Version | Version of the app associated with the event | `string` |
| App Name | Name of the sampled app | `string` |
| Architecture | Architecture of the symbol | `string` |
| Binary Code Directory Hash | Code directory hash of the binary | `string` |
| Binary Path | Path to the currently executing binary | `string` |
| Binary Team ID | Team ID of the binary signature | `string` |
| Binary UUID | Universally unique identifier of the binary | `string` |
| Dynamic Library Code Directory Hash | Code directory hash of the dynamic library | `string` |
| Dynamic Library Path | Path to the dynamic library that contains this symbol | `string` |
| Dynamic Library Team ID | Team ID of the dynamic library signature | `string` |
| Dynamic Library UUID | Universally unique identifier  of the dynamic library from which this symbol comes | `string` |
| Symbol Name | Name of the symbol (if known) | `string` |
| Symbol Offset | Offset for the symbol in the binary | `string` |
| Symbol Count | Number of times symbol appears in this sample | `long` |
| Dynamic Library Version | Version (either bundle version or mach object file format version) of the dynamic library using the symbol | `string` |
| Binary Version | Version (either bundle version or mach object file format version) of the binary calling the symbol | `string` |
| Caller Path | Path to dynamic library that calls this symbol | `string` |
| Caller Symbol Name | Name of the symbol that calls this symbol | `string` |

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
- [ARKit World Tracking](arkit-world-tracking.md)
  Review the configured settings for world tracking in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/app-runtime-usage)*