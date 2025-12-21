# tvOS 18.4 Release Notes

**Framework**: tvOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 18.4 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 18.4. The SDK comes bundled with Xcode 16.3, available from the Mac App Store. For information on the compatibility requirements for Xcode 16.3, see [`Xcode 16.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-16_3-release-notes).

##### Background Assets

###### New Features

- The Background Assets framework is now supported for visionOS apps on visionOS 2.4 or later and tvOS apps on tvOS 18.4 or later.  (138008978)

##### Libxml2

###### Deprecations

- The custom allocation API for libxml2 is deprecated starting in macOS Sequoia 15.4, iOS 18.4, tvOS 18.4, visionOS 2.4, and tvOS 18.4.  If this API is not used, no changes are required.  If this API is currently used, make changes to call `malloc()` instead of `xmlMalloc()` or `xmlMallocAtomic()`; call `realloc()` instead of `xmlRealloc()`; call `free()` instead of `xmlFree()` and call `strdup()` instead of `xmlMemStrdup()`.  Stop calling `xmlMemSetup()`, `xmlMemGet()`, `xmlGcMemSetup()` and `xmlGcMemGet()` to set custom allocation functions.  Do not set global variables `xmlMalloc`, `xmlMallocAtomic`, `xmlRealloc`, `xmlFree`, and `xmlMemStrdup`.  Internally, libxml2 and libxslt will now use the system allocator instead of this API, so do not rely on these libraries using the custom allocation API.  (138404994)

##### Storekit

###### New Features

- New StoreKit APIs support [`Advanced Commerce API`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/advanced-commerce-api/) in-app purchases.  (118528943)
- By using the new purchase option API `introductoryOfferEligibility(compactJWS:)`, you can now set a preference for whether an introductory offer should be redeemed during a purchase. This API requires you to sign a payload on your server in order to either apply the offer (even if the customer is not eligible) or block it.  (136152740)
- New properties `appTransactionID`, `originalPlatform`, and `period` are now available in [`AppTransaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/apptransaction), [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction), [`Transaction.Offer`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/offer-swift.struct), and [`Product.SubscriptionInfo.RenewalInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo).  (136395697)
- The `Platform` symbol used by originalPlatform in AppTransaction has been moved to `AppStore.Platform`.  (143632084)
- The introductory offer eligibility preference API in PurchaseOption has been renamed to `introductoryOfferEligibility(compactJWS:)`.  (143905053)
- `watchOS` is removed as an option in the AppStore.Platform API. `watchOS` is now combined with `iOS`.  (145578780)

###### Resolved Issues

- Fixed: StoreKit helper application quits with NSCocoaErrorDomain error 4097 during a purchase.  (140317005) (FB15907723)
- Fixed: StoreKit APIs might return errors from the StoreKit 2 domain during a purchase.  (144191684)

###### Known Issues

- Calling `isEligibleForIntroOffer(for:)` will return false if there is no user account signed in.  (146119524)  The user should sign in with their App Store account to request introductory offer eligibility.

###### Deprecations

- [`Transaction.currentEntitlement(for:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/currententitlement(for:)) is now deprecated. This API returns the latest transaction that entitles the user to a product, which may not include transactions originated for family shared subscriptions. Use the `Transaction.currentEntitlements(for:)` method to get all the transactions that entitle the user to a product.  (138320205)

##### Swiftui

###### Resolved Issues

- Fixed: A color set by the `tint(_:)` modifier does not override the tint color of buttons in that view’s confirmation dialogs and alerts.  (138774306)
- Fixed: For apps compiled against iOS 18.4 beta, applying `defaultVisibility(.hidden)` to customizable toolbar items does not hide the item by default on iOS.  (139815290)
- Fixed: When NavigationStack or NavigationSplitView content updates, the environment is not invalidated unless properties in the environment have changed.  (139855826)
- Fixed: `.onPreferenceChange` modifier’s closure argument is required to be `@Sendable`. This might cause concurrency diagnostics that’s unnecessary if the closure needs to access main actor-isolated values. This particular closure shouldn’t have to be this restrictive.  (145238570)

##### System Calls

###### New Features

- fileport_makeport(2) and fileport_makefd(2) are now APIs with manual pages.  (66571768) (FB8270900)

##### Urlsession

###### New Features

- To enable the new HTTP loading mode, set `usesClassicLoadingMode` to false on URLSessionConfiguration. The new loading mode will become the default in a future release.  (89390075)

## See Also

- [tvOS 18.6 Release Notes](tvos-18_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 18.5 Release Notes](tvos-18_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 18.3 Release Notes](tvos-18_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 18.2 Release Notes](tvos-18_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 18.1 Release Notes](tvos-18_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 18 Release Notes](tvos-18-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-18_4-release-notes)*