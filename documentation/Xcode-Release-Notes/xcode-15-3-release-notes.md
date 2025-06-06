# Xcode 15.3 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 15.3 includes SDKs for iOS 17.4, iPadOS 17.4, tvOS 17.4, watchOS 10.4, macOS Sonoma 14.4, and visionOS 1.1. The Xcode 15.3 release supports on-device debugging in iOS 12 and later, tvOS 12 and later, watchOS 4 and later, and visionOS. Xcode 15.3 requires a Mac running macOS Sonoma 14 or later.

##### General

###### Resolved Issues

- Fixed: Xcode is now deterministic about the order in which string comments are concatenated when updating String Catalogs.   (119389516)

###### Known Issues

- Some Macs recently received a macOS system update which disabled the simulator runtimes used by Xcode, including the simulators for iOS, tvOS, watchOS, and visionOS. If your Mac received this update, you will receive the following error message and will be unable to use the simulator: ```None
 The com.apple.CoreSimulator.SimRuntime.iOS-17-2 simulator runtime is not available.
 Domain: com.apple.CoreSimulator.SimError
 Code: 401
 Failure Reason: runtime profile not found using "System" match policy
 Recovery Suggestion: Download the com.apple.CoreSimulator.SimRuntime.iOS-17-2 simulator runtime from the Xcode 
``` (127498625)  To resume using the simulator, please reboot your Mac.  After rebooting, check Xcode Preferences → Platforms to ensure that the simulator runtime you would like to use is still installed.  If it is missing, use the Get button to download it again.

##### App Intents

###### Known Issues

- AppIntents may fail to execute when the target’s minimum deployment target is iOS 15.0 or earlier  (123798206) (FB13664020)  Add the ENABLE_APPINTENTS_DEPLOYMENT_AWARE_PROCESSING=NO build flag to your target(s)

##### Apple Clang Compiler

###### New Features

- You can now use API Notes to add attributes to C++ APIs declared in a C++ namespace.  (113403829)
- The compiler now correctly applies API Notes attributes to globals declared in `extern "C++"` blocks.  (114382260)

##### Build System

###### New Features

- Schemes provide a new “Override Architectures” build option, which controls the set of architectures that will be built for all targets in the workspace, including Swift packages. The recommended option (and default for new schemes) is “Match Run Destination”. Full details are available by clicking the information icon next to the “Override Architectures” setting on the scheme build options sheet in Xcode.  (66146584)

###### Resolved Issues

- Fixed: The scheme name is no longer included in the derived data intermediates path when performing archive builds or other builds where the `DEPLOYMENT_LOCATION` build setting is set to `YES`. This may necessitate changes to custom build scripts.  (100990646)
- Fixed a bug where when a mergeable library in a framework inside an XCFramework is merged into a larger binary, the library sometimes would not be removed from the framework when the framework is embedded in the product.  (114836725) (FB13100730)
- Fixed a bug where in a workspace with multiple projects, if a target is configured to merge the binaries of its immediate dependencies into its binary, it would not see that those dependencies were built as mergeable if they were in different projects from itself.  (115400802) (FB13160508)
- Fixed a bug where creating an xcframework from a framework or library located at a path containing a symlink (such as /var which is a symlink to /private/var) would fail.  (115786062) (FB13191683)

##### C++ Standard Library

###### New Features

- The following new features have been implemented: - P0645 - Text formatting (`std::format`)
- P2286R8 - Formatting ranges
- P1206R7 - `ranges::to`: A function to convert any range to a container
- P2520R0 - `move_iterator<T*>` should be a random access iterator
- P1328R1 - `constexpr type_info::operator==()`
- P2693R1 - Formatting `thread::id`
- P2505R5 - Monadic operations for `std::expected`
- P2711R1 - Making multi-param constructors of views `explicit`
- P2136R3 - `std::invoke_r`
- P2494R2 - Relaxing range adaptors to allow for move only types
- P2585R0 - Improving default container formatting
- P0408R7 - Efficient access to `basic_stringbuf`’s buffer
- P2474R2 - `std::ranges::views::repeat`
- P0009R18 - `std::mdspan`
- P2093R14 - Formatted output (`std::ostream` overload is not implemented yet)
- Algorithms like `std::equal`, `std::ranges::equal`, `std::find`, and `std::ranges::find` are now lowered to `std::memcmp` in some cases, which can lead to massive performance improvements (up to 40x)
- The performance of `dynamic_cast` on its hot path was greatly improved
- The performance of `std::sort` and `std::ranges::sort` was improved by up to 50% for arithmetic types  (120908845)

###### Deprecations

- The following items have been deprecated or removed: - The `<experimental/coroutine>` header has been removed. Please use `<coroutine>` instead.
- The `<experimental/algorithm>` and `<experimental/functional>` headers have been removed, since all the contents have been implemented in namespace `std`.
- Several incidental transitive includes have been removed from libc++. If you get diagnostics for missing declarations after updating, please ensure that you have the appropriate includes in your source files.
- The global variables `std::allocator_arg`, `std::defer_lock`, `std::try_to_lock`, `std::adopt_lock`, and `std::piecewise_construct` have been removed in C++03 mode. They were previously provided as an extension, however that made it impossible to implement them correctly (as inline variables) in C++17 mode, which led to bugs. We decided to remove the niche extension and fix the C++17 bugs instead.
- The `std::strstreambuf`, `std::istrstream`, `std::ostrstream`, and `std::strstream` classes have been marked as deprecated, according to the C++98 Standard.  (120909028)

##### Carplay Simulator

###### New Features

- List of preset configurations for you to use as well as the ability to create a new configuration. Switching between and modifying configurations is accessible via the CarPlay Simulator menu bar item.   (114585849)
- Navigation metadata is now observable in CarPlay Simulator.  (117149888)

##### Devices

###### Resolved Issues

- Fixed: Running a WatchOS app that requires the companion iOS app to be installed will result in the error “An application bundle was not found at the provided path” when the run destination is set to a Watch via iPhone Simulator pair.  (119640671)
- Fixed: Debug sessions may unexpectedly disconnect in periods of high memory utilization on device.  (122593837)

###### Known Issues

- In certain circumstances, an app can’t read the contents of its own data container after replacing the content of the data container using Xcode or devicectl.  (116698465) (FB13253099)

##### Documentation

###### Resolved Issues

- Fixed: Objective-C documentation builds can miss pages  (115195433)

##### Instruments

###### Resolved Issues

- Fixed an issue where recording CPU Profiler on a Simulator device causes only first second of data to be presented.  (106003509)
- Fixed: `xctrace record` now requires executing user to be an admin.  (114202990)
- Fixed an issue where xctrace would crash when recording with only the ‘Time Profiler’ Instrument.  (120422536) (FB13512248)
- Fixed: Xcode 15.3 or newer should be used for building Custom Instruments packages on macOS 14.4+.  (121143107)

##### Localization

###### New Features

- After exporting localizations from the Product menu, Xcode will now reveal the exported files in Finder.  (40559853)

###### Resolved Issues

- Fixed: Newly created .strings and .stringsdict files are now marked as localized in the source language by default.   (64910037)
- Fixed an issue where Xcode could fail to export or import localizations when the path to Xcode.app contains spaces.   (109700392) (FB12199098)
- Fixed an issue where “Export Localizations” could fail for targets supporting iOS and visionOS.   (113228759)
- Fixed: Languages in the String Catalog Editor will now show a minimum of 1% translation progress if any strings are translated at all.   (118790070) (FB13410677)

##### Metal Debugger

###### Known Issues

- The Metal Debugger will not work with connected devices in Xcode versions earlier than 15.3 when Xcode 15.3 or later is installed on the same system.  (121627817)  If Xcode 15.3 or later has been installed, use Xcode 15.3 or later when requiring the Metal Debugger to work with connected devices.

##### Previews

###### New Features

- Added the ability to export a screenshot of the current preview using the main menu: Editor > Canvas > Export Preview Screenshot  (49361141)
- Crashes in an app under preview that happen after initial launch now show the crash report in the canvas.  (105087132)

###### Resolved Issues

- Fixed: Previews fail when Swift files  require more than 4096 compiler arguments  (92630764) (FB10004742)
- Fixed: Previews could fail when previewing files in a widget shared by both a watchOS app and an iOS app.  (108017929)
- Fixed: Exporting previews diagnostics could hang Xcode  (114111390)
- Fixed: Previewing two different devices could fail  (116060127)
- Fixed: Previews could fail when a file is in multiple targets where one of them is unsupported and one of them is supported  (116861569) (FB13264099)
- Fixed: The previews canvas incorrectly shows some previews as still in the middle of updating  (117094988)
- Fixed: Crash reports for previewed processes do not show up readily in some cases  (117133804)
- Fixed: Previews could fail for certain projects where the scheme contained test targets  (117681195) (FB13314466)

##### Proximity Reader

###### Known Issues

- Calling [`MobileDocumentReaderSession.requestDocument(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/proximityreader/mobiledocumentreadersession/requestdocument(_:)) or [`PaymentCardReaderSession.readPaymentCard(_:)`](https://developer.apple.comhttps://developer.apple.com/documentation/proximityreader/paymentcardreadersession/readpaymentcard(_:)-8jol5) from the iOS Simulator results in `unknown` or `readCancelled` errors being thrown.  (123651094)  Test your app on a physical iOS device or use Xcode 15.2 to debug your app on the iOS Simulator.

##### Signing Distribution

###### Resolved Issues

- Fixed: When archiving your target, if the run destination selected is not a generic device (ex. “Any iOS Device”), Xcode will attempt to archive for the appropriate generic device based on the selected run destination’s platform. There is now an option in the scheme editor “Allow Archiving for Simulator” which will enable Xcode to select the appropriate generic simulator device if a simulator is selected.  (121255551)
- Fixed: Resolved an issue where the app notarization workflow could fail to report informative errors when the development team was in a contract pending state on App Store Connect. Resolved an issue where the app notariation workflow could incorrectly report that a failed upload was successful.  (122816678)

##### Simulator

###### Known Issues

- When attempting to boot a simulator device shortly after installing its runtime or updating to a new version of macOS, Gatekeeper scanning may temporarily prevent boot.  This can appear as an “Unable to boot the Simulator” or “-308” error.  (118038020)  Wait a few minutes before trying the operation again to allow Gatekeeper to complete its scan.
- When attempting to boot a simulator device after an XProtect update is installed, Gatekeeper scanning may temporarily prevent boot.  This can appear as an “Unable to boot the Simulator” or “-308” error.  (124035288)  Wait a few minutes before trying the operation again to allow Gatekeeper to complete its scan.

##### Storekit

###### New Features

- You can enable and disable StoreKit dialogs in your app through the StoreKit Testing in Xcode configuration settings. This controls the same behavior as the StoreKitTest [`SKTestSession.disableDialogs`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession/3579480-disabledialogs) property and it is enabled by default.  (107622572)

##### Swift

###### New Features

- Under strict concurrency checking, every global or static variable must be either isolated to a global actor or be both immutable and of `Sendable` type. ```swift
   var mutableGlobal = 1
   // warning: var 'mutableGlobal' is not concurrency-safe because it is non-isolated global shared mutable state
   // (unless it is top-level code which implicitly isolates to @MainActor)
 
   final class NonsendableType {
     init() {}
   }
 
   struct S {
     static let immutableNonsendable = NonsendableType()
     // warning: static property 'immutableNonsendable' is not concurrency-safe because it is not either conforming to 'Sendable' or isolated to a global actor
   }
``` The attribute `nonisolated(unsafe)` can be used to annotate a global variable (or any form of storage) to disable static checking of data isolation, but note that without correct implementation of a synchronization mechanism to achieve data isolation, dynamic run-time analysis from exclusivity enforcement or tools such as Thread Sanitizer could still identify failures. ```swift
   nonisolated(unsafe) var global: String
``` [`SE-0412`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0412-strict-concurrency-for-global-variables.md)  (121120491)
- Default value expressions can now have the same isolation as the enclosing function or the corresponding stored property: ```swift
   @MainActor
   func requiresMainActor() -> Int { ... }
 
   class C {
     @MainActor
     var x: Int = requiresMainActor()
   }
 
   @MainActor func defaultArg(value: Int = requiresMainActor()) { ... }
``` For isolated default values of stored properties, the implicit initialization only happens in the body of an `init` with the same isolation. This closes an important data-race safety hole where global-actor-isolated default values could inadvertently run synchronously from outside the actor. [`SE-0411`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0411-isolated-default-values.md)  (121121487)

###### Resolved Issues

- Fixed an issue under strict concurrency checking with `-strict-concurrency=complete` or `-strict-concurrency=targeted` where the compiler would generate `Sendable` warnings on calls to `AsyncIteratorProtocol.next()` generated by `for await` loops inside an actor-isolated context.  (119613738)
- Fixed: Swift 5.10 closes all known holes in the static data-race safety model under complete concurrency checking. When writing code with `-strict-concurrency=complete`, all potential for data races will be diagnosed at compile time unless an explicit unsafe opt out, such as `nonisolated(unsafe)` or `@unchecked Sendable`, has been applied.  (120816587)
- Fixed: Under strict concurrency checking with `-strict-concurrency=complete`, the compiler will incorrectly apply `nonisolated` to synthesized default and memberwise initializers of global actor isolated types in some cases involving property wrappers, init accessors, or private stored properties whose initializer expressions are global actor isolated. This will result in an error message about returning from the initializer without initializing the stored property.  (121282537)

##### Swift Packages

###### Resolved Issues

- When opening a package, Xcode no longer creates separate schemes for the package’s test targets. Instead, these are added to the Test scheme action for the appropriate scheme.  (117871488)

##### Templates

###### Resolved Issues

- Fixed: The visionOS section is missing in the new File workflow (File -> New -> File).  (122595488)

##### Testing

###### New Features

- If an Objective-C or C++ exception is thrown on a background thread, including those owned by the Swift runtime, it will now be recorded as a test failure before the test process terminates.  (110073990)

###### Resolved Issues

- Fixed: XCTest now requires iOS 13.0 and tvOS 13.0.  (104632233)
- Fixed: XCTest UI Automation APIs are main-thread-bound. This is now enforced at compile-time.  (108214525)
- Fixed: `XCTContext.runActivity(named:block:)` is now annotated `@preconcurrency @MainActor` in Swift. Most callers using it from a synchronous test function will be unaffected. Callers using it from an `async` test function will need to `await` it or mark their test function `@MainActor`.  (110664415)
- Fixed: Starting in this release, synchronous closures passed to `XCTestCase.addTeardownBlock()` are now explicitly isolated to the main actor in Swift. Previously, such closures would run on the main actor but not be explicitly isolated to it. Asynchronous teardown blocks are not affected.  (115078758)

###### Known Issues

- Tests with more than one test case targeting macOS may not produce screen recordings in the result bundle. In the case where screen recordings are not available, screenshots are provided.  (118342983)

##### Thread Performance Checker

###### Resolved Issues

- Fixed: Thread Performance Checker emits a new category of runtime issues called “Known Hangs” which shows developers where in their code hangs are known to affect users of their apps.  (102045928)

##### Visionos

###### Resolved Issues

- Fixed: USDz assets appear as missing textures (pink stripes) for visionOS apps when viewing in the selectable preview in Xcode  (120443849)
- Fixed: iOS apps with a deployment target set to 17.2, 17.3, or 17.4 fail to run on Apple Vision Pro.  (120444126)
- Fixed: Texture Coordinate nodes now behave as expected  (121959312)

## See Also

- [Xcode 15.4 Release Notes](xcode-15_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.2 Release Notes](xcode-15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.1 Release Notes](xcode-15_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.0.1 Release Notes](xcode-15_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15 Release Notes](xcode-15-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-15_3-release-notes)*