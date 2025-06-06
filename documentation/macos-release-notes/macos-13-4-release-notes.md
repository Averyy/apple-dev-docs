# macOS Ventura 13.4 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 13.3 SDK provides support to develop apps for Mac computers running Ventura 13.4. The SDK comes bundled with Xcode 14.3, available from the Mac App Store. For information on the compatibility requirements for Xcode 14.3, see [`Xcode 14.3 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-14_3-release-notes).

##### Apple Studio Display

###### Known Issues

- Apple Studio Display firmware update starts showing progress but never completes. (107287354)  To install other updates including future macOS Beta Updates, click “More info…” in Software Update Settings, uncheck Apple Studio Display firmware update, and click “Install Now.”

##### Css

###### Resolved Issues

- Fixed increasing `column-count` above 2 not updating the layout. (71808738)

##### File Bookmark

###### Resolved Issues

- Fixed a regression in macOS Ventura 13.3 where a security check causes bookmark resolution to fail when the path contains Unicode characters stored with composed normalization. As an example, this prevented files in Finder from opening when double-clicked. (107550080)

##### Swiftui

###### Resolved Issues

- Fixed: Using `ImageRenderer` within a `ShareLink`’s `preview` closure crashed the running application. (107763234)

## See Also

- [macOS Ventura 13.5 Release Notes](macos-13_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.3 Release Notes](macos-13_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.2 Release Notes](macos-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.1 Release Notes](macos-13_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13 Release Notes](macos-13-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-13_4-release-notes)*