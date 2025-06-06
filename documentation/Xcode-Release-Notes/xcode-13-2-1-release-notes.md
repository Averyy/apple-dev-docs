# Xcode 13.2.1 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

#### Overview

Xcode 13.2.1 includes SDKs for iOS 15.2, iPadOS 15.2, tvOS 15.2, watchOS 8.3, and macOS Monterey 12.1. The Xcode 13.2.1 release supports on-device debugging for iOS 9 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 13.2.1 requires a Mac running macOS 11.3 Big Sur or later.

##### General

###### Resolved Issues

- Resolved an issue where the Mac App Store version of Xcode failed during package resolution with the error `Internal error: missingPackageDescriptionModule` when using Swift packages either standalone or as dependencies in an Xcode project or workspace. (86435800) (FB9807887)

###### Known Issues

- Xcode contains a copy of the log4j library that has the CVE-2021-44228 security vulnerability. Xcode automatically downloads an updated version of this library and installs it into `~/Library/Caches/com.apple.amp.itmstransporter`. When submitting apps to the App Store, Xcode uses the updated version of the library. (86390060)

##### Apple Clang Compiler

###### Resolved Issues

- Fixed an issue where apps built with Xcode 13 or Xcode 13.1 sometimes crashed at launch with an error reporting that the `libswift_Concurrency.dylib` library was not loaded. This only affected apps that used Swift Concurrency features (such as `async`/`await`), deployed to iOS prior to 15, tvOS prior to 15, or watchOS prior to 8, and had bitcode enabled. (86349088)

## See Also

- [Xcode 13.4.1 Release Notes](xcode-13_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.4 Release Notes](xcode-13_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.3.1 Release Notes](xcode-13_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.3 Release Notes](xcode-13_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.2 Release Notes](xcode-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.1 Release Notes](xcode-13_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13 Release Notes](xcode-13-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-13_2_1-release-notes)*