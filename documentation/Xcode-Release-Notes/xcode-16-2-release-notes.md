# Xcode 16.2 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 16.2 includes SDKs for iOS 18.2, iPadOS 18.2, tvOS 18.2, watchOS 11.2, macOS Sequoia 15.2, and visionOS 2.2. The Xcode 16.2 release supports on-device debugging in iOS 15 and later, tvOS 15 and later, watchOS 7 and later, and visionOS. Xcode 16.2 requires a Mac running macOS Sonoma 14.5 or later.

##### Downloadable Hardware Support

###### New Features

- Starting with Xcode 16.2, Xcode can add support for new hardware without needing to update the entire Xcode app.  Xcode will check when launching the app if a hardware support update is available and will install it.  For the equivalent from the command-line, run `xcodebuild -runFirstLaunch -checkForNewerComponents`. When there is hardware support available, the installer package will be stored in `~/Library/Developer/Packages`, and can be copied for installation and setup purposes for other machines.  (138789379)

###### Known Issues

- Xcode 16.2 with iPhone 16e, iPad Air (M3), and iPad (A16) Device Support is unable to thin for these device during ad-hoc distribution.  (136340970)
- When using Xcode 16.2 with iPhone 16e, iPad Air (M3), and iPad (A16) Device Support, these new devices are not available in the device selector.  (138526898)  Use iPhone 14 as an alternative to iPhone 16e.  Use iPad Air (M2) as an alternative to iPad Air (M3).
- When creating an asset for iPhone 16e using Xcode 16.2 and iPhone 16e Device Support, the warning “Warning: Could not get trait set for device iPhone17,5 with version 18.3” will be displayed although it will still work.  When deploying large asset catalogs for iPhone 16e, it may take longer.  (139181651)
- In order to use iPhone 16e in the simulator with Xcode 16.2, download both the iPhone 16e Device Support and the iOS 18.3 Simulator Runtime from Xcode > Settings > Components.  iPhone 16e is not currently compatible with iOS 18.4 beta.  (143996070)
- In order to use iPad Air (M3) or iPad (A16) in the simulator with Xcode 16.2, download both the iPhone 16e, iPad Air (M3), and iPad (A16) Device Support and the iOS 18.3.1 Simulator Runtime from Xcode > Settings > Components.  iPad Air (M3) and iPad (A16) are not currently compatible with iOS 18.4 beta 2.  (143996162)

##### General

###### New Features

- The Command Line Tools package now supports using the `swift test` command to build and run package tests written with Swift Testing.  (136424541)

###### Known Issues

- Sometimes running parallel Tests on macOS run destinations never finishes.  (138772707)

##### Localization

###### Resolved Issues

- Fixed crashes and other anomalies that could occur in the String Catalog editor when multiple editor tabs are open to the same file with different sort or filter criteria. (FB14665353)  (136257968)

##### Predictive Code Completion

###### Resolved Issues

- Fixed: Improved predictive completions that start with type names and initializer calls. Please note, this improvement requires macOS 15.1 or later.  (128085056)
- Fixed: Improved predictive completions when steered by an `override` completion.  (129624498)
- Fixed an issue where predictions starting with certain Swift keywords, like `func` and `struct`, might be expanded to words like “function” and “structure”.   (134784783)
- Fixed: Predictive Code Completion more consistently calls functions with the correct parameters and ordering.  (138219794)
- Fixed: Improved predictive completion accuracy in situations where a property name is being predicted or fed to the model by the selection in the code completion window.  (138437280)
- Fixed an issue where a predictive completion never loads.  (138784998)

##### Previews

###### Resolved Issues

- Fixed: Previews should now work fine without permissions errors if you place derived data in protected locations like Downloads, Desktop, or Documents.  (129866404)
- Fixed: Projects that built object files as universal could sometimes fail to preview.  (133653290)
- Fixed: Targets using `internal import SwiftUI` would fail to preview.  (136173813)
- Fixed: Previews could fail to find bundled resources for some targets that produced very large binaries.  (136292512) (FB15176682)
- Fixed: Previews could have crashed with unknown selector errors if `-ObjC` or `-all_load` were passed as linker flags for the previewed module.  (136970660)
- Fixed: Processing crash reports for user code could sometimes cause PreviewShell to crash instead if an address was interpreted as a negative number.  (137644422)
- Fixed: In Xcode 16.0, unoptimized debug builds implicitly wrap usages of SwiftUI `some View` types (such as the return type from `body`) in `AnyView`. This is done to allow SwiftUI Previews to dynamically replace the implementation of methods like `body` without building separate copies of the entire project. While functionally equivalent, using `AnyView` in some cases can lead to slower SwiftUI performance when a view returning `some View` from its `body` is used as a direct child of a lazy container. This can be worked around by wrapping those views in an `HStack` or `VStack` , for example: ```None
 List {
     ForEach(…) {
         HStack {
             MyRowView()
         }
     }
 }
``` Alternatively, there is a new build setting `SWIFT_ENABLE_OPAQUE_TYPE_ERASURE` that controls the implicit wrapping of views in `AnyView`. To get fast SwiftUI previews, the setting defaults to `YES`, but can be set to `NO` if you want to experiment with how this affects debug-time performance in specific targets in your project. This will have no effect on release builds, which is where performance should be accurately evaluated. Xcode 16.2 adds experimental support for disabling the build setting while retaining preview usage, though preview performance will degrade significantly.  (138952991)

###### Known Issues

- macOS projects that use hardened runtime but no sandboxing may run into timeout errors when attempting to preview if the project is complex enough.   (139070284)  Enable sandboxing or disable hardened runtime while developing.

##### Simulator

###### Resolved Issues

- CoreSimulator now supports a mode in which the developer has full control over devices in the default device set.  The system won’t create default devices nor manage pairing relationships between watches and phones in that set when placed into this mode.  To do this, please set the following preference: ```None
 defaults write com.apple.CoreSimulator EnableDefaultSetCreation -bool NO
``` (139023701)
- Fixed: CoreSimulatorService may increase in memory usage over time, with usage of simulator processes.  (140213488)

###### Known Issues

- On systems that do not have Internet access, Xcode cannot reach the index for SDK to Simulator runtime mapping information. This will cause Xcode to list current simulators as ‘Other Installed Platforms’ and consider the current platform as missing.  (135367176)  To download a copy of the latest index run: ```None
 curl -O https://devimages-cdn.apple.com/downloads/xcode/simulators/index2.dvtdownloadableindex
``` Then copy the index to the offline system and run the following command to set the index: ```None
 defaults write com.apple.dt.Xcode DVTDownloadableIndex <path/to/the/copied/index2.dvtdownloadableindex>
``` Remember to repeat this workaround when upgrading to newer simulator runtimes, or newer Xcode, on systems without Internet access.
- Simulator process launch may stall for around 3-5 minutes per runtime as GateKeeper scans the simulator dyld shared cache. GateKeeper will need to scan the simulator dyld shared cache whenever: - The simulator dyld shared cache is rebuilt.
- An Xprotect update is installed (~weekly). The simulator dyld shared cache will need to be rebuilt whenver: - macOS is updated.
- A new or updated simulator runtime is installed.  (138219140)  You will need to wait for scananing to complete, which is easiest to do by monitoring CPU activity of the syspolicyd process on the system.  There is currently no visual indication of this progress.

##### Swift

###### Resolved Issues

- Fixed: Apps using Swift/C++ interoperability may not be back deployable to operating systems earlier than iOS 16, watchOS 9, and tvOS 16.  (140823785)

###### Known Issues

- Memory leaks can occur when calling async functions bridged from Objective-C and building in the Swift 6 language mode.  (134442168)  Pass `-checked-async-objc-bridging=off` to the Swift compiler using “Other Swift Flags” in Xcode build settings.
- Xcode targets using Swift/C++ interoperability and having a deployment target of less than iOS 16 or tvOS 16 may not build for iOS or tvOS simulators.  (141232269)

##### Swift Package Manager

###### Resolved Issues

- Fixed an issue where lldb couldn’t attach to the Swift Testing host binary.  (136630386)

## See Also

- [Xcode 16.4 Release Notes](xcode-16_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 16.3 Release Notes](xcode-16_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 16.1 Release Notes](xcode-16_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 16 Release Notes](xcode-16-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-16_2-release-notes)*