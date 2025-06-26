# tvOS 18.2 Release Notes

**Framework**: tvOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 18.2 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 18.2. The SDK comes bundled with Xcode 16.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 16.2, see [`Xcode 16.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-16_2-release-notes).

##### Swiftui

###### Resolved Issues

- Fixed: Compiling in the Swift 6 language mode might cause an `@Entry` error due to “static property `defaultValue` is not concurrency-safe because non-‘Sendable’ type”.  (133885814)
- Fixed: Views won’t accept dropped directories if [`UTType.directory`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/directory) or [`UTType.fileURL`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/fileurl) are not in the list of accepted content types for drop.  (138158126)

## See Also

- [tvOS 18.6 Beta Release Notes](tvos-18_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 18.5 Release Notes](tvos-18_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 18.4 Release Notes](tvos-18_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 18.3 Release Notes](tvos-18_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 18.1 Release Notes](tvos-18_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 18 Release Notes](tvos-18-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-18_2-release-notes)*