# Xcode 11.4.1 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 11.4.1 includes SDKs for iOS 13.4, iPadOS 13.4, tvOS 13.4, watchOS 6.2, and macOS Catalina 10.15.4. The Xcode 11.4.1 release supports on-device debugging for iOS 8 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 11.4.1 requires a Mac running macOS Catalina 10.15.2 or later.

##### Apple Clang Compiler

###### Resolved Issues

- Fixed a crash that could occur when compiling with `-fstack-check` and `-fomit-frame-pointer` on x86_64, if the stack was not 16-byte aligned before the call to the stack check function `__darwin_chkstk`. (61028954) (FB7644341)

##### Asset Catalog

###### Known Issues

- iOS apps with asset catalogs built with Xcode 11.4 may experience slower image loading performance in Dark Mode when deployed to devices running iOS 13.3 or earlier. (61200701) (FB7648891) : Add a symbol glyph to the app’s asset catalog.

##### Instruments

###### Resolved Issues

- Fixed an issue where Instruments wouldn’t record [`os_log`](https://developer.apple.com/documentation/os/os_log) and `os_signpost` data when targeting Simulator devices. (60883664) (FB7639664)

##### Interface Builder

- Fixed an issue that caused some [`UINavigationBar`](https://developer.apple.com/documentation/UIKit/UINavigationBar) appearance properties set in storyboard and XIB documents to be ignored when building with Xcode 11.4. (60883063) (FB7639654)

##### Linking

###### Resolved Issues

- The linker no longer sanitizes `-segprot` permissions and allows programs to be built with different `init` and `max` segment permissions. Note that future OS releases may not support non-standard segment permissions. (61137066)

##### Previews

###### Resolved Issues

- Fixed an issue that could cause previews to fail for applications built with Mac Catalyst or sandboxed macOS applications when Xcode is not in the `/Applications` folder. (57096274, 61216983)

##### Signing and Distribution

###### Known Issues

- Automatic signing may fail to make changes to app IDs that use a seed prefix and not a team ID prefix. (59672760) (FB7593038) : Adjust your app ID manually on the [`Apple Developer`](https://developer.apple.comhttps://developer.apple.com/account) website, then return to Xcode to generate a provisioning profile.

###### Resolved Issues

- Resolved a crash in the distribution workflow caused by a failure to detect the platform of an archived binary. (61228514)

##### Simulator

###### Resolved Issues

- Simulator pointer capture mode now handles the original Apple Magic Mouse. (59437811, 61227692)
- Fixed an issue where large binaries could cause watchdog timeouts or failures to launch in the simulator. (61013375)

##### Siri Intents

###### Resolved Issues

- Fixed an issue that prevented generation of source files from intent definition files when using the Legacy Build System. (60591035, 61227177)

##### Swift

###### Resolved Issues

- Fixed a crash that could occur in Swift code that imported an Objective-C class defined with the `objc_runtime_name` attribute. (60888835)

##### Swift Packages

###### Resolved Issues

- Fixed an issue where an error like “Swift package product A is linked as a static library by B and C. This will result in duplication of library code.” was incorrectly emitted if an app and an embedded app extension or helper tool statically linked the same package product. If you previously set the `DISABLE_DIAMOND_PROBLEM_DIAGNOSTIC` build setting to work around this issue, you can delete this setting now. (59310009, 61227255)

##### Testing

###### Resolved Issues

- Fixed a bug which could cause test runners to crash when resuming from a breakpoint fired on a background thread while the main thread is suspended by a waiter. (61228606)

## See Also

- [Xcode 11.7 Release Notes](xcode-11_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.6 Release Notes](xcode-11_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.5 Release Notes](xcode-11_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.4 Release Notes](xcode-11_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.3.1 Release Notes](xcode-11_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes
- [Xcode 11.3 Release Notes](xcode-11_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes
- [Xcode 11.2.1 Release Notes](xcode-11_2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.2 Release Notes](xcode-11_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.1 Release Notes](xcode-11_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11 Release Notes](xcode-11-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-11_4_1-release-notes)*