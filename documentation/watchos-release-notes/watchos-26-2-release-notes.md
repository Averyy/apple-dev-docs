# watchOS 26.2 Release Notes

**Framework**: watchOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 26.2 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 26.2. The SDK comes bundled with Xcode 26.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.2, see [`Xcode 26.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_2-release-notes).

##### Instruments

###### Resolved Issues

- Fixed: The Allocations instrument sometimes fails to report reference counting operations for native Swift types.  (163080666)

##### Storekit

###### New Features

- [`AppStore.ageRatingCode`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/appstore/ageratingcode) API provides the current age rating code for your app. Use this property to fetch the age rating and compare it with the last known rating to check for changes.  (160960740)

###### Resolved Issues

- Fixed: An issue prevents the purchase of a subscription using a win-back offer when testing with StoreKit Testing in Xcode.  (162357552) (FB20604848)
- Fixed: `SubscriptionStatus.all` returning old `SubscriptionStatus` after a subscription change.  (163505178)

## See Also

- [watchOS 26.3 Beta Release Notes](watchos-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 26.1 Release Notes](watchos-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 26 Release Notes](watchos-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-26_2-release-notes)*