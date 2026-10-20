# HealthKit updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to HealthKit.

#### Overview

Browse notable changes in [HealthKit](../HealthKit/HealthKit.md).

#### June 2026

##### Workout zones

- Access workout zone data for heart rate and cycling power. Read zone configurations and time-in-zone information from workouts using [`HKWorkoutZoneGroup`](../HealthKit/hkworkoutzonegroup.md).
- Retrieve a person’s preferred zones from Health Settings with [`preferredWorkoutZoneConfiguration(for:)`](../HealthKit/hkhealthstore/preferredworkoutzoneconfiguration%28for%29.md).
- Provide custom zones for specific workouts using [`HKWorkoutZoneConfiguration`](../HealthKit/hkworkoutzoneconfiguration.md).
- Receive real-time zone updates during active workout sessions through [`HKLiveWorkoutBuilderDelegate`](../HealthKit/hkliveworkoutbuilderdelegate.md).

##### Menopause API

- Record and query menopausal state information using point-in-time samples. Track perimenopause, menopause, or confirmed absence of menopausal state with [`menopausalState`](../HealthKit/hkcategorytypeidentifier/menopausalstate.md) and [`HKCategoryValueMenopausalState`](../HealthKit/hkcategoryvaluemenopausalstate.md). See [Recording and querying menopausal state](../HealthKit/recording-and-querying-menopausal-state.md).
- Track bleeding that occurs after menopause using [`bleedingAfterMenopause`](../HealthKit/hkcategorytypeidentifier/bleedingaftermenopause.md). This category type uses [`HKCategoryValueVaginalBleeding`](../HealthKit/hkcategoryvaluevaginalbleeding.md) to record bleeding intensity.

#### June 2025

- Start workout sessions on iOS using [`HKLiveWorkoutBuilder`](../HealthKit/hkliveworkoutbuilder.md).
- Query medications that a person has added to the Health app, using [`HKUserAnnotatedMedicationQueryDescriptor`](../HealthKit/hkuserannotatedmedicationquerydescriptor.md) and the times they’ve logged that medication using [`HKMedicationDoseEventType`](../HealthKit/hkmedicationdoseeventtype.md).

#### September 2024

- Apple Watch Series 10 supports the Shallow Depth and Pressure capability. Use [`underwaterDepth`](../HealthKit/hkquantitytypeidentifier/underwaterdepth.md) and [`waterTemperature`](../HealthKit/hkquantitytypeidentifier/watertemperature.md) to read depth and temperature data from shallow dives.

#### June 2024

##### General

- Create HealthKit apps for VisionOS.
- Associate perceived and estimated exertion values with workouts. Use [`workoutEffortScore`](../HealthKit/hkquantitytypeidentifier/workouteffortscore.md) and [`estimatedWorkoutEffortScore`](../HealthKit/hkquantitytypeidentifier/estimatedworkouteffortscore.md) to read and write exertion data. Use [`relateWorkoutEffortSample(_:with:activity:completion:)`](../HealthKit/hkhealthstore/relateworkouteffortsample%28_,with,activity,completion%29.md) to associate exertion data with a workout, and [`HKWorkoutEffortRelationshipQuery`](../HealthKit/hkworkouteffortrelationshipquery.md) to query for associated exertion data.
- Access water temperature data from swimming workouts. Any Apple Watch Ultra records [`waterTemperature`](../HealthKit/hkquantitytypeidentifier/watertemperature.md) samples during swimming workouts.
- Read and write mental well-being samples using the [`HKStateOfMind`](../HealthKit/hkstateofmind.md), [`HKPHQ9Assessment`](../HealthKit/hkphq9assessment.md), and [`HKGAD7Assessment`](../HealthKit/hkgad7assessment.md) data types.
- Track menstrual flow and intermenstrual bleeding during pregnancy using the [`bleedingDuringPregnancy`](../HealthKit/hkcategorytypeidentifier/bleedingduringpregnancy.md) and [`bleedingAfterPregnancy`](../HealthKit/hkcategorytypeidentifier/bleedingafterpregnancy.md) data types.

#### June 2023

- Now available in iPadOS. Health data automatically synchronizes between a person’s iPhone, iPad, and Apple Watch.
- Create custom, interval-based workouts. You can use either distance or time for the intervals, and sync the intervals to a group, such as a workout class.
- Mirror workout sessions in your iOS app. This includes the ability to control the workout session from the iOS app, and the ability to send data between the iOS and watchOS apps during an active workout session.
- Access batches of higher-rate motion data from Apple Watch. New Core Motion APIs provide 800 Hz accelerometer data and 200 Hz device motion data. Use this data to analyze someone’s motion after performing an action, like swinging a golf club.
- Measure time spent outdoors and average light intensity with new data types.
- Track cycling with new data types for tracking someone’s power, speed, cadence, and functional threshold power.

## See Also

### Technology and frameworks
- [Accelerate updates](./accelerate.md)
  Learn about important changes to Accelerate.
- [Accessibility updates](./accessibility.md)
  Learn about important changes to Accessibility.
- [ActivityKit updates](./activitykit.md)
  Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](./adattributionkit.md)
  Learn about important changes to AdAttributionKit.
- [App Clips updates](./appclips.md)
  Learn about important changes in App Clips.
- [App Intents updates](./appintents.md)
  Learn about important changes in App Intents.
- [AppKit updates](./appkit.md)
  Learn about important changes to AppKit.
- [Apple Intelligence updates](./apple-intelligence.md)
  Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](./applemapsserverapi.md)
  Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](./applepencil.md)
  Learn about important changes to Apple Pencil.
- [ARKit updates](./arkit.md)
  Learn about important changes to ARKit.
- [Audio Toolbox updates](./audiotoolbox.md)
  Learn about important changes to Audio Toolbox.
- [AuthenticationServices updates](./authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/healthkit)*