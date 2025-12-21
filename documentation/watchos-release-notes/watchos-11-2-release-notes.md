# watchOS 11.2 Release Notes

**Framework**: watchOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 11.2 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 11.2. The SDK comes bundled with Xcode 16.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 16.2, see [`Xcode 16.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-16_2-release-notes).

##### Battery Health

###### Resolved Issues

- Fixed: This update addresses potential inaccurate estimates of battery health reporting for some devices on watchOS 11.2 Beta 1 & 2.  (139724084)

##### Storekit

###### Resolved Issues

- Fixed: Resolved an issue where using `SubscriptionStoreView` might cause an app to crash when running watchOS 11. If your app runs on watchOS versions 11.0 or 11.1, use the ‘buttons’ subscription store control style to work around the crash.  (138045666)

##### Swiftui

###### Resolved Issues

- Fixed: Compiling in the Swift 6 language mode might cause an `@Entry` error due to “static property `defaultValue` is not concurrency-safe because non-‘Sendable’ type”.  (133885814)
- Fixed: Views won’t accept dropped directories if [`UTType.directory`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/directory) or [`UTType.fileURL`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/fileurl) are not in the list of accepted content types for drop.  (138158126)

## See Also

- [watchOS 11.6 Release Notes](watchos-11_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 11.5 Release Notes](watchos-11_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 11.4 Release Notes](watchos-11_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 11.3 Release Notes](watchos-11_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 11.1 Release Notes](watchos-11_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 11 Release Notes](watchos-11-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-11_2-release-notes)*