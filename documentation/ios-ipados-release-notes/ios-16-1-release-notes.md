# iOS 16.1 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS 16.1 SDK provides support to develop apps for iPhone and iPad running iOS 16.1. The SDK comes bundled with Xcode 14.1 RC, available from [`Beta Software Downloads`](https://developer.apple.comhttps://developer.apple.com/download/). For information on the compatibility requirements for Xcode 14.1, see [`Xcode 14.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-14_1-release-notes).

##### Home

###### Known Issues

- You might receive an alert to turn on Wi-Fi when pairing a Matter accessory. (98460235)  Ensure your device is connected to your Wi-Fi network.
- Adjusting the color or color temperature might result in an unexpected color set on a Matter accessory. (98578966)
- Accessory details might not open if a Matter accessory is unreachable. (99232316)
- The device that initiates the pairing needs to use the same iCloud account as the home hub. Only the owner of a home, not an invited user, can pair Matter accessories. (76012945)

##### Memory Allocation

###### Known Issues

- The system memory allocator `free` operation zeroes out all deallocated blocks in iOS 16.1 beta or later. Invalid accesses to free memory might result in new crashes or corruption, including: - Read-after-free bugs that previously observed the old contents of a block may now observe zeroes instead
- Write-after-free bugs may now cause subsequent calls to `calloc` to return non-zero memory To debug these issues, use Address Sanitizer and Guard Malloc (see `libgmalloc(3)`). (97449075)

##### Storekit

###### Resolved Issues

- Fixed an issue where restoring transactions wouldn’t prompt for authentication or restore any transactions if there was no App Store account signed in. (99506258)

- Fixed an issue where purchasing or restoring in-app transactions with hosted content would block new purchases or restores from processing. (100117681)

## See Also

- [iOS & iPadOS 16.6 Release Notes](ios-ipados-16_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.5 Release Notes](ios-ipados-16_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.4 Release Notes](ios-ipados-16_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.3 Release Notes](ios-ipados-16_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.2 Release Notes](ios-ipados-16_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS 16 Release Notes](ios-16-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iPadOS 16 Release Notes](ipados-16-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-16_1-release-notes)*