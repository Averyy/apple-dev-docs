# Media Device Extension Performance

**Framework**: Analytics Reports

Review Media Device Extension performance in your apps.

#### Overview

The data in this report contains performance measures for Media Device Extension usage. The metrics include Video Start Up Time, Activate to Start Time, and Session Duration. The report presents each measure along with a configuration made up of multiple dimensions.

#### Report Fields

| Report Field | Description | Data Type |
| --- | --- | --- |
| Discovery Sessions | Count of discovery sessions | integer |
| Discovered Devices | Sum of devices discovered per discovery session | integer |
| Device Discovery Time | Average time spent in seconds between discovery start and the first device being discovered | float |
| Activation Events | Count of activation events | integer |
| PIN Authorization Events | Count of events requested to authorize via PIN | integer |
| Password Authorization Events | Count of events requested to authorize via Password | integer |
| Activation Time | Average time spent in seconds between endpoint activation start and endpoint activation complete | float |
| Playback Requests | Count of playback session requests | integer |
| AppLaunch Playback Requests | Count of App Launch playback session requests | integer |
| URL Playback Requests | Count of URL playback session requests | integer |
| Activate to Playback Start Time | Average time spent in seconds between the end of endpoint activation and the initiation of the playback session | float |
| Playback Startup Time | Average time spent in seconds from initiation of the playback session to the start of playback of the first item | float |
| Playback Duration | Average duration in seconds that the Media Device Extension session was active | float |
| Realtime Requests | Count of realtime session requests | integer |
| Audio Realtime Requests | Count of audio realtime session requests | integer |
| Audio and Video Realtime Requests | Count of audio and video realtime session requests | integer |
| Activate to Realtime Start Time | Average time spent in seconds between the end of endpoint activation and the initiation of the realtime session | float |
| Realtime Startup Time | Average time spent in seconds from initiation of the realtime session to the start of the realtime session | float |
| Good Realtime Sessions | Count of realtime sessions that meet expected quality | integer |
| Bad Realtime Sessions | Count of realtime sessions that do not meet expected quality | integer |
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
- [App Neural Footprint](app-neural-footprint.md)
  Analyze how much memory your process induces the Apple Neural Engine to wire down on your process’s behalf.
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
- [Cellular Plan Provisioning](cellular-plan-provisioning.md)
  Analyze how often people use your app for eSim install and the success rate.
- [Custom Language Model Builds Failed](custom-language-model-builds-failed.md)
  Analyze how often your app-triggered rebuild of a custom language model failed.
- [Display Power Information](display-power-information.md)
  Review your app’s impact on display pixel attributes.
- [Embedding Generation](embedding-generation.md)
  Analyze details about embedding generation throughput in your app.
- [HTTP Live Streaming Playback Errors](http-live-streaming-playback-errors.md)
  Analyze playback errors that your app receives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/analytics-reports/media-device-extension-performance)*