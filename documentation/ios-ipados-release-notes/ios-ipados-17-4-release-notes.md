# iOS & iPadOS 17.4 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 17.4 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 17.4. The SDK comes bundled with Xcode 15.3, available from the Mac App Store. For information on the compatibility requirements for Xcode 15.3, see [`Xcode 15.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15_3-release-notes).

##### General

###### Known Issues

- Default browser choice screen might not show up when intended and apps requiring certain managed entitlements might not install or show an error.  (121566625)  Open Settings and navigate to Privacy & Security > Location Services. Toggle location services off for 10 seconds, and then turn it back on.

##### Alternative App Marketplaces

###### Known Issues

- For apps on an alternative marketplace that use [`Background Assets`](https://developer.apple.comhttps://developer.apple.com/documentation/backgroundassets), assets download after first launch instead of after installation.  (118965723)
- Large license IDs that a marketplace sets for an app that it distributes may cause app installation to fail.    (123357711) (FB13639300)  Choose a `licenseID` for the `ALDLicenseAttribute` initializer [`init(licenseID:)`](https://developer.apple.comhttps://developer.apple.com/documentation/applicensedeliverysdk/aldlicenseattribute/init(licenseid:)) that’s less than `Int64.max`.

##### App Store

###### Resolved Issues

- Fixed: Certain App Store product sheets will show a “Cannot Connect to iTunes Store” error.  (121523272)

##### Apple Maps and Carplay in Vehicle Instrument Clusters

###### New Features

- In iOS 17.4, with supported CarPlay vehicles, Apple Maps will present a new instrument cluster experience with information about upcoming maneuvers. Users will be able to swap the desired display type between the main and instrument cluster screen by tapping the map configuration button on the upper right of the Maps main screen.  (122833170)

##### Browserenginekit

###### Resolved Issues

- Fixed: The symbol [`createVisibilityPropagationInteraction`](https://developer.apple.comhttps://developer.apple.com/documentation/browserenginekit/propagating-view-visibility-information-to-browser-extensions) is missing in the SDK.  (119845855)

##### Gestures Reactions

###### New Features

- Developers can control the default behavior of Reactions with the key `NSCameraReactionEffectGesturesEnabledDefault`. This is controlled per application and user choice will override application declared defaults  (113811074)

##### Homekit

###### Resolved Issues

- Fixed: Viewing HomeKit camera live video might not work when away from home.  (121166796)

##### Maps

###### Resolved Issues

- Fixed: MapKit SwiftUI apps might show incorrect map mode for walking and cycling routes.  (121085728)

##### Messages

###### Resolved Issues

- Fixed: Stickers (Memoji and 3rd party) might appear blank.  (120994483)

##### Object Capture

###### New Features

- A new manual bounding box flow is now initiated if automatic object detection fails to find an object, particularly in cases where there is no salient ground plane.  In this flow, the user is expected to utilize the standard manual bounding box controls to indicate the bounding box of the object to capture by adjusting the provided starting box placed in the world in front of the user.  You can determine if this mode has been activated by observing for the new element `.objectNotDetected`, which will be added to the `ObjectCaptureSession`’s `Feedback` set when the manual flow has been activated.  You can use this to provide notification and/or instructions to the user about this manual box flow as desired.  (113474123)

###### Resolved Issues

- Fixed an issue where an `ObjectCaptureView` was incorrectly rotating the point cloud view in landscape UI orientations.  (114248688) (FB13030239)
- Fixed: PhotogrammetrySession creation on iOS is now significantly faster.  (114458164)
- Fixed a memory leak when ObjectCaptureSession was used in a SwiftUI Environment or was torn down without waiting for cleanup to finish.  (114481678) (FB13057864)

##### Passkeys

###### Resolved Issues

- Fixed: Registering passkeys might not work on certain websites.  (122217903)

##### Podcasts

###### Resolved Issues

- Fixed: Tapping on a podcast show from Recently Searched occasionally returns you to the Recently Searched view instead of the podcast show product page.  (120915925)

##### Setup Assistant

###### Resolved Issues

- Fixed: Pairing might fail when using Quick Start to set up a new device.  (120982013)

##### Shared Ipad

###### Resolved Issues

- Fixed: Users might be greeted with a “Loading” screen in the Files app immediately after log in on a Shared iPad.  (122092017)

##### Siri

###### New Features

- Siri can respond in a combination of English and Hindi, depending on the primary language you use to interact with Siri. In the Settings app, go to Siri & Search > Language > English (India) and choose English & Hindi as the Preferred Response Language. Then ask Siri something in Hindi.  (114742290)

##### Storekit

###### New Features

- In StoreKit testing in Xcode, a billing error StoreKit [`message`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/message) will be sent when a subscription tries to renew while the `Enable Billing Retry on Renewal` setting is enabled in the StoreKit configuration file. Use the [`messages listener`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/message/3954510-messages) API to control when StoreKit messages are displayed in your app.  (101869442)
- `productDescriptionHidden(_:)` API can be used to configure the visibility of product descriptions in `ProductView`, `StoreView` and `SubscriptionStoreView` instances within a view hierarchy. When building with Xcode 15.3, the view modifier can be used even if your app is running on iOS 17.0, iPadOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, visionOS 1.0, or later. When implementing a product view style, it can support this new view modifier by checking the `descriptionVisibility` property on the configuration value.  (110414819) (FB12261973)
- You can use [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) to present promotional offers by adding the `subscriptionPromotionalOffer(offer:signature:)` modifier. If you’re already using [`inAppPurchaseOptions(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/inapppurchaseoptions(_:)) modifier to support promotional offers for StoreKit views, you should adopt the new API instead when your app is running on iOS 17.4, iPadOS 17.4, macOS 14.4, tvOS 17.4, watchOS 10.4, visionOS 1.1 or later. Do not use both APIs to apply a promotional offer for the same view.  (115358806)

###### Resolved Issues

- Fixed: The [`isEligibleForIntroOffer`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/3803203-iseligibleforintrooffer) property and [`isEligibleForIntroOffer(for:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/3791958-iseligibleforintrooffer) method now reflect ineligibility in cases where a customer would otherwise be eligible for the offer if they weren’t actively subscribed. This means a customer which is not currently eligible for an introductory offer may become eligible in the future. Customers who redeem an introductory offer for a given subscription group will continue to never be eligible for another introductory offer in that subscription group. You can detect this case this by checking if any one transaction with a matching [`subscriptionGroupID`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/3749718-subscriptiongroupid) has the [`type`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/offer/4307073-type) property on [`offer`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/4307076-offer) set to [`introductory`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/offertype/3822309-introductory).  (103604770) (FB11889732)
- Fixed an issue causing SKAdNetwork versions 2.2 and 3.0 to not accept impressions or send postbacks.  (121223565)
- Fixed an issue causing some approved Ask to Buy purchases to fail.  (121249405)

##### Swiftui

###### New Features

- `Table` now supports dynamic numbers of columns with the new `TableColumnForEach`.  (79492167) (FB9189673)
- Popover presentations now automatically dismiss if they go outside the safe area.  (100811375)

###### Resolved Issues

- Fixed: Resolved an issue with programmatically present an alert or sheet simultaneously with dismissing another sheet. The new alert or sheet would not show but now it will. If you have code that presents the same sheet programmatically from multiple places in your view hierarchy at the same time, that sheet might no longer appear. Make sure that any `sheet` modifiers that are in the view hierarchy at the same time use distinct `isPresented` or `item` bindings.  (117475214)

##### Webkit

###### Resolved Issues

- Fixed HTML content not displaying in a Simulator, affecting projects using the web extension project template.  (121338366)

## See Also

- [iOS & iPadOS 17.6 Release Notes](ios-ipados-17_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.5 Release Notes](ios-ipados-17_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.3 Release Notes](ios-ipados-17_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.2 Release Notes](ios-ipados-17_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.1 Release Notes](ios-ipados-17_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17 Release Notes](ios-ipados-17-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-17_4-release-notes)*