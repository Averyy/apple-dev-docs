# CAMetalLayer Performance

**Framework**: Analytics Reports

Review CAMetalLayer metadata and performance in your app.

#### Overview

The data in this report contains metadata and performance information about how your app uses CAMetalLayer.

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
| Bundle Short Version | The short bundle version of the client process. | `string` |
| App Version | Version of the app associated with the event | `string` |
| Layer Name | The name of the layer (if known). | `string` |
| Process Name | The name of the CAMetalLayer client process. | `string` |
| Active Duration | The amount of time, in seconds, that the most active layer in the CAMetalLayer client session actively generates new on-screen content. | `float` |
| Average Height | The average height, in pixels, of the chosen CAMetalLayer over the course of the session. | `float` |
| Average Width | The average width, in pixels, of the chosen CAMetalLayer over the course of the session. | `float` |
| Client Lifetime Duration | The number of seconds the client process existed (estimated). | `float` |
| Lifetime Active Layer Count | The total number of layers observed during the client’s lifetime. | `integer` |
| Presented Frame Command Buffer Count | The number of command buffers associated with presented frames of the chosen CAMetalLayer. | `integer` |
| Presented Frame Count | The number of presented frames, as determined by counting presented CAMetalDrawables of the chosen CAMetalLayer. | `integer` |
| Skipped Frame Count | The number of skipped frames, for example, CAMetalDrawables created but not put on glass. | `integer` |
| Total Presented Drawables Count | The total presented CAMetalDrawables across all CAMetalLayers of the client process, not just the most active CAMetalLayer. This approximates the proportion of the CAMetalDrawables reported. | `integer` |
| On Glass Present Lateness Count | The count of frames that arrived late on glass. | `integer` |
| Presented CPU End-To-End Drawable Total | The total end-to-end CPU walltime, in milliseconds, for all CAMetalDrawables for the chosen layer during the client’s lifetime. | `float` |
| Presented On GPU Walltime Total | The total on-GPU walltime, in milliseconds, attributed to CAMetalDrawables for the chosen layer during the client’s lifetime. | `float` |
| On Glass Present Lateness Total | The total estimated on-glass presentation lateness, in milliseconds, for drawables for the chosen layer during the lifetime of the client process. | `float` |
| Presented GPU End-To-End Drawable Total | The total end-to-end GPU walltime, in milliseconds, for all CAMetalDrawables for the chosen layer during the client’s lifetime. | `float` |
| Presented GPU Done-To-Completed Total | The total amount of time, in milliseconds, spent waiting for drawables to land on glass after GPU work completion from the selected CAMetalLayer. | `float` |
| On Glass Interval Total | The total on-glass interval, in milliseconds, for CAMetalDrawables from the selected CAMetalLayer. | `float` |
| On Glass Interval Count | The total number of on-glass frame (CAMetalDrawables) intervals for the given CAMetalLayer. | `integer` |

#### Glossary

| Dimension | Value | Definition |
| --- | --- | --- |
| Bundle Short Version | ExampleBundleShortVersion.0.1.2 | Placeholder short version |
| App Version | Example.BundleVersion.0.1.2 | Placeholder bundle version |
| Layer Name | ExampleLayerName | Placeholder example layer name |
| Process Name | ExampleProcessName | Placeholder example process name |

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
- [Streaming Downloads Performance](streaming-downloads-performance.md)
  Review download performance when using the AVAssetDownloadTask APIs in your apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/cametallayer-performance)*