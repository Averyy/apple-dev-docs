# iOS & iPadOS 27.3 Beta Release Notes

**Framework**: iOS & iPadOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

The iOS & iPadOS 27.3 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 27.3 beta. The SDK comes bundled with Xcode 27.3. For information on the compatibility requirements for Xcode 27.3, see [Xcode 27.3 Release Notes](../Xcode-Release-Notes/xcode-27_3-release-notes.md).

### App Intents

#### Known Issues

- If you define `authenticationPolicy` on an `AppEntity` or `AppEntity` property that requires unlock, Siri AI might not request an unlock before it displays these entities. (190573761)

### Live Caller ID Lookup

#### New Features

- The system now keeps a set of unused evaluation keys uploaded to your Live Caller ID Lookup service, and when it runs out of pre-uploaded keys, it automatically falls back to sending a fresh evaluation key inline with the query. When a query includes an evaluation key, your service must use it directly instead of looking one up by the user identifier. (187726157)

#### Deprecations

- Live Caller ID Lookup now requires the shard count in a service’s PIR configuration to be a power of two, for example 256, 512, 1024, or 2048. The system rejects a configuration whose shard count isn’t a power of two. Configurations that already use a power-of-two shard count work with earlier releases and need no changes. (191651833)

### NEURLFilter

#### New Features

- The system now keeps a set of unused evaluation keys uploaded to your NEURLFilter PIR service, and when it runs out of pre-uploaded keys, it automatically falls back to sending a fresh evaluation key inline with the query. When a query includes an evaluation key, your service must use it directly instead of looking one up by the user identifier. (187726173)

#### Deprecations

- NEURLFilter no longer supports user tiers. The system no longer calls your service’s `/token-key-for-user-token` endpoint and instead uses the first valid public key in your Privacy Pass token issuer directory. (191651440)
- NEURLFilter now limits a service’s PIR configuration to at most 65,536 shards and requires the shard count to be a power of two, for example, 256, 512, 1024, or 2048. The system rejects a configuration that exceeds the limit or whose shard count isn’t a power of two. Configurations that already meet both constraints work with earlier releases and need no changes. (191651462)
- Your NEURLFilter service URL and Privacy Pass issuer URL must now be declared statically in your app’s Info.plist, and providing them only at runtime is deprecated. Add an `NSPIRConfiguration` dictionary to your app’s Info.plist (not the URL filter extension’s) with a `PIRServerURL` key and a `PrivacyPassIssuerURL` key. `PIRServerURL` corresponds to `pirServerURL`, and `PrivacyPassIssuerURL` corresponds to `pirPrivacyPassIssuerURL` and defaults to `PIRServerURL` when absent. Each value should contain only the host name of your server. If you also set these values at runtime, they must match the Info.plist values exactly, or the system fails to start the filter with an invalid configuration error. (191651632)

### StoreKit

#### New Features

- Multiseat subscriptions let a customer purchase multiple seats for an auto-renewable subscription and invite others to join it. Check whether a subscription supports multiseat purchases through the new `supportsMultiSeatPurchase` property on `Product` and `AdvancedCommerceProduct`, which reflects the setting you configure in App Store Connect. (164581840)

#### Resolved Issues

- Fixed: If you test Ask to Buy in the Sandbox environment while signed in to an iCloud account that is a member of a Family Sharing group, you might be unable to view or approve sandbox Ask to Buy requests. (190639717)

### StoreKit Testing in Xcode

#### Resolved Issues

- Fixed: Making an in-app purchase for a subscription that is a member of a subscription bundle incorrectly allows the user to unbundle instead of throwing an error. (186018916)

#### Known Issues

- When you launch an app that uses `SKTestSession` for the first time, some StoreKit Test API calls might hang. (186670057) (FB24651858)

  **Workaround:** Set a StoreKit configuration file in your scheme’s run options, then rerun the tests.

### SwiftUI

#### Resolved Issues

- In apps built with the iOS 26 SDK,`ScrollEdgeEffectStyle.soft` rendered a fully transparent edge above a `safeAreaBar(edge:)` when running on iOS 27.  In iOS 27.3 and later, these apps get the iOS 27 soft edge effect. (188312290)

## See Also

### iOS & iPadOS 27
- [iOS & iPadOS 27.2 Release Notes](./ios-ipados-27_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 27 Release Notes](./ios-ipados-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-27_3-release-notes)*