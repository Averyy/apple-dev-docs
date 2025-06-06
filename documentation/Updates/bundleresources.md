# Bundle Resources updates

**Framework**: Updates

Learn about important changes to Bundle Resources.

#### Overview

Browse notable changes in [`Bundle Resources`](https://developer.apple.com/documentation/BundleResources).

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
- [ContactsUI updates](contactsui.md)
  Learn about important changes to ContactsUI.
- [Core Location updates](corelocation.md)
  Learn about important changes to Core Location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/updates/bundleresources)*