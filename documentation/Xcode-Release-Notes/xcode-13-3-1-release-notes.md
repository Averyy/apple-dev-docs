# Xcode 13.3.1 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

#### Overview

Xcode 13.3.1 includes SDKs for iOS 15.4, iPadOS 15.4, tvOS 15.4, watchOS 8.5, and macOS Monterey 12.3. The Xcode 13.3.1 release supports on-device debugging for iOS 15.4, iPadOS 15.4, tvOS 15.4, watchOS 8.5 and later. Xcode 13.3.1 requires a Mac running macOS Monterey 12 or later.

##### Apple Clang Compiler

###### Resolved Issues

- Fixed: Exporting an app that uses Swift’s concurrency features from an archive with bitcode might fail when the app targets iOS 13.0–14.7, watchOS 6.0–7.6, or tvOS 13.0–14.7. (89271047)
- When you target iOS 13.4 and later and enable bitcode, the bitcode segment is now stripped correctly. This fixes a crash that prevented some apps from running in older operating systems (iOS 14 and earlier). (90024354) (FB9951126)

## See Also

- [Xcode 13.4.1 Release Notes](xcode-13_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.4 Release Notes](xcode-13_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.3 Release Notes](xcode-13_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.2.1 Release Notes](xcode-13_2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.2 Release Notes](xcode-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.1 Release Notes](xcode-13_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13 Release Notes](xcode-13-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-13_3_1-release-notes)*