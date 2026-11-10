# macOS Monterey 12.3 Release Notes

**Framework**: macOS Release Notes  
**Role**: Article

Update your apps to use new features, and test your apps against API changes.

## Overview

The macOS 12.3 SDK provides support to develop apps for Mac computers running macOS Monterey 12.3. The SDK comes bundled with Xcode 13.3.1. For information on the compatibility requirements for Xcode 13.3.1, see [Xcode 13.3.1 Release Notes](../Xcode-Release-Notes/xcode-13_3_1-release-notes.md).

### Apple Pay

#### New Features

- Developers can express payment network preference in [`PKPaymentRequest`](../PassKit/pkpaymentrequest.md). Network preference is determined by the order of [`supportedNetworks`](../PassKit/pkpaymentrequest/supportednetworks.md). This won’t override the user’s default card selection, but if the card is multi-SSD, then the network preference order determines which SSD is selected. (80827905)

### Authentication

#### New Features

- Support is added to the passkey technology preview, enabling signing in to passkey-compatible websites and apps on Mac and iPad using an iPhone with a saved passkey. (87998252)

### Game Controller

#### New Features

- Support is now available for new DualSense adaptive trigger firmware features available via [`GCDualSenseAdaptiveTrigger`](../GameController/gcdualsenseadaptivetrigger.md). (87433163)

### iWork

#### Known Issues

- Collaboration scenarios might not work when the user configures the system to a right-to-left language. (89078453)

  **Workaround:** Use iWork.com to collaborate in Safari using a right-to-left language.

### Kernel

#### Deprecations

- The kernel extensions used by Dropbox Desktop Application and Microsoft OneDrive are no longer available. Both service providers have replacements for this functionality; Dropbox is currently in beta. (85890896)

### libc++

#### New Features

- The following new C++20 and C++23 features are now implemented:

  - C++20 library concepts defined in `<concepts>`.
  - `constexpr` for `std::swap()` and swap-related functions.
  - Miscellaneous `constexpr`-ification in the library.
  - `std::atomic` now default initializes as expected.
  - A `.contains()` method for associative containers.
  - Added `std::bind_front()`. (88131816)

#### Deprecations

- Some extensions in `std::tuple` were removed to fix bugs caused by those extensions:

  - Tuples can no longer be constructed from fewer than the number of elements in the tuple. Previously, elements that weren’t specified were default-constructed; now this is a compiler error.
  - A tuple can no longer be constructed from an array.
  - The `std::result_of` and `std::is_literal_type` type traits are no longer available in C++20 mode, as specified in the Standard.

### Python

#### Deprecations

- Python 2.7 was removed from macOS in this update. Developers should use Python 3 or an alternative language instead. (39795874)

### StoreKit

#### New Features

- [`SKTestSession`](../StoreKitTest/sktestsession.md) has three new methods to simulate a subscription requiring price increase consent, simulate consenting to a pending price increase, and simulate declining a price increase in automated tests. (84556183)

- `SKTestSession` has two new Boolean properties to simulate billing retry and grace period in automated tests. You can identify and simulate the resolution of billing retry issues using the same APIs as interrupted purchases. (83956205)

- Users can now test the billing retry and grace period states using StoreKit Testing in Xcode. Use Xcode 13.3 or later to enable billing retry testing and toggle whether the app offers a grace period. Use [`isInBillingRetry`](../StoreKit/product/subscriptioninfo/renewalinfo/isinbillingretry.md) and [`gracePeriodExpirationDate`](../StoreKit/product/subscriptioninfo/renewalinfo/graceperiodexpirationdate.md) to handle these states in the app. (83938270)

- `StoreKit` error types now conform to [`LocalizedError`](../Foundation/localizederror.md). (78735204)

- Users can test subscription price increase behavior using StoreKit Testing in Xcode. Use Xcode 13.3 or later to set a price increase, then use [`paymentQueueShouldShowPriceConsent(_:)`](../StoreKit/skpaymentqueuedelegate/paymentqueueshouldshowpriceconsent%28_%29.md), [`showPriceConsentIfNeeded()`](../StoreKit/skpaymentqueue/showpriceconsentifneeded%28%29.md), and [`priceIncreaseStatus`](../StoreKit/product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.property.md) in the app. (58770817)

- Some types in `StoreKit` now have a `localizedDescription` read-only `String` instance property. This property can be used to get a human-readable description of the value, localized for the device’s current locale. These types include: [`Product.ProductType`](../StoreKit/product/producttype.md), [`Product.SubscriptionInfo.RenewalState`](../StoreKit/product/subscriptioninfo/renewalstate.md), [`expirationReason`](../StoreKit/product/subscriptioninfo/renewalinfo/expirationreason-swift.property.md), [`priceIncreaseStatus`](../StoreKit/product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.property.md), [`Transaction.OfferType`](../StoreKit/transaction/offertype-swift.struct.md), [`Product.SubscriptionOffer.OfferType`](../StoreKit/product/subscriptionoffer/offertype.md), [`Product.SubscriptionOffer.PaymentMode`](../StoreKit/product/subscriptionoffer/paymentmode-swift.struct.md), [`Product.SubscriptionPeriod.Unit`](../StoreKit/product/subscriptionperiod/unit-swift.enum.md), [`Transaction.RevocationReason`](../StoreKit/transaction/revocationreason-swift.struct.md), and [`Transaction.OwnershipType`](../StoreKit/transaction/ownershiptype-swift.struct.md). (78735060)

### Universal Control

#### Known Issues

- Drag-and-drop scenarios might not work for some file types and apps. (88106322)
- Some third-party keyboards and mice might encounter issues when using additional functionality, like scroll wheels. (88106362)

### WebKit

#### Deprecations

- Support for inline viewing of PostScript files is no longer available. (88172449)

## See Also

### macOS 12
- [macOS Monterey 12.5 Release Notes](./macos-12_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.4 Release Notes](./macos-12_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.2 Release Notes](./macos-12_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.1 Release Notes](./macos-12_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.0.1 Release Notes](./macos-12_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-12_3-release-notes)*