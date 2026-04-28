# visionOS 26.4 Release Notes

**Framework**: visionOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The visionOS 26.4 SDK provides support for developing apps for Apple Vision Pro devices running visionOS 26.4. The SDK comes bundled with Xcode 26.4, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.4, see [`Xcode 26.4 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_4-release-notes).

##### Address Sanitizer

###### Known Issues

- Address Sanitizer and Thread Sanitizer might hang on macOS 26.4, iOS 26.4, tvOS 26.4, watchOS 26.4, and visionOS 26.4 when building with Xcode 26.3 or older.  (171762808) **Workaround:** Use Xcode 26.4 when testing applications with Address Sanitizer or Thread Sanitizer.

##### Background Assets

###### New Features

- You can now check the status of an asset pack while offline by calling `localStatus(ofAssetPackWithID:)` or `assetPackIsAvailableLocally(withID:)` on the shared asset pack manager. The former method returns all available status information. The latter returns only a Boolean value but can be called synchronously. Not all status information is available offline.  (164498466)
- You can make the latest version of an asset pack available locally by calling `ensureLocalAvailability(of:requireLatestVersion:)` on the shared asset pack manager and passing `true` to the `shouldUpdate` parameter.  (166237389)

###### Resolved Issues

- Fixed: Apps might crash when downloading asset packs.  (169648111)

##### Foveated Streaming

###### New Features

- visionOS 26.4 supports NVIDIA CloudXR with foveated streaming, enabling apps to display high-resolution, low-latency immersive content on Apple Vision Pro. To implement this new feature, refer to the Apple Developer documentation for [`FoveatedStreaming`](https://developer.apple.comhttps://developer.apple.com/documentation/foveatedstreaming).  (170184382)

###### Resolved Issues

- Fixed: The current remote streaming API `public static func remote (serverName: String)` does not include the signaling headers which is used for Vision Pro connection with the server. The signaling headers can be used for authentication and for manipulating the remote scene.  (170085006)

###### Known Issues

- If the user takes off Apple Vision Pro while using the ‘FoveatedStreaming’ feature to stream CloudXR-enabled content, the steam will not pause as expected and the battery will drain.  (171672303) **Workaround:** Setup passcode in Vision Pro to avoid this issue
- User input is unsupported for targets beyond 4 meters.   (172134620) **Workaround:** Ensure that your UI is within 4 meters from the streaming space origin. If you run into this issue and input stops working for the UI that was originally outside of the 4 meter distance, force quit the app to get it working again.

##### Managed App Distribution

###### Known Issues

- `ManagedAppView` might render blank when multiple apps are displayed simultaneously in Managed App Distribution.  (171016274) **Workaround:** Display a single `ManagedAppView` in Managed App Distribution.

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

- [visionOS 26.5 Beta 4 Release Notes](visionos-26_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 26.3 Release Notes](visionos-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 26.2 Release Notes](visionos-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 26.1 Release Notes](visionos-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [visionOS 26 Release Notes](visionos-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/visionos-release-notes/visionos-26_4-release-notes)*