# macOS Sonoma 14.4 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 14.4 SDK provides support to develop apps for Mac computers running Sonoma 14.4. The SDK comes bundled with Xcode 15.3, available from the Mac App Store. For information on the compatibility requirements for Xcode 15.3, see [`Xcode 15.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15_3-release-notes).

##### Appkit

###### Resolved Issues

- Fixed an issue where center or right aligned NSTextField appears blurry.  (120819010)
- Fixed: Resolves an issue where pointer style does not update when browsing in Safari.  (121131986)

##### Core Audio

###### Known Issues

- To improve security and stability, using launchctl kickstart -k is no longer permitted for critical system processes. If a process must be forcefully terminated, it is recommended to use kill instead.  (123028502)

##### Core Ml

###### New Features

- ML Program models that are loaded with `MLComputeUnits.cpuOnly` will use a new high performance CPU backend that takes advantage of Accelerate framework’s BNNS library.  (114037934)

##### Createml

###### Resolved Issues

- Fixed: When using the transfer learning algorithm option, the CreateML app and framework object detection template might fail to converge and cause poor model quality and produce more than expected false positives.  (114480994)

##### Finder

###### Resolved Issues

- Fixed: Resolves an issue where tiling a window causes the desktop picture to turn black.  (118044617)

##### Messages

###### Resolved Issues

- Fixed: Stickers (Memoji and 3rd party) might appear blank.  (120994483)

##### Passkeys

###### Resolved Issues

- Fixed: Registering passkeys might not work on certain websites.  (122217903)

##### Software Updates

###### Resolved Issues

- Fixed: Updates to macOS 14.4 starting from macOS 11.0–12.3.1 will not work.  (120548971)

##### Storekit

###### New Features

- `productDescriptionHidden(_:)` API can be used to configure the visibility of product descriptions in `ProductView`, `StoreView` and `SubscriptionStoreView` instances within a view hierarchy. When building with Xcode 15.3, the view modifier can be used even if your app is running on iOS 17.0, iPadOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, visionOS 1.0, or later. When implementing a product view style, it can support this new view modifier by checking the `descriptionVisibility` property on the configuration value.  (110414819) (FB12261973)
- You can use [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) to present promotional offers by adding the `subscriptionPromotionalOffer(offer:signature:)` modifier. If you’re already using [`inAppPurchaseOptions(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/inapppurchaseoptions(_:)) modifier to support promotional offers for StoreKit views, you should adopt the new API instead when your app is running on iOS 17.4, iPadOS 17.4, macOS 14.4, tvOS 17.4, watchOS 10.4, visionOS 1.1 or later. Do not use both APIs to apply a promotional offer for the same view.  (115358806)

###### Resolved Issues

- Fixed: The [`isEligibleForIntroOffer`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/3803203-iseligibleforintrooffer) property and [`isEligibleForIntroOffer(for:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/3791958-iseligibleforintrooffer) method now reflect ineligibility in cases where a customer would otherwise be eligible for the offer if they weren’t actively subscribed. This means a customer which is not currently eligible for an introductory offer may become eligible in the future. Customers who redeem an introductory offer for a given subscription group will continue to never be eligible for another introductory offer in that subscription group. You can detect this case this by checking if any one transaction with a matching [`subscriptionGroupID`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/3749718-subscriptiongroupid) has the [`type`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/offer/4307073-type) property on [`offer`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/4307076-offer) set to [`introductory`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/offertype/3822309-introductory).  (103604770) (FB11889732)

##### Swiftui

###### New Features

- `Table` now supports dynamic numbers of columns with the new `TableColumnForEach`.  (79492167) (FB9189673)

###### Resolved Issues

- Fixed: DatePicker in macOS reset focus to the first date component when its bound date changes and `timeZone` is overriden in the environment.  (97376561)

##### Synchronization

###### New Features

- New `os_sync_wait_on_address` APIs have been added. They are expected to be used for implementing synchronization primitives that do not have a sense of ownership. Please file feedback if you need Synchronization functionality not covered by existing API.  (94759935) (FB10141068)

## See Also

- [macOS Sonoma 14.6 Release Notes](macos-14_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.5 Release Notes](macos-14_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.3 Release Notes](macos-14_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.2 Release Notes](macos-14_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.1 Release Notes](macos-14_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14 Release Notes](macos-14-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-14_4-release-notes)*