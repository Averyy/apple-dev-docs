# tvOS 12.2 Release Notes

**Framework**: tvOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 12.2 SDK provides support for developing tvOS apps for Apple TV devices running tvOS 12.2. The SDK comes bundled with Xcode 10.2 available from the Mac App Store. For information on the compatibility requirements for Xcode 10.2, see [`Xcode Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes).

##### App Store

###### Promoting Your Subscriptions with New Offers

StoreKit now supports subscription offers in addition to introductory offers, so apps with auto-renewable subscriptions can provide a discounted price for a specific duration for existing and previously subscribed customers. You can use subscription offers to help win back subscribers who have canceled their subscriptions or promote an upgrade to another subscription at a special price. Customers can accept the offer even if they’ve already completed an introductory offer.

StoreKit introduces a new array of [`SKProductDiscount`](https://developer.apple.com/documentation/StoreKit/SKProductDiscount) objects within the [`SKProduct`](https://developer.apple.com/documentation/StoreKit/SKProduct) class to display offers within your app to eligible customers. Add a new [`SKPaymentDiscount`](https://developer.apple.com/documentation/StoreKit/SKPaymentDiscount) object within the [`SKPayment`](https://developer.apple.com/documentation/StoreKit/SKPayment) class to allow these offers to be accepted by the customer.

## See Also

- [tvOS 12.4 Release Notes](tvos-12_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 12.1.2 Release Notes](tvos-12_1_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 12.1.1 Release Notes](tvos-12_1_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 12 Release Notes](tvos-12-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-12_2-release-notes)*