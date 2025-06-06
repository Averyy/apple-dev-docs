# macOS Sonoma 14.1 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 14 SDK provides support to develop apps for Mac computers running Sonoma 14.1. The SDK comes bundled with Xcode 15, available from the Mac App Store. For information on the compatibility requirements for Xcode 15, see [`Xcode 15 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-15-release-notes).

##### Remote Widgets

###### Resolved Issues

- Fixed: Remote Widgets might render blank on mismatched iOS and macOS releases.  (115436466)

##### Wallet

###### Resolved Issues

- Fixed: Some event ticket passes might fail to ingest into Wallet when added from a website on a Mac.  (115216417)

##### Widgetkit

###### Known Issues

- In widgets `Text(_:style:)` doesn’t animate its content by default.  (107582710)  To explicitly request an animation, use the `View.contentTransition(_:)` modifier.

##### Iphone 12 in France

###### Notes

- Updates the iPhone 12 for users in France to accommodate a test protocol for Specific Absorption Rate (SAR) testing. For more information, visit this website: [`https://support.apple.com/kb/HT213923`](https://developer.apple.comhttps://support.apple.com/kb/HT213923)  (116601274)

## See Also

- [macOS Sonoma 14.6 Release Notes](macos-14_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.5 Release Notes](macos-14_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.4 Release Notes](macos-14_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.3 Release Notes](macos-14_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14.2 Release Notes](macos-14_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Sonoma 14 Release Notes](macos-14-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-14_1-release-notes)*