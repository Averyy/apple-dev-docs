# visionOS 2.4 Release Notes

**Framework**: visionOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The visionOS 2.4 SDK provides support for developing apps for Apple Vision Pro devices running visionOS 2.4. The SDK comes bundled with Xcode 16.3, available from the Mac App Store. For information on the compatibility requirements for Xcode 16.3, see [`Xcode 16.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-16_3-release-notes).

##### Apple Intelligence

###### Resolved Issues

- Fixed: Genmoji in volumetric apps is not yet supported, causing the app to crash when invoked.  (144808840)
- Fixed: After enabling Apple Intelligence, users might be in a state where Apple Intelligence features are stuck downloading.  (144886219)

##### Apple Tv App

###### Resolved Issues

- Fixed: User is unable to enter non-Latin characters in the search bar.  (143041679)

##### Background Assets

###### New Features

- The Background Assets framework is now supported for visionOS apps on visionOS 2.4 or later and tvOS apps on tvOS 18.4 or later.  (138008978)

##### Guest User

###### Known Issues

- Guest User access request might fail if an Apple Vision Pro running visionOS 2.4 beta is paired to a device running iOS 18.3 or earlier.  (140292089)  Update both devices to latest versions of visionOS 2.4 beta and iOS 18.4 beta.

##### Libxml2

###### Deprecations

- The custom allocation API for libxml2 is deprecated starting in macOS Sequoia 15.4, iOS 18.4, tvOS 18.4, visionOS 2.4, and tvOS 18.4.  If this API is not used, no changes are required.  If this API is currently used, make changes to call `malloc()` instead of `xmlMalloc()` or `xmlMallocAtomic()`; call `realloc()` instead of `xmlRealloc()`; call `free()` instead of `xmlFree()` and call `strdup()` instead of `xmlMemStrdup()`.  Stop calling `xmlMemSetup()`, `xmlMemGet()`, `xmlGcMemSetup()` and `xmlGcMemGet()` to set custom allocation functions.  Do not set global variables `xmlMalloc`, `xmlMallocAtomic`, `xmlRealloc`, `xmlFree`, and `xmlMemStrdup`.  Internally, libxml2 and libxslt will now use the system allocator instead of this API, so do not rely on these libraries using the custom allocation API.  (138404994)

##### Personal Hotspot

###### Resolved Issues

- Fixed: FaceTime calls might fail to initiate or be received when using certain configurations of Personal Hotspot.  (146330524)

##### Realitykit

###### Resolved Issues

- Fixed: In RealityKit applications, imported USD files with blend shape animations might not play as expected.  (140970189) (FB16047963)

##### Settings

###### Known Issues

- After resetting network settings or all settings, the Home View might not appear and hand gestures might not work.   (147616530)  Power off and on the Vision Pro to complete the reset process and access the Home View.

##### Simulator

###### Resolved Issues

- Fixed: A crash dialog might appear during asset compilation for some projects, though Xcode will continue to run.  (142380552)

###### Known Issues

- Safari Extensions do not appear in iOS or visionOS simulator.  (147511062)

##### Spatial Gallery

###### New Features

- Spatial Gallery is now available. This app features a selection of spatial photos, videos, and panoramas curated by Apple for Apple Vision Pro. With Spatial Gallery, users will enjoy breathtaking and intimate moments spanning art, culture, entertainment, lifestyle, nature, sports, and travel, with new content released regularly.  (145675333)

##### Storekit

###### New Features

- New StoreKit APIs support [`Advanced Commerce API`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/advanced-commerce-api/) in-app purchases.  (118528943)
- By using the new purchase option API `introductoryOfferEligibility(compactJWS:)`, you can now set a preference for whether an introductory offer should be redeemed during a purchase. This API requires you to sign a payload on your server in order to either apply the offer (even if the customer is not eligible) or block it.  (136152740)
- New properties `appTransactionID`, `originalPlatform`, and `period` are now available in [`AppTransaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/apptransaction), [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction), [`Transaction.Offer`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/offer-swift.struct), and [`Product.SubscriptionInfo.RenewalInfo`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo).  (136395697)
- The `Platform` symbol used by originalPlatform in AppTransaction has been moved to `AppStore.Platform`.  (143632084)
- The introductory offer eligibility preference API in PurchaseOption has been renamed to `introductoryOfferEligibility(compactJWS:)`.  (143905053)
- `watchOS` is removed as an option in the AppStore.Platform API. `watchOS` is now combined with `iOS`.  (145578780)

###### Resolved Issues

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
- Fixed: The `glassBackgroundEffect(.feathered)` is rendered as a black box when applied to content with an implicit stack modifier, such as an overlay or border.   (144412802)
- Fixed: `.onPreferenceChange` modifier’s closure argument is required to be `@Sendable`. This might cause concurrency diagnostics that’s unnecessary if the closure needs to access main actor-isolated values. This particular closure shouldn’t have to be this restrictive.  (145238570)

##### System Calls

###### New Features

- fileport_makeport(2) and fileport_makefd(2) are now APIs with manual pages.  (66571768) (FB8270900)

##### Urlsession

###### New Features

- To enable the new HTTP loading mode, set `usesClassicLoadingMode` to false on URLSessionConfiguration. The new loading mode will become the default in a future release.  (89390075)

## See Also

- [visionOS 2.5 Release Notes](visionos-2_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.3 Release Notes](visionos-2_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.2 Release Notes](visionos-2_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 2.1 Release Notes](visionos-2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 2 Release Notes](visionos-2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos-release-notes/visionos-2_4-release-notes)*