# macOS Tahoe 26.2 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 26.2 SDK provides support to develop apps for Mac computers running Tahoe 26.2. The SDK comes bundled with Xcode 26.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.2, see [`Xcode 26.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_2-release-notes).

##### Airdrop

###### Resolved Issues

- Fixed: Devices set to “Everyone” on 26.2 beta 1 are not discoverable by devices on 26.2 beta 2.  (163636875)

##### Instruments

###### Resolved Issues

- Fixed: The Allocations instrument sometimes fails to report reference counting operations for native Swift types.  (163080666)

##### Rdma Over Thunderbolt

###### New Features

- Enables low-latency communication between Thunderbolt 5 hosts for use cases including distributed AI inference using MLX.  (164123391)

##### Storekit

###### New Features

- [`AppStore.ageRatingCode`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/appstore/ageratingcode) API provides the current age rating code for your app. Use this property to fetch the age rating and compare it with the last known rating to check for changes.  (160960740)

###### Resolved Issues

- Fixed: An issue prevents the purchase of a subscription using a win-back offer when testing with StoreKit Testing in Xcode.  (162357552) (FB20604848)
- Fixed: `SubscriptionStatus.all` returning old `SubscriptionStatus` after a subscription change.  (163505178)

##### Virtualization

###### Resolved Issues

- Fixed: The serial number published for the virtual machine is 0, which prevents iCloud and related applications from functioning correctly.  (163055944)

##### Xcode

###### Deprecations

- Xcode 16.4 requires a Mac running macOS Sequoia 15.3 through macOS Tahoe 26.1.  (164757281)

## See Also

- [macOS Tahoe 26.3 Beta Release Notes](macos-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Tahoe 26.1 Release Notes](macos-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Tahoe 26 Release Notes](macos-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-26_2-release-notes)*