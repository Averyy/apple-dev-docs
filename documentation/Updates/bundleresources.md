# Bundle Resources updates

**Framework**: Updates

Learn about important changes to Bundle Resources.

#### Overview

Browse notable changes in [`Bundle Resources`](https://developer.apple.com/documentation/BundleResources).

#### June 2026

##### New Entitlements

- Access Private Cloud Compute in your [`Foundation Models`](https://developer.apple.com/documentation/FoundationModels) app using the [`com.apple.developer.private-cloud-compute`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.private-cloud-compute) entitlement.
- Request insights relating to transactional activities using the [`TrustInsights`](https://developer.apple.com/documentation/TrustInsights) framework with the [`Trust Insights`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.trustinsights.base) entitlement.
- Display energy device names and usage statistics in the Home app using the [`EnergyKit`](https://developer.apple.com/documentation/EnergyKit) framework with the [`EnergyKit LoadEvents Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.energykit.loadevents-experience) entitlement.
- Add suggested actions to your messaging app based on message content with the [`Suggested Actions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.suggested-actions) entitlement and the [`Suggested Actions`](https://developer.apple.com/documentation/SuggestedActions) framework.
- Integrate a third-party media sharing protocol into the system route picker with the [`com.apple.developer.media-device-extension`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.media-device-extension) entitlement.
- Manage access to connected USB devices for macOS and Linux virtual machines with the [`Accessory Access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.accessory-access.usb) entitlement.
- Protect your app against use-after-free vulnerabilities with guard objects, which the system enables automatically when you set [`com.apple.security.hardened-process.enhanced-security-version`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.enhanced-security-version) to version `2` or greater. To turn off guard objects if they impact performance, use the [`com.apple.security.hardened-process.no-guard-objects`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.no-guard-objects) entitlement.

##### New Information Property List Keys

- Declare the media device extension protocols your app supports with [`MDESupportedProtocols`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/MDESupportedProtocols).
- Indicate that your app supports URL-based playback through a media device extension with [`MDESupportsUniversalURLPlayback`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/MDESupportsUniversalURLPlayback).
- Control whether only one view’s gesture recognizers can be active at a time with [`NSViewGestureRecognizerIsExclusive`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSViewGestureRecognizerIsExclusive).
- Declare that your app handles touch input natively, without relying on AppKit’s extra mouse emulation, with [`NSIsTouchNative`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSIsTouchNative).
- Suppress keyboard shortcuts for menu items while any non-exclusive gesture recognizer is active with [`NSGestureRecognizerSuppressesMainMenuActions`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSGestureRecognizerSuppressesMainMenuActions).

##### Updated Entitlements

- Define the app category to enable Cellular Network Slicing with [`5G Network Slicing App Category`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.slicing.appcategory). To set the application category for web browser apps, use `browser-9003`. You can also set the category to `mc-9500` for mission-critical apps that need access to ultra-constrained cellular networks.
- Define the app category for carrier-constrained satellite network access with [`com.apple.developer.networking.carrier-constrained.appcategory`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.networking.carrier-constrained.appcategory). To set the application category for payment apps, use `payment-8015`. You can also set the category to `health-fitness-8014` for health and fitness apps.

#### June 2025

##### New Entitlements

- Include passthrough in screen capture on visionOS with the  [`Passthrough in screen capture`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.screen-capture.include-passthrough) entitlement.
- Enable low-latency wireless networking for streaming game content on visionOS with the  [`Low-Latency Streaming`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.low-latency-streaming) entitlement.
- Manage home device electricity usage with the [`EnergyKit Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.energykit) entitlement.
- Access the GPU from a background task with the [`Background GPU Access`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.background-tasks.continued-processing.gpu) entitlement.
- Opt in to additional security checks with the [`com.apple.security.hardened-process`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process) entitlement.
- Enable security hardening protections with the [`com.apple.security.hardened-process.enhanced-security-version`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.enhanced-security-version) entitlement.
- Mark memory the system uses for internal platform state as read only with the [`com.apple.security.hardened-process.dyld-ro`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.dyld-ro) entitlement.
- Protect memory you use for pointers by opting in to type-aware memory allocation with the [`com.apple.security.hardened-process.hardened-heap`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.hardened-heap) entitlement.
- Opt in to additional platform restrictions with the [`com.apple.security.hardened-process.platform-restrictions`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.hardened-process.platform-restrictions) entitlement.
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
- Lock your app’s windows in place relative to a person with the [`Window Follow Mode`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.window-body-follow) entitlement.
- Add custom adapters to the Foundation Models framework with the doc://com.apple.documentation/documentation/bundleresources/entitlements/com.apple.developer.foundation-model-adapter entitlement.
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