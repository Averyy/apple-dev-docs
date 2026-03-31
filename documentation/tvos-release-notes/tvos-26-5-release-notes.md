# tvOS 26.5 Beta Release Notes

**Framework**: tvOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 26.5 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 26.5 beta. The SDK comes bundled with Xcode 26.5, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.5, see [`Xcode 26.5 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_5-release-notes).

##### Storekit

###### New Features

- You can read pricing information for subscriptions that have a monthly with 12-month commitment billing plan configuration in App Store Connect or StoreKit Testing in Xcode through the new `PricingTerms` model on `SubscriptionInfo.pricingTerms`.  (150388310)
- You can specify the billing plan type to use for subscriptions that have a monthly with 12-month commitment billing plan configuration using the new `billingPlanType` `PurchaseOption`.  (150388542)
- Read customer entitlement metadata for subscriptions purchased with a monthly billing plan type through the new `CommitmentInfo` data model on `Transaction` and `SubscriptionRenewalInfo`.  (150388746)
- When you import both StoreKit and SwiftUI, you can merchandise the monthly billing plan configuration for subscriptions that have a monthly with 12-month commitment billing plan using built-in styles through the new `preferredSubscriptionPricingTerms(_:) API`.  (150389069)

##### Storekittest

###### Known Issues

- `SKTestSession` cannot use the selected StoreKit configuration during unit tests, resulting in failed test actions.  (172583218) (FB22237318) **Workaround:** To use `SKTestSession` in 26.3 and 26.4, build and run the app on device using the same StoreKit configuration as the test. Then close the app and run the unit test using `SKTestSession` without changing any configuration settings in the test environment. This allows the configuration to be saved on device before the test begins and maintain your selected configuration settings through the test session.

## See Also

- [tvOS 26.4 Release Notes](tvos-26_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 26.3 Release Notes](tvos-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 26.2 Release Notes](tvos-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 26.1 Release Notes](tvos-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 26 Release Notes](tvos-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-26_5-release-notes)*