# Audio Toolbox updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to Audio Toolbox.

#### Overview

Browse notable changes in [Audio Toolbox](../AudioToolbox/AudioToolbox.md).

#### June 2024

##### Spatial audio with AUSpatialMixer

- Adjust the spatial mixer orientation to match someone’s head pose via compatible AirPods by setting the new [`kAudioUnitProperty_SpatialMixerEnableHeadTracking`](../AudioToolbox/kaudiounitproperty_spatialmixerenableheadtracking.md) property to `true`. The system requires your app to have the [`com.apple.developer.coremotion.head-pose`](../BundleResources/entitlements/com.apple.developer.coremotion.head-pose.md) entitlement to observe this property.
- Tailor spatial mixing output according to a person’s personalized spatial audio profile that they configure in Settings by adding the [`com.apple.developer.spatial-audio.profile-access`](../BundleResources/entitlements/com.apple.developer.spatial-audio.profile-access.md) entitlement to your app.
- Instruct spatial mixing to ignore the new system spatial audio toggle in Control Center by adding the [`AVGameBypassSystemSpatialAudio`](../BundleResources/information-property-list/avgamebypasssystemspatialaudio.md) key to your app’s `Info.plist`.

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
- [AuthenticationServices updates](./authenticationservices.md)
  Learn about important changes to AuthenticationServices.
- [AVFAudio updates](./avfaudio.md)
  Learn about important changes to AVFAudio.
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.
- [AVKit updates](./avkit.md)
  Learn about important changes to AVKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/audiotoolbox)*