# watchOS 26.4 Beta Release Notes

**Framework**: watchOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 26.4 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 26.4 beta. The SDK comes bundled with Xcode 26.4, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.4, see [`Xcode 26.4 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_4-release-notes).

##### Apple Maps

###### Known Issues

- Directions might fail to load on Watch when the companion iPhone is connected.  (168923852)  Start directions from the companion iPhone.

##### Movement Disorder Api

###### Resolved Issues

- Fixed: The Movement Disorder API has enhanced analytics around database access errors.  (129771567)

##### Networking

###### Resolved Issues

- Fixed: Multiple processes leak `CFRunLoopSource` objects when Automatic proxy configuration (PAC) or Auto proxy discovery are configured. For clients of the `CFNetworkExecuteProxyAutoConfigurationURL` and `CFNetworkExecuteProxyAutoConfigurationScript` API, please check to make sure your process is not working around the leak by overreleasing the `CFRunLoopSourceRef` returned by those functions or the `CFArrayRef` and `CFErrorRef` passed to the completion.  (166839810) (FB21376045)

##### Storekit

###### New Features

- New fields [`revocationType`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.property) and [`revocationPercentage`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction/revocationpercentage) have been added to [`Transaction`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/transaction).  (148858551)

##### Swiftui

###### Resolved Issues

- Fixed: SwiftUI does not surface the latest `.userActivity` as the current user activity.  (163136831)

##### Workout

###### Known Issues

- When you start a workout with Workout Buddy enabled, the timer might appear to be delayed by a few seconds before it starts counting.  (169030068)  Disable Workout Buddy in the Workout app settings.

## See Also

- [watchOS 26.3 Release Notes](watchos-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 26.2 Release Notes](watchos-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 26.1 Release Notes](watchos-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 26 Release Notes](watchos-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-26_4-release-notes)*