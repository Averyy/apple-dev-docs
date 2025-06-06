# AVFAudio updates

**Framework**: Updates

Learn about important changes to AVFAudio.

#### Overview

Browse notable changes in [`AVFAudio`](https://developer.apple.com/documentation/AVFAudio).

#### June 2024

##### Spatial Audio with Avaudioengine

- Adjust the [`AVAudioEnvironmentNode`](https://developer.apple.com/documentation/AVFAudio/AVAudioEnvironmentNode) orientation to match someone’s head pose via compatible AirPods by setting the new [`isListenerHeadTrackingEnabled`](https://developer.apple.com/documentation/AVFAudio/AVAudioEnvironmentNode/isListenerHeadTrackingEnabled) property to `true`. The system requires your app to have the [`com.apple.developer.coremotion.head-pose`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.coremotion.head-pose) entitlement to observe this property.
- Tailor [`AVAudioEnvironmentNode`](https://developer.apple.com/documentation/AVFAudio/AVAudioEnvironmentNode) output according to a person’s personalized spatial audio profile that they configure in Settings by adding the [`com.apple.developer.spatial-audio.profile-access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.spatial-audio.profile-access) entitlement to your app.
- Instruct [`AVAudioEnvironmentNode`](https://developer.apple.com/documentation/AVFAudio/AVAudioEnvironmentNode) to ignore the new system spatial audio toggle in Control Center by adding the [`AVGameBypassSystemSpatialAudio`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/AVGameBypassSystemSpatialAudio) key to your app’s `Info.plist`.

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
- [AVFoundation updates](avfoundation.md)
  Learn about important changes to AVFoundation.
- [Bundle Resources updates](bundleresources.md)
  Learn about important changes to Bundle Resources.
- [ContactsUI updates](contactsui.md)
  Learn about important changes to ContactsUI.
- [Core Location updates](corelocation.md)
  Learn about important changes to Core Location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/avfaudio)*