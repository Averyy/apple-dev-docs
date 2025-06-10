# watchOS 11.1 Release Notes

**Framework**: watchOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 11.1 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 11.1. The SDK comes bundled with Xcode 16.1, available from the Mac App Store. For information on the compatibility requirements for Xcode 16.1, see [`Xcode 16.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-16_1-release-notes).

##### Storekit

###### Resolved Issues

- Fixed: In StoreKit Testing in Xcode, the offer identifier in the subscription renewal info might be reported incorrectly for offer codes.  (133774710)

##### Swiftui

###### Resolved Issues

- Fixed: Using `if #available` in @WidgetBundleBuilder and @SceneBuilder crashes on prior OS versions due to “unknown OS version.”  (136098106)

##### Widgetkit

###### Resolved Issues

- Fixed: Rectangular complications and Watch-specific custom Live Activity views use the wrong font metrics, causing title2 and title3 to render much larger than intended and largeTitle to render much smaller than intended. Additionally, custom Live Activity views use the wrong default font (SF Pro instead of SF Compact).  (135831317)

## See Also

- [watchOS 11.5 Release Notes](watchos-11_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 11.4 Release Notes](watchos-11_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 11.3 Release Notes](watchos-11_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 11.2 Release Notes](watchos-11_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 11 Release Notes](watchos-11-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-11_1-release-notes)*