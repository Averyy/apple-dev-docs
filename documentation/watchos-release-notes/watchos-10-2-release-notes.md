# watchOS 10.2 Release Notes

**Framework**: watchOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 10.2 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 10.2. The SDK comes bundled with Xcode 15.1, available from the Mac App Store. For information on the compatibility requirements for Xcode 15.1, see [`Xcode 15.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15_1-release-notes).

##### Airdrop

###### Resolved Issues

- Fixed: Sending an AirDrop or using NameDrop to an 17.0 or 17.1 device might fail sporadically.  (117925962)

##### Apple Music

###### Resolved Issues

- Fixed: The Favorite Songs playlist might take a while to appear on some iOS/iPadOS, watchOS, and tvOS devices.  (117219873)

##### Imessage Contact Key Verification

###### New Features

- With iMessage Contact Key Verification, users can choose to further verify that they are messaging only with the people they intend. iMessage Contact Key Verification uses Key Transparency to enable automatic verification that the iMessage key distribution service returns device keys that have been logged to a verifiable and auditable map. When a user enables the feature, they will be notified about any validation errors directly in the Messages conversation transcript and Apple ID Settings. For even higher security, iMessage Contact Key Verification users can compare a contact verification code in person, on FaceTime, or through another secure call. They can also choose to create or edit a contact and save a public key to turn on iMessage Contact Key Verification with that person. All devices signed into your iCloud account must be on the minimum supported version of iOS 17.2 Beta, macOS 14.2 Beta, or watchOS 10.2 Beta. If you wish to keep using other devices on older versions of the OS, you will need to sign out of iMessage on these devices in order to enable contact key verification.  (111356044)

###### Resolved Issues

- Fixed: Users might see that they’re are not eligible to enable Contact Key Verification on some of their upgraded devices.  (117044482)

###### Known Issues

- The Learn More links do not link to Knowledge Base articles during Beta.  (101563811)

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

- Fixed: Resolved an issue with programmatically present an alert or sheet simultaneously with dismissing another sheet. The new alert or sheet would not show. Now it will. If you have code that presents the same sheet programmatically from multiple places in your view hierarchy at the same time, that sheet might no longer appear. Make sure that any `sheet` modifiers that are in the view hierarchy at the same time use distinct `isPresented` or `item` bindings.  (106343561) (FB12038918)
- Fixed: Resolved a possible Swift access conflict crash that could occur with toolbar items.  (113992797)
- Fixed: To prevent unintentional implicit dependency cycles, ImageRenderer no longer sends Observable updates when the image it produces changes. This change  affect the behavior when a dependency is explicitly declared by observing the ImageRenderer’s publisher.  (116836341)

## See Also

- [watchOS 10.6 Release Notes](watchos-10_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 10.5 Release Notes](watchos-10_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 10.4 Release Notes](watchos-10_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 10.3 Release Notes](watchos-10_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 10.1 Release Notes](watchos-10_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 10 Release Notes](watchos-10-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-10_2-release-notes)*