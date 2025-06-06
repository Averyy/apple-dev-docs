# iOS & iPadOS 17.2 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 17.2 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 17.2. The SDK comes bundled with Xcode 15.1, available from the Mac App Store. For information on the compatibility requirements for Xcode 15.1, see [`Xcode 15.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15_1-release-notes).

##### Airdrop

###### Resolved Issues

- Fixed: Sending an AirDrop or using NameDrop to an 17.0 or 17.1 device might fail sporadically.  (117925962)

##### Apple Music

###### Resolved Issues

- Fixed: The Favorite Songs playlist might take a while to appear on some iOS/iPadOS, watchOS, and tvOS devices.  (117219873)

##### Avkit

###### Resolved Issues

- Fixed: `AVCaptureEventInteraction` does not currently respond to the Action button.  (112861854)

##### Camera

###### New Features

- Capture spatial video with remarkable depth on iPhone 15 Pro to view in 3D in the Photos app on Apple Vision Pro. Turn on spatial video capture in Settings > Camera > Formats, then capture spatial videos in Video mode in the Camera app.  (102470597)
- Added support for depth with select `AVCaptureDeviceFormats` on `AVCaptureDeviceTypeBuiltInTripleCamera`. Depth is now available on a wider range of `videoZoomFactors` on iPhone 15 Pro’s `AVCaptureDeviceTypeBuiltInTripleCamera` and iPhone 15’s `AVCaptureDeviceTypeBuiltInDualWideCamera` with select `AVCaptureDeviceFormats`. Select `AVCaptureDeviceFormats` now offer the ability to zoom when depth is enabled without a disruptive reconfiguration.  (110654309)

##### Fitness+

###### Known Issues

- While streaming a Fitness+ workout via AirPlay, real-time metrics might be missing if the stream was started through the AirPlay button in the top left corner of the video player.  (118467046)  Use the AirPlay button located in the bottom right corner of the video player to start the stream.

##### Imessage Contact Key Verification

###### New Features

- With iMessage Contact Key Verification, users can choose to further verify that they are messaging only with the people they intend. iMessage Contact Key Verification uses Key Transparency to enable automatic verification that the iMessage key distribution service returns device keys that have been logged to a verifiable and auditable map. When a user enables the feature, they will be notified about any validation errors directly in the Messages conversation transcript and Apple ID Settings. For even higher security, iMessage Contact Key Verification users can compare a contact verification code in person, on FaceTime, or through another secure call. They can also choose to create or edit a contact and save a public key to turn on iMessage Contact Key Verification with that person. All devices signed into your iCloud account must be on the minimum supported version of iOS 17.2 Beta, macOS 14.2 Beta, or watchOS 10.2 Beta. If you wish to keep using other devices on older versions of the OS, you will need to sign out of iMessage on these devices in order to enable contact key verification.  (111356044)

###### Resolved Issues

- Fixed: When verifying another user, Contact Verification Code will not show unless both users are on beta 4 or higher.   (114462363)
- Fixed: After verifying a contact, the verificaton checkmark might not show up in Messages app.  (116142336)
- Fixed: Users might see an error to Turned Off transcript every few hours.   (116405131)
- Fixed: Users might see that they’re are not eligible to enable Contact Key Verification on some of their upgraded devices.  (117044482)

###### Known Issues

- The Learn More links do not link to Knowledge Base articles during Beta.  (101563811)

##### Journal

###### New Features

- Journal is a new app that helps iPhone users reflect and practice gratitude through journaling.  (117631805)

###### Resolved Issues

- Fixed: Setting a schedule for notifications will cause Journaling Suggestions notifications to not trigger. However, user will continue to receive Journal App notifications with the set schedule beginning 3 days after onboarding to Journaling Suggestions.  (116999378)
- Fixed: Users might see duplicate journaling suggestions.  (117099386)
- Fixed: Journaling Suggestions might not get populated.  (117170356)

##### Journaling Suggestions Api

###### New Features

- Journaling Suggestions provides a visual picker interface for iPhone apps. The picker displays personal Moments that occur in someone’s life, such as their workouts and exercise, places they visit, a trip they take, a person they connect with, their photo memory highlights, Photos in their library, a song or podcast they listen to. Only suggestions explicitly added by the user will be shared with an app.  If your app donates activities or interactions to SiriKit or CallKit or if someone authorizes your app to save data to HealthKit, some data might show up as part of Journaling Suggestions.  (117044228)

###### Known Issues

- Landscape mode is not supported for Journaling Suggestions API.  (117154771)  Please use Portrait mode only.

##### Messages

###### Resolved Issues

- Fixed: Unlocalized string shown for member count in the full screen Map View of Group Messages might appear (e.g. `DETAIL_NUMBER_OF_PEOPLE_LABEL`).  (117287022)

##### Music App

###### Resolved Issues

- Fixed: Apple Music recently searched content might not appear in the recently searched section of the Search tab in the Music app, on devices that had iOS 17.2 Beta 1, Beta 2 or Beta 3 installed. Library recently searched items are unaffected.  (117109015)

##### Personal Hotspot

###### Resolved Issues

- Fixed: Some third-party devices might be unable to connect to iPhone Personal Hotspot.  (113517807)

##### Storekit

###### New Features

- New pricing properties `price`, `currency`, and `currencyCode` are now available on [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction). If an offer was applied to the transaction, a new property `offer` is available to see information about it (id, type, payment mode), as well as convenience properties `offerID`, `offerType`, and `offerPaymentMode`.  (106650768)

###### Resolved Issues

- Fixed: The StoreKit 2 Transaction properties `price`, `currency`, and `Offer.paymentMode` now have Optional types.  (116592563)
- Fixed: The StoreKit 2 Transaction properties `price`, `currency`, and `Offer.paymentMode` now have Optional types.  (116809380)
- Fixed an issue causing `productViewControllerDidFinish(_:)` method in [`SKStoreProductViewControllerDelegate`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/skstoreproductviewcontrollerdelegate) to be called before the page is dismissed.  (117113118) (FB13284259)
- Fixed an issue causing the refund request “Done” button to not dismiss the sheet when using StoreKit Testing in Xcode.  (117482750)
- Fixed an issue where StoreKit 2 `deviceVerification` was incorrect, which caused transaction verification to fail.  (117689523) (FB13315344)

##### Storekit Testing in Xcode

###### New Features

- New testing functionality to send [`Purchase Intents`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/purchaseintent) to apps using StoreKit Testing in Xcode from the Transaction Manager.  (101034395)

##### Swift Charts

###### Resolved Issues

- Fixed an issue where a scrollable chart did not respect the initial non-zero binding value passed to `chartScrollPosition`.  (114889276)

##### Swiftui

###### New Features

- Use `_logChanges()` to log causes of SwiftUI view updates. Call the new debugging method `_logChanges()` in the body of a SwiftUI view to log information about why the system is updating the view. For example: ```swift
     struct MyView: View {
         var body: some View {
             #if DEBUG
             let _ = Self._logChanges()
             #endif
             // … rest of view body …
         }
     }
``` As well as the physical property names, “@self” marks that the view value itself has changed, and “@identity” marks that the identity of the view has changed (that is, that the persistent data associated with the view has been recycled for a new instance of the same type). The new `_logChanges()` method is like the existing `_printChanges()` one, except that the new method uses the system console, which is useful in some debugging workflows. Calls to `_logChanges()` log at the info level to the “com.apple.SwiftUI” subsystem with the category “Changed Body Properties”.  (113352555)

###### Resolved Issues

- Fixed: Resolved a possible Swift access conflict crash that could occur with toolbar items.  (113992797)
- Fixed: To prevent unintentional implicit dependency cycles, ImageRenderer no longer sends Observable updates when the image it produces changes. This change  affect the behavior when a dependency is explicitly declared by observing the ImageRenderer’s publisher.  (116836341)

##### Widgetkit

###### Resolved Issues

- Fixed: In widgets `Text(_:style:)` does not animate its content by default.  (107582710)

## See Also

- [iOS & iPadOS 17.6 Release Notes](ios-ipados-17_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.5 Release Notes](ios-ipados-17_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.4 Release Notes](ios-ipados-17_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.3 Release Notes](ios-ipados-17_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17.1 Release Notes](ios-ipados-17_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 17 Release Notes](ios-ipados-17-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-17_2-release-notes)*