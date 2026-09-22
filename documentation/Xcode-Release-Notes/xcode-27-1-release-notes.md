# Xcode 27.1 Beta Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 27.1 beta includes Swift 6.4 and SDKs for iOS 27.1, iPadOS 27, tvOS 27, watchOS 27, macOS 27, and visionOS 27. Xcode 27.1 beta supports on-device debugging in iOS 17 and later, tvOS 17 and later, watchOS 10 and later, and visionOS. Xcode 27.1 beta requires a Mac running macOS Tahoe 26.6 or later.

See [`Xcode Support`](https://developer.apple.comhttps://developer.apple.com/support/xcode/) to learn more about compatible platforms and deployment targets.

##### Mac Catalyst

###### Known Issues

- Projects that use APIs specific to iOS 27.1 show compile errors when building for Mac Catalyst (“undeclared identifier”, “not found”, “has no member”, “cannot find”, etc). (185924957) **Workaround:** Use build-time conditionals like `#if !targetEnvironment(macCatalyst)` (Swift) or `#if !TARGET_OS_MACCATALYST` (ObjC) to isolate affected code.
- Projects that target iOS 27.1 show no Mac Catalyst run destination available. (187046347) **Workaround:** Add a Mac Catalyst 27.0 minimum deployment in target settings.

##### Previews

###### New Features

- The canvas overrides picker now includes a Display group for previewing content on a device’s alternative display. (182598534)

##### Simulator

###### Known Issues

- Initial Simulator launch can take several minutes. (187708500)
- StandBy is unavailable in the iPhone Duo Simulator runtime. (187708663)
- Running and debugging most app extensions is unavailable in the iPhone Duo Simulator runtime. (187708767)

## See Also

- [Xcode 27.2 Beta Release Notes](xcode-27_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 27 Release Notes](xcode-27-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-27_1-release-notes)*