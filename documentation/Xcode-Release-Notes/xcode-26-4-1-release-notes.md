# Xcode 26.4.1 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 26.4.1 includes Swift 6.3 and SDKs for iOS 26.4, iPadOS 26.4, tvOS 26.4, macOS 26.4, and visionOS 26.4. Xcode 26.4.1 supports on-device debugging in iOS 15 and later, tvOS 15 and later, watchOS 8 and later, and visionOS. Xcode 26.4.1 requires a Mac running macOS Tahoe 26.2 or later.

##### Metrickit

###### Resolved Issues

- Fixed crash for MetricKit apps built with Xcode 26.4 due to missing symbols when running on iOS, macOS, and visionOS versions below 26.4. Please rebuild your app with the updated Xcode to resolve the issue.  (173827073) (FB22384135)

##### Swift Compiler

###### Resolved Issues

- Fixed stack-allocation bugs in async functions that caused “freed pointer was not the last allocation” crashes, particularly in `swift_asyncLet_finish`. These long-standing issues became more frequent in Swift 6.2 and 6.3 due to optimizer improvements.  (173974857)

## See Also

- [Xcode 26.5 Beta 2 Release Notes](xcode-26_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.4 Release Notes](xcode-26_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.3 Release Notes](xcode-26_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.2 Release Notes](xcode-26_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.1.1 Release Notes](xcode-26_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26.0.1 Release Notes](xcode-26_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 26 Release Notes](xcode-26-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-26_4_1-release-notes)*