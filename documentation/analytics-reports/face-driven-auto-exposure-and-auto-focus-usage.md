# Face-Driven Auto Exposure and Auto Focus Usage

**Framework**: Analytics Reports

Analyze how people use face-driven auto exposure (AE) and auto focus (AF) in your app.

#### Overview

The data in this report details how often people turn or toggle off face-driven auto exposure (AE) and auto focus (AF) in your apps. Use the data to understand whether usage is related to number of people in the scene, lux levels, clients, or stream format.

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
| Client ID Type | Type of client ID. 0 is unspecified, 1 is unknown external client, 2 is unknown internal client, 3 is camera.app, 4 is messages.app, 5 is FaceTime, 6 is WhatsApp, 7 is FacebookMessengerApp, 8 is Skype, 9 is WeChat, 10 is Measure (new), 11 is Instagram, 12 is Snapchat, 13 is TikTok, 14 is WebEx, 15 is Zoom, 16 is Google Hangouts, 17 is Blue Jeans, 18 is Go To Meeting, 19 is Join.me, 20 is Houseparty, 21 is Cisco Jabber, 22 is Microsoft Teams, 23 is In Call Service, 24 is Meet In One, 25 is Google Meet, 26 is Slack, 27 is QuickTime Player, 28 is Photo Booth, 29 is Tencent, 30 is Discord, 31 is OBS, 32 is Ding Talk, 33 is Sidecar Extension, 34 is ContinuityCaptureD, 35 is DeskView, 36 is Brave Browser, 37 is Chrome, 38 is MS Edge, 39 is Firefox, 40 is Telegram, 41 is Line, 42 is Ecamm, 43 is Camo. | `integer` |

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

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/face-driven-auto-exposure-and-auto-focus-usage)*