# Spotlight Query Performance

**Framework**: Analytics Reports

Review how your app uses Spotlight queries.

#### Overview

The data in this report contains information about on-device Spotlight query performance.

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
| Query Kind | The kind of query | `string` |
| Quality of Service Level | The query quality of service  level | `string` |
| Cancel Status | Whether someone canceled the query | `boolean` |
| Protection Class | Protection class of the query | `string` |
| Total Execution Time | The total time of the query from submitting to the scheduler to finish | `float` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Query Kind | DefaultQuery | A normal CoreSpotlight query |
| Query Kind | GroupedTopNQuery | A top-N query with grouped results (SPI) |
| Query Kind | FlatTopNQuery | A top-N query |
| Query Kind | CompletionQuery | Query to request query completions |
| Query Kind | CoalescingCollectingQuery | Query to collect a coalesced result set (unique values of attribute) (SPI) |
| Query Kind | CountingQuery | Query to count the number of results (SPI) |
| Query Kind | GroupedCountingQuery | Query to count the number of results per group (SPI) |
| Quality of Service Level | QOS_CLASS_UNSPECIFIED | OS quality of service level |
| Quality of Service Level | QOS_CLASS_BACKGROUND | OS quality of service level |
| Quality of Service Level | QOS_CLASS_UTILITY | OS quality of service level |
| Quality of Service Level | QOS_CLASS_DEFAULT | OS quality of service level |
| Quality of Service Level | QOS_CLASS_USER_INITIATED | OS quality of service level |
| Quality of Service Level | QOS_CLASS_USER_INTERACTIVE | OS quality of service level |
| Protection Class | NSFileProtectionComplete | Standard file protection mode |
| Protection Class | NSFileProtectionCompleteUnlessOpen | Standard file protection mode |
| Protection Class | NSFileProtectionCompleteUntilFirstUserAuthentication | Standard file protection mode |
| Protection Class | Priority | SPI (no third party data in this class) |
| Total Execution Time | 0 | Represents range from -Infinity to 0.05 |
| Total Execution Time | 1 | Represents range from 0.05 to 0.1 |
| Total Execution Time | 2 | Represents range from 0.1 to 0.15 |
| Total Execution Time | 3 | Represents range from 0.15 to 0.2 |
| Total Execution Time | 4 | Represents range from 0.2 to 0.25 |
| Total Execution Time | 5 | Represents range from 0.25 to 0.3 |
| Total Execution Time | 6 | Represents range from 0.3 to 0.4 |
| Total Execution Time | 7 | Represents range from 0.4 to 0.5 |
| Total Execution Time | 8 | Represents range from 0.5 to 0.6 |
| Total Execution Time | 9 | Represents range from 0.6 to 0.7 |
| Total Execution Time | 10 | Represents range from 0.7 to 0.8 |
| Total Execution Time | 11 | Represents range from 0.8 to 0.9 |
| Total Execution Time | 12 | Represents range from 0.9 to 1 |
| Total Execution Time | 13 | Represents range from 1 to 1.5 |
| Total Execution Time | 14 | Represents range from 1.5 to 2 |
| Total Execution Time | 15 | Represents range from 2 to 2.5 |
| Total Execution Time | 16 | Represents range from 2.5 to 3 |
| Total Execution Time | 17 | Represents range from 3 to 3.5 |
| Total Execution Time | 18 | Represents range from 3.5 to 4 |
| Total Execution Time | 19 | Represents range from 4 to 5 |
| Total Execution Time | 20 | Represents range from 5 to 6 |
| Total Execution Time | 21 | Represents range from 6 to 7 |
| Total Execution Time | 22 | Represents range from 7 to 8 |
| Total Execution Time | 23 | Represents range from 8 to 9 |
| Total Execution Time | 24 | Represents range from 9 to 10 |
| Total Execution Time | 25 | Represents range from 10 to 15 |
| Total Execution Time | 26 | Represents range from 15 to 20 |
| Total Execution Time | 27 | Represents range from 20 to 25 |
| Total Execution Time | 28 | Represents range from 25 to 30 |
| Total Execution Time | 29 | Represents range from 30 to 60 |
| Total Execution Time | 30 | Represents range from 60 to 90 |
| Total Execution Time | 31 | Represents range from 90 to 120 |
| Total Execution Time | 32 | Represents range from 120 to 150 |
| Total Execution Time | 33 | Represents range from 150 to 180 |
| Total Execution Time | 34 | Represents range from 180 to 240 |
| Total Execution Time | 35 | Represents range from 240 to 300 |
| Total Execution Time | 36 | Represents range from 300 to +Infinity |

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
- [Streaming Downloads Performance](streaming-downloads-performance.md)
  Review download performance when using the AVAssetDownloadTask APIs in your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/spotlight-query-performance)*