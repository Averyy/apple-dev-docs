# Xcode 12.5.1 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

#### Overview

Xcode 12.5.1 includes SDKs for iOS 14.5, iPadOS 14.5, tvOS 14.5, watchOS 7.4, and macOS Big Sur 11.3. The Xcode 12.5.1 release supports on-device debugging for iOS 9 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 12.5.1 requires a Mac running macOS Big Sur 11 or later.

##### Debugging

###### Resolved Issues

- Improved the performance of the Variables View in very large projects. (75381959, 78035413)

##### Signing and Distribution

###### Resolved Issues

- Resolved an issue in which Xcode failed to `codesign` using a smart card. (78035219)

##### Source Control

###### Known Issues

- When you select Upload Key after you clone a repository from a source control provider and associate a locally-generated key with that repository, Xcode doesn’t upload the key. (78824500) : Add the key using the source control provider’s website.

##### Swift Packages

###### Resolved Issues

- Fixed an issue where `swift build` exited silently when building a program with package dependencies and a large compiler crash output. (77558631)
- Fixed an issue where command-line builds of packages sometimes didn’t print a “Build complete!” message. (77669218)

###### Known Issues

- Authentication may fail when using Xcode Server with Swift Packages. (77331504) : Add `-scmProvider xcode` to the `xcodebuild` arguments in the bot’s configuration.

##### Testing

###### Resolved Issues

- Fixed an issue which caused XCTest UI Recording to not emit automation code in iOS, tvOS, or watchOS. (77511696) (FB9096691)

###### Known Issues

- UI interruption monitors don’t work in watchOS. (59571331)
- UI Test Recording fails to generate code for iOS Simulator targets if recording starts after code execution stops at a breakpoint. (77924295) : With no breakpoint set, place your cursor within a test method and press the record button.

## See Also

- [Xcode 12.5 Release Notes](xcode-12_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.4 Release Notes](xcode-12_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.3 Release Notes](xcode-12_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.2 Release Notes](xcode-12_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.1 Release Notes](xcode-12_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.0.1 Release Notes](xcode-12_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12 Release Notes](xcode-12-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-12_5_1-release-notes)*