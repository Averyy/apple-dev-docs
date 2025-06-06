# iOS & iPadOS 15.4 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 15.4 SDK provides support to develop apps for iPhone, iPad, and iPod touch devices running iOS & iPadOS 15.4. The SDK comes bundled with Xcode 13.3.1, available from the Mac App Store. For information on the compatibility requirements for Xcode 13.3.1, see [`Xcode 13.3.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-13_3_1-release-notes).

##### Apple Pay

###### New Features

- Developers can express payment network preference in [`PKPaymentRequest`](https://developer.apple.com/documentation/PassKit/PKPaymentRequest). Network preference is determined by the order of [`supportedNetworks`](https://developer.apple.com/documentation/PassKit/PKPaymentRequest/supportedNetworks). This won’t override the user’s default card selection, but if the card is multi-SSD, then the network preference order determines which SSD is selected. (80827905)

##### Authentication

###### New Features

- Support is added to the passkey technology preview, enabling signing in to passkey-compatible websites and apps on Mac and iPad using an iPhone with a saved passkey. (87998254)

###### Known Issues

- Signing in to an iPad is limited to apps in this release.

##### Developer Settings

###### New Features

- You can now use Settings > Developer Settings > Run Throughput Test to view average results for ping packet loss, idle ping latency, and download and upload speeds. (81870452)

##### Game Controller

###### New Features

- Support is now available for new DualSense adaptive trigger firmware features available via [`GCDualSenseAdaptiveTrigger`](https://developer.apple.com/documentation/GameController/GCDualSenseAdaptiveTrigger). (87433163)

##### Health App

###### Known Issues

- The Health app crashes when you attempt to onboard the Blood Oxygen feature from within the app. (87617635)
- If Health sharing is skipped when setting up an Apple Watch for a family member, it can’t be enabled later. (87210981)

##### Healthkit

###### New Features

- Verifiable health records now support adding vaccination records in the EU Digital COVID Certificate (EU DCC) format to the Wallet and Health apps. (79917344)
- `HealthKit` query APIs in Swift now support async/await syntax, which simplifies the structure of code that previously used completion callbacks. (74040680)

##### Home

###### Known Issues

- Matter accessories with multiple end points might be unreachable in the Home App. (86170578)
- Matter accessories may go to a “No Response” state after pairing with the Home App. (86497690)  Remove the accessory from Home, reset the accessory, and add it back to Home. If the issue persists, remove your home hub from Home and re-add it. If the issue continues to persist, remove the home hub and create a new one.
- Adding a Matter accessory to a third-party app fails if an Apple Home doesn’t exist. (80341813)  Launch the Home App and create a home hub first.

##### Itunes

###### Known Issues

- Purchasing or downloading content again from the iTunes Store and TV app might fail on some devices. (86772291)  Rebooting the device may resolve the issue.

##### Libc++

###### New Features

- The following new C++20 and C++23 features are now implemented: - C++20 library concepts defined in `<concepts>`.
- `constexpr` for `std::swap()` and swap-related functions.
- Miscellaneous `constexpr`-ification in the library.
- `std::atomic` now default initializes as expected.
- A `.contains()` method for associative containers.
- Added `std::bind_front()`. (88131816)

###### Deprecations

- Some extensions in `std::tuple` were removed to fix bugs caused by those extensions: - Tuples can no longer be constructed from fewer than the number of elements in the tuple. Previously, elements that weren’t specified were default-constructed; now this is a compiler error.
- A tuple can no longer be constructed from an array.
- The `std::result_of` and `std::is_literal_type` type traits are no longer available in C++20 mode, as specified in the Standard.

##### Messages

###### Known Issues

- A conversation transcript won’t scroll after viewing a photo in QuickLook. (87855403)  Back out of the conversation and then reopen it to restore scrolling.

##### Phone

###### Known Issues

- Emergency SOS “Call with 5 Presses” is disabled for all users outside of India to fix an issue that caused this setting to unintentionally default for some users. (86189447)

##### Settings

###### Known Issues

- In the Throughput Test results, the Idle Ping Latency is reported in incorrect units. For example, an actual ping latency of 123.32 ms is shown as 0.12 ms. (87599982)

##### Shareplay

###### New Features

- A new [`Group Activities`](https://developer.apple.com/documentation/GroupActivities) API allows you to present UI that enables starting a SharePlay session from within your app. (88099397)

###### New Features

- [`SKTestSession`](https://developer.apple.com/documentation/StoreKitTest/SKTestSession) has three new methods to simulate a subscription requiring price increase consent, simulate consenting to a pending price increase, and simulate declining a price increase in automated tests. (84556183)
- StoreKit records an ad impression if the framework displays an ad for a minimum of 2 seconds, down from the previous minimum of 3 seconds. (85874835)

- `SKTestSession` has two new Boolean properties to simulate billing retry and grace period in automated tests. You can identify and simulate the resolution of billing retry issues using the same APIs as interrupted purchases. (83956205)

- Users can now test the billing retry and grace period states using StoreKit Testing in Xcode. Use Xcode 13.3 or later to enable billing retry testing and toggle whether the app offers a grace period. Use [`isInBillingRetry`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo/isInBillingRetry) and [`gracePeriodExpirationDate`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo/gracePeriodExpirationDate) to handle these states in the app. (83938270)

- You can now test offer codes with StoreKit Testing in Xcode. Configure offers for codes in Xcode 13.3 or later, and test redeeming them using [`presentCodeRedemptionSheet()`](https://developer.apple.com/documentation/StoreKit/SKPaymentQueue/presentCodeRedemptionSheet()). (63692551)

- Users can test subscription price increase behavior using StoreKit Testing in Xcode. Use Xcode 13.3 or later to set a price increase, then use [`paymentQueueShouldShowPriceConsent(_:)`](https://developer.apple.com/documentation/StoreKit/SKPaymentQueueDelegate/paymentQueueShouldShowPriceConsent(_:)), [`showPriceConsentIfNeeded()`](https://developer.apple.com/documentation/StoreKit/SKPaymentQueue/showPriceConsentIfNeeded()), and [`priceIncreaseStatus`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo/priceIncreaseStatus-swift.property) in the app. (58770817)

- `StoreKit` error types now conform to [`LocalizedError`](https://developer.apple.com/documentation/Foundation/LocalizedError). (78735204)

- Some types in `StoreKit` now have a `localizedDescription` read-only `String` instance property. This property can be used to get a human-readable description of the value, localized for the device’s current locale. These types include: [`Product.ProductType`](https://developer.apple.com/documentation/StoreKit/Product/ProductType), [`Product.SubscriptionInfo.RenewalState`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalState), [`expirationReason`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo/expirationReason-swift.property), [`priceIncreaseStatus`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionInfo/RenewalInfo/priceIncreaseStatus-swift.property), [`Transaction.OfferType`](https://developer.apple.com/documentation/StoreKit/Transaction/OfferType-swift.struct), [`Product.SubscriptionOffer.OfferType`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionOffer/OfferType), [`Product.SubscriptionOffer.PaymentMode`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionOffer/PaymentMode-swift.struct), [`Product.SubscriptionPeriod.Unit`](https://developer.apple.com/documentation/StoreKit/Product/SubscriptionPeriod/Unit-swift.enum), [`Transaction.RevocationReason`](https://developer.apple.com/documentation/StoreKit/Transaction/RevocationReason-swift.struct), and [`Transaction.OwnershipType`](https://developer.apple.com/documentation/StoreKit/Transaction/OwnershipType-swift.struct). (78735060)

- [`SKAdNetwork`](https://developer.apple.com/documentation/StoreKit/SKAdNetwork) implementation can now be unit tested using the [`StoreKit Test`](https://developer.apple.com/documentation/StoreKitTest) framework. You can use the `SKAdTestSession` class to test the validity of ad impressions, update conversion values on test postbacks, and receive test postbacks at the server. This class also displays the URL to which the optional developer postback is sent. (59571961)

###### Known Issues

- When testing with StoreKit Testing in Xcode, the following APIs don’t work in the simulator: [`presentCodeRedemptionSheet()`](https://developer.apple.com/documentation/StoreKit/SKPaymentQueue/presentCodeRedemptionSheet()), [`paymentQueueShouldShowPriceConsent(_:)`](https://developer.apple.com/documentation/StoreKit/SKPaymentQueueDelegate/paymentQueueShouldShowPriceConsent(_:)), and [`showPriceConsentIfNeeded()`](https://developer.apple.com/documentation/StoreKit/SKPaymentQueue/showPriceConsentIfNeeded()). (85982859)  Test these APIs using an iOS device.

##### Uikit

###### New Features

- All animations created with [`UIView`](https://developer.apple.com/documentation/UIKit/UIView) block APIs or [`UIViewPropertyAnimator`](https://developer.apple.com/documentation/UIKit/UIViewPropertyAnimator) run at up to 120 Hz on iPhones with ProMotion displays. (86175551)

## See Also

- [iOS & iPadOS 15.6 Release Notes](ios-ipados-15_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.5 Release Notes](ios-ipados-15_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.3 Release Notes](ios-ipados-15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.2 Release Notes](ios-ipados-15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15.1 Release Notes](ios-ipados-15_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 15 Release Notes](ios-ipados-15-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15_4-release-notes)*