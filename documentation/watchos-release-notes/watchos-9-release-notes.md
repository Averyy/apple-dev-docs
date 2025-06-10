# watchOS 9 Release Notes

**Framework**: watchOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 9 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 9. The SDK comes bundled with Xcode 14, available from the Mac App Store. For information on the compatibility requirements for Xcode 14, see [`Xcode 14 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-14-release-notes).

##### General

- After updating to watchOS 9, your Apple Watch Series 4 or Series 5 will recalibrate and then estimate its maximum battery capacity more accurately. (93206868)

##### Callkit

###### Known Issues

- Compilation of apps integrated with CallKit might result in an error: “Value of type `CXProviderConfiguration` has no member `supportedHandleTypes` on watchOS 9”. (97582165)  Use `__supportedHandleTypes` instead of `supportedHandleTypes`.

##### Coregraphics

###### Deprecations

- To improve security, `CGImageCreate` enforces parameter correctness on macOS 13 Ventura, iOS 16, iPadOS 16, watchOS 9, and tvOS 16. Passing an incorrect `CGImageByteOrderInfo` is no longer supported, and will result in images failing to load. (94855401)

##### Devicediscoveryui

###### Known Issues

- Devices running beta 4 or later aren’t backwards compatible with devices running earlier beta versions. (95233878)

##### Health

###### New Features

- AFib History is now available in the United States. (95627199)

##### Healthkit

###### New Features

- HealthKit workout APIs now support multisport workouts with activities of swimming, cycling, and running. (82588168)

- New data types for running workout metrics like running power, ground contact time, vertical oscillation, running speed, and stride length. (82974514)

##### Networking

###### New Features

- Added `NSURLSession` support for client-certificate based authentication. (24523955)

- Added `URLSession` support for Private Access Tokens. (82937526)

###### Deprecations

- FTP is deprecated for `URLSession` and related APIs. Please adopt modern secure networking protocols such as HTTPS. (92623659)

##### Storekit

###### New Features

- The `recentSubscriptionStartDate` property is included in [`Product.SubscriptionInfo.RenewalInfo`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo). It represents the date that marks the start of the most recent period of continuous subscription. A period is considered a continuous subscription if there’s no more than a 60-day gap between any two subscribed periods. (86599570)

- Present the offer code redemption sheet with the [`offerCodeRedemption(isPresented:onCompletion:)`](https://developer.apple.com/documentation/SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:)) view modifier in your SwiftUI apps. (85321941)

- The StoreKit Messages API allows you to control when App Store messages are displayed in your app. (85321880)

- `Product` has new properties for localizing prices and subscription periods. For iOS 15, iPadOS 15, macOS 12, tvOS 15, and watchOS 8 or later use `priceFormatStyle` to format numbers derived from `price`. Use `subscriptionPeriodFormatStyle` to format durations of time relating to a subscription period. On iOS 16, iPadOS 16, macOS 13, tvOS 16, and watchOS 9 or later use `subscriptionPeriodUnitFormatStyle` to format single units of a subscription period. (93780442)

- A property environment is included in [`Product.SubscriptionInfo.RenewalInfo`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo) and [`Transaction`](https://developer.apple.com/documentation/StoreKit/Transaction). It represents the server environment in which the `RenewalInfo` and `Transaction` occurred, respectively. (85988753)

- [`AppTransaction`](https://developer.apple.com/documentation/StoreKit/AppTransaction) allows developers to cryptographically verify that the app was purchased on the App Store. (86739279)

- All [`StoreKit`](https://developer.apple.com/documentation/StoreKit) APIs are now annotated for sendability and main actor isolation. (84157048)

###### Deprecations

- Deprecated the SKDownload API and removed the option to upload nonconsumable in-app purchase assets for Apple to host. In addition, support for managing these assets in App Store Connect is no longer available as of April 2022. (89764253)

##### Swiftui

###### New Features

- Custom types conforming to `ToolbarContent` now support dynamic properties like `@Environment`. (94117842)

- For `control`, [`Section`](https://developer.apple.com/documentation/SwiftUI/Section), or other views that have a [`Label`](https://developer.apple.com/documentation/SwiftUI/Label), the [`ViewBuilder`](https://developer.apple.com/documentation/SwiftUI/ViewBuilder) content now automatically arranges and styles multiple views as hierarchical elements, such as `title` and `subtitle`. If the `label` views are intended to be arranged horizontally rather than hierarchically, wrap the views within an [`HStack`](https://developer.apple.com/documentation/SwiftUI/HStack). (85184563)

##### Voice Shortcuts

###### Known Issues

- When saying an App Shortcut phrase to Siri, Siri launches the app or ends up with an unexpected result. (93611920)

##### Wallet

###### Known Issues

- American Express cards might need to be removed and re-added to Wallet after updating to watchOS 9 beta 6 or later. (97990752)

## See Also

- [watchOS 9.6 Release Notes](watchos-9_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.5 Release Notes](watchos-9_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.4 Release Notes](watchos-9_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.3 Release Notes](watchos-9_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.2 Release Notes](watchos-9_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.1 Release Notes](watchos-9_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-9-release-notes)*