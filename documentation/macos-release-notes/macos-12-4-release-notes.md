# macOS Monterey 12.4 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 12.4 SDK provides support to develop apps for Mac computers running macOS Monterey 12.4. The SDK comes bundled with Xcode 13.4, available from the Mac App Store. For information on the compatibility requirements for Xcode 13.4, see [`Xcode 13.4 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-13_4-release-notes).

##### Core Foundation

###### Known Issues

- XCTest is unable to interact with any TCC dialogs in this release (such as the ones asking the user for access privilege to their camera or microphone). There is no workaround. (92766684)

##### Store Kit

###### Resolved Issues

- Fixed an issue so developers using StoreKit 2 can now initiate a subscription offer purchase for a product that the customer currently subscribes to. (89152302)

##### Universal Control

###### Known Issues

- Universal Control in this release isn’t compatible with macOS 12.3 and iOS 15.4.  Use Universal Control between macOS 12.4 and iOS 15.5. (91136128)

## See Also

- [macOS Monterey 12.5 Release Notes](macos-12_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.3 Release Notes](macos-12_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.2 Release Notes](macos-12_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.1 Release Notes](macos-12_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Monterey 12.0.1 Release Notes](macos-12_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-12_4-release-notes)*