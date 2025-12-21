# visionOS 26.2 Release Notes

**Framework**: visionOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The visionOS 26.2 SDK provides support for developing apps for Apple Vision Pro devices running visionOS 26.2. The SDK comes bundled with Xcode 26.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.2, see [`Xcode 26.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_2-release-notes).

##### Airdrop

###### Resolved Issues

- Fixed: Devices set to “Everyone” on 26.2 beta 1 are not discoverable by devices on 26.2 beta 2.  (163636875)

##### Game Controller

###### New Features

- Include the new `GCUIEventTypeStylus` option in the bit-mask passed to `GCEventInteraction.handledEventTypes` (UIKit) or `.handlesGameControllerEvents(matching:)` (SwiftUI) if your application needs to handle input from Logitech Muse using the Game Controller framework.  By default, input from Logitech Muse is delivered to your application as UIKit or SwiftUI events.  (160811739)

###### Resolved Issues

- Fixed: The force values reported for the Logitech Muse tip and secondary buttons are not normalized. Use the `GCPhysicalInputExtents` object obtained from the `physicalExtents` property to inspect the range of measurable force values and to scale the normalized value into that range.  (159136834)

##### Instruments

###### Resolved Issues

- Fixed: The Allocations instrument sometimes fails to report reference counting operations for native Swift types.  (163080666)

##### Storekit

###### New Features

- [`AppStore.ageRatingCode`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/appstore/ageratingcode) API provides the current age rating code for your app. Use this property to fetch the age rating and compare it with the last known rating to check for changes.  (160960740)

###### Resolved Issues

- Fixed: An issue prevents the purchase of a subscription using a win-back offer when testing with StoreKit Testing in Xcode.  (162357552) (FB20604848)
- Fixed: `SubscriptionStatus.all` returning old `SubscriptionStatus` after a subscription change.  (163505178)

##### Tv Shareplay

###### Resolved Issues

- Fixed: Users are unable to SharePlay DRM content from the TV app.  (163515064)

## See Also

- [visionOS 26.3 Beta Release Notes](visionos-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 26.1 Release Notes](visionos-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 26 Release Notes](visionos-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_2-release-notes)*