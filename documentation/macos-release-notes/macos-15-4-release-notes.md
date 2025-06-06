# macOS Sequoia 15.4 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 15.4 SDK provides support to develop apps for Mac computers running Sequoia 15.4. The SDK comes bundled with Xcode 16.3, available from the Mac App Store. For information on the compatibility requirements for Xcode 16.3, see [`Xcode 16.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-16_3-release-notes).

##### Apple Intelligence

###### Known Issues

- After restoring macOS 15.4, some Apple Intelligence features might not be available or you might see “Downloading support…”.  (145297891)  Restarting your device might resolve the issue.

##### Automatic Assessment Configuration

###### Resolved Issues

- Fixed: Assessment session might be interrupted in high-memory use conditions.  (144416806)

##### Driver Extensions

###### Known Issues

- After updating to macOS 15.4 beta, you might experience issues with loading installed drivers.  (145330084) (FB16547388)  Go to System Settings > General > Login Items & Extensions and disable your affected driver extensions. Restart your Mac. After restarting, go back to System Settings > General > Login Items & Extensions and re-enable the affected driver extensions.

##### Fskit

###### New Features

- FSKit is now available, enabling delivery of user space file systems as Application Extensions. These file systems support integration with DiskArbitration.  (44900760)

##### Game Controller

###### Resolved Issues

- Fixed: Game controllers might stop responding when accessibility features, such as Voice Over, are enabled.  (141497799)

##### Hvf

###### Known Issues

- Availability checking is disabled for C APIs in hvf.  (147323772)  To enable availability checking, add this ahead of any headers: ```None
 #define BUILD_FOR_APPLE_SDK 1
```

##### Libxml2

###### Deprecations

- The custom allocation API for libxml2 is deprecated starting in macOS Sequoia 15.4, iOS 18.4, tvOS 18.4, visionOS 2.4, and tvOS 18.4.  If this API is not used, no changes are required.  If this API is currently used, make changes to call `malloc()` instead of `xmlMalloc()` or `xmlMallocAtomic()`; call `realloc()` instead of `xmlRealloc()`; call `free()` instead of `xmlFree()` and call `strdup()` instead of `xmlMemStrdup()`.  Stop calling `xmlMemSetup()`, `xmlMemGet()`, `xmlGcMemSetup()` and `xmlGcMemGet()` to set custom allocation functions.  Do not set global variables `xmlMalloc`, `xmlMallocAtomic`, `xmlRealloc`, `xmlFree`, and `xmlMemStrdup`.  Internally, libxml2 and libxslt will now use the system allocator instead of this API, so do not rely on these libraries using the custom allocation API.  (138404994)

##### Networking

###### Resolved Issues

- Fixed: On Ethernet, 169.254.169.254 causes functionality issues on CI build machines due to Local Network Privacy restrictions.  (145297894) (FB16541221)

##### Podcasts

###### New Features

- Podcasts Search provides suggestions as you type to help you find what you’re looking for.  (144169175)

##### Scsicontrollerdriverkit

###### New Features

- Four new API’s have been introduced: `UserMapBundledParallelTaskCommandAndResponseBuffers`, `BundledParallelTaskCompletion`, `UserProcessBundledParallelTasks` and `UserCompleteBundledParallelTask`. These APIs introduce the concepts of bundled I/Os and shared memory, for parallel task command and response buffers. The shared memory addresses the RPC copy overhead. Bundled I/O enables the exchange of multiple I/Os in a single API call (in both submission and completion path), instead of handing over one I/O at a time between DriverKit and DriverExtension. This helps mitigate the DriverKit latencies while interacting with DriverExtension. The `IOUserSCSIParallelInterfaceController.iig` file explains the concepts of I/O bundling and shared memory for parallel task and response buffers. If DriverExtension has considerably lower I/O performance compared to the KernelExtension for workloads with high queue depths or very small I/O sizes (i.e. 4KB), try using these new APIs.  (134516478)

##### Sd Card Reader

###### New Features

- Apple silicon Macs with an internal SD card reader now support SDUC cards larger than 2TB.  (122898691)

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

###### New Features

- On macOS `.sheet`, `.alert` and `.confirmationDialog` modal presentations conditionally allow app termination (via the menu item, ⌘Q, Software Update, etc.) automatically. This is now configurable with two new modifiers, [`presentationPreventsAppTermination(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/presentationpreventsapptermination(_:)) and [`dialogPreventsAppTermination(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/dialogpreventsapptermination(_:)).  (141551605)

###### Resolved Issues

- Fixed: A color set by the `tint(_:)` modifier does not override the tint color of buttons in that view’s confirmation dialogs and alerts.  (138774306)
- Fixed: For apps compiled against iOS 18.4 beta, applying `defaultVisibility(.hidden)` to customizable toolbar items does not hide the item by default on iOS.  (139815290)
- Fixed: When NavigationStack or NavigationSplitView content updates, the environment is not invalidated unless properties in the environment have changed.  (139855826)
- Fixed: `.onPreferenceChange` modifier’s closure argument is required to be `@Sendable`. This might cause concurrency diagnostics that’s unnecessary if the closure needs to access main actor-isolated values. This particular closure shouldn’t have to be this restrictive.  (145238570)

##### System Calls

###### New Features

- fileport_makeport(2) and fileport_makefd(2) are now APIs with manual pages.  (66571768) (FB8270900)

##### Uiwritingtoolscoordinator

###### Resolved Issues

- Fixed: In macOS 15.4 beta, NSWritingToolsCoordinatorDelegate method `-writingToolsCoordinator:requestsRangeInContextWithIdentifierForPoint:completion:` is marked as optional and will not be called.  (142681236)

##### Urlsession

###### New Features

- To enable the new HTTP loading mode, set `usesClassicLoadingMode` to false on URLSessionConfiguration. The new loading mode will become the default in a future release.  (89390075)

##### Virtual Machines

###### Resolved Issues

- Fixed: M4 Macs are unable to launch virtual machine, and attempts result in a system restart.  (145309647) (FB16542958)

##### Webkit

###### New Features

- Added support for `WKWebExtension`, `WKWebExtensionContext`, and `WKWebExtensionController` Swift and Objective-C classes to support integrating Web Extensions into WebKit-based browsers.  (121537087)

##### Writing Tools

###### Resolved Issues

- Fixed: After generating a list, key point, table, or summary in the pop-over, selecting “Replace” results in an error message.  (145186545)

## See Also

- [macOS Sequoia 15.5 Release Notes](macos-15_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.3 Release Notes](macos-15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.2 Release Notes](macos-15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15.1 Release Notes](macos-15_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sequoia 15 Release Notes](macos-15-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-15_4-release-notes)*