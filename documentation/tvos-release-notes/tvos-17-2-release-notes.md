# tvOS 17.2 Release Notes

**Framework**: tvOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 17.2 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 17.2. The SDK comes bundled with Xcode 15.1, available from the Mac App Store. For information on the compatibility requirements for Xcode 15.1, see [`Xcode 15.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15_1-release-notes).

##### Apple Music

###### Resolved Issues

- Fixed: The Favorite Songs playlist might take a while to appear on some iOS/iPadOS, watchOS, and tvOS devices.  (117219873)

##### Storekit

###### New Features

- New pricing properties `price`, `currency`, and `currencyCode` are now available on [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction). If an offer was applied to the transaction, a new property `offer` is available to see information about it (id, type, payment mode), as well as convenience properties `offerID`, `offerType`, and `offerPaymentMode`.  (106650768)

###### Resolved Issues

- Fixed: The StoreKit 2 Transaction properties `price`, `currency`, and `Offer.paymentMode` now have Optional types.  (116592563)
- Fixed: The StoreKit 2 Transaction properties `price`, `currency`, and `Offer.paymentMode` now have Optional types.  (116809380)
- Fixed an issue causing the refund request “Done” button to not dismiss the sheet when using StoreKit Testing in Xcode.  (117482750)
- Fixed an issue where StoreKit 2 `deviceVerification` was incorrect, which caused transaction verification to fail.  (117689523) (FB13315344)

##### Swift Charts

###### Resolved Issues

- Fixed an issue where a scrollable chart did not respect the initial non-zero binding value passed to `chartScrollPosition`.  (114889276)

##### Swiftui

###### New Features

- Use `_logChanges()` to log causes of SwiftUI view updates. Call the new debugging method `_logChanges()` in the body of a SwiftUI view to log information about why the system is updating the view. For example: ```swift
     struct MyView: View {
         var body: some View {
             #if DEBUG
             let _ = Self._logChanges()
             #endif
             // … rest of view body …
         }
     }
``` As well as the physical property names, “@self” marks that the view value itself has changed, and “@identity” marks that the identity of the view has changed (that is, that the persistent data associated with the view has been recycled for a new instance of the same type). The new `_logChanges()` method is like the existing `_printChanges()` one, except that the new method uses the system console, which is useful in some debugging workflows. Calls to `_logChanges()` log at the info level to the “com.apple.SwiftUI” subsystem with the category “Changed Body Properties”.  (113352555)

###### Resolved Issues

- Fixed: Resolved a possible Swift access conflict crash that could occur with toolbar items.  (113992797)
- Fixed: To prevent unintentional implicit dependency cycles, ImageRenderer no longer sends Observable updates when the image it produces changes. This change  affect the behavior when a dependency is explicitly declared by observing the ImageRenderer’s publisher.  (116836341)

## See Also

- [tvOS 17.6 Release Notes](tvos-17_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.5 Release Notes](tvos-17_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.4 Release Notes](tvos-17_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.3 Release Notes](tvos-17_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 17.1 Release Notes](tvos-17_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 17 Release Notes](tvos-17-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-17_2-release-notes)*