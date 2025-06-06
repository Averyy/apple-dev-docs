# watchOS 9.1 Release Notes

**Framework**: Watchos Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The watchOS 9.1 SDK provides support to develop watchOS apps for Apple Watch devices running watchOS 9.1. The SDK comes bundled with Xcode 14.1 RC, available from [`Beta Software Downloads`](https://developer.apple.comhttps://developer.apple.com/download/). For information on the compatibility requirements for Xcode 14.1, see [`Xcode 14.1 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-14_1-release-notes).

##### Memory Allocation

###### Known Issues

- The system memory allocator `free` operation zeroes out most deallocated blocks in watchOS 9.1 beta or later. Invalid accesses to free memory might result in new crashes or corruption, including: - Read-after-free bugs that previously observed the old contents of a block may now observe zeroes instead
- Write-after-free bugs may now cause subsequent calls to `calloc` to return non-zero memory

To debug these issues, use Address Sanitizer and Guard Malloc (see `libgmalloc(3)`). (97449075)

## See Also

- [watchOS 9.6 Release Notes](watchos-9_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.5 Release Notes](watchos-9_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.4 Release Notes](watchos-9_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.3 Release Notes](watchos-9_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 9.2 Release Notes](watchos-9_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [watchOS 9 Release Notes](watchos-9-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchos-release-notes/watchos-9_1-release-notes)*