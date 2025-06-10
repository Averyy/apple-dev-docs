# Bundle Resources updates

**Framework**: Updates

Learn about important changes to Bundle Resources.

#### Overview

Browse notable changes in [`Bundle Resources`](https://developer.apple.com/documentation/BundleResources).

#### June 2025

##### New Entitlements

- Include passthrough in screen capture on visionOS with the  [`Passthrough in screen capture`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.screen-capture.include-passthrough) entitlement.
- Enable low-latency wireless networking for streaming game content on visionOS with the  [`Low-Latency Streaming`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.low-latency-streaming) entitlement.
- Manage home device electricity usage with the [`com.apple.developer.energykit`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.energykit) entitlement.
- Access the GPU from a background task with the [`Background GPU Access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.background-tasks.continued-processing.gpu) entitlement.
- Opt in to additional security checks with the [`Hardened Process`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process) entitlement.
- Enable security hardening protections with the [`Enhanced Security`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.enhanced-security-version) entitlement.
- Mark memory the system uses for internal platform state as read only with the [`Enable Read-Only Platform Memory`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.dyld-ro) entitlement.
- Protect memory you use for pointers by opting in to type-aware memory allocation with the [`Hardened Heap`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.hardened-heap) entitlement.
- Opt in to additional platform restrictions with the [`Additional Runtime Platform Restrictions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.platform-restrictions) entitlement.
- Access subscribable or publishable Wi-Fi Aware services with the [`com.apple.developer.wifi-aware`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.wifi-aware) entitlement.
- Indicate that your app is optimized for a carrier-constrained network with the [`com.apple.developer.networking.carrier-constrained.app-optimized`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.carrier-constrained.app-optimized) entitlement.
- Define the category in which your app accesses a carrier-constrained network with the [`com.apple.developer.networking.carrier-constrained.appcategory`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.carrier-constrained.appcategory) entitlement.
- Report the types of identity documents your app provides with the [`Digital Credentials API - Mobile Document Provider`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.identity-document-services.document-provider.mobile-document-types) entitlement.
- Indicate that your app can be the default dialer app on someone’s device with the [`Default Dialer App`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.dialing-app) entitlement.
- Obtain wireless service predictions with the [`Wireless Insights Service Predictions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.wireless-insights.service-predictions) entitlement.
- Indicate that your app can be the default carrier messaging app on someone’s device with the [`Default Carrier Messaging App`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.carrier-messaging-app) entitlement.
- Access the camera region in your visionOS app with the [`Camera Region access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.arkit.camera-region.allow) entitlement.
- Share a coordinate space with other devices with the [`Shared Coordinate Space access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.arkit.shared-coordinate-space.allow) entitlement.
- Stop the system from capturing your app’s content with the [`App-Protected Content`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.protected-content) entitlement.
- Lock your app’s windows in place relative to a person with the [`Follow Mode for Windows`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.window-body-follow) entitlement.
- Add custom adapters to the Foundation Models framework with the [`com.apple.developer.foundation-model-adapter`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.foundation-model-adapter) entitlement.
- Indicate that your app can be the default dialer app on someone’s device with the [`Default Dialer App`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.dialing-app) entitlement.

##### New Information Property List Keys

- Describe why your app tracks an accessory’s position and location with [`NSAccessoryTrackingUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAccessoryTrackingUsageDescription).
- Indicate that the system should automatically download your asset packs and keep them up to date with [`BAHasManagedAssetPacks`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BAHasManagedAssetPacks).
- Use Apple’s service to host your asset packs with [`BAUsesAppleHosting`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BAUsesAppleHosting).
- Identify the app group that your app and extension use to share asset packs with [`BAAppGroupID`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/BAAppGroupID).
- Describe Wi-Fi Aware services your app publishes and subscribes to with [`WiFiAwareServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/WiFiAwareServices).
- Indicate that your app supports game mode with [`LSSupportsGameMode`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/LSSupportsGameMode).

##### Updated Entitlements

- Add the [`com.apple.developer.kernel.increased-memory-limit`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.kernel.increased-memory-limit) entitlement to your visionOS app.

##### Updated Information Property List Keys

- Indicate that your visionOS app supports spatial gamepads with [`GCSupportedGameControllers`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/GCSupportedGameControllers).

#### June 2024

##### New Entitlements

- Enable access to a Personalized Sound Profile to allow the app to use the information in the profile to render audio with [`com.apple.developer.spatial-audio.profile-access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.spatial-audio.profile-access).
- Enable access to head tracking info to allow an app to render audio with head tracking with [`com.apple.developer.coremotion.head-pose`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.coremotion.head-pose).
- Allow CoreMIDI to match MIDIDriverKit drivers with devices that support MIDI with [`com.apple.developer.driverkit.family.midi`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.driverkit.family.midi).

##### Updated Entitlement

- Define the app category to enable Cellular Network Slicing with [`5G Network Slicing App Category`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.slicing.appcategory). To set the application category for streaming apps, use `streaming-9001`. You can also set the category to `gaming-6014` for gaming apps, and `communication-9000` for communication apps.

##### New Infoplist Keys

- Indicate if the game app bypasses system spatial audio with [`AVGameBypassSystemSpatialAudio`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/AVGameBypassSystemSpatialAudio).
- Indicate to the system that your app receives copies of re-engagement postbacks, a type of postback introduced in iOS 17.5, with [`EligibleForAdAttributionKitReengagementPostbackCopies`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/EligibleForAdAttributionKitReengagementPostbackCopies).
- Indicate to the system that your app supports the Music Haptics feature with [`MusicHapticsSupported`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/MusicHapticsSupported).
- Indicate to the system the interfaces AccessorySetupKit uses to discover and configure accessories using Bluetooth or Wi-Fi with [`NSAccessorySetupSupports`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAccessorySetupSupports).
- Provide the company identifier for a Bluetooth accessory when enabling the use of AccessorySetupKit via `NSAccessorySetupKitEnabled` with [`NSAccessorySetupBluetoothCompanyIdentifiers`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAccessorySetupBluetoothCompanyIdentifiers).
- Provide the name for a Bluetooth accessory when enabling the use of AccessorySetupKit via `NSAccessorySetupKitEnabled` with [`NSAccessorySetupBluetoothNames`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAccessorySetupBluetoothNames).
- Provide the services for a Bluetooth accessory when enabling the use of AccessorySetupKit via `NSAccessorySetupKitEnabled` with [`NSAccessorySetupBluetoothServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSAccessorySetupBluetoothServices).
- Provide a message that tells the user why the app requests access to financial data stored in Wallet with [`NSFinancialDataUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSFinancialDataUsageDescription).
- Track “finished” consumable in-app purchases in StoreKit and return the transactions when iterating the `Transaction` APIs with [`SKIncludeConsumableInAppPurchaseHistory`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/SKIncludeConsumableInAppPurchaseHistory).

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

*[View on Apple Developer](https://developer.apple.com/documentation/updates/bundleresources)*