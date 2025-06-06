# Audio Toolbox updates

**Framework**: Updates

Learn about important changes to Audio Toolbox.

#### Overview

Browse notable changes in [`Audio Toolbox`](https://developer.apple.com/documentation/AudioToolbox).

#### June 2024

##### Spatial Audio with Auspatialmixer

- Adjust the spatial mixer orientation to match someone’s head pose via compatible AirPods by setting the new [`kAudioUnitProperty_SpatialMixerEnableHeadTracking`](https://developer.apple.com/documentation/AudioToolbox/kAudioUnitProperty_SpatialMixerEnableHeadTracking) property to `true`. The system requires your app to have the [`com.apple.developer.coremotion.head-pose`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.coremotion.head-pose) entitlement to observe this property.
- Tailor spatial mixing output according to a person’s personalized spatial audio profile that they configure in Settings by adding the [`com.apple.developer.spatial-audio.profile-access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.spatial-audio.profile-access) entitlement to your app.
- Instruct spatial mixing to ignore the new system spatial audio toggle in Control Center by adding the [`AVGameBypassSystemSpatialAudio`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/AVGameBypassSystemSpatialAudio) key to your app’s `Info.plist`.

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
- [Core Location updates](corelocation.md)
  Learn about important changes to Core Location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/audiotoolbox)*