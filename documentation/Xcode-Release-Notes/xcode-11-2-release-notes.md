# Xcode 11.2 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 11.2 includes SDKs for iOS 13.2, macOS Catalina 10.15, watchOS 6.1, and tvOS 13.2. Xcode 11.2 supports on-device debugging for iOS 8 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 11.2 requires a Mac running macOS Mojave 10.14.4 or later.

> ❗ **Important**: Storyboards containing a [`UITextView`](https://developer.apple.com/documentation/UIKit/UITextView) will cause the app to crash on operating system versions earlier than iOS 13.2 and tvOS 13.2 if compiled with Xcode 11.2. (56808566)

> ❗ **Important**: Storyboards containing a [`UITextView`](https://developer.apple.com/documentation/UIKit/UITextView) will cause the app to crash on macOS versions earlier than macOS 10.15.1 if compiled on a Mac running macOS 10.15.1. (56873523)

##### Devices

###### Resolved Issues

- Errors during iOS app installation are now surfaced as installation failures rather than reporting that “Install claimed to have succeeded, but the application could not be found.” (54367725)

##### Interface Builder

###### New Features

- Added support for configuring [`WKInterfaceAuthorizationAppleIDButton`](https://developer.apple.com/documentation/WatchKit/WKInterfaceAuthorizationAppleIDButton) styles. (53251536)

###### Known Issues

- Setting the Selected Segment Tint Color of a segmented control in Interface Builder to a named color will cause a failure when the view is loaded on iOS 12 and earlier. (55254963) : Set the segmented control’s [`selectedSegmentTintColor`](https://developer.apple.com/documentation/UIKit/UISegmentedControl/selectedSegmentTintColor) in an [`awakeFromNib()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/awakeFromNib()) method.

###### Resolved Issues

- Fixed an issue with [`UITabBarController`](https://developer.apple.com/documentation/UIKit/UITabBarController) where decoding an instance from a storyboard would create extra views at the left end of the screen. If you worked around this issue on Xcode 11.0 or 11.1 by creating a subclass of [`UITabBarController`](https://developer.apple.com/documentation/UIKit/UITabBarController) and hiding extra views in the initializer you can remove the workaround. (55310448)
- Fixed a crash that occurred in iOS/tvOS projects when reselecting the currently selected color in a user-defined runtime attribute. (55464140)
- The host system’s appearance no longer affects which fallback color is archived for an adaptive asset catalog color. (55570108)

##### Localization

###### Resolved Issues

- Fixed a crash when importing a localization with `xcodebuild` into a project referencing a Swift package. (55636751)

##### Previews

###### Resolved Issues

- Xcode Previews now support using static variables in inner structs. (45235180)
- Xcode Previews now correctly resolve build settings that are relative to your project’s `SRCROOT`. (51569011)
- Fixed a crash in Xcode Previews when rendering macOS views that had a zero width or height. (51952905)
- Xcode Previews now passes `BUILT_PRODUCTS_DIR` correctly as a `DYLD_FRAMEWORK_PATH` when rendering previews to allow you to reference and resolve built frameworks and other products. (53967108)
- Functions tagged with `@ViewBuilder` now preview correctly in Xcode Previews. (54433866)
- Xcode Previews now correctly support structs, functions, and other types marked with `@available`. (54568910)
- Fixed an issue where some SwiftUI tutorials failed to build or preview with Xcode Previews. (54732993)
- Fixed a crash in the SwiftUI inspectors when inspecting some [`Color`](https://developer.apple.com/documentation/SwiftUI/Color) types. (55129285)

##### Simulator

###### New Features

- simctl video recording now produces smaller video files, supports HEIC compression, and takes advantage of hardware encoding support where available. In addition, the ability to record video on iOS 13, tvOS 13, and watchOS 6 devices has been restored. (50625716, 54409532, 55207068). > **Note**: The flags and arguments supported by simctl video recording have changed. See `xcrun simctl help io` for more information.
- Simulator now has a menu item and keyboard shortcut to bring up the app switcher in iOS simulators. (54793361)
- In [`AVAssetExportSession`](https://developer.apple.com/documentation/AVFoundation/AVAssetExportSession), the [`allExportPresets()`](https://developer.apple.com/documentation/AVFoundation/AVAssetExportSession/allExportPresets()) type method now returns presets in iPhone 11, iPhone 11 Pro, and iPhone 11 Pro Max simulators. (55659811)
- `xcrun simctl list --json` now includes more information about devices and runtimes, including the device type used by each device. (55671833)

###### Known Issues

- Third party “endpoint security” software may cause slow simulators, system freezes, or prevent debug processes from running in simulators reliably. This sometimes manifests as `debugserver` disconnections or simulator applications receiving a `SIGKILL` signal. (55853555) : Uninstall the third party software.

###### Resolved Issues

- Fixed a crash loop that could occur on macOS 10.15 Catalina when using iCloud Drive in simulated devices running older versions of iOS. (51392951, 54282967, 54818084)
- Fixed an issue causing simulated devices running iOS 13 to display a black window instead of enabling an external display or a CarPlay display. (53966664)
- Resolved an issue that prevented apps from installing on iOS 8.4 simulators. (55646411) > **Note**: iOS 8.4 and 9.x simulators are only supported when running on macOS 10.14 Mojave.
- Simulators no longer shut down when a process inside the simulator misuses Metal APIs or attempts to execute an invalid shader. (55725833)

##### Swift

###### Known Issues

- If a module is built with `BUILD_LIBRARIES_FOR_DISTRIBUTION` and contains a public type with the same name as the module itself, clients will fail to import the module. (19481048) (FB5863238) : Rename either the type or the module to remove the conflict.

##### Swift Compiler

###### New Features

- Swift function builders use a new type checking algorithm that improves compile times and eliminates many instances of “unable to type-check this expression in reasonable time” errors for SwiftUI-heavy code. (50150793)

###### Resolved Issues

- The enum `NEHotspotConfigurationError` in the [`Network Extension`](https://developer.apple.com/documentation/NetworkExtension) framework changed back to `NS_ENUM` (from `NS_ERROR_ENUM`), as it was before Xcode 11.0. (54134493)
- Fixed a runtime crash that would occur when running watch apps statically linked with Swift libraries. (55082864)

##### Swift Packages

###### Known Issues

- If an iOS, tvOS, or watchOS app uses a Swift Package that builds a dynamic library, it cannot be submitted to the App Store. (55564324) : Modify the Package manifest to build a static library.

###### Resolved Issues

- The scheme autogenerated for a Swift package will be automatically updated when the package adds or removes targets. (50586754, 54777895)

##### Swiftui

###### Resolved Issues

- All downloadable project files from the SwiftUI tutorials inside Xcode’s documentation viewer now download. (55575465)

##### Watchos

###### Known Issues

- Launching the watch App on an iOS simulator will cause `NTKFaceSnapshotServices` to continuously crash in the background. The watch app should function as normal. (56349123) : To stop crashes, quit the simulator or erase content and settings.

###### Resolved Issues

- watchOS applications may be built with the watchOS 6 SDK and a deployment target of watchOS 5.3. (55360395)

## See Also

- [Xcode 11.7 Release Notes](xcode-11_7-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.6 Release Notes](xcode-11_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.5 Release Notes](xcode-11_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.4.1 Release Notes](xcode-11_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.4 Release Notes](xcode-11_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.3.1 Release Notes](xcode-11_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes
- [Xcode 11.3 Release Notes](xcode-11_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes
- [Xcode 11.2.1 Release Notes](xcode-11_2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11.1 Release Notes](xcode-11_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 11 Release Notes](xcode-11-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-11_2-release-notes)*