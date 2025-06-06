# Call Services and Call Performance

**Framework**: Analytics Reports

Review your app’s use of call services and call performance.

#### Overview

The data in this report contains information about call performance. It includes details such as call duration, call-termination reason, and call status across different call types.

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
| Call Termination Reason | Reason for call termination. | `string` |
| Call Connected | A Value of ‘True’ indicates call was in connected state, for example, call and audio were established; ‘False’ otherwise. | `boolean` |
| Call Ended | A value of ‘True’ if call terminated; ‘False’ otherwise. | `boolean` |
| Call Grouped | A value of ‘True’ if this was a grouped or conference call; ‘False’  otherwise. | `boolean` |
| Incoming Call | A value of ‘True’ if call was an incoming or received call; ‘False’ if call was outgoing call. | `boolean` |
| Relay | A value of ‘True’ if call was relayed and answered on another device, for example, incoming call notification seen on iPhone and Watch,  and answered on Watch. In this case, the call is still ongoing in iPhone but relayed to Watch. ‘False’ otherwise. | `boolean` |
| Normal Call End | A value of ‘True’ if call termination was normal termination, for example, no error or failure case; ‘False’ if call terminated due to error or failure. | `boolean` |
| Call Duration | Duration, in milliseconds, from call-start to call-end. | `integer` |
| Spam | The category for spam call. | `string` |
| Spam Risk | The spam risk level associated with the received spam calls. | `string` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Call Termination Reason | NoReason | No Reason |
| Call Termination Reason | AnsweredElsewhere | Answered Elsewhere |
| Call Termination Reason | Declined | Declined |
| Call Termination Reason | DeclinedElsewhere | Declined Elsewhere |
| Call Termination Reason | DeclinedWithText | Declined With Text |
| Call Termination Reason | RemoteUnavailable | Remote Unavailable |
| Call Termination Reason | RemoteHangup | Remote Hangup |
| Call Termination Reason | HandedOff | Handed Off |
| Call Termination Reason | RelayFailedConferenceFailed | Relay Failed Conference Failed |
| Call Termination Reason | RelayFailedNoRelayDevice | Relay Failed No Relay Device |
| Call Termination Reason | HostDeviceBusy | Host Device Busy |
| Call Termination Reason | ComponentCrashed | Component Crashed |
| Call Termination Reason | RelayFailedRelayDeviceRelayNotEnabled | Relay Failed Relay Device Relay Not Enabled |
| Call Termination Reason | NoLocalLink | No Local Link |
| Call Termination Reason | CallFailed | Call Failed |
| Call Termination Reason | RemoteBusy | Remote Busy |
| Call Termination Reason | ClientDeviceBusy | Client Device Busy |
| Call Termination Reason | DialFailed | Dial Failed |
| Call Termination Reason | AccountUnsupported | Account Unsupported |
| Call Termination Reason | NetworkUnsupported | Network Unsupported |
| Call Termination Reason | MMIOrUSSDLikely | MMI Or USSD Likely |
| Call Termination Reason | FilteredOut | Filtered Out |
| Call Termination Reason | ProviderCrashed | Provider Crashed |
| Call Termination Reason | MediaStartFailed | Media Start Failed |
| Call Termination Reason | MediaServerCrashed | Media Server Crashed |
| Call Termination Reason | ManagedDevicePolicyRestricted | Managed Device Policy Restricted |
| Call Termination Reason | Kicked | Kicked |
| Call Termination Reason | LetMeInRequestRejected | Let Me In Request Rejected |
| Call Termination Reason | InvalidConversationLink | Invalid Conversation Link |
| Call Termination Reason | ConversationLinksDisabled | Conversation Links Disabled |
| Call Termination Reason | NoDestinationsAvailable | No Destinations Available |
| Call Termination Reason | CallFailedNilCallProvider | Call Failed Nil Call Provider |
| Call Termination Reason | ApplicationNotForegrounded | Application Not Foregrounded |
| Call Termination Reason | AVConferencedCrashed | AV Conferenced Crashed |
| Call Termination Reason | CallAgain | Call Again |
| Call Termination Reason | UnknownParticipantAdded | Unknown Participant Added |
| Call Termination Reason | CallScreeningTimeout | Call Screening Timeout |
| Call Termination Reason | VisionCallEstablishmentVersionMismatch | Vision Call Establishment Version Mismatch |
| Call Termination Reason | DecryptionTimeout | Decryption Timeout |
| Call Termination Reason | IDSQueryRatelimited | IDS Query Rate limited |
| Call Duration | 0 | Represents range from -Infinity to 0 |
| Call Duration | 1 | Represents range from 0 to 5000 |
| Call Duration | 2 | Represents range from 5000 to 10000 |
| Call Duration | 3 | Represents range from 10000 to 15000 |
| Call Duration | 4 | Represents range from 15000 to 20000 |
| Call Duration | 5 | Represents range from 20000 to 25000 |
| Call Duration | 6 | Represents range from 25000 to 30000 |
| Call Duration | 7 | Represents range from 30000 to 45000 |
| Call Duration | 8 | Represents range from 45000 to 60000 |
| Call Duration | 9 | Represents range from 60000 to 120000 |
| Call Duration | 10 | Represents range from 120000 to 180000 |
| Call Duration | 11 | Represents range from 180000 to 240000 |
| Call Duration | 12 | Represents range from 240000 to 300000 |
| Call Duration | 13 | Represents range from 300000 to 360000 |
| Call Duration | 14 | Represents range from 360000 to 420000 |
| Call Duration | 15 | Represents range from 420000 to 480000 |
| Call Duration | 16 | Represents range from 480000 to 540000 |
| Call Duration | 17 | Represents range from 540000 to 600000 |
| Call Duration | 18 | Represents range from 600000 to 1200000 |
| Call Duration | 19 | Represents range from 1200000 to 1800000 |
| Call Duration | 20 | Represents range from 1800000 to +Infinity |
| Spam | business | business |
| Spam | debt-collection | debt-collection |
| Spam | emergency-alert | emergency-alert |
| Spam | fraud | fraud |
| Spam | government | government |
| Spam | health | health |
| Spam | informational | informational |
| Spam | not-for-profit | not-for-profit |
| Spam | personal | personal |
| Spam | political | political |
| Spam | public-service | public-service |
| Spam | prison | prison |
| Spam | spam | spam |
| Spam | spoofed | spoofed |
| Spam | survey | survey |
| Spam | telemarketing | telemarketing |
| Spam | trusted | trusted |
| Spam | none | spam identified but category not set |
| Spam | undefined | carrier sets a category not defined in CB |
| Spam Risk | High | High |
| Spam Risk | Medium | Medium |
| Spam Risk | Low | Low |

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

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/call-services-and-call-performance)*