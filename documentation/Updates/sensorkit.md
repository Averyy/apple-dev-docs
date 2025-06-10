# SensorKit updates

**Framework**: Updates

Learn about important changes to SensorKit.

#### Overview

Browse notable changes in [`SensorKit`](https://developer.apple.com/documentation/SensorKit).

#### March 2024

##### Sensors

- Use the [`electrocardiogram`](https://developer.apple.com/documentation/SensorKit/SRSensor/electrocardiogram) property to collect electrocardiogram (ECG) data samples, and the [`pedometerData`](https://developer.apple.com/documentation/SensorKit/SRSensor/pedometerData) class to get the data.
- Use the [`photoplethysmogram`](https://developer.apple.com/documentation/SensorKit/SRSensor/photoplethysmogram) property to collect photoplethysmogram (PPG) data samples, and the [`SRPhotoplethysmogramOpticalSample`](https://developer.apple.com/documentation/SensorKit/SRPhotoplethysmogramOpticalSample) and [`SRPhotoplethysmogramSample`](https://developer.apple.com/documentation/SensorKit/SRPhotoplethysmogramSample) classes to get the data.

#### June 2023

##### Sensors

- Use the [`faceMetrics`](https://developer.apple.com/documentation/SensorKit/SRSensor/faceMetrics) property to analyze a person’s facial expressions, and the [`SRFaceMetrics`](https://developer.apple.com/documentation/SensorKit/SRFaceMetrics) class to get the data.
- Use the [`heartRate`](https://developer.apple.com/documentation/SensorKit/SRSensor/heartRate) property to collect a person’s heart rate from devices, and the [`CMHighFrequencyHeartRateData`](https://developer.apple.com/documentation/CoreMotion/CMHighFrequencyHeartRateData) class to get the data.
- Use the [`odometer`](https://developer.apple.com/documentation/SensorKit/SRSensor/odometer) property to analyze movements during workouts, and the [`CMOdometerData`](https://developer.apple.com/documentation/CoreMotion/CMOdometerData) class to get the data.
- Use the [`siriSpeechMetrics`](https://developer.apple.com/documentation/SensorKit/SRSensor/siriSpeechMetrics) property to collect data about a person’s voice — such as tenor, pitch, and cadence — and the [`SRSpeechMetrics`](https://developer.apple.com/documentation/SensorKit/SRSpeechMetrics) class to get the data. People who previously authorized speech metric data collection need to reauthorize before data collection can continue.
- Use the [`wristTemperature`](https://developer.apple.com/documentation/SensorKit/SRSensor/wristTemperature) property to collect sequential wrist temperatures while a person is sleeping, and the [`SRWristTemperature`](https://developer.apple.com/documentation/SensorKit/SRWristTemperature) class to get the data.

##### Configuration

- To opt out of collecting data for user activity from sensors in your app, set the [`SRResearchDataGeneration`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SRResearchDataGeneration) key to `NO`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/updates/sensorkit)*