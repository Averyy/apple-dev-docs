# Streaming Downloads Performance

**Framework**: Analytics Reports

Review download performance when using the AVAssetDownloadTask APIs in your apps.

#### Overview

You can use the [`AVAssetDownloadTask`](https://developer.apple.comhttps://developer.apple.com/documentation/avfoundation/avassetdownloadtask) API and others in [`AVFoundation`](https://developer.apple.comhttps://developer.apple.com/av-foundation) to download the [`HTTP Live Streaming`](https://developer.apple.comhttps://developer.apple.com/streaming) (HLS) content to disk for offline playback. The data in this report contains aggregate information about download performance.

- Privacy Measures: Data for this report is collected from select 3rd party apps. Each data point in this report comes from at least 200 downloads. Data points with fewer downloads are omitted.
- Data Source: Data in this report only comes from devices that opt in to share data with Apple and developers.
- Historical Data: One-time snapshots for this report are available beginning in February 2024, if there are events for the report.

#### Report Fields

| Report Field | Description | Data Type |
| --- | --- | --- |
| Download Count | Total number of downloads | integer |
| Interface Type | Type of network interface for the playback. Values can be of type: `WiFi`, `Cellular`, `Loopback`, `Wired`, `Cache`, or `Unknown`. | string |
| Download Speed Distribution | Distribution of the download speeds, in bits per second. Values are an array of percentiles: 10th, 25th, 50th, 75th, 95th, 99th. | list of float |
| Downloaded Bytes Distribution | Distribution of the total number of bytes downloaded. Values are an array of percentiles: 10th, 25th, 50th, 75th, 95th, 99th. | list of float |
| Download Error Rate | Download failure rate in percentages | float |
| Date | Date when the event occurred | string |
| Territory | Country or region in which the event occurred | string |
| Device | Type of device on which the event occurred | string |
| Platform Version | Operating System (OS) version on the device on which the event occurred | string |
| Build Type | Build type of device on which the event occurred | string |
| Build | Build of device on which the event occurred | string |

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
- [Networking Connection Activity](networking-connection-activity.md)
  Review how your app uses network connections.
- [Spotlight Query Performance](spotlight-query-performance.md)
  Review how your app uses Spotlight queries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/streaming-downloads-performance)*