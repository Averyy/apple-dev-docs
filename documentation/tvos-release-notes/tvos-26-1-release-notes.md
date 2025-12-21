# tvOS 26.1 Release Notes

**Framework**: tvOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The tvOS 26.1 SDK provides support to develop tvOS apps for Apple TV devices running tvOS 26.1. The SDK comes bundled with Xcode 26.1, available from the Mac App Store. For information on the compatibility requirements for Xcode 26.1, see [`Xcode 26.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-26_1-release-notes).

##### Background Assets

###### Resolved Issues

- Fixed: `AssetPackManager.url(for:)` unexpectedly throws an error when looking up the URL for a locally available asset file.  (157959878) (FB19512759)

##### Game Controller

###### Resolved Issues

- Fixed: The time returned by `GCPressedStateInput.lastPressedStateTimestamp` is not in the correct time domain.  (159124910)

##### Swiftui

###### Resolved Issues

- Fixed: The `navigationLinkIndicatorVisibility` modifier crashes when run on iOS 17, iOS 18 and aligned releases. You must recompile your app against the 26.1 SDK to receive this fix.  (158236264) (FB19613386)
- Fixed: `sheet` uses a modal sheet presentation style instead of full-screen presentation style.  (158812856)

## See Also

- [tvOS 26.3 Beta Release Notes](tvos-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 26.2 Release Notes](tvos-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [tvOS 26 Release Notes](tvos-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvos-release-notes/tvos-26_1-release-notes)*