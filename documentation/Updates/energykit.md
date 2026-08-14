# EnergyKit updates

**Framework**: Updates

Learn about important changes to EnergyKit.

#### Overview

Browse notable changes in [`EnergyKit`](https://developer.apple.com/documentation/energykit).

#### June 2026

##### Electric Vehicle Charging Behavior

- Track and explain electric vehicle charging behavior with [`ElectricVehicleStatusEvent`](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent), which provides discrete snapshots that capture why a vehicle isn’t charging when connected, when charging will begin, and why charging started or stopped.
- Use `ElectricVehicleChargingReason` to explain charging state transitions. The framework provides `ActiveReason` for reasons why charging starts or resumes, and `IdleReason` for reasons why the vehicle remains idle when connected to a charger.
- Define charging targets with [`ElectricVehicleStatusEvent.ChargingTarget`](https://developer.apple.com/documentation/energykit/electricvehiclestatusevent/chargingtarget-swift.struct) to show when charging begins and when it will complete, including the target charge, scheduled start time, and estimated completion time.

##### Device Identification

- Identify electrical load devices with type safety using [`ElectricalLoadDevice`](https://developer.apple.com/documentation/energykit/electricalloaddevice).
- Access device names through the [`deviceName`](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/devicename) property for electric vehicles, and the [`deviceName`](https://developer.apple.com/documentation/energykit/electrichvacloadevent/devicename) property for HVAC devices.

##### Performance Metrics

- Estimate driving range and battery temperature to give more context about a charging session using [`ElectricVehicleLoadEvent.ElectricalMeasurement.PerformanceMetrics`](https://developer.apple.com/documentation/energykit/electricvehicleloadevent/electricalmeasurement/performancemetrics-swift.struct).

##### Home App Integration

- Display your app’s energy data in the Home app by adopting the [`EnergyKit LoadEvents Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.energykit.loadevents-experience). The Home app automatically shows activity logs, historical charts, trend notifications, and whole-home energy usage based on your submitted events.

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

*[View on Apple Developer](https://developer.apple.com/documentation/updates/energykit)*