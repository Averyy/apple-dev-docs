# Verify with Wallet Document Requests

**Framework**: Analytics Reports

Review how your app uses identity and authorization APIs.

#### Overview

The data in this report shows calls to the PKIdentityAuthorizationController requestDocument API by apps requesting identity documents from Wallet.

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
| Address | If set, the app requests the user’s address. The value is the retention period specified by the app (-1 means “indefinite retention”, -2 means “no retention”). | `integer` |
| Age | If set, the app requests the user’s age. The value is the retention period specified by the app (-1 means “indefinite retention”, -2 means “no retention”). | `integer` |
| Age At Least | If set, the app requests whether the user is above a certain age. The value is the retention period specified by the app (-1 means “indefinite retention”, -2 means “no retention”). | `integer` |
| Age at Least Years | If the “ageAtLeast” element is populated, this is the age that the app requests. | `integer` |
| Date of Birth | If set, the app requests the user’s date of birth. The value is the retention period specified by the app (-1 means “indefinite retention”, -2 means “no retention”). | `integer` |
| Document Expiration Date | If set, the app requests the expiration date of the user’s document. The value is the retention period specified by the app (-1 means “indefinite retention”, -2 means “no retention”). | `integer` |
| Family Name | If set, the app requests the user’s family name. The value is the retention period specified by the app (-1 means “indefinite retention”, -2 means “no retention”). | `integer` |
| Driving Privileges | If set, the app requests the user’s driving privileges. The value is the retention period specified by the app (-1 means “indefinite retention”, -2 means “no retention”). | `integer` |
| Document Type | The type of document the app requests | `string` |
| Document Number | If set, the app requests the document number of the user’s document. The value is the retention period specified by the app (-1 means “indefinite retention”, -2 means “no retention”). | `integer` |
| Portrait | If set, the app requests the user’s portrait. The value is the retention period specified by the app (-1 means “indefinite retention”, -2 means “no retention”). | `integer` |
| Outcome | Strings that describe the outcome of the requestDocument call | `string` |
| Is Developer Test ID | If true, the document is a test ID instead of a real ID | `boolean` |
| Issuing Authority | If set, the app requests the issuing authority of the user’s document. The value is the retention period specified by the app (-1 means “indefinite retention”, -2 means “no retention”). | `integer` |
| Given Name | If set, the app requests the user’s given name. The value is the retention period specified by the app (-1 means “indefinite retention”, -2 means “no retention”). | `integer` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Document Type | drivers-license | A US driver’s license |
| Outcome | success | Presentment succeeded |
| Outcome | userCancelled | User cancelled the sheet |
| Outcome | appCancelled | The app cancelled the sheet |
| Outcome | validationFailed | The provided request was invalid |
| Outcome | presentmentFailed | Some other error prevented presentment |

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

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/verify-with-wallet-document-requests)*