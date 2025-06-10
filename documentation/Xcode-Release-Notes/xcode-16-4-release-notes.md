# Xcode 16.4 Beta Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 16.4 beta includes SDKs for iOS 18.5, iPadOS 18.5, tvOS 18.5, watchOS 11.5, macOS Sequoia 15.5, and visionOS 2.5. The Xcode 16.4 beta release supports on-device debugging in iOS 15 and later, tvOS 15 and later, watchOS 7 and later, and visionOS. Xcode 16.4 beta requires a Mac running macOS Sequoia 15.3 or later.

##### Apple Clang Compiler

###### Resolved Issues

- Fixed: The base template for `std::char_traits` is restored after being removed in Xcode 16.3; it is still deprecated and is going to be removed in a future release. Restoring the base template allows code that attempts to instantiate `char_traits` with types that are not provided by the Standard (for example, `std::basic_string<long long>` and similar) to still compile, giving it more time to transition.   (149025504)

##### Device

###### New Features

- The command `devicectl diagnose` now obtains a sysdiagnose from your Mac and all available devices by default.  (104845318)

##### Instruments

###### Resolved Issues

- Fixed: Improved error handling for the Processor Trace Instrument when targeting binary not signed with get-task-allow entitlement.   (139032322)

##### Source Editor

###### Resolved Issues

- Fixed: Some C++ headers were experiencing crashes in syntax highlighting and Quick Help.  (148020379)

## See Also

- [Xcode 16.3 Release Notes](xcode-16_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 16.2 Release Notes](xcode-16_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 16.1 Release Notes](xcode-16_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 16 Release Notes](xcode-16-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-16_4-release-notes)*