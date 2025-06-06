# Xcode 12.3 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 12.3 includes SDKs for iOS 14.3, iPadOS 14.3, tvOS 14.3, watchOS 7.2, and macOS Big Sur 11.1. The Xcode 12.3 release supports on-device debugging for iOS 9 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 12.3 requires a Mac running macOS 10.15.4 or later.

##### General

###### Resolved Issues

- Improved responsiveness of macOS mouse and keyboard events while under heavy load, such as when building a large project while running Simulator. (71819679)

###### Known Issues

- The first time you launch Xcode on a Mac with Apple silicon without Rosetta installed, Xcode prompts you to install Rosetta. The prompt prevents any interaction, and blocks Xcode from launching. (70853975) (FB8848625) : Launch an x86_64 process to trigger the system’s Rosetta prompt.

##### Build System

###### Resolved Issues

- Fixed an issue where `xcodebuild` sometimes logged unexpected output about failed event streams. (33401512)

##### Devices

###### Resolved Issues

- Fixed an issue that caused Xcode to spontaneously lose device configuration information for an Apple Watch. This data loss caused Xcode to either crash or display an error stating that your app “cannot be installed on (null)”. (54768855)
- Fixed an issue where Xcode could fail to prepare a wirelessly connected iOS device for debugging with the error “Failed _shouldMakeReadyForDevelopment check”. (61227501) (FB7649607)
- Fixed an issue that blocked simulator runtimes from being available when running command-line tools like `simctl` or `xcodebuild` from a non-root LaunchDaemon, or when launching as a different user from the current user (for example, with `sudo` or `launchctl`). (62188195, 69738053)
- Fixed an issue that could cause Xcode to get interrupted when copying symbols from iOS devices, and never finish preparing iOS devices for debugging. The failure mainly occurred on Xcode installations used to debug multiple iOS devices which are running the same version of iOS. This bug impacted the performance of launching executables on iOS devices and attaching the debugger to them. (68221778) (FB8611135)

##### Documentation Viewer

###### Resolved Issues

- Fixed a crash that could happen when opening the Documentation Window if you installed Xcode outside of `/Applications`. (70631583)

##### Interface Builder

###### Resolved Issues

- Fixed iOS storyboard rendering issues when using [`UISplitViewController`](https://developer.apple.com/documentation/UIKit/UISplitViewController) simulated metric sizes with [`UITabBarController`](https://developer.apple.com/documentation/UIKit/UITabBarController). (69054879) (FB8704013)
- Fixed an issue that caused Xcode to warn about multiple deprecated system color references in saved documents. (69667149) (FB8749086)
- Fixed an issue where the background color of a [`UITextField`](https://developer.apple.com/documentation/UIKit/UITextField) could appear transparent in your app instead of the default color. (70559650)

##### Scenekit

###### Known Issues

- On a Mac with Apple silicon, SceneKit editor may display pixelated graphics or an empty window. (71239899, 71395291, 72141599) : Click on the Display option icon at the bottom-right of the 3D viewport, then disable the Outline selection and Grid options.

##### Simulator

###### New Features

- `simctl` now prints “Recording started” to `stderr` when it has enqueued the first frame of a video recording. Scripts or other automation can wait for that message before proceeding, to ensure the first part of the operation is captured in the resulting video. (57915463)

###### Resolved Issues

- `simctl` video recordings no longer cut off the end of the video when no screen updates are happening. The recording timeline now holds the last frame and extends until you terminate the recording with Control-C (SIGINT). (67952344) (FB8565355)
- CoreSimulator now excludes its caches directory from Time Machine backups by default. (68782191)

###### Known Issues

- When using macOS Big Sur 11.0 or 11.0.1 on your Mac, you can’t run a simulated device with watchOS 6, and you can’t run apps with 32-bit code in simulated devices running watchOS 7. This issue is fixed in macOS Big Sur 11.1. (69093569)
- Siri may not respond in a simulated device running on a Mac with Apple silicon. (71604992)
- Apps may not detect all game controller events when running in simulated devices on Macs with Apple silicon. (71651414)

##### Swift

###### Resolved Issues

- Fixed a failure that could occur when compiling a project with Mac Catalyst that imports [`OSLog`](https://developer.apple.com/documentation/OSLog) from Swift. (68597591)

## See Also

- [Xcode 12.5.1 Release Notes](xcode-12_5_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.5 Release Notes](xcode-12_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 12.4 Release Notes](xcode-12_4-release-notes.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-12_3-release-notes)*