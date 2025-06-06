# HealthKit updates

**Framework**: Updates

Learn about important changes to HealthKit.

#### Overview

Browse notable changes in [`HealthKit`](https://developer.apple.com/documentation/HealthKit).

#### September 2024

- Apple Watch Series 10 supports the Shallow Depth and Pressure capability. Use [`underwaterDepth`](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/3958703-underwaterdepth) and [`waterTemperature`](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/3958704-watertemperature) to read depth and temperature data from shallow dives.

#### June 2024

##### General

- Create HealthKit apps for VisionOS.
- Associate perceived and estimated exertion values with workouts. Use [`workoutEffortScore`](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/4338081-workouteffortscore) and [`estimatedWorkoutEffortScore`](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/4338078-estimatedworkouteffortscore) to read and write exertion data. Use [`relateWorkoutEffortSample(_:with:activity:completion:)`](https://developer.apple.com/documentation/healthkit/hkhealthstore/4337961-relateworkouteffortsample) to associate exertion data with a workout, and [`HKWorkoutEffortRelationshipQuery`](https://developer.apple.com/documentation/HealthKit/HKWorkoutEffortRelationshipQuery) to query for associated exertion data.
- Access water temperature data from swimming workouts. Any Apple Watch Ultra records [`waterTemperature`](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/3958704-watertemperature) samples during swimming workouts.
- Read and write mental well-being samples using the [`HKStateOfMind`](https://developer.apple.com/documentation/HealthKit/HKStateOfMind), [`HKPHQ9Assessment`](https://developer.apple.com/documentation/HealthKit/HKPHQ9Assessment), and [`HKGAD7Assessment`](https://developer.apple.com/documentation/HealthKit/HKGAD7Assessment) data types.
- Track menstrual flow and intermenstrual bleeding during pregnancy using the [`bleedingDuringPregnancy`](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/4338072-bleedingduringpregnancy) and [`bleedingAfterPregnancy`](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/4338071-bleedingafterpregnancy) data types.

##### June 2023

- Now available in iPadOS. Health data automatically synchronizes between a person’s iPhone, iPad, and Apple Watch.
- Create custom, interval-based workouts. You can use either distance or time for the intervals, and sync the intervals to a group, such as a workout class.
- Mirror workout sessions in your iOS app. This includes the ability to control the workout session from the iOS app, and the ability to send data between the iOS and watchOS apps during an active workout session.
- Access batches of higher-rate motion data from Apple Watch. New Core Motion APIs provide 800 Hz accelerometer data and 200 Hz device motion data. Use this data to analyze someone’s motion after performing an action, like swinging a golf club.
- Measure time spent outdoors and average light intensity with new data types.
- Track cycling with new data types for tracking someone’s power, speed, cadence, and functional threshold power.

## See Also

- [Accelerate updates](accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Intents updates](appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
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
- [Bundle Resources updates](bundleresources.md)
  Learn about important changes to Bundle Resources.
- [ContactsUI updates](contactsui.md)
  Learn about important changes to ContactsUI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/healthkit)*