# visionOS 1.1 Release Notes

**Framework**: Visionos Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The visionOS 1.1 SDK provides support for developing apps for Apple Vision Pro devices running visionOS 1.1. The SDK comes bundled with Xcode 15.3, available from the Mac App Store. For information on the compatibility requirements for Xcode 15.3, see [`Xcode 15.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15_3-release-notes).

##### General

###### Resolved Issues

- Fixed: Apps built for visionOS changing scene types or upgrading from a compatible app will crash on launch if previously launched on a device.  (121478050)

##### 3rd Party Apps

###### Known Issues

- Some third-party apps might crash on launch or during use when Accessibility options are enabled.  (122506670) (FB13595783)  Disable any Accessibility options before launching impacted apps.

##### Accessibility

###### Resolved Issues

- Fixed: The AccessibilityShortcut preference is reset if VoiceOver is toggled via triple-click of the crown immediately after completing setup.  (121466353)

##### App Placement

###### New Features

- Near-user boundary for volumetric scenes have been modified. Users will now be able to reposition volumetric scenes much closer than before, which will enable easier direct interaction with the volumetric scene content.  (120926205)

##### App Store Submission

###### Resolved Issues

- Fixed: Apps built for visionOS are unable to use the front-facing-camera UI Required Device Capability.   (121465787)

##### Control Center

###### Resolved Issues

- Fixed: Opening Control Center during tracking fail or while transitioning into Travel Mode will lead to the Control Center indicator disappearing.  (119676121)

###### Known Issues

- The Control Center indicator might be missing.  (121071017)  Reboot your Apple Vision Pro.

##### Immersive Space

###### Resolved Issues

- Fixed: Immersive apps might not resume automatically if Apple Vision Pro is taken off and put back in a different location.  (122561314)

##### Lock Screen

###### Resolved Issues

- Fixed: Passcodes containing a character which uses a diacritic can’t be used to unlock Apple Vision Pro.  (122551154)

##### Mac Virtual Display Airplay Wireless

###### Known Issues

- Mac Virtual Display and AirPlay are known to conflict when used concurrently. Concurrent usage might result in performance degradation including connection failure.  (110475215)

##### Markup

###### Resolved Issues

- Fixed: Markup is not available for use in the visionOS Simulator.  (122125666)

##### Notifications

###### Known Issues

- Users might see session interruption notifications that are not relevant to their app.  (123124097)  Filter notifications against audio session of choice like so: NotificationCenter.default.addObserver(forName: AVAudioSession.interruptionNotification, object: AVAudioSession.sharedInstance(), queue: nil) { … }

##### Passcode

###### Resolved Issues

- Fixed: Passcode UI not obscured in screen recording and sharing.  (121482327)

##### Passkeys

###### Resolved Issues

- Fixed: Registering passkeys might not work on certain websites.  (122217903)

##### Persona Enrollment

###### Resolved Issues

- Fixed: Eye tracking may not be accurate after Persona capture until the next time you put on Apple Vision Pro.   (121630768)

##### Realitykit

###### Resolved Issues

- Fixed: In multi-scene apps, custom [`Systems`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/system) created for each scene are now released when the scene is dismissed.  (116190653)
- Fixed: RealityKit reports incorrect visualBounds for Attachments, which may impact entity placement. Larger attachments may be clipped due to the incorrect visualBounds values.  (121887607)
- Fixed: A scene associated with the RealityRenderer might be incorrectly registered to a non-RealityRenderer system resulting in a crash.  (122392672)

###### Known Issues

- A scene associated with the RealityRenderer using a custom system is not updated every frame.  (110476883)  Update your components by subscribing to SceneEvents.Update rather than using a System.
- Assigning a new VideoPlayerComponent to an Entity that already has one will result in a black video screen.  (117087641)  Reuse the existing VideoPlayerComponent or remove the existing one first before assigning the new one.

##### Settings

###### Resolved Issues

- Fixed: Users might not be able to shut down Apple Vision Pro from Settings.  (120555236)

##### Shadergraph Materials

###### Known Issues

- ShaderGraph material node compositions might result in invalid visual output.  (122723231)  Avoid using a common asset node for both a surface shader and a geometry modifier within a single material or duplicate the asset node if needed.

##### Simulator

###### Resolved Issues

- Fixed: Simulator might quit unexpectedly when using Apple Studio Display or other 4-channel systems for audio output.  (122506938)

##### Siri

###### Resolved Issues

- Fixed: Siri may be unusable.  (122361345)
- Fixed: Unable to invoke Siri in simulator.  (122514562)

##### Storekit

###### New Features

- New pricing properties `price`, `currency`, and `currencyCode` are now available on [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction). If an offer was applied to the transaction, a new property `offer` is available to see information about it (id, type, payment mode), as well as convenience properties `offerID`, `offerType`, and `offerPaymentMode`.  (106650768)
- `productDescriptionHidden(_:)` API can be used to configure the visibility of product descriptions in `ProductView`, `StoreView` and `SubscriptionStoreView` instances within a view hierarchy. When building with Xcode 15.3, the view modifier can be used even if your app is running on iOS 17.0, iPadOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, visionOS 1.0, or later. When implementing a product view style, it can support this new view modifier by checking the `descriptionVisibility` property on the configuration value.  (110414819) (FB12261973)
- You can use [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) to present promotional offers by adding the `subscriptionPromotionalOffer(offer:signature:)` modifier. If you’re already using [`inAppPurchaseOptions(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/swiftui/view/inapppurchaseoptions(_:)) modifier to support promotional offers for StoreKit views, you should adopt the new API instead when your app is running on iOS 17.4, iPadOS 17.4, macOS 14.4, tvOS 17.4, watchOS 10.4, visionOS 1.1 or later. Do not use both APIs to apply a promotional offer for the same view.  (115358806)

###### Resolved Issues

- Fixed: The [`isEligibleForIntroOffer`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/3803203-iseligibleforintrooffer) property and [`isEligibleForIntroOffer(for:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/product/subscriptioninfo/3791958-iseligibleforintrooffer) method now reflect ineligibility in cases where a customer would otherwise be eligible for the offer if they weren’t actively subscribed. This means a customer which is not currently eligible for an introductory offer may become eligible in the future. Customers who redeem an introductory offer for a given subscription group will continue to never be eligible for another introductory offer in that subscription group. You can detect this case this by checking if any one transaction with a matching [`subscriptionGroupID`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/3749718-subscriptiongroupid) has the [`type`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/offer/4307073-type) property on [`offer`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/4307076-offer) set to [`introductory`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/offertype/3822309-introductory).  (103604770) (FB11889732)
- Fixed an issue causing the refund request “Done” button to not dismiss the sheet when using StoreKit Testing in Xcode.  (117482750)
- Fixed: Apps which configure a [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) to show terms of service & privacy policy links with automatic or URL destinations will now open the URLs in the default browser.  (120985657) (FB13540404)

##### Swiftui

###### New Features

- Immersive Space displacement value added to the Environment, indicating when the system has moved an Immersive Space from its default position for an active SharePlay session.  (117694400)
- Introduced named SwiftUI coordinate space for Immersive Space. Allows cross-window coordinate conversions to an open immersive space.  (118422388)

###### Resolved Issues

- Fixed: Volumes using the `defaultSize(_: Rect3D, in: UnitLength)` modifier to specify size, will now be the specified physical size at all display zooms.  (116579319) (FB13240946)
- Fixed: If the display zoom is changed in settings while a volume with a physical size is open, the content might be clipped.  (120554484)

###### Known Issues

- If the display zoom is changed in settings while a volume with a physical size is open, the content might be clipped.  (120806632)  Closing the volume or force-quitting the app.

##### Ui Frameworks

###### Resolved Issues

- Fixed: Navigation bar display title modes are now respected and result in a smaller or larger navigation bar title.  (114283700)

##### Uikit

###### Resolved Issues

- Fixed: `UIApplication. setAlternateIconName(_:completionHandler:)` is not supported in native visionOS apps. This does not affect compatible apps running on visionOS.  (120929653) (FB13535833)

##### Vibrancy

###### Resolved Issues

- Fixed: `UILabel.preferredVibrancy` only supported semantic label colors, but now it supports all colors. ```None
 let label = UILabel()
 label.preferredVibrancy = .automatic // default value
 label.textColor = .red // label will be rendered as vibrant red.
``` (115106359)

## See Also

- [visionOS 1.3 Release Notes](visionos-1_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 1.2 Release Notes](visionos-1_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS Release Notes](visionos-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos-release-notes/visionos-1_1-release-notes)*