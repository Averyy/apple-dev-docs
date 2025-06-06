# Xcode 13.2 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

#### Overview

Xcode 13.2 includes SDKs for iOS 15.2, iPadOS 15.2, tvOS 15.2, watchOS 8.3, and macOS Monterey 12.1. The Xcode 13.2 release supports on-device debugging for iOS 9 and later, tvOS 9 and later, and watchOS 2 and later. Xcode 13.2 requires a Mac running macOS 11.3 Big Sur or later.

##### General

###### Known Issues

- If you’re using Swift packages either standalone or as dependencies in an Xcode project or workspace, the Mac App Store version of Xcode fails during package resolution with the error “Internal error: missingPackageDescriptionModule.” (86435800) : Download Xcode 13.2 directly from the [`Apple Developer website`](https://developer.apple.comhttps://developer.apple.com/download/all/?q=Xcode%2013.2).

###### New Features

- Xcode 13.2 includes support for app projects you create with Swift Playgrounds 4. (84436977)

##### Apple Clang Compiler

###### Known Issues

- Apps built with Xcode 13 or Xcode 13.1 that make use of Swift Concurrency features (such as `async`/`await`), deploy to iOS prior to 15, tvOS prior to 15, or watchOS prior to 8, and have bitcode enabled may crash at launch with an error reporting that the `libswift_Concurrency.dylib` library was not loaded. (86349088) : Add `-Wl,-weak-lswift_Concurrency -Wl,-rpath,/usr/lib/swift` to Other Linker Flags in the app’s build settings.

##### Build System

###### New Features

- The build system and Swift compiler have a new mode that better utilizes available cores, resulting in faster builds for Swift projects. The mode is opt-in, and you can enable it globally with the following user default: ```shell
defaults write com.apple.dt.XCBuild EnableSwiftBuildSystemIntegration 1
``` Please report any issues with the new build system mode through Feedback Assistant. (84467780)

###### Known Issues

- Xcode SwiftUI Previews may occasionally fail with an error message about a modified `.h` file, such as “file `Header.h` has been modified since the module file `Module.pcm` was built: `mtime` changed.” (85938686) : To resolve the issue, delete the Clang module cache by running the following command in Terminal: `rm -rf "$TMPDIR/../C/clang/ModuleCache"`. Then try to preview the file again.
- If an input to a build task is missing, the build system emits an error and cancels the build; however, it still reports a successful build. (86028889)

##### Devices

###### Resolved Issues

- Resolved an issue where an iOS device could become unavailable for development when the system can’t prepare a paired watch for development. (82111305) (FB9533359)

##### Interface Builder

###### Resolved Issues

- Fixed an issue where Xcode crashed after you enabled a bar appearance in the inspector and then undid the action. (83695512)

##### Localization

###### Resolved Issues

- Fixed an issue where the compiler didn’t extract some strings when exporting for localization. (82144823) (FB9537440)

##### Metal

###### New Features

- TextureConverter 1.1 adds support for decompressing textures during build time. You can also use TextureConverter as a standalone tool to decompress textures outside the build process. Set the file path for the decompressed file with the `--decompressed` option. (82632250)
- TextureConverter 1.1 adds support for error metrics. Set the `--metrics` option to calculate at compression time, or use `--compare` to calculate the error between two texture files. (82632360)
- TextureConverter 1.1 adds support for skipping compression when the output texture is up to date. Use the `--check_date` option to compare the modified date and time of the input and output textures. Use the `--check_details` option to compare the version of TextureConverter you used for compression with the compression options you used (KTX files only). (83534773)

##### Organizer

###### New Features

- Added support for smart insights notifications. You can now receive notifications when monitoring power and performance metrics in your app. To enable notifications, click the bell icon in the top right of the Xcode Organizer’s Regressions view. (66497478)

##### Previews

###### Deprecations

- On-device previews no longer include watchOS and tvOS previews. Run the app to see your user interface. (84032315)

##### Project Navigator

###### Resolved Issues

- Xcode performance is no longer affected when source code displays several warnings and errors. (84533671)

###### Known Issues

- Xcode declares the wrong type identifier for GPX files (`com.topographix.gpx` instead of `com.topografix.gpx`). This can interrupt other applications that operate on `com.topografix.gpx` files. (86333977) (FB9804569)

##### Signing and Distribution

###### Resolved Issues

- Resolved an issue where Xcode required every component of a Mac app to have a provisioning profile when uploading to App Store Connect. (83833905) (FB9677186)

##### Simulator

###### Resolved Issues

- Resolved an issue that prevented iPhone mini simulators from launching in Virtual Machines that don’t support Metal pass-through. (83663966) (FB9663296) : This fix may increase CPU use and impact overall performance when running on some hardware or in a virtual machine. If necessary you can enable higher performance by reducing quality using the following: ```shell
defaults write com.apple.CoreSimulator FramebufferServerUseLowQualityScaling 1
``` This mode isn’t suitable for taking screenshots, recording videos, or comparing images.

###### Known Issues

- CarPlay Simulator is only supported in macOS 12 Monterey. (85324172)

##### Source Control

###### Known Issues

- Selecting “Open in Code Review” from “Show Last Change For Line” may sometimes open an editor that never loads. (78592315) : Disable and reenable Code Review mode.

##### Source Editor

###### Resolved Issues

- Fixed an issue where a project using a CocoaPods installation without a “Debug” configuration set up could have a mismatch between building and semantic functionality in the editor, leading to problems like the editor showing “live issues” that don’t exist when building. (84502615) (FB9717206)

##### Storekit

###### New Features

- StoreKit testing includes new subscription renewal rates in terms of months. If you test on operating systems earlier than macOS Monterey 12.1, iOS 15.2, tvOS 15.2, and watchOS 8.3, the operating system uses the deprecated rates in terms of days to approximate the renewal rates. (76929977)

##### Swift

###### New Features

- You can now use Swift Concurrency in applications that deploy to macOS Catalina 10.15, iOS 13, tvOS 13, and watchOS 6 or newer. This support includes `async`/`await`, actors, global actors, structured concurrency, and the task APIs. (70738378)

###### Resolved Issues

- Fixed an issue that prevented Swift libraries depending on Combine from building for targets including armv7 and i386 architectures. (82183186, 82189214)
- Fixed an issue that caused availability checks in iPhone and iPad apps running on a Mac with Apple silicon to always return `true`, which caused iOS apps running in macOS Big Sur to see iOS 15 APIs as available, resulting in crashes. These availability checks now return the correct result for apps compiled with Xcode 13.2. (83378814)
- Mac apps built with Mac Catalyst that use Swift Concurrency now launch in an operating system prior to macOS 12 Monterey. (84393581)
- watchOS apps that use Swift Concurrency and deploy prior to watchOS 8 now build for 64-bit watchOS simulator targets without link errors. (84394162)
- You can now use TestFlight to distribute apps that use Swift Concurrency and deploy to operating systems prior to iOS 15, macOS 12 Monterey, tvOS 15, and watchOS 8. (84645973)

###### Known Issues

- Applications linking to RealityKit with iOS 15 or macOS 12 Monterey SDKs fail to launch in previous operating systems. (79584511) : Add `OTHER_LD_FLAGS = -weak_framework RealityFoundation` to your Xcode project settings to allow running RealityKit apps in older operating systems.
- Apps that use Swift Concurrency and are built for operating systems prior to macOS 10.15, iOS 13, tvOS 13, or watchOS 6 fail to launch on those earlier operating systems. (86419499) (FB9807625)

##### Swift Packages

###### Resolved Issues

- Fixed an issue where Template assistant didn’t offer file customization options when you created a new file in a Swift Package. (65109424) (FB7854693)
- Resolved an issue where Swift packages with binary targets sometimes failed with a “no such module” error when attempting to import the module of a binary target. (77465707)

##### Templates

###### Resolved Issues

- The SwiftUI Core Data templates now set `automaticallyMergesChangesFromParent` to `true` on their view context, so changes are visible in the view context as they occur, including when you use Core Data with CloudKit. (73022349) (FB8967865)

##### Testing

###### New Features

- Xcode can now provide code coverage information when running tests for a Swift package on a Mac with Apple silicon. (71769076) (FB8919898)

###### Resolved Issues

- Resolved an issue where XCTest incorrectly reported the frame property of `XCUIElement` in some cases, particularly when the element was part of another process such as an App Extension. (41007601) (FB5354471)
- Xcode can now run XCTest test methods marked `async` in macOS Catalina 10.15, iOS 13, tvOS 13, and watchOS 6 or newer. (80039766)

##### Xcode Cloud

###### Known Issues

- When onboarding new products to Xcode Cloud, Xcode doesn’t include a Start Condition, causing the onboarding to fail. (84641030) : During onboarding, manually add a Start Condition to the default workflow.

## See Also

- [Xcode 13.4.1 Release Notes](xcode-13_4_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.4 Release Notes](xcode-13_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.3.1 Release Notes](xcode-13_3_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.3 Release Notes](xcode-13_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.2.1 Release Notes](xcode-13_2_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13.1 Release Notes](xcode-13_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 13 Release Notes](xcode-13-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-13_2-release-notes)*