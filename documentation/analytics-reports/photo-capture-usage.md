# Photo Capture Usage

**Framework**: Analytics Reports

Analyze how your app uses Photo capture in photos.

#### Overview

The data in this report contains aggregate information about camera metrics that includes details from V5 and smart styles.

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
| Port Type | Port type of the primary camera for camera preview. | `string` |
| Photo Format | Format used by the capture. | `boolean` |
| Delivered Dimension Height | Height of the delivered photo. | `integer` |
| Delivered Dimension Width | Width of the delivered photo. | `integer` |
| Semantic Scene Type | Semantic scene type; possible values are Food, Indoor, Outdoor, and Sunset. | `integer` |
| Camera Posture | Camera posture during still capture; possible values are Unspecified = 0, Portrait = 1, RotatedPortrait = 2,   Landscape = 3, RotatedLandscape = 4, FaceUp = 5, and FaceDown = 6. | `integer` |
| Output File Type | File format of the image captured; possible values are HEIF, JPEG, ProRAW, BayerRAW, and TIFF. | `integer` |
| Smart Style Cast Type | An integer enum that represents the selected smart style cast for the capture. These integers are based on the CMISmartStyleCastType MakerNote enum for smart style cast; possible values are 1: Standard, 2: Neutral, 3: Rose Gold, 4: Amber, 5: Cool Rose, 6: Natural, 7: Quiet, 8: Vibrant, 9: Cozy,10: Ethereal, 11: Dramatic, 12: Luminous, 13: Stark B&W, 14: Gold, and 15: Muted B&W. | `integer` |
| Lux Level | AE-derived lux level for the captured scene. For flash captures, this is the lux level before the pre-flash stage. | `integer` |
| UI Zoom | Zoom value aligned to camera app UI at capture time. | `float` |
| Smart Style Color Bias | Color setting in style with a range from -1 to 1. | `float` |
| Smart Style Tone Bias | Tone setting in style with a range from -1 to 1. | `float` |
| Smart Style Intensity | Intensity setting in style with a range from 0 to 1. | `float` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Port Type | ‘PortTypeBack’ | rear |
| Port Type | ‘PortTypeFront’ | front |
| Port Type | ‘PortTypeBackTelephoto’ | tele |
| Port Type | ‘PortTypeBackSuperWide’ | rear super wide |
| Port Type | ‘PortTypeFrontSuperWide’ | front super wide |
| Lux Level | 0 | Represents range from -Infinity to -1 |
| Lux Level | 1 | Represents range from -1 to 0 |
| Lux Level | 2 | Represents range from 0 to 1 |
| Lux Level | 3 | Represents range from 1 to 2 |
| Lux Level | 4 | Represents range from 2 to 5 |
| Lux Level | 5 | Represents range from 5 to 10 |
| Lux Level | 6 | Represents range from 10 to 21 |
| Lux Level | 7 | Represents range from 21 to 46 |
| Lux Level | 8 | Represents range from 46 to 100 |
| Lux Level | 9 | Represents range from 100 to 215 |
| Lux Level | 10 | Represents range from 215 to 464 |
| Lux Level | 11 | Represents range from 464 to 1000 |
| Lux Level | 12 | Represents range from 1000 to 2154 |
| Lux Level | 13 | Represents range from 2154 to 4641 |
| Lux Level | 14 | Represents range from 4641 to 10000 |
| Lux Level | 15 | Represents range from 10000 to 21544 |
| Lux Level | 16 | Represents range from 21544 to 46415 |
| Lux Level | 17 | Represents range from 46415 to 100000 |
| Lux Level | 18 | Represents range from 100000 to +Infinity |
| UI Zoom | 0 | Represents range from -Infinity to 0 |
| UI Zoom | 1 | Represents range from 0 to 0.49 |
| UI Zoom | 2 | Represents range from 0.49 to 0.51 |
| UI Zoom | 3 | Represents range from 0.51 to 0.6 |
| UI Zoom | 4 | Represents range from 0.6 to 0.7 |
| UI Zoom | 5 | Represents range from 0.7 to 0.8 |
| UI Zoom | 6 | Represents range from 0.8 to 0.9 |
| UI Zoom | 7 | Represents range from 0.9 to 0.99 |
| UI Zoom | 8 | Represents range from 0.99 to 1.01 |
| UI Zoom | 9 | Represents range from 1.01 to 1.19 |
| UI Zoom | 10 | Represents range from 1.19 to 1.21 |
| UI Zoom | 11 | Represents range from 1.21 to 1.49 |
| UI Zoom | 12 | Represents range from 1.49 to 1.51 |
| UI Zoom | 13 | Represents range from 1.51 to 1.99 |
| UI Zoom | 14 | Represents range from 1.99 to 2.01 |
| UI Zoom | 15 | Represents range from 2.01 to 2.49 |
| UI Zoom | 16 | Represents range from 2.49 to 2.51 |
| UI Zoom | 17 | Represents range from 2.51 to 2.99 |
| UI Zoom | 18 | Represents range from 2.99 to 3.01 |
| UI Zoom | 19 | Represents range from 3.01 to 3.99 |
| UI Zoom | 20 | Represents range from 3.99 to 4.01 |
| UI Zoom | 21 | Represents range from 4.01 to 4.99 |
| UI Zoom | 22 | Represents range from 4.99 to 5.01 |
| UI Zoom | 23 | Represents range from 5.01 to 6 |
| UI Zoom | 24 | Represents range from 6 to 7.99 |
| UI Zoom | 25 | Represents range from 7.99 to 8.01 |
| UI Zoom | 26 | Represents range from 8.01 to 10 |
| UI Zoom | 27 | Represents range from 10 to 12 |
| UI Zoom | 28 | Represents range from 12 to 14.99 |
| UI Zoom | 29 | Represents range from 14.99 to 15.01 |
| UI Zoom | 30 | Represents range from 15.01 to 20 |
| UI Zoom | 31 | Represents range from 20 to 24.99 |
| UI Zoom | 32 | Represents range from 24.99 to 25.01 |
| UI Zoom | 33 | Represents range from 25.01 to +Infinity |
| Smart Style Color Bias | 0 | Represents range from -Infinity to -1 |
| Smart Style Color Bias | 1 | Represents range from -1 to -0.8 |
| Smart Style Color Bias | 2 | Represents range from -0.8 to -0.6 |
| Smart Style Color Bias | 3 | Represents range from -0.6 to -0.4 |
| Smart Style Color Bias | 4 | Represents range from -0.4 to -0.2 |
| Smart Style Color Bias | 5 | Represents range from -0.2 to -0.01 |
| Smart Style Color Bias | 6 | Represents range from -0.01 to 0.01 |
| Smart Style Color Bias | 7 | Represents range from 0.01 to 0.2 |
| Smart Style Color Bias | 8 | Represents range from 0.2 to 0.4 |
| Smart Style Color Bias | 9 | Represents range from 0.4 to 0.6 |
| Smart Style Color Bias | 10 | Represents range from 0.6 to 0.8 |
| Smart Style Color Bias | 11 | Represents range from 0.8 to 1 |
| Smart Style Color Bias | 12 | Represents range from 1 to +Infinity |
| Smart Style Tone Bias | 0 | Represents range from -Infinity to -1 |
| Smart Style Tone Bias | 1 | Represents range from -1 to -0.8 |
| Smart Style Tone Bias | 2 | Represents range from -0.8 to -0.6 |
| Smart Style Tone Bias | 3 | Represents range from -0.6 to -0.4 |
| Smart Style Tone Bias | 4 | Represents range from -0.4 to -0.2 |
| Smart Style Tone Bias | 5 | Represents range from -0.2 to -0.01 |
| Smart Style Tone Bias | 6 | Represents range from -0.01 to 0.01 |
| Smart Style Tone Bias | 7 | Represents range from 0.01 to 0.2 |
| Smart Style Tone Bias | 8 | Represents range from 0.2 to 0.4 |
| Smart Style Tone Bias | 9 | Represents range from 0.4 to 0.6 |
| Smart Style Tone Bias | 10 | Represents range from 0.6 to 0.8 |
| Smart Style Tone Bias | 11 | Represents range from 0.8 to 1 |
| Smart Style Tone Bias | 12 | Represents range from 1 to +Infinity |
| Smart Style Intensity | 0 | Represents range from -Infinity to 0 |
| Smart Style Intensity | 1 | Represents range from 0 to 0.01 |
| Smart Style Intensity | 2 | Represents range from 0.01 to 0.1 |
| Smart Style Intensity | 3 | Represents range from 0.1 to 0.2 |
| Smart Style Intensity | 4 | Represents range from 0.2 to 0.3 |
| Smart Style Intensity | 5 | Represents range from 0.3 to 0.4 |
| Smart Style Intensity | 6 | Represents range from 0.4 to 0.5 |
| Smart Style Intensity | 7 | Represents range from 0.5 to 0.6 |
| Smart Style Intensity | 8 | Represents range from 0.6 to 0.7 |
| Smart Style Intensity | 9 | Represents range from 0.7 to 0.8 |
| Smart Style Intensity | 10 | Represents range from 0.8 to 0.9 |
| Smart Style Intensity | 11 | Represents range from 0.9 to 1 |
| Smart Style Intensity | 12 | Represents range from 1 to +Infinity |

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

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/photo-capture-usage)*