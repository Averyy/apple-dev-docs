# macOS 27.3 Golden Gate Beta Release Notes

**Framework**: macOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

The macOS 27.3 SDK provides support to develop apps for Mac computers running macOS 27.3 Golden Gate beta. The SDK comes bundled with Xcode 27.3. For information on the compatibility requirements for Xcode 27.3, see [Xcode 27.3 Release Notes](../Xcode-Release-Notes/xcode-27_3-release-notes.md).

### DriverKit

#### New Features

- DriverKit 27.3 adds `IOUserSCSIParallelInterfaceController::UserCopyDataBuffer`, which supersedes the deprecated `UserGetDataBuffer` and has the same API interface. `UserCopyDataBuffer` returns the buffer at +1, so you must release it when you finish. (190089334)

#### Deprecations

- `IOUserSCSIParallelInterfaceController::UserGetDataBuffer` is deprecated in DriverKit 27.3 because it leaks memory. Use `UserCopyDataBuffer` instead. `UserCopyDataBuffer` returns the buffer at +1, so you must release it when you finish. (184905119) (FB24326124)

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

### StoreKit Testing in Xcode

#### Resolved Issues

- Fixed: Making an in-app purchase for a subscription that is a member of a subscription bundle incorrectly allows the user to unbundle instead of throwing an error. (186018916)

#### Known Issues

- When you launch an app that uses `SKTestSession` for the first time, some StoreKit Test API calls might hang. (186670057) (FB24651858)

  **Workaround:** Set a StoreKit configuration file in your scheme’s run options, then rerun the tests.

## See Also

### macOS 27
- [macOS 27.2 Golden Gate Release Notes](./macos-27_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS 27 Golden Gate Release Notes](./macos-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-27_3-release-notes)*