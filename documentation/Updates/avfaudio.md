# AVFAudio updates

**Framework**: Updates  
**Role**: Article

Learn about important changes to AVFAudio.

#### Overview

Browse notable changes in [AVFAudio](../AVFAudio/AVFAudio.md).

#### June 2024

##### Spatial audio with AVAudioEngine

- Adjust the [`AVAudioEnvironmentNode`](../AVFAudio/avaudioenvironmentnode.md) orientation to match someone’s head pose via compatible AirPods by setting the new [`isListenerHeadTrackingEnabled`](../AVFAudio/avaudioenvironmentnode/islistenerheadtrackingenabled.md) property to `true`. The system requires your app to have the [`com.apple.developer.coremotion.head-pose`](../BundleResources/entitlements/com.apple.developer.coremotion.head-pose.md) entitlement to observe this property.
- Tailor [`AVAudioEnvironmentNode`](../AVFAudio/avaudioenvironmentnode.md) output according to a person’s personalized spatial audio profile that they configure in Settings by adding the [`com.apple.developer.spatial-audio.profile-access`](../BundleResources/entitlements/com.apple.developer.spatial-audio.profile-access.md) entitlement to your app.
- Instruct [`AVAudioEnvironmentNode`](../AVFAudio/avaudioenvironmentnode.md) to ignore the new system spatial audio toggle in Control Center by adding the [`AVGameBypassSystemSpatialAudio`](../BundleResources/information-property-list/avgamebypasssystemspatialaudio.md) key to your app’s `Info.plist`.

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
- [AVFoundation updates](./avfoundation.md)
  Learn about important changes to AVFoundation.
- [AVKit updates](./avkit.md)
  Learn about important changes to AVKit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/avfaudio)*