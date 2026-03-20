# tvOS 26.4 RC Release Notes

**Framework**: tvOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 26.4 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 26.4 RC. The SDK comes bundled with Xcode 26.4, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.4, see [`Xcode 26.4 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_4-release-notes).

##### Address Sanitizer

###### Known Issues

- Address Sanitizer and Thread Sanitizer might hang on macOS 26.4, iOS 26.4, tvOS 26.4, watchOS 26.4, and visionOS 26.4 when building with Xcode 26.3 or older.  (171762808) **Workaround:** Use Xcode 26.4 when testing applications with Address Sanitizer or Thread Sanitizer.

##### Background Assets

###### New Features

- You can now check the status of an asset pack while offline by calling `localStatus(ofAssetPackWithID:)` or `assetPackIsAvailableLocally(withID:)` on the shared asset pack manager. The former method returns all available status information. The latter returns only a Boolean value but can be called synchronously. Not all status information is available offline.  (164498466)
- You can make the latest version of an asset pack available locally by calling `ensureLocalAvailability(of:requireLatestVersion:)` on the shared asset pack manager and passing `true` to the `shouldUpdate` parameter.  (166237389)

###### Resolved Issues

- Fixed: Apps might crash when downloading asset packs.  (169648111)

##### Networking

###### Resolved Issues

- Fixed: Multiple processes leak `CFRunLoopSource` objects when Automatic proxy configuration (PAC) or Auto proxy discovery are configured. For clients of the `CFNetworkExecuteProxyAutoConfigurationURL` and `CFNetworkExecuteProxyAutoConfigurationScript` API, please check to make sure your process is not working around the leak by overreleasing the `CFRunLoopSourceRef` returned by those functions or the `CFArrayRef` and `CFErrorRef` passed to the completion.  (166839810) (FB21376045)

##### Storekit

###### New Features

- New fields [`revocationType`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.property) and [`revocationPercentage`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/revocationpercentage) have been added to [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction).  (148858551)

###### Resolved Issues

- Fixed: Purchase Intents might not be emitted from the intents sequence when the app is launched from the background.  (168958783) (FB21767675)

##### Swiftui

###### Resolved Issues

- Fixed: SwiftUI does not surface the latest `.userActivity` as the current user activity.  (163136831)

###### Known Issues

- Multiple implicit SwiftUI animations (triggered by `RealityViewContent.animate` or `Entity.animate`) that modify a RealityKit component’s properties, are combined only when the implicit animations target the same set of component properties. For example, if you initiate an implicit animation on Transform.scale and then initiate an implicit animation on Transform.scale and Transform.translation then the animations affecting the scale property will be independent of each other, and will not combine. In this case, the most recently initiated animation will overwrite the scale property.  (169723142) **Workaround:** Ensure the same component properties are animated by subsequent implicit animations when possible.

## See Also

- [tvOS 26.3 Release Notes](tvos-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 26.2 Release Notes](tvos-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 26.1 Release Notes](tvos-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 26 Release Notes](tvos-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-26_4-release-notes)*