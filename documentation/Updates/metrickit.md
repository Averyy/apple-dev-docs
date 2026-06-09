# MetricKit updates

**Framework**: Updates

Learn about important changes to MetricKit.

#### Overview

Browse notable changes in [`MetricKit`](https://developer.apple.com/documentation/MetricKit).

#### June 2026

##### Metric Manager

- Adopt [`MetricManager`](https://developer.apple.com/documentation/MetricKit/MetricManager) to receive metric and diagnostic reports through asynchronous sequences. `MetricManager` replaces [`MXMetricManager`](https://developer.apple.com/documentation/MetricKit/MXMetricManager) and its subscriber protocol. For an overview of the MetricKit reporting model, see [`Monitoring app performance with MetricKit`](https://developer.apple.com/documentation/MetricKit/monitoring-app-performance-with-metrickit).
- Receive daily aggregated performance data through [`MetricReport`](https://developer.apple.com/documentation/MetricKit/MetricReport), which conforms to `Codable` and `Sendable` for straightforward serialization and safe cross-actor use.
- Receive event-based diagnostic data through [`DiagnosticReport`](https://developer.apple.com/documentation/MetricKit/DiagnosticReport). Handle each metric type using [`MetricResult`](https://developer.apple.com/documentation/MetricKit/MetricResult). For information on working with metric values and diagnostic data in MetricKit reports, see [`Analyzing app performance with MetricKit`](https://developer.apple.com/documentation/MetricKit/analyzing-app-performance-with-metrickit).

##### State Contextualized Metrics

- Use the [`StateReporting`](https://developer.apple.com/documentation/StateReporting) framework with MetricKit to segment performance data by app-defined states in addition to intervals. For information on integrating the StateReporting framework with MetricKit, see [`Getting started with StateReporting`](https://developer.apple.com/documentation/StateReporting/getting-started-with-statereporting).

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/metrickit)*