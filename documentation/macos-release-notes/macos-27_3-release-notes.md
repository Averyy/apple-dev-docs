# macOS 27.3 Golden Gate Beta 2 Release Notes

**Framework**: macOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

The macOS 27.3 SDK provides support to develop apps for Mac computers running macOS 27.3 Golden Gate beta 2. The SDK comes bundled with Xcode 27.3. For information on the compatibility requirements for Xcode 27.3, see [Xcode 27.3 Release Notes](../Xcode-Release-Notes/xcode-27_3-release-notes.md).

### App Intents

#### New Features

- The Video schema domain is now available for apps to integrate with Siri AI on tvOS, iOS, macOS, and visionOS. (189805051)

### Apple Video Podcasts in the TV App

#### New Features

- Apple Video Podcasts are now available in the Apple TV app. Watch full episodes of your favorite video podcasts, and pick up where you left off from Apple Podcasts. (192370477)

### CoreImage

#### New Features

- CIRAWFilter now relies on resources that aren’t included with the operating system. To download them, use the `downloadresources` and `downloadallresources` methods of CIRAWFilter. (190766743)

### DriverKit

#### New Features

- DriverKit 27.3 adds `IOUserSCSIParallelInterfaceController::UserCopyDataBuffer`, which supersedes the deprecated `UserGetDataBuffer` and has the same API interface. `UserCopyDataBuffer` returns the buffer at +1, so you must release it when you finish. (190089334)

#### Deprecations

- `IOUserSCSIParallelInterfaceController::UserGetDataBuffer` is deprecated in DriverKit 27.3 because it leaks memory. Use `UserCopyDataBuffer` instead. (184905119) (FB24326124)

### mBoot

#### Resolved Issues

- Fixed: Only a single core is available when you boot Linux or other third-party operating systems from a custom raw boot object on Mac computers with M5 Pro, M5 Max, and M5 Ultra chips. (182898702) (FB23916610)

### NEURLFilter

#### New Features

- The system now keeps a set of unused evaluation keys uploaded to your NEURLFilter PIR service, and when it runs out of pre-uploaded keys, it automatically falls back to sending a fresh evaluation key inline with the query. When a query includes an evaluation key, your service must use it directly instead of looking one up by the user identifier. (187726173)

#### Deprecations

- NEURLFilter no longer supports user tiers. The system no longer calls your service’s `/token-key-for-user-token` endpoint and instead uses the first valid public key in your Privacy Pass token issuer directory. (191651440)
- NEURLFilter now limits a service’s PIR configuration to at most 65,536 shards and requires the shard count to be a power of two, for example, 256, 512, 1024, or 2048. The system rejects a configuration that exceeds the limit or whose shard count isn’t a power of two. Configurations that already meet both constraints work with earlier releases and need no changes. (191651462)
- Your NEURLFilter service URL and Privacy Pass issuer URL must now be declared statically in your app’s Info.plist, and providing them only at runtime is deprecated. Add an `NSPIRConfiguration` dictionary to your app’s Info.plist (not the URL filter extension’s) with a `PIRServerURL` key and a `PrivacyPassIssuerURL` key. `PIRServerURL` corresponds to `pirServerURL`, and `PrivacyPassIssuerURL` corresponds to `pirPrivacyPassIssuerURL` and defaults to `PIRServerURL` when absent. Each value should contain only the host name of your server. If you also set these values at runtime, they must match the Info.plist values exactly, or the system fails to start the filter with an invalid configuration error. (191651632)

### Privacy & Security

#### New Features

- macOS 27.3 beta 2 introduces increased transparency and more granular options for two APIs: Device Control and Data Access, and Full Disk Access. Before granting an app such extraordinary access, users should understand that it puts all of the data on their Mac at risk. These changes are designed to help them do that and to empower them to make informed decisions about their own data and privacy. The changes include:

  - A split of Device Control and Data Access into two settings: (1) System & App Protection Override, and (2) Accessibility
  - A single method for granting permissions by selecting the requesting app from a list
  - Guidance to encourage users to grant access to just the specific apps (for System & App Protection Override) or folders (for Full Disk Access) that are required for their workflows
  - Increased visibility into the wide range of data apps will receive access to or control over if full permissions are granted
  - The option for users to configure apps to ask every time they require access
  - A transparency indicator when a requesting app is controlling another app using System & App Protection Override

  You should be prepared to adjust how you onboard users and make sure apps can gracefully handle having access to only a limited set of folders or apps when utilizing these APIs. Users will see these updates when approving new app permission requests. All app permissions previously granted by users will remain in effect.

  If your apps use Full Disk Access for disk backup, or the new Accessibility settings to provide assistive technologies, you can request entitlements to deliver the same experience for new installations that they offered before macOS 27.3. Currently, known apps aren’t affected and will keep the same experience without an entitlement. Additional entitlement details will be available soon. (192585326)

#### Known Issues

- Apps that received permission to control other apps through the new System & App Protection Override setting might encounter issues interacting with Safari and other applications that use WebKit. (192510863)
- Apps that use the CoreGraphics API to post input events, such as mouse and keyboard events, might not display a live activity properly. This issue does not affect apps that use the Accessibility API or apps that install listening event taps. (192728601)

### Rosetta

#### Deprecations

- macOS now notifies users when an audio plug-in or print dialog extension that requires Rosetta is used, and lists these plug-ins in the Intel-based apps list in General settings. To avoid the notification, check with the developer for an Apple silicon version of the plug-in or extension. (180686443)
- macOS now notifies you when you print using a printer driver that requires Rosetta but is not yet updated for Apple silicon. macOS also prompts you to install Rosetta if it isn’t already installed. To avoid notifications, use AirPrint, which is built into most printer models and requires no additional driver installation, or contact the driver developer to learn whether an update for Apple silicon is available or planned. (188594616)

### SCSIControllerDriverKit

#### New Features

- SCSIControllerDriverKit now supports software controllers. A software controller declares itself by setting `kIOPropertySoftwareIOKey` (an `OSBoolean`, from `<IOKit/storage/IOStorageControllerCharacteristics.h>`) through `UserSetHBAProperties()`. The system honors this setting only before controller initialization completes, so it stays fixed for the life of the controller. Such a controller doesn’t create any DMA mappings, and your dext can access the data buffer associated with a particular I/O through the `UserCopyDataBuffer` API. (182426393) (FB23797269)

### Siri

#### Known Issues

- On macOS, Siri cannot find app entities donated to Spotlight by third-party apps unless those entities conform to a schema. (191273925)

### Speech

#### Resolved Issues

- Fixed: An assertion failure occurs when you use `CaptureInputSequenceProvider` in a “Mac (Designed for iPad)” target. (187921017) (FB24862729)

### StoreKit

#### New Features

- Multiseat subscriptions let a customer purchase multiple seats for an auto-renewable subscription and invite others to join it. Check whether a subscription supports multiseat purchases through the new `supportsMultiSeatPurchase` property on `Product` and `AdvancedCommerceProduct`, which reflects the setting you configure in App Store Connect. (164581840)

#### Resolved Issues

- Multiseat invitation and data sharing consent APIs now take the original transaction ID of a multiseat subscription instead of its subscription group ID. `AppStore.presentMultiSeatInvitationSheet(from:originalTransactionID:)`, `AppStore.presentMultiSeatDataSharingConsentSheet(from:originalTransactionID:)`, `Product.SubscriptionInfo.multiSeatDataSharingConsentEligibility(originalTransactionID:)`, and the SwiftUI `multiSeatInvitationSheet(isPresented:originalTransactionID:onCompletion:)` and `multiSeatDataSharingConsentSheet(isPresented:originalTransactionID:onCompletion:)` modifiers accept the `originalID` of the subscription’s transaction, and the `multiSeatDataSharingConsentEligibility` instance property of `Product.SubscriptionInfo` is no longer available. To avoid a missing symbol crash, recompile your app with the latest SDK. (191322945)

### StoreKit Testing in Xcode

#### Resolved Issues

- Fixed: Making an in-app purchase for a subscription that is a member of a subscription bundle incorrectly allows the user to unbundle instead of throwing an error. (186018916)
- Fixed: When you launch an app that uses `SKTestSession` for the first time, some StoreKit Test API calls might hang. (186670057) (FB24651858)

### Testing

#### New Features

- `automationmodetool enable-automationmode-without-authentication` no longer accepts administrator passwords from standard input. Instead, it always prompts for authentication in the UI with biometrics or a password. To enable this mode, log in to the macOS administrator account through the UI and run the command at least once. The setting persists across restarts. (173706149)

## See Also

### macOS 27
- [macOS 27.2 Golden Gate Release Notes](./macos-27_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS 27 Golden Gate Release Notes](./macos-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-27_3-release-notes)*