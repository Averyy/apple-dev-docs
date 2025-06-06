# Networking Connection Activity

**Framework**: Analytics Reports

Review how your app uses network connections.

#### Overview

The data in this report contains information about your application’s use of network connections. This includes bytes sent and received, and duration of connections.

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
| Completion Reason | Network connection completion reason | `string` |
| Download Bytes Bins | Number of bytes, in bins, downloaded during the network connection | `string` |
| Duration In Seconds Bins | Duration in seconds of the network connection | `string` |
| Error | Errors during the network connection | `string` |
| Is Background | Whether the app making the request is in the background when making the network connection call | `boolean` |
| Upload Bytes Bins | Number of bytes, in bins, uploaded during the network connection | `string` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Completion Reason | Success | Successful completion |
| Completion Reason | Failure | Failure |
| Completion Reason | Cancelled | Cancelled |
| Completion Reason | None | Unknown |
| Download Bytes Bins | <=0 | 0 bytes |
| Download Bytes Bins | ]0,1000] | Less than 1KB |
| Download Bytes Bins | ]1000,10000] | 1KB to 10KB |
| Download Bytes Bins | ]10000,100000] | 10KB to 100KB |
| Download Bytes Bins | ]100000,1000000] | 100KB to 1MB |
| Download Bytes Bins | ]1000000,3000000] | 1MB to 3MB |
| Download Bytes Bins | ]3000000,5000000] | 3MB to 5MB |
| Download Bytes Bins | ]5000000,10000000] | 5MB to 10MB |
| Download Bytes Bins | >10000000 | Greater than 10MB |
| Duration In Seconds Bins | <=0 | Few ms |
| Duration In Seconds Bins | ]0,0.5] | Less than 500ms |
| Duration In Seconds Bins | ]0.5,1] | 500ms to 1 second |
| Duration In Seconds Bins | ]1,1.5] | 1 to 1.5 seconds |
| Duration In Seconds Bins | ]1.5,2] | 1.5 to 2 seconds |
| Duration In Seconds Bins | ]2,2.5] | 2 to 2.5 seconds |
| Duration In Seconds Bins | ]2.5,3] | 2.5 to 3 seconds |
| Duration In Seconds Bins | ]3,3.5] | 3 to 3.5 seconds |
| Duration In Seconds Bins | ]3.5,4] | 3.5 to 4 seconds |
| Duration In Seconds Bins | ]4,4.5] | 4 to 4.5 seconds |
| Duration In Seconds Bins | ]4.5,5] | 4.5 to 5 seconds |
| Duration In Seconds Bins | ]5,5.5] | 5 to 5.5 seconds |
| Duration In Seconds Bins | ]5.5,6] | 5.5 to 6 seconds |
| Duration In Seconds Bins | ]6,6.5] | 6 to 6.5 seconds |
| Duration In Seconds Bins | ]6.5,7] | 6.5 to 7 seconds |
| Duration In Seconds Bins | ]7,7.5] | 7 to 7.5 seconds |
| Duration In Seconds Bins | ]7.5,8] | 7.5 to 8 seconds |
| Duration In Seconds Bins | ]8,8.5] | 8 to 8.5 seconds |
| Duration In Seconds Bins | ]8.5,9] | 8.5 to 9 seconds |
| Duration In Seconds Bins | ]9,9.5] | 9 to 9.5 seconds |
| Duration In Seconds Bins | ]9.5,10] | 9.5 to 10 seconds |
| Duration In Seconds Bins | ]10,11] | 10 to 11 seconds |
| Duration In Seconds Bins | ]11,12] | 11 to 12 seconds |
| Duration In Seconds Bins | ]12,13] | 12 to 13 seconds |
| Duration In Seconds Bins | ]13,14] | 13 to 14 seconds |
| Duration In Seconds Bins | ]14,15] | 14 to 15 seconds |
| Duration In Seconds Bins | ]15,16] | 15 to 16 seconds |
| Duration In Seconds Bins | ]16,17] | 16 to 17 seconds |
| Duration In Seconds Bins | ]17,19] | 17 to 19 seconds |
| Duration In Seconds Bins | ]19,21] | 19 to 21 seconds |
| Duration In Seconds Bins | ]21,23] | 21 to 23 seconds |
| Duration In Seconds Bins | ]23,25] | 23 to 25 seconds |
| Duration In Seconds Bins | ]25,30] | 25 to 30 seconds |
| Duration In Seconds Bins | ]30,35] | 30 to 35 seconds |
| Duration In Seconds Bins | ]35,40] | 35 to 40 seconds |
| Duration In Seconds Bins | ]40,45] | 40 to 45 seconds |
| Duration In Seconds Bins | ]45,50] | 45 to 50 seconds |
| Duration In Seconds Bins | ]50,60] | 50 to 60 seconds |
| Duration In Seconds Bins | ]60,120] | 60 to 120 seconds |
| Duration In Seconds Bins | ]120,240] | 120 to 240 seconds |
| Duration In Seconds Bins | ]240,300] | 240 to 300 seconds |
| Duration In Seconds Bins | ]300,600] | 300 to 600 seconds |
| Duration In Seconds Bins | ]600,1800] | 600 to 1800 seconds |
| Duration In Seconds Bins | >1800 | greater than 1800 seconds |
| Error | 0 | No error |
| Error | -1001 | CFURL Error timeout |
| Error | Others | Refer to CFNetworkErrors |
| Upload Bytes Bins | <=0 | 0 bytes |
| Upload Bytes Bins | ]0,1000] | Less than 1KB |
| Upload Bytes Bins | ]1000,10000] | 1KB to 10KB |
| Upload Bytes Bins | ]10000,100000] | 10KB to 100KB |
| Upload Bytes Bins | ]100000,1000000] | 100KB to 1MB |
| Upload Bytes Bins | ]1000000,3000000] | 1MB to 3MB |
| Upload Bytes Bins | ]3000000,5000000] | 3MB to 5MB |
| Upload Bytes Bins | ]5000000,10000000] | 5MB to 10MB |
| Upload Bytes Bins | >10000000 | Greater than 10MB |

## See Also

- [AirPlay Errors](airplay-errors.md)
  Analyze AirPlay errors in your apps.
- [AirPlay Performance](airplay-performance.md)
  Review AirPlay performance in your apps.
- [App Crashes Expanded](app-crashes-expanded.md)
  Analyze the rate at which your app crashes.
- [App Installs Performance](app-installs-performance.md)
  Analyze details about installation success and failure rates for your apps.
- [App Storage Reads and Writes](app-storage-reads-and-writes.md)
  Analyze how often your app uses disk reads and writes.
- [Audio Overloads](audio-overloads.md)
  Analyze how many audio glitches people experience in your app.
- [Bluetooth LE Session Duration](bluetooth-le-session-duration.md)
  Analyze how long your app uses Bluetooth Low Energy (LE) connections.
- [Bluetooth System Wakes](bluetooth-system-wakes.md)
  Analyze details about bluetooth system wakes that your app causes.
- [CAMetalLayer Performance](cametallayer-performance.md)
  Review CAMetalLayer metadata and performance in your app.
- [Custom Language Model Builds Failed](custom-language-model-builds-failed.md)
  Analyze how often your app-triggered rebuild of a custom language model failed.
- [Display Power Information](display-power-information.md)
  Review your app’s impact on display pixel attributes.
- [HTTP Live Streaming Playback Errors](http-live-streaming-playback-errors.md)
  Analyze playback errors that your app receives.
- [Launch Image Over Memory Limit](launch-image-over-memory-limit.md)
  Analyze how often your app fails to load because it’s over the memory limit.
- [Spotlight Query Performance](spotlight-query-performance.md)
  Review how your app uses Spotlight queries.
- [Streaming Downloads Performance](streaming-downloads-performance.md)
  Review download performance when using the AVAssetDownloadTask APIs in your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/networking-connection-activity)*