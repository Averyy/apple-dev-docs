# Xcode 16 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 16 includes SDKs for iOS 18, iPadOS 18, tvOS 18, watchOS 11, macOS Sequoia 15, and visionOS 2. The Xcode 16 release supports on-device debugging in iOS 15 and later, tvOS 15 and later, watchOS 7 and later, and visionOS. Xcode 16 requires a Mac running macOS Sonoma 14.5 or later.

##### General

###### Notes

- Predictive Code Completion is now supported on all Apple silicon Macs.  (130449481)
- Predictive Code Completion is not supported when running Xcode in a Virtual Machine.  (129198328)
- Developing for visionOS requires a Mac with Apple silicon.  (114799042)

###### New Features

- Copy and paste from the build settings editor now uses xcconfig file syntax.  (14333348) (FB5925390)
- The Project Navigator’s “Open As” context menu now supports choosing default editors per file type  (24666459)
- Xcode 16 includes predictive code completion, powered by a machine learning model specifically trained for Swift and Apple SDKs. Predictive code completion requires a Mac with Apple silicon, running macOS 15.  (116310768)
- xcodebuild supports importing and exporting a downloaded platform to on disk. The simulator disk image can be exported to disk, so that it can be applied to Xcode installations on other machines that require the simulator runtime, without needing to redownload. There is an optional `-exportPath` argument for `xcodebuild -downloadAllPlatforms [-exportPath <pathToSave/>]` and `xcodebuild -downloadPlatform <platformName> [-exportPath <pathToSave/>]`. Example: ```None
 xcodebuild -downloadPlatform iOS -exportPath ~/MySimulators/
``` To import, run `xcodebuild -importPlatform <pathToSimulator.dmg>`, note that `xcrun simctl runtime add <pathToSimulator.dmg>` also works.  (129189162)

###### Resolved Issues

- Fixed: `xcodebuild -showBuildSettings` now uses the new build system, to match the settings used when performing an actual build. This may result in some differences in the build settings emitted compared to the earlier implementation, particularly in the presence or absence of `-scheme` and `-destination` options to `xcodebuild`.  (58870112) (FB7549715)
- Fixed an issue where the Add Frameworks dialog in the target editor would not show any results for a target building against the DriverKit SDK.  (107754792) (FB12103199)
- Updating the location of a path-based package dependency through the ‘Add Package Dependency’ panel now correctly update the existing reference to the new path, instead of silently failing.  (114293235)
- Fixed: Fix-its referring to changes in other files now offer offer a ‘Show’ action that will navigate to the location where the change fix-it is suggested, and offer a new fix-it annotation.  (119522152)
- Fixed: Resolved an issue where passing the `--background` flag to the `xcdebug` tool would unexpectedly bring Xcode to the foreground.  (120553994)
- Fixed: With Swift Explicitly-Built modules enabled, compilation of Swift targets’ modules no longer incorrectly inherits additional search paths from target configurations of their Swift dependencies in the same project.  (122501504)
- Fixed an issue where a build failure might not cancel a Build & Run action, thus causing an attempt to install or launch an invalid application on the run destination.  (125737915)
- Fixed: The RealityKit debugger might fail to capture complex scenes running on a physical device. In such cases, the simulator can be used instead.  (128373818)
- Fixed: Code completion might not always offer predictions.  (128708703)
- Fixed: Debugging RealityKit apps that target macOS, requires that the version of macOS installed on the host machine is 15.0 or newer.  (129308033)
- Fixed: Swift projects that set a deployment target of macOS 10.14, iOS 12.0, watchOS 5.0, tvOS 12.0 and use constants from float.h such as FLT_RADIX in Swift sources will not link correctly. This will cause a crash when running on those OS versions. The crash will not occur when running on macOS 10.14.4, iOS 12.2, watchOS 5.2, tvOS 12.2 or later.  (130107191)
- Fixed: Xcode 16 beta 3 will fail to launch for some users. Users who have not installed Xcode 16 beta or Xcode 16 beta 2 will see a “Loading a plug-in failed” alert.  (131066390)
- Fixed: AppIntents may fail to build project if there are duplicate title values for AppIntent conformances within the same target.  (131192911)
- Fixed: Varying a source language string in a String Catalog by plural will now use the correct plural cases for each language when propagating the same change to already-translated languages.   (132042468)

###### Known Issues

- Xcode 16 beta 5 may crash when opening Source Editor if running macOS Sequoia, beta 4 or older.   (130609632)  Install macOS Sequoia beta 5.
- Users that upgrade to Xcode 16 after having previously installed Xcode 16 Beta 6 or Xcode 16 RC may experience Developer Disk Image mounting errors when using iPhone 16 or Apple Watch Series 10 devices.  (136364979) (FB15189777)  Open Terminal.app and run ```None
 sudo installer -pkg /Applications/Xcode.app/Contents/Resources/Packages/XcodeSystemResources.pkg -target /
``` (replacing the path to Xcode 16 if necessary.)

###### Deprecations

- The simulator runtimes are currently available on the Apple Developer website, but will no longer be posted through the website in future updates.  Please use `xcodebuild -downloadPlatform <platform> -exportPath <path>` command to download the runtime and then `xcodebuild -importPlatform <path/simruntime.dmg>` to install it.  For more details, see [`Installing and managing Simulator runtimes`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/installing-additional-simulator-runtimes).  (133776444)

##### App Distribution

###### Known Issues

- When building for ad hoc distribution, some iOS apps may have their watchOS apps uninstall or fail to launch with an error about needing an iPhone App when one already exists.  (135240308)

##### Apple Clang Compiler

###### New Features

- For a re-exported module, Clang now looks for API Notes in the re-exporting module’s apinotes file. For example: ```None
 module ExportAsCore {
   header "ExportAsCore.h"
   export_as ExportAs
 }
 
 module ExportAs {
   header "ExportAs.h"
   export *
 }
``` Clang now allows declaring API Notes for symbols from ExportAsCore module in ExportAs.apinotes file.  (121680760)
- The following C++26 features have been implemented: - Remove undefined behavior from lexing. ([`P2621R2 (DR)`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2621r2.pdf))
- Making non-encodable string literals ill-formed ([`P1854R4 (DR)`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p1854r4.pdf)).
- Add @, $, and ` to the basic character set ([`P2558R2`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2558r2.html)).
- Unevaluated strings ([`P2361R6`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2361r6.pdf)) The following C++23 features have been implemented: - The Equality Operator You Are Looking For. ([`P2468R2`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2468r2.html))
- Labels at the end of compound statements. ([`P2324R2`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2324r2.pdf))
- static operator(). ([`P1169R4`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p1169r4.html))
- char8_t Compatibility and Portability Fix. ([`P2513R3`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2513r3.html))
- static operator[]. ([`P2589R1`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2589r1.pdf))
- Permitting static constexpr variables in constexpr functions. ([`P2647R1`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2647r1.html))
- consteval needs to propagate up. ([`P2564R3(DR)`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2564r3.html))
- Referencing The Unicode Standard. ([`P2736R2`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2736r2.pdf)) The following C++20 features have been implemented: - typename optional in more contexts.([`P0634R3`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2018/p0634r3.html))
- Structured binding extensions. ([`P1091R3`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p1091r3.html), [`P1381R1`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p1381r1.html))
- Parenthesized initialization of aggregates. ([`P0960R3`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p0960r3.html), [`P1975R0`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2019/p1975r0.html))  (128912178)

###### Resolved Issues

- Fixed looking up module maps in all subdirectories of provided header search paths.  (106677321)

###### Deprecations

- The following items have been deprecated or removed: Using -e without space after it to specify entry function to linker is disallowed now.  (130452096)

##### Asset Catalogs

###### New Features

- The Asset Catalog context menu has a new “Find References to Item” option that initiates an “Asset References” find for the selected asset  (104226484)
- Asset catalogs now provide an inspector property for enabling system color and image accessors for generated asset symbols, which allows Swift packages to opt-in to generating these accessors.  (113704993)
- Code completion results for generated asset symbols now display asset thumbnails  (114392937)
- The Find Navigator has a new “Asset References” query type that locates asset references as string literals or Swift/Objective-C generated symbols  (126376146)

###### Resolved Issues

- Fixed: Improved thumbnail rendering for asset catalog images.  (114343652)
- Fixed an issue where the Attributes Inspector wasn’t displayed for items in a Sticker Catalog.  (120438144) (FB13512995)

##### Build System

###### New Features

- Beginning in Xcode 16, the build system coordinates with the Clang and Swift compilers to discover and build module dependencies of project sources as a set of explicit tasks in the build log. Explicitly built modules provide more actionable error messages when compilation errors are diagnosed, improve debugger performance, and allow the build system to make better scheduling decisions which maximize parallelism.  (112943296)
- New build settings have been added to facilitate adoption of Swift 6. The `SWIFT_VERSION` build setting now allows building with the Swift 6 language mode. Projects can incrementally migrate to Swift 6 by opting into features individually using the new build settings under `Swift Compiler - Upcoming Features`.  (114638076)

###### Resolved Issues

- Fixed: Xcode now renames files such as TargetName-InfoPlist.strings to InfoPlist.strings at build time, even when the Info.plist file is fully generated by the build system.  (108824512)
- Fixed: Resolved an issue where “Clean Build Folder” would have no effect in some workspaces containing a project without any targets.  (116412043)
- Fixed: Xcode now uses `lipo` to create universal static libraries instead of `libtool`. Universal static libraries will now automatically use the 64-bit format if they exceed the maximum size allowed by the 32-bit format.  (117911543) (FB13331562)
- Fixed an issue where previously resolved Swift compiler diagnostics would reappear in the log and issue navigator in subsequent builds.  (119533281)
- Fixed an issue where projects using SwiftPM build tool plugins would sometimes report internal inconsistency errors when building.  (121851192) (FB13565986)
- Fixed: The build system now computes dependency information from command line arguments in more scenarios, reducing the likelihood of nondeterministic build failures. In some cases this may require shell script build phases to add output file dependency declarations.  (125596258)
- Fixed: Building a project that contains only warnings no longer reveals the issue navigator on build completion. Instead, a new behavior option for ‘Build > Generates Warnings’ was introduced that is distinct from ‘Build > Generates Errors’.  (127064801)

##### C++ Standard Library

###### New Features

- You can now turn on C++ Standard Library hardening in the Build Settings. Turning on hardening enables checks for common cases of misuse of the standard library APIs; if a check fails, the program is reliably terminated, helping prevent security vulnerabilities and diagnose some cases of undefined behavior. The library provides several hardening modes, including low-overhead modes that can be used in production. For more details, please refer to the [`hardening documentation`](https://developer.apple.comhttps://developer.apple.com/xcode/cpp/#library-hardening). - Note that turning on hardening might expose latent bugs in your code and cause it to terminate at runtime. Please make sure to fix any issues exposed by hardening in your code in a development environment before turning it on in production. The following new features and enhancements have been implemented: - [`P0020R6`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2017/p0020r6.html) — Floating Point Atomic
- [`P2443R1`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p2443r1.html) — `views::chunk_by`
- [`P2821R5`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2821r5.html) — `span.at()`
- [`P1659R3`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2021/p1659r3.html) — `starts_with` and `ends_with`
- [`P2302R4`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2302r4.html) — `std::ranges::contains` (note: `std::ranges::contains_subrange` not implemented yet)
- [`P0543R3`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p0543r3.html) — Saturation arithmetic
- [`P2905R2`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2905r2.html) — Runtime format strings
- [`P2918R2`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2918r2.html) — Runtime format strings II
- [`P2447R6`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2447r6.html) — `std::span` over an initializer list
- [`P1759R6`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p1759r6.html) — Native handles and file streams
- [`P2467R1`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2467r1.html) — Support exclusive mode for fstreams
- [`P2697R1`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2697r1.pdf) — Interfacing `bitset` with `string_view`
- [`P2497R0`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2497r0.html) — Testing for success or failure of `<charconv>` functions
- [`P2538R1`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2538r1.html) — ADL-proof `std::projected`
- [`P2909R4`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2023/p2909r4.html) — Fix formatting of code units as integers (Dude, where’s my char?)
- [`P2517R1`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2517r1.html) — Add a conditional noexcept specification to `std::apply`
- [`P2539R4`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2022/p2539r4.html) — Should the output of `std::print` to a terminal be synchronized with the underlying stream?  (128950351)

###### Deprecations

- The following items have been deprecated or removed: - Removed the type alias `allocator<T>::is_always_equal` in C++26 (P2868R3).
- You can use the compatibility macro `_LIBCPP_ENABLE_CXX26_REMOVED_ALLOCATOR_MEMBERS` to make the alias available again.
- Removed the `std::basic_string::reserve()` overload with no parameters in C++26. Use `shrink_to_fit` instead (P2870R3).
- You can use the compatibility macro `_LIBCPP_ENABLE_CXX26_REMOVED_STRING_RESERVE` to make the header and its contents available again.
- Removed header `<codecvt>` and all its contents in C++26 (P2871R3).
- You can use the compatibility macro `_LIBCPP_ENABLE_CXX26_REMOVED_CODECVT` to make the header and its contents available again.
- Removed `std::shared_ptr::unique`  in C++20 and later modes (P0619R4 section D.14).
- You can use the compatibility macro `_LIBCPP_ENABLE_CXX20_REMOVED_SHARED_PTR_UNIQUE` to make the function available again.
- Deprecated `std::numeric_limits::has_denorm` and `std::numeric_limits::has_denorm_loss` (P0619R4)
- The non-standard constructor `std::future_error(std::error_code)` has been removed. Please use the `std::future_error(std::future_errc)` constructor provided in C++17 instead.
- The headers `<experimental/deque>`, `<experimental/forward_list>`, `<experimental/list>`, `<experimental/map>`, `<experimental/memory_resource>`, `<experimental/regex>`, `<experimental/set>`, `<experimental/string>`, `<experimental/unordered_map>`, `<experimental/unordered_set>`, and `<experimental/vector>` have been removed as all their contents have been implemented in namespace `std` in previous releases.
- Removed a code path from `std::variant` that led to narrowing conversions behaving in a non-standard way (now that [`P1957`](https://developer.apple.comhttps://www.open-std.org/jtc1/sc22/wg21/docs/papers/2020/p1957r2.html) has been implemented in the compiler). This can cause a visible behavior change in some code using `std::variant`’s constructor. As a temporary workaround, use the `_LIBCPP_ENABLE_NARROWING_CONVERSIONS_IN_VARIANT` macro that restores the previous behavior; this compatibility macro will be removed in a future release.
- The macro `_LIBCPP_ENABLE_CXX20_REMOVED_ALLOCATOR_MEMBERS` has been deprecated and will be removed in a future release. This macro previously re-enabled redundant members of `std::allocator<T>` like `pointer`, `reference`, `rebind`, `address`, `max_size`, `construct`, `destroy`, and the two-argument overload of `allocate`. However, this led to the library being non-conforming due to incorrect constexpr-ness.
- The macros `_LIBCPP_ENABLE_CXX17_REMOVED_FEATURES` and `_LIBCPP_ENABLE_CXX20_REMOVED_FEATURES` have been deprecated and will be removed in a future release. These macros used to re-enable all features that were removed in the C++17 and C++20 standards. Instead of using these macros, please use the macros that re-enable individual features.  (128950615)

##### Carplay Simulator

###### New Features

- UI Refresh as well as the ability for you to rename configurations and screen record in CarPlay Simulator. Modifying and switching between configurations is accessible via a drop down in the main CarPlay Simulator window. Screen recording is accessible via the toolbar in the main CarPlay Simulator window.  (124405895)

##### Clang

###### New Features

- Clang now supports generating code to call typed allocators. To enable this support for C allocation functions such as `malloc()` set the `CLANG_ENABLE_C_TYPED_ALLOCATOR_SUPPORT` build setting to `YES`. For C++ allocations with `operator new`, set `CLANG_ENABLE_CPLUSPLUS_TYPED_ALLOCATOR_SUPPORT` to `YES`.  (132456928)

##### Command Line Tools

###### New Features

- Symbolication command line tools such as `atos `and `symbols` now support binaries and dSYMs with DWARFv5 debug info format.  (28041592)

##### Containerization

###### Resolved Issues

- Fixed: An app might not be able to read the contents of its own data container after replacing the content of the data container using Xcode or devicectl.  (116698465) (FB13253099)

##### Create Ml

###### Resolved Issues

- Fixed: Training fails towards the end of the Object Tracking training process if user loses internet connection.  (130111589)

##### Debugging

###### New Features

- LLDB can now import explicitly-built Swift and Clang modules directly. If the first expression evaluation in LLDB takes a long time due to Clang module compilation, consider adopting explicit modules in your project.  (84105971)
- The debug bar provides a control to view the current backtrace in the source editor, unified with contextual relevant source code for each frame in the source editor  (102907696)
- When targeting macOS 15, iOS 18, … or later, the default debug info format is DWARF 5.  (110925733)
- Xcode can debug crash logs and core files, within our outside the context of an Xcode project file and accompanying source files. The debug session allows full access to lldb commands in the console. Unsymbolicated frames in backtraces can be symbolicated by using the “Load Symbols” contextual menu item to add dsyms or symbol rich binaries.  (114104872)
- Code snippets are available in the LLDB console  (117042240)
- When the debugger is being used to inspect a crashed process or a crash log, the source editor annotation at the crashing line of code shows an explanation of the crash reason along with a link to more documentation about the crash reason.  (117428116)
- The MallocStackLogging lite mode diagnostic for recording malloc callstacks is now up to twice as CPU efficient for single-threaded workloads, and up to 10x less runtime overhead for multi-threaded workloads when used on macOS 15, iOS 18, and aligned releases.  (118902575)
- After selecting the process entry in the Debug Navigator, users can now use the `Delete` key or contextual menu to stop the process.  (121154261)
- Exception backtrace is shown more logically in Debug Navigator, especially when shown together with async recorded backtraces.  (121675894)

###### Resolved Issues

- Fixed: Breakpoints created in the LLDB console are now reflected in the breakpoint navigator and source editor  (10442078)
- Fixed: LLDB will now initialize the Swift compiler used for expression evaluation with the exact configuration of the Swift module at the current breakpoint instead of merging all compiler flags from the entire application. This makes search path mismatches less likely.  (115188886)
- Fixed: Xcode’s Memory Graph Debugger is now more efficient, using significantly less memory when loading and displaying memory graphs.  (118510874)
- Fixed an issue in the memory graph debugger where the inspector would not display allocation backtraces for objects in a saved memgraph file.  (120755580)
- Fixed: When debugging or profiling arm64/arm64e apps on macOS 15, iOS 18, tvOS 18, or visionOS 2, SwiftUI symbols should now be present.  (127698015)

###### Deprecations

- Diagnostics option “Malloc Stack Logging” no longer allows selecting “All Allocations and Free History” and instead tracks live allocations only.  (126948168)

##### Devices

###### New Features

- `devicectl` now provides commands to manage the developer disk images present on your Mac. See `devicectl manage ddis --help` for more information.   (114472187)
- `devicectl list devices` now supports hiding column headers in its textual output via the `--hide-headers` flag.   (119357626)
- `devicectl device process launch` now supports a `--console` option to capture standard output and standard error from the launched app and to wait until the app exits.  (123516594)
- `devicectl's --device` flag can now supports using a device’s name, DNS name, CoreDevice identifier, UDID, serial number, or ECID.  (123703862)
- Core Device has improved error reporting when an app fails to launch.  (123922504)

###### Resolved Issues

- Fixed: Xcode no longer changes the currently selected run destination implicitly when there is a transient loss of connectivity to the device. Xcode will keep the disconnected device selected with an indicator of its disconnected status.  (38378613)
- Fixed: Improved error reporting when we fail to enable DDI services on a device.  (114012346) (FB12987859)
- Fixed: Xcode no longer keeps an active connection to AppleTVs discovered in the local area network. Xcode will only connect on demand to a device on the local area network when the user attempts to interact with the device in the Devices and Simulators Window, Build & Run to the device, or use a Debugger feature on the device. This change in behavior only applies to devices running tvOS 17 or newer.  (115668388)
- Fixed: The process launch time of the devicectl command line tool has been improved.  (119057359)
- Fixed an issue where the Xcode Devices and Simulators Window shows outdated information when the user attempts to pair with a device for development.  (123271553)
- Fixed: When Xcode fails to install an application to a connected device, it presents improved error messages and recovery suggestions for common causes along with documentation about codesigning.  (123533550)
- Fixed: Pairing the same device again may cause the device to appear in the “Disconnected” section of the Device and Simulator Window.   (131072881)
- Fixed: When targeting an Apple Watch (or simulator) that is in Nightstand Mode, Xcode will fail to launch the application with an “application failed to launch” error.  (134250531) (FB14855711)

###### Known Issues

- Xcode is sometimes unable to determine if developer mode is enabled when using a device over the network.  (131662031) (FB14298506)  Connect the device directly to the Mac using a USBC or Lightning cable, then place the device in airplane mode to force Xcode to use the deivce over the wired connection.  Once Xcode is successfully using the device over the wired connection, you can turn airplane mode back on, and Xcode will continue to use the wired connection.
- If Xcode is unable to determine the state of developer mode on a device, it will report that developer mode is disabled, possibly leading to confusion if developer mode is actually enabled.  (133418906)

##### Documentation

###### New Features

- Swift-DocC has the ability to combine overloaded methods when `--enable-experimental-overloaded-symbol-presentation` is added to “Other DocC Flags” (`OTHER_DOCC_FLAGS`).  (38183676)
- Write documentation links to on-page headings and topic sections using `<doc:SomePage#Some-heading-title>`  (78908451)
- Swift-DocC now supports writing and building documentation for C++ APIs.  (117904434)
- Swift-DocC now warns about documentation for parameters and return values that doesn’t exist for that documented API.  (118739612)

###### Resolved Issues

- Fixed: Documentation extension files no longer require unique file names.  (117174884)
- Fixed: Documentation extension files for symbols with Swift and Objective-C representations can now use either language representation’s spelling for relative symbol links.  (120380627)
- Fixed: Objective-C symbols with language refined representations in Swift now display distinct documentation hierarchies for Swift and Objective-C.  (122300247) (FB13585944)

##### Foundation

###### Resolved Issues

- Fixed: If meeting both of the following scenarios, your app may crash on launch on platforms earlier than the latest versions of the respective OS with errors indicating missing symbols in `NSDecimal`: - You use any of the following `NSDecimal` functions in Swift
- You release an app compiled with Xcode 16, and the app runs on an OS version earlier than macOS 15.0, iOS 18.0, tvOS 18.0, watchOS 11.0, or visionOS 2.0 Your app may also fail to compile if you use `NSDecimalString(_:_:)` in the app. : This does not affect apps calling these functions from Objective-C or apps running on the latest versions of the respective OS.  (133371820) (FB14696453)

##### Instruments

###### New Features

- ‘Flatten Recursion’ feature in the new call tree detects and collapses cases of indirect recursion.   (6823780) (FB5940449)
- Recording options for a document and Instruments are now available directly in the document window when starting from a template. Subsequent runs can be reconfigured using ‘Next Recording’ button available in the runs sidebar.   (40923253)
- ‘Data Mining’ popover in the new call tree has been redesigned, optimizing for adding more functions and displaying longer symbol names.   (61782150)
- Custom Instruments:  element can now be used to create aggregation of os-log and os-signpost backtraces.   (66603961)
- Instruments document window has a new sidebar that gives access and overview of all runs in the document. Runs in the sidebar can be renamed and removed using context menu actions.    (103073589)
- Runs in the trace document now store its zoom level and scroll position separately, making it easy to switch between them and preserve visualization context.    (108528537)
- Improved the performance of `heap`, `leaks`, the Leaks instrument, and the Xcode memory graph debugger when analyzing processes which heavily use Swift.  (111248508)
- ⌘. shortcut can now be used to stop a trace recording.   (113574234)
- The flame graph is a new alternate visualization mode in the new call tree. Zooming in shows lower-weighted functions, and hovering along the ruler at the top displays tooltips down the entire stack.  (115313793)
- The new call tree enhances user responsiveness and provides progress bar feedback during longer running computations.   (122577386)
- `heap`, `leaks`, the Leaks instrument, and the Xcode memory graph debugger now label untyped allocations pointed to by stored properties of Swift types for easier identification.  (127317183)

###### Resolved Issues

- Fixed a sporadic crash happening when recording trace with the ‘Allocations’ Instrument.   (27975091)
- Fixed an issue where Instruments would show an error saying ‘Required kernel recording resources are in use by another document’ and prevent further recordings in the same document.   (93788278)
- Fixed an issue where libraries would be missing symbolication information when recording in a windowed mode.   (114650647)
- Fixed a crash happening when recording using ‘Animation Hitches’ template.    (114715443)
- Fixed: Eliminated application hangs when using filter bar in the ‘Symbols’ window.   (118244818)
- Fixed: Upon importing a file into Instruments, timeline is now automatically sized to fit the entire trace.   (118467393)
- Fixed an issue where Instruments wouldn’t respect ‘Working Directory’ override when launching applications on a macOS platform.   (123194792) (FB13631596)
- Fixed an issue where tracks in the main and pinned timeline could appear selected at the same time.   (125189186)

###### Known Issues

- UI State of the new call tree is not being saved in trace documents.   (113659508)
- When “Focus on Subtree” is used in the new call tree to focus a node, subsequent function applications are not possible.    (116369374)  To apply functions again, remove all currently focused nodes using control in the “Jump Bar”.
- “Top Functions” view is not available in the new call tree.   (123702178)
- Legacy call tree is still used in the following Instruments: Allocations, Leaks, CPU Counters when using arithmetic formulas, Sample Importer.   (124118051)
- Xcode Debugger fails to capture memory graph from processes running in watchOS Rosetta Simulator destinations.  (132023793)

###### Deprecations

- ‘Always use deferred mode’ option has been removed from Instruments. To record in deferred mode, use custom templates mechanism.   (120497357)

##### Interface Builder

###### Deprecations

- `@IBDesignable` views are deprecated and will no longer be rendered in the Interface Builder canvas.  (115873872)

##### Linking

###### New Features

- `dyld_info` gained support for code disassembly (`-disassemble`) and an improved Objective-C metadata inspection (`-objc`).  (65914062)
- A new code deduplication algorithm brings additional code size savings and an improved static link time performance. It is enabled by default in release builds.  (125995452)

###### Resolved Issues

- Fixed: A branch out of range errors in large binaries have been resolved with an improved branch island generation.  (117077862) (FB13282296)

###### Deprecations

- `-ld_classic` linker option is deprecated and will be removed in a future release.  (128502299)

##### Localization

###### New Features

- The String Catalog filter bar now supports more complex search criteria such as “Begins With” and “Does Not Contain”. It also supports filtering by specific translation states.  (82717148) (FB9594524)
- You can now mark strings in a String Catalog as not to be translated via “Mark as “Don’t Translate”” in the context menu. When such strings are exported via Product > “Export Localizations”, they will be marked with the translate=no attribute in the XLIFF file. This feature may be useful for strings that are still being iterated on and are not ready to be translated. The String Catalog editor prevents translation of strings marked as “Don’t Translate”.  (89342670)
- You can now filter for specific string tables or directory names in the Localization Catalog editor sidebar. This also works for language names in String Catalogs.  (90328598)
- Comments can now be added to String Catalogs for strings that did not already specify a comment in source code.  (102872845)
- Columns in the String Catalog editor can now be hidden via the context menu on the column headers.  (104674245)
- The String Catalog editor now supports showing inline warnings and errors for various issues with strings or their variation structures. Some issues will also display with Fix-Its to quickly fix the problem automatically.  (110193206)
- Errors and warnings are now emitted by the String Catalog editor when format specifier types in a translation conflict with those in the source string. For example, an error would be produced if “%@” was changed to “%lld” for the same argument number in a translation. Issues are also produced when a single string contains conflicting format specifiers or a mixture of numbered and unnumbered variables. For example, both “The %1$@ crossed the %1$lld” and “The %1$@ crossed the %lld” are incorrect and would be diagnosed.  (110196313)
- You can now jump from an entry in a String Catalog to the usages of that string in source code. To quickly jump to a string usage, click the jump arrow that appears when hovering over a key or choose “Jump to Source” from the Editor menu. To see a list of all discovered usages, see the Attributes Inspector.  (111711007)
- The Source Editor now supports jumping to the String Catalog that contains translations for the selected string literal. This is available via “Jump to String Catalog” in the context menu or via the same shortcuts as Jump to Definition.  (111711244)
- The Localization Catalog editor now displays a “Don’t Translate” badge next to strings marked translate=no in the XLIFF file.  (123834701)
- The String Catalog editor now supports showing the source code referencing the selected string key in the assistant editor.  (125265332)
- Warnings are now emitted by the String Catalog editor for stale strings. Fix-Its are provided to remove the string if you no longer need it or to manage manually if you’d like to keep it around.  (125992742)
- Tooltips in String Catalogs now provide insight into why a particular string cannot be edited.   (129254023)

###### Resolved Issues

- Fixed: When exporting localizations, Sticker Packs now treat accessibility labels as localizable. File names are no longer considered localizable.  (43449067)
- Fixed: Xcode no longer extracts strings from SwiftUI Previews for localization. Such strings will no longer be extracted to String Catalogs or included by Product > Export Localizations.  (75628856)
- Fixed: Significantly improved the performance of importing localizations into large projects or workspaces via Product > “Import Localizations” or via `xcodebuild -importLocalizations`.  (90510590)
- Fixed: When exporting or importing localizations, Swift Packages now only build for the platforms supported by clients within the workspace. Top-level packages within the workspace will build for platforms with custom deployment targets via the `platforms` field in the Manifest file, or macOS if no platforms have overridden deployment targets.  (94611040) (FB10094909)
- Fixed: Clicking a build error or warning emitted about a String Catalog now takes you to the problematic string when clicked.  (105166406)
- Fixed: Xcode no longer extracts known template strings from Interface Builder files to String Catalogs. An example would be the generic “Table View Cell” string.  (105301878)
- Fixed: Text replacements defined in System Settings are now supported in the String Catalog editor.  (107765948)
- Fixed more instances where String Catalogs would not detect a string that was removed from source code.  (108864739)
- Fixed: Filter text, selection, and expansion state are now preserved when switching languages in the String Catalog editor.  (110973472) (FB12383661)
- Fixed: Xcode 16 now uses xcstringstool instead of genstrings for discovering NSLocalizedString and similar legacy APIs that do not support extraction via the Swift compiler. This improves the reliability of string extraction in a number of instances in both Swift and C-family languages, including:
- Swift unicode escape sequences are now understood inside NSLocalizedString and sibling APIs. (20886479) (FB9810924)
- Padding and decimal precision information in format specifiers are now preserved when adding argument positionals. (FB5482238)
- String literals embedded in sub-expressions are no longer extracted. For example, no strings will be extracted from `NSLocalizedString(myFunction(@"substring"), @"comment")` (70008199)
- Empty string keys are now supported via NSLocalizedString. (85523152)
- Explicitly-escaped quotation marks in Swift multi-line string literals are now properly supported. (86601019)
- Strings will never be extracted from SwiftUI API in code comments. (33320518)  (111709535)
- Fixed: Xcode now sets the SWIFT_EMIT_LOC_STRINGS build setting to YES to enable compiler-based string extraction at the project level when adding a new String Catalog or migrating a .strings or .stringsdict file, as long as this setting was not already overridden to NO. Xcode would previously do this at the target level and only upon migration.  (114116199)
- Fixed: Marking an untranslated string for review or as reviewed will now use the source string as the translation. To use an empty string instead, hold down option to reveal alternate menu options.  (117266728) (FB13291503)
- Fixed: String Catalogs will now also be updated when building for testing.  (118902862)
- Fixed an issue in the String Catalog editor that could have prevented varied strings from being edited when the default value was specified in source code.  (122470742) (FB13594100)
- Fixed an issue where the context menu in String Catalog Editor may apply to the wrong row when a different row is selected.  (124500442)
- Fixed: Refined keyboard navigation within a String Catalog. ⌘↑ and ⌘↓/⏎ move vertically up and down rows within a column, while ⇥ and ⇧⇥ move horizontally through rows.   (125435426)
- Fixed an issue where Xcode or xcodebuild could emit empty .strings files to /tmp during various localization operations.  (126644251)
- Fixed an issue where .strings and .stringsdict files would no longer be deleted from disk after migration to .xcstrings.  (129936269)
- Fixed: LOCALIZED_STRING_MACRO_NAMES now once again supports referring to property wrappers.  (130446922) (FB14041161)
- Fixed: Resolved a long hang that could occur when loading and interacting with large String Catalogs.  (130619985)
- Fixed an error “No “original” attribute provided for strings from table” that could occur when exporting localizations.   (131190361) (FB14207838)
- Fixed: Xcode now remembers column visibility settings in String Catalog editor. Use the context menu on the string table header to adjust column visibility.   (131930622)

###### Deprecations

- As of Xcode 16, the genstrings command-line tool is considered deprecated. String Catalogs in Xcode provide a way to automatically aggregate localizable strings from source code using the Swift compiler and other technologies. If you still need to find basic usages of NSLocalizedString in Swift and C-family source code outside the context of String Catalogs and without using the compiler, you can use the `xcstringstool` utility instead. The following invocation would extract NSLocalizedString and similar API from the input source files and generate a .strings file, similar to genstrings: `xcrun xcstringstool extract --legacy-localizable-strings -o <output-directory> --output-format strings <input-files>`  (102887793)

##### Lock Screen

###### Resolved Issues

- Fixed: Lock Screen Quick Action buttons might disappear.  (128096099)

##### Lockedcameracapture

###### Resolved Issues

- Fixed: Capture Extensions are unable to fetch previously captured assets from PhotoKit when unlocked  (123529801)
- Fixed: Device may lock when recording video  (123639753)
- Fixed: When LockedCameraCapture’s openApplication API is called, the app’s CameraCaptureIntent is also called.  (126696751)
- Fixed: Keyboards are unresponsive in Capture Extensions  (128563059)
- Fixed: Capture Extensions with limited photo library access are unable to load asset resources from PhotoKit  (128646538)
- Fixed: HEIC/HEVC photos will show up as black in Capture Extensions.  (129292977)
- Fixed: Dictation does not work in Capture Extensions  (130017435)
- Fixed: Launching Capture Extensions may also concurrently prompt to open the app.  (130313693)
- Fixed: Capture Extensions may crash with false “Camera not actively used” termination reason, including during extension to app transitions.  (130846437)

###### Known Issues

- Logging does not appear in Xcode when debugging Capture Extensions when using “Attach to Process”.  (129785280)  Use “Attach to Process by PID or Name” in Xcode to debug Capture Extensions.
- Apps launched via Lock Screen Quick Action buttons will not run the CameraCaptureIntent perform function.   (133404039)
- Capture Extensions or apps launched via CameraCaptureIntent may erroneously crash with “AVCaptureEventInteraction not installed” reason  (133578610)

##### Memory Tools

###### Resolved Issues

- Fixed: When running on beta 5 of macOS 15 Sequoia, iOS 18, or aligned OS builds, memory tools like Xcode’s Memory Graph Debugger and Instruments’ Leaks template, may fail unexpectedly or crash. This includes the command-line tools `leaks`, `heap`, `vmmap`, and `malloc_history` when run against live macOS or Simulator processes.  (132747700)

##### Metal Debugger

###### New Features

- The Metal Debugger now supports capturing a macOS app by pressing a keyboard shortcut.  (48403037)
- The Xcode metal debugger adds support for metal-shaderconverter enabling source-level shader validation, debugging, and profiling for HLSL shaders  (116155434)

##### Metal Offline Compiler

###### Resolved Issues

- Fixed: Building GPU binaries using metal-tt with deployment targets prior to iOS 18 and macOS 15 has undefined behavior and can result in incorrect compilation or a crash  (129366607)

##### Mps Graph Viewer

###### New Features

- Xcode can now open MPS Graph packages. The new MPS Graph viewer let’s you inspect your pre-trained machine learning networks and visualize how they would be executed on Apple Silicon.  (116472862)

##### Playgrounds

###### Resolved Issues

- Fixed: Xcode Playgrounds may compile code with Swift language version 5 even when the playground is configured to language version 6.  (128711228)
- Fixed: Users may be unable to add files to a Playground.  (131866503)

##### Previews

###### New Features

- Xcode 16 brings a new execution engine for Previews that supports a larger range of projects and configurations. Now with shared build products between Build and Run and Previews, switching between the two is instant. Performance between edits in the source code is also improved for many projects, with increases up to 30%.  (37353090)
- Previews now support previewing views inside of static libraries.  (50492391)
- `PreviewModifier` is a new preview API for defining and applying reusable work between previews. Preview modifier can use an async and throwing initializer to load data, for example. Then in a separate call that data can be applied to any preview with that modifier. This makes it easier to load and apply data when using patterns like SwiftData, for example.  (108233218)
- `@Previewable` is a new macro that can be applied to any SwiftUI property wrapper so it can be used directly inside of a #Preview without needing to define an intermediate wrapper view. This is especially common for the use of `@State`, which can now be written as `@Previewable @State var myState = <initial value>` directly inside of the `#Preview`.  (110570957) (FB12298419)

###### Resolved Issues

- Fixed: Previews now support previewing inside of bundle targets  (51419685)
- Fixed: Previewing inside of files with methods of types nested in extensions no longer fails.  (74739568) (FB9019661)
- Fixed: Previews now work with targets that have platform filters applied, including in packages.  (83077196)
- Fixed: Previews now provides non-crash errors faster.  (110123477)
- Fixed: Previews now builds the exact same targets and with the same configuration as build and run, for example test targets are no longer built if only included in the test action.  (113656160)
- Fixed an issue when previewing to a physical phone when the phone has a paired watch.  (113893496) (FB12965086)
- Fixed: Previews no longer fail when previewing static functions with inout parameters.  (116098246)
- Fixed: Previews no longer fail when previewing functions that contain keyword escapes via backticks.  (117967670) (FB13338319)
- Fixed: When previewing for macOS, previews forwards more text editing commands to the UI under preview instead of sending them to Xcode, for example Command-Delete, allowing for a wider range of keyboard shortcut testing.  (118245789)
- Fixed: Selectable preview mode will not allow for selecting individual views.  (119504914)
- Fixed an issue with an intermittent error appearing in the canvas when switching between files.  (121353412)
- Fixed: Selection is not working for Xcode previews targeting visionOS.  (121870481)
- Fixed an issue when preivewing apps that need to run under Rosetta.  (122317524)
- Fixed warnings when using strict concurrency in Swift, and generated symbols from Asset Catalogs.  (122467732) (FB13593895)
- Fixed: Some large or complex projects may fail to build and run if they are scanning for specific Mach-O sections in their binaries.   (123416939)
- Fixed an issue when previewing a local package that imports another local package.  (123798299) (FB13664021)
- Fixed: `#Preview` now takes a @ViewBuilder for SwiftUI so `return` is no longer needed in the `#Preview` body. This only applies to previews of SwiftUI content, not to previews of AppKit or UIKit content which continue to be non-builder closures.  (123866442)
- Fixed: Better support for multi-platform applications.  (124202250) (FB13678152)
- Fixed issues around project names that contain special characters.  (125490102) (FB13699939)
- Fixed an issue where previews would not cancel inflight workspace builds when making code changes.  (126081025) (FB13715222)
- Fixed: Significantly improved performance of previewing in large projects.  (129167645)
- Fixed an issue where previews could fail in targets that use an xcframework.  (129592247) (FB13841857)
- Fixed: Previews may fail the first time you open a project that uses non-system macros.  (129604770)
- Fixed an issue where previews was incorrectly applying platform filters.  (129862695)

##### Project Management

###### New Features

- Xcode 16 introduces several new streamlined file creation workflows. Use “New Empty File” from the Project Navigator’s context menu to quickly create a new Swift file without any confirmation dialogs. Use Copy, Paste, and Duplicate from the Edit menu to create a new file from an existing file. Finally, you can cut text from the Source Editor, and then use the “New File from Clipboard” command while holding the option key in the Project Navigator’s context menu to quickly extract part of a source file into a new file.  (96547991)
- The Xcode target editor now only shows major OS versions in the list of suggested deployment target versions.  (118566415)
- You can now configure Supported Destinations, Bundle Identifier, Version and Build numbers, and several other attributes for all supported target types in the Xcode project editor, including frameworks, app extensions, watchOS apps, and more.  (122243197)
- Minimize project file changes, and avoid version control conflicts with buildable folder references. Convert an existing group to a buildable folder with the “Convert to Folder” context menu item in the Project Navigator.  Buildable folders only record the folder path into the project file without enumerating the contained files. This minimizes diffs to the project when files are added and removed, and avoids source control conflicts with your team. To use a folder as an opaque copiable resource, the default behavior before Xcode 16, uncheck the “Build Folder Contents” option in the File Inspector.  (123729918)
- The Project Navigator now defaults to creating groups with associated folders when using the “New Group” and “New Group from Selection” commands. To create a group without a folder, hold option in the context menu to reveal the “New Group without Folder” variant of the command.  (127396845)

###### Resolved Issues

- Fixed: The new xcodebuild flag of `-packageAuthorizationProvider keychain|netrc` can now be used to force usage of keychain or netrc as the authorizaion provider. This improves Xcode’s package registry support.  (118898849)
- Fixed: Xcode projects once again support package dependencies on packages in the same directory or a parent path. This support had been temporarily removed because it could cause Xcode to crash.  (126308647)

##### Project Navigator

###### Resolved Issues

- Fixed: The Swift Migrator (Edit > Convert > To Current Swift Syntax) has been removed. For more information, see [`Migrating to Swift 6`](https://developer.apple.comhttp://swift.org/migration).  (123486127)
- Fixed: xcodebuild now validates the format version number of Xcode projects for compatibility when performing builds.  (125385745)

##### Quick Actions

###### New Features

- Quick Actions now supports semantic search, which provides results that match the intent of a query without needing to exactly match the text.  (119402784)
- Quick Actions now displays enhanced result descriptions for certain actions.  (123842506)
- Quick Actions now supports acronym search e.g. the query “nef” matches the action “New > Empty File”.  (124293396)

###### Resolved Issues

- Fixed an issue where Quick Actions wouldn’t include results for certain menu items until the containing menus were manually opened.  (123789065)

##### Reality Composer Pro

###### New Features

- Timelines allows you to sequence actions to be executed in a particular order or at a particular time. Reality Composer Pro makes it easy to edit and configure those actions on a timeline and then initate the timeline to play based on a trigger.  (75589529)
- You can now use VirtualEnvironmentProbeComponent to control the lightning of your virtual environment.   (117770245)
- You can now create a docking region for the video playback area. You can use a built-in video to preview the surface reflections, or supply your own video asset. `Reflection_Diffuse` and `Reflection_Specular` allow you to fine-tune how the video stream is reflected in your scene.  (117926001)
- You can control the audio properties of an immersive environment using `RevertComponent`.   (118421316)
- The number of texcoords has been extended from 2 to 8. The 6 new buffers support `float2`, `float3` and `float4` data.  The first 2 buffers continue to support only `float2` data.  (123364636)

###### Resolved Issues

- Fixed: Modifying animation action parameters may result in actions overlapping with other actions on the same animation track.  (124014280)
- Fixed: Using the option  may results in a compilation failure of Reality Composer Pro projects.  (125624179)
- Fixed: Dragging an animation clip from an Animation Library component to a Timeline will result in the Play Animation action having an incorrect duration of 1 second.  (127395965)
- Fixed: A Notification Action will not cause a Notification Trigger to fire, even if they use the same String value. Update to use the new property name, `RealityKit.NotificationTrigger.Identifier`, to be able to observe a Notification posted by a NotificationAction in your Reality Composer Pro Timeline. The identifier you provide in your Reality Composer Pro Timeline NotificationAction will be delivered in the Notification’s userInfo under the key `NotificationAction.identifierKey`.  (127825336)
- Fixed: No warning is shown in cases where a Replace Behavior action is targeting an entity without a Behavior Component  (128011054)
- Fixed: Using HDR format video for docking region preview video fails to play and provides no errors. (impacts preview only)  (128098120)
- Fixed: Selecting an action with a target entity and then clearing the target automatically puts the user in target selection mode.  (128187376)
- Fixed: On some machines with Intel-integrated GPUs Reality Composer Pro and Xcode’s RealityKit Inspector may exhibit image corruption.  (128230028)
- Fixed: Viewport rotation slider does not affect the rendering of the environment.  (128497583)
- Fixed: A menu option under File > Developer Capture may not be visible when Reality Composer Pro is running without any documents open.  (128507720)
- Fixed: When selecting targets for animation actions, objects may lose its material settings.  (128865110)
- Fixed: Adding multiple audio resources with the same name to an Audio Library Component may cause Reality Composer Pro to crash.  (129223668)
- Fixed: Nested Timelines do not loop infinitely.  (129304213)
- Fixed: The Reverb Component has changed and will not apply a reverb effect until you reselect your previous reverb using Reality Composer Pro and re-deploy your project to your Apple Vision Pro.  (129951626)

###### Known Issues

- Authoring light spill is not supported on Intel Macs.  (124170457)
- Grounding shadow may be visible on the ground plane even if the grid hidden.  (127603652)
- A Behavior that has a Notification trigger may not work if the notification is posted immediately after calling Entity.load().  (128506951)  Post the notification after a short delay.
- Disabling and re-enabling the Docking Region component in Reality Composer Pro can cause the component width to not be editable  (133285221)  Either close and re-open Reality Composer Pro, or switch to a different scene tab and back

##### Realitykit Inspector

###### Resolved Issues

- Fixed: Capture Entity Hierarchy does not work when running designed for iPad apps on visionOS.   (128028088)

##### Safari Web Extensions

###### Resolved Issues

- Fixed: The safari-web-extension-converter may fail when creating a new project.  (130299863)

##### Signing Distribution

###### Resolved Issues

- Fixed: When building for macOS, Xcode 16 will now validate that any provisioning profiles used allow list all of the restricted entitlements you’ve specified in your entitlements files. This validation ensures that your app will successfully install, launch, and make use of system capabilities and services that require the entitlement. This may result in a build error if you are using a provisioning profile that doesn’t allow list the restricted entitlements you need. Automatic signing will generate a new provisioning profile for you, buit if you are using manual signing then you will need to visit your account at [`https://developer.apple.com/account`](https://developer.apple.comhttps://developer.apple.com/account) to create a new provisioning profile.  (48821779)
- Fixed: Xcode 16 stores downloaded provisioning profiles in a new location on disk, at ~/Library/Developer/Xcode/UserData/Provisioning Profiles. Xcode will still load previously downloaded profiles from the previous location.  (54347894)
- Fixed: Xcode signing better handles capabilities that are public for development and managed for distribution. This fixes an issue when distributing apps where the development capability would sometimes be used instead of the managed distribution capability.  (122413905)
- Fixed: `xcodebuild` will crash when exporting an archive using manual signing if there is no provisioningProfiles key provided in the export options plist.  (128040128) (FB13797243)
- Fixed: Submitting an iOS app with the Web Browser Engine Host entitlement to the App Store or for local distribution may fail with the error `App contains binaries that have no valid architectures for distribution.`  (135387309)

##### Simulator

###### New Features

- Xcode 16’s visionOS simulator now includes support for simulated FaceTime calls. You can use this feature to test your SharePlay experience with a simulated group session on the visionOS simulator. To start a simulated visionOS FaceTime call, select one of the participant configurations in the “FaceTime” submenu of the simulator’s “Features” menubar item. For example, select Features > FaceTime > User and 4 Spatial Participants to start a call with four simulated participants using their spatial Personas.  (112669619)

###### Resolved Issues

- Fixed: Resolves a bug that limited the number of times that an iOS app could be rebuilt and launched to the local Mac destination designed for iPad.  (110895896) (FB12364137)
- Fixed: When attempting to boot a simulator device after your system installs an XProtect update, the simulated device should boot more reliably (encountering less “Unable to boot the Simulator” or “-308” errors).  However, performance will not be optimized for boots that occur prior to GateKeeper completing a re-scan of the simulator runtime’s dyld cache (usually within a few minutes).  (118038020)

###### Known Issues

- On systems that do not have Internet access, Xcode cannot reach the index for SDK to Simulator runtime mapping information. This will cause Xcode to list current simulators as ‘Other Installed Platforms’ and consider the current platform as missing.  (135367176)  To download a copy of the latest index run: `curl -O https://devimages-cdn.apple.com/downloads/xcode/simulators/index2.dvtdownloadableindex` Then copy the index to the offline system and run the following command to set the index: `defaults write com.apple.dt.Xcode DVTDownloadableIndex <path/to/the/copied/index2.dvtdownloadableindex>` Remember to repeat this workaround when upgrading to newer simulator runtimes, or newer Xcode, on systems without Internet access.

##### Source Control

###### Resolved Issues

- Fixed: Xcode now properly handles “insteadOf” rules in git config  (52076700)
- Fixed: The git command line tool distributed with Xcode 16 Beta does not contain PCRE support.  (119158145)
- Fixed: Xcode now looks up the user’s known_hosts files for trusted keys when connecting to remote servers via SSH  (128175533)

##### Source Editor

###### New Features

- Added support for EditorConfig. The editor now respects indentation settings given in `.editorconfig` files. Xcode supports the following settings: `indent_style`, `tab_width`, `indent_size`, `end_of_line`, `insert_final_newline`, `max_line_length`, and `trim_trailing_whitespace`. See [`https://editorconfig.org`](https://developer.apple.comhttps://editorconfig.org) for more information. Settings from `.editorconfig` files normally take precedence over settings given in the “Text Editing” section of View > Inspectors > File for a file or group. This can be disabled by unchecking the “Prefer Settings from EditorConfig” checkbox on the Indentation tab of Xcode > Settings > Text Editing.  (20796230)
- There is a new “Extract to File” refactor action. Users can now click on a top level declaration in Swift files (class, struct, enum, extension, function) and click on “Extract to File” in the “Refactor” section, which will extract the declaration to a new file, as well as the relevant comments and imports. Users can also select any code and click on “Extract Selection to File” in the “Refactor” section, which will extract that selection to a new file.  (39453975)
- Added the “Reformat to Width” command to the Editor > Structure menu. This command splits long lines containing member access and function call expressions onto multiple lines. The target width is given with the “Reformat code at column” setting on the Editing tab of Xcode > Settings > Text Editing. Reformatting can happen automatically when using code completion by checking the “Automatically reformat when completion code” checkbox. The editor can visually show column by checking the “Show reformatting guide”, which was formerly called the “Page Guide”. The target width can also be set using the `max_line_length` EditorConfig setting.  (94577507) (FB10083417)
- When editing an XML file, closing an opening XML tag will automatically insert a matching closing tag.    (132524389)
- Word movements are now more granular, and will not skip characters such as parenthesis.    (133017821)

###### Known Issues

- Changes to `.editorconfig` are not reflected immediately in open files.  (120389049)  Quit and restart Xcode.

##### Storekit

###### New Features

- macOS now supports in-app [`Offer Code`](https://developer.apple.com﻿https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes/) redemption. Use [`StoreKit Testing in Xcode`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode/) to ensure your app responds correctly when customers redeem a Mac App Store Offer Code.  (60096251)
- You can now assign product and subscription images in the StoreKit configuration in Xcode. Use these images in-app when creating and testing [`ProductViews`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/productview) and [`StoreViews`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/storeview). Subscription groups now support adding localized names and descriptions. And, you can configure a test license agreement and test privacy policies to display in your [`SubscriptionStoreView`](https://developer.apple.comhttps://developer.apple.com/documentation/storekit/subscriptionstoreview) when testing with Xcode.  (114228169)
- New win-back offer APIs can be tested using [`StoreKit Testing in Xcode`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/setting-up-storekit-testing-in-xcode/). Configure win-back offers for your auto-renewable subscriptions in the StoreKit configuration, and simulate different scenarios of a customer’s eligibility for each offer.  (118535734)
- New win-back offer APIs can be tested using StoreKit Testing in Xcode. Configure win-back offers for your auto-renewable subscriptions in the StoreKit configuration, and simulate different scenarios of a customer’s eligibility for each offer.  (118893438)

###### Resolved Issues

- Fixed an issue causing some custom build configurations to fail because of the StoreKit configuration sync if the bundleID of the target is missing.  (129705753) (FB13871078)

###### Known Issues

- The StoreKit Transaction Manager might be unresponsive when performing actions while an app is running in a debug session. The affected actions include: create a new purchase, send a purchase intent, and edit an active or expired subscription.  (126700294)  Close the transaction manager, detach the app from the current debug session by stopping the process in Xcode, then re-open the transaction manager. You can open and use the app as normal on your device or simulator and perform actions in the transaction manager as long as there is no active debug session.

##### Swift

###### New Features

- Swift now allows usage of non-copyable C++ types.  (83358475)
- You can now suppress `Copyable` on protocols, generic parameters, and existentials: ```swift
 // Protocol does not require conformers to be Copyable.
 protocol Flower: ~Copyable {
   func bloom()
 }
 
 // Noncopyable type
 struct Marigold: Flower, ~Copyable {
   func bloom() { print("Marigold blooming!") }
 }
 
 // Copyable type
 struct Hibiscus: Flower {
   func bloom() { print("Hibiscus blooming!") }
 }
 
 func startSeason(_ flower: borrowing some Flower & ~Copyable) {
   flower.bloom()
 }
 
 startSeason(Marigold())
 startSeason(Hibiscus())
``` By writing `~Copyable` on a generic type, you’re suppressing a default `Copyable` constraint that would otherwise appear on that type. This permits noncopyable types, which have no `Copyable` conformance, to conform to such protocols and be substituted for those generic types. Full functionality of this feature requires the newer Swift 6 runtime, so a minimum deployment target of iOS 18, macOS 15, etc, is recommended.  See Swift Evolution proposal SE-427 for more details.  (101653009)
- When calling a C++ function from Swift, you no longer have to pass the arguments that have default values.  (103975014)
- The Wrapped type of an Optional now supports noncopyable types. See Swift Evolution proposal SE-0437 for details.  (117753275)
- The Pointee type of an UnsafePointer/UnsafeMutablePointer now supports noncopyable types. See Swift Evolution proposal SE-0437 for details.  (117753867)
- Swift overlay for the C++ standard library now supports visionOS.  (123516182)
- You can now call virtual methods of a C++ type from Swift, if the C++ type is a reference type (i.e. is annotated as `SWIFT_IMMORTAL_REFERENCE` or `SWIFT_SHARED_REFERENCE`).  (123852577)
- Swift 5.10 missed a semantic check from [`SE-0309`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0309-unlock-existential-types-for-all-protocols.md). In type context, a reference to a protocol `P` that has associated types or `Self` requirements should use the `any` keyword, but this was not enforced in nested generic argument positions. This is now an error as required by the proposal: ```swift
   protocol P { associatedtype A }
   struct Outer<T> { struct Inner<U> { } }
   let x = Outer<P>.Inner<P>()  // error
``` To correct the error, add `any` where appropriate, for example: `Outer<any P>.Inner<any P>`.  (125985138)
- Swift 5.10 accepted certain invalid opaque return types from [`SE-0346`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0346-light-weight-same-type-syntax.md). If a generic argument of a constrained opaque return type didn’t satisfy the requirements on the primary associated type, the generic argument was silently ignored and type checking would proceed as if it weren’t stated. This now results in a diagnostic: ```swift
   protocol P<A> { associatedtype A: Sequence }
   struct G<A: Sequence>: P {}
 
   func f() -> some P<Int> { return G<Array<Int>>() }  // error
``` The return type above should be written as `some P<Array<Int>>` to match the return statement. The old broken behavior in this situation can also be restored, by removing the erroneous constraint and using the more general upper bound `some P`.  (125985588)
- A `for`-`in` loop statement can now accept a pack expansion expression, enabling iteration over the elements of its respective value pack. This form supports pattern matching, control transfer statements, and other features available to a `Sequence`-driven `for`-`in` loop, except for the `where` clause. Below is an example implementation of the equality operator for tuples of arbitrary length using pack iteration: ```swift
   func == <each Element: Equatable>(lhs: (repeat each Element),
                                     rhs: (repeat each Element)) -> Bool {
 
     for (left, right) in repeat (each lhs, each rhs) {
       guard left == right else { return false }
     }
     return true
   }
``` The elements of the value pack corresponding to the pack expansion expression are evaluated on demand, meaning the ith element is evaluated on the ith iteration: ```swift
   func doSomething(_: some Any) {}
 
   func evaluateFirst<each T>(_ t: repeat each T) {
     for _ in repeat doSomething(each t) {
       break
     }
   }
 
   evaluateFirst(1, 2, 3) 
   // 'doSomething' will be called only on the first element of the pack.
``` [`SE-0408`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0408-pack-iteration.md)  (125986029)
- The Swift 6 language mode will open existential values with “self-conforming” types (such as `any Error` or `@objc` protocols) passed to generic functions. For example: ```swift
   func takeError<E: Error>(_ error: E) { }
 
   func passError(error: any Error) {
     takeError(error)  // Swift 5 does not open `any Error`, Swift 6 does
   }
``` This behavior can be enabled prior to the Swift 6 language mode using the upcoming language feature `ImplicitOpenExistentials`.

[`SE-0352`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0352-implicit-open-existentials.md)  (125991349)

- Non-built-in expression macros can now be used as default arguments that expand at each call site. For example, a custom `#CurrentFile` macro used as a default argument in ‘Library.swift’ won’t be expanded to `"Library.swift"`: ```swift
   @freestanding(expression)
   public macro CurrentFile() -> String = ...
 
   public func currentFile(name: String = #CurrentFile) { name }
``` Instead, it will be expanded at where the function is called: ```swift
   print(currentFile())
   // Prints "main.swift"
``` The expanded code can also use declarations from the caller side context: ```swift
   var person = "client"
   greetPerson(/* greeting: #informalGreeting */)
   // Prints "Hi client" if macro expands to "Hi \(person)"
``` [`SE-0422`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0422-caller-side-default-argument-macro-expression.md)  (125991596)
- Tasks now gain the ability to respect Task Executor preference. This allows tasks executing default actors (which do not declare a custom executor), and nonisolated asynchronous functions to fall back to a preferred executor, rather than always executing on the default global pool. The executor preference may be stated using the `withTaskExecutorPreference` function: ```swift
   nonisolated func doSomething() async { ... }
   
   await withTaskExecutorPreference(preferredExecutor) {
     doSomething()
``` Or when creating new unstructured or child-tasks (e.g. in a task group): ```swift
   Task(executorPreference: preferredExecutor) {
     // executes on 'preferredExecutor'
     await doSomething() // doSomething body would execute on 'preferredExecutor'
   }
``` [`SE-0417`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0417-task-executor-preference.md)  (125991889)
- Functions can now specify the type of error that they throw as part of the function signature. For example: ```swift
   func parseRecord(from string: String) throws(ParseError) -> Record { ... }
``` A call to `parseRecord(from:)` will either return a `Record` instance or throw an error of type `ParseError`. For example, a `do..catch` block will infer the `error` variable as being of type `ParseError`: ```swift
   do {
     let record = try parseRecord(from: myString)
   } catch {
     // error has type ParseError
   }
``` Typed throws generalizes over throwing and non-throwing functions. A function that is specified as `throws` (without an explicitly-specified error type) is equivalent to one that specifies `throws(any Error)`, whereas a non-throwing is equivalent to one that specifies `throws(Never)`. Calls to functions that are `throws(Never)` are non-throwing. Typed throws can also be used in generic functions to propagate error types from parameters, in a manner that is more precise than `rethrows`. For example, the `Sequence.map` operation can propagate the thrown error type from its closure parameter, indicating that it only throws errors of the same type as that closure does: ```swift
   extension Sequence {
     func map<T, E>(_ body: (Element) throws(E) -> T) throws(E) -> [T] { ... }
   }
``` When given a non-throwing closure as a parameter, `map` will not throw. [`SE-0413`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0413-typed-throws.md)  (125992062)
- The Standard Library now provides APIs for performing collection operations over noncontiguous elements. For example: ```swift
   var numbers = Array(1...15)
 
   // Find the indices of all the even numbers
   let indicesOfEvens = numbers.indices(where: { $0.isMultiple(of: 2) })
 
   // Perform an operation with just the even numbers
   let sumOfEvens = numbers[indicesOfEvens].reduce(0, +)
   // sumOfEvens == 56
 
   // You can gather the even numbers at the beginning
   let rangeOfEvens = numbers.moveSubranges(indicesOfEvens, to: numbers.startIndex)
   // numbers == [2, 4, 6, 8, 10, 12, 14, 1, 3, 5, 7, 9, 11, 13, 15]
   // numbers[rangeOfEvens] == [2, 4, 6, 8, 10, 12, 14]
``` The standard library now provides a new `indices(where:)` function which creates a `RangeSet` - a new type representing a set of discontiguous indices. `RangeSet` is generic over its index type and can be used to execute operations over noncontiguous indices such as collecting, moving, or removing elements from a collection. Additionally, `RangeSet` is generic over any `Comparable` collection index and can be used to represent a selection of items in a list or a refinement of a filter or search result. [`SE-0270`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0270-rangeset-and-collection-operations.md)  (125993055)
- Noncopyable enums can be pattern-matched with switches without consuming the value you switch over: ```swift
   enum Lunch: ~Copyable {
     case soup
     case salad
     case sandwich
   }
   
   func isSoup(_ lunch: borrowing Lunch) -> Bool {
     switch lunch {
       case .soup: true
       default: false
     }
   }
``` See Swift Evolution proposal SE-432 for more details.  (126282962)
- The noncopyable fields of certain types can now be consumed individually: ```swift
   struct Token: ~Copyable {}
 
   struct Authentication: ~Copyable {
     let id: Token
     let name: String
 
     mutating func exchange(_ new: consuming Token) -> Token {
       let old = self.id  // <- partial consumption of 'self'
       self = .init(id: new, name: self.name)
       return old
     } 
   }
``` See Swift Evolution proposal SE-429 for more details.  (126715654)
- Swift 6 comes with a new language mode that prevents the risk of data races at compile time. This guarantee is accomplished through ; the compiler validates that data passed over a boundary between concurrently executing code is either safe to reference concurrently, or mutually exclusive access to the value is enforced.  The data-race safety checks were previously available in Swift 5.10 through the `-strict-concurrency=complete` compiler flag. Complete concurrency checking in Swift 5.10 was overly restrictive, and Swift 6 removes many false-positive data-race warnings through better `Sendable` inference, new analysis that proves mutually exclusive access when passing values with non-`Sendable` type over isolation boundaries, and more. You can enable the Swift 6 language mode using the `-swift-version 6` compiler flag.  (129020586)
- Since its introduction in Swift 5.1 the `@TaskLocal` property wrapper was used to create and access task-local value bindings. Property wrappers introduce mutable storage, which was now properly flagged as potential source of concurrency unsafety. In order for Swift 6 language mode to not flag task-locals as potentially thread-unsafe, task locals are now implemented using a macro. The macro has the same general semantics and usage patterns, however there are two source-break situations which the Swift 6 task locals cannot handle: Using an implicit default `nil` value for task local initialization, when combined with a type alias: ```swift
   // allowed in Swift 5.x, not allowed in Swift 6.x
   
   typealias MyValue = Optional<Int> 
   
   @TaskLocal
   static var number: MyValue // Swift 6: error, please specify default value explicitly
   
   // Solution 1: Specify the default value
   @TaskLocal
   static var number: MyValue = nil
   
   // Solution 2: Avoid the type-alias
   @TaskLocal
   static var number: Optional<Int>
``` At the same time, task locals can now be declared as global properties, which wasn’t possible before.  (129181514)
- The compiler is now capable of determining whether or not a value that doesn’t conform to the `Sendable` protocol can safely be sent over an isolation boundary. This is done by introducing the concept of *isolation regions - that allows the compiler to reason conservatively if two values can affect each other. Through the usage of isolation regions, the compiler can now prove that sending a value that doesn’t conform to the `Sendable` protocol over an isolation boundary cannot result in races because the value (and any other value that might reference it) isn’t used in the caller after the point of sending allowing code like the following to compile: ```swift
   actor MyActor {
       init(_ x: NonSendableType) { ... }
   }
   
   func useValue() {
     let x = NonSendableType()
     let a = await MyActor(x) // Error without Region Based Isolation!
   }
``` (129182113)
- Region Based Isolation is now extended to enable the application of an explicit `sending` annotation to function parameters and results. A function parameter or result that is annotated with `sending` is required to be disconnected at the function boundary and thus possesses the capability of being safely sent across an isolation domain or merged into an actor-isolated region in the function’s body or the function’s caller respectively. Example: ```swift
   func parameterWithoutSending(_ x: NonSendableType) async {
     // Error! Cannot send a task-isolated value to the main actor!
     await transferToMainActor(x)
   }
   
   func parameterWithSending(_ x: sending NonSendableType) async {
     // Ok since `x` is `sending` and thus disconnected.
     await transferToMainActor(x)
   }
``` [`SE-0430`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0430-transferring-parameters-and-results.md)  (129182529)
- The compiler would now automatically employ `Sendable` on functions and key path literal expressions that cannot capture non-Sendable values. This includes partially-applied and unapplied instance methods of `Sendable` types, as well as non-local functions. Additionally, it is now disallowed to utilize `@Sendable` on instance methods of non-Sendable types. Let’s use the following type to illustrate the new inference rules: ```swift
   public struct User {
     var name: String
 
     func getAge() -> Int { ... }
   }
``` Key path `\User.name` would be inferred as `WritableKeyPath<User, String> & Sendable` because it doesn’t capture any non-Sendable values. The same applies to keypath-as-function conversions: ```swift
   let _: @Sendable (User) -> String = \User.name // Ok
``` A function value produced by an un-applied reference to `getAge` would be marked as `@Sendable` because `User` is a `Sendable` struct: ```swift
   let _ = User.getAge // Inferred as `@Sendable (User) -> @Sendable () -> Int`
 
   let user = User(...)
   user.getAge // Inferred as `@Sendable () -> Int`
``` [`SE-0418`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0418-inferring-sendable-for-methods.md)  (129182930)
- `async` functions can now explicitly inherit the isolation of their caller by declaring an `isolated` parameter with the default value of `#isolation`: ```swift
 func poll(isolation: isolated (any Actor)? = #isolation) async -> [Item] {
   // implementation
 }
``` When the caller is actor-isolated, this allows it to pass isolated state to the function, which would otherwise have concurrency problems.  The function may also be able to eliminate unwanted scheduling changes, such as when it can quickly return in a fast path without needing to suspend. [`SE-0420`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0420-inheritance-of-actor-isolation.md)  (129183122)
- You can now use `@preconcurrency` attribute to replace static actor isolation checking with dynamic checks for witnesses of synchronous nonisolated protocol requirements when the witness is isolated. This is common when Swift programs need to interoperate with frameworks written in C/C++/Objective-C whose implementations cannot participate in static data race safety. ```swift
   public protocol ViewDelegateProtocol {
     func respondToUIEvent()
   }
``` It’s now possible for a `@MainActor`-isolated type to conform to `ViewDelegateProtocol` by marking conformance declaration as `@preconcurrency`: ```swift
   @MainActor
   class MyViewController: ViewDelegateProtocol {
     func respondToUIEvent() {
       // implementation...
     }
   }
``` The compiler would emit dynamic checks into the `respondToUIEvent()` witness to make sure that it’s always executed in `@MainActor` isolated context. Additionally, the compiler would emit dynamic actor isolation checks for: - `@objc` thunks of synchronous actor-isolated members of classes.
- Synchronous actor-isolated function values passed to APIs that erase actor isolation and haven’t yet adopted strict concurrency checking.
- Call-sites of synchronous actor-isolated functions imported from Swift 6 libraries. The dynamic actor isolation checks can be disabled using the flag `-disable-dynamic-actor-isolation`. [`SE-0423`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0423-dynamic-actor-isolation.md)  (129183347)
- You can now require a function value to carry its actor isolation dynamically in a way that can be directly read by clients: ```swift
   func apply<R>(count: Int,
                 operation: @isolated(any) async () -> R) async -> [R]
       where R: Sendable {
     // implementation
   }
``` The isolation can read with the `.isolation` property, which has type `(any Actor)?`: ```swift
   let iso = operation.isolation
``` This capability has been adopted by the task-creation APIs in the standard library.  As a result, creating a task with an actor-isolated function will now synchronously enqueue the task on the actor, which can be used for transitive event-ordering guarantees if the actor guarantees that jobs will be run in the order they are enqueued, as `@MainActor` does.  If the function is not explicitly isolated, Swift still retains the right to optimize enqueues for functions that actually start by doing work with different isolation from their formal isolation. [`SE-0431`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0431-isolated-any-functions.md)  (129183477)
- Serial executor gains a new customization point `checkIsolation()`, which can be implemented by custom executor implementations in order to provide a last resort check before the isolation asserting APIs such as `Actor.assumeIsolated` or `assertIsolated` fail and crash. This specifically enables Dispatch to implement more sophisticated isolation checking, and now even an actor which is “on a queue which is targeting another specific queue” can be properly detected using these APIs. [`SE-0424`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0424-custom-isolation-checking-for-serialexecutor.md)  (129183881)
- Closures can now appear in pack expansion expressions, which allows you to construct a parameter pack of closures where each closure captures the corresponding element of some other parameter pack. For example: ```swift
   struct Manager<each T> {
     let fn: (repeat () -> (each T))
 
     init(_ t: repeat each T) {
       fn = (repeat { each t })
     }
   }
``` (129184039)
- Distributed actors now have the ability to support complete split server / client systems, thanks to the new `@Resolvable` macro and runtime changes. It is now possible to share an “API module” between a client and server application, declare a resolvable distributed actor protocol with the expected API contract and perform calls on it, without knowing the specific type the server is implementing those actors as. Declaring such protocol looks like this: ```swift
 import Distributed 
 
 @Resolvable
 protocol Greeter where ActorSystem: DistributedActorSystem<any Codable> {
   distributed func greet(name: String) -> String
 }
``` (See [`SE-0428`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0428-resolve-distributed-actor-protocols.md) for further examples)  (129184344)

###### Resolved Issues

- Fixed: Using an `Optional` value as a `consuming` parameter may lead to the compiler crashing when the `?` operator is applied to that parameter.  (116127887)
- Fixed: The static methods of C++ classes imported to Swift are no longer getting “Mutating” suffix when there is a non-static const member function with the same name.  (120858502)
- Fixed: Ownership errors inside of a `switch` statement with a non-`Copyable` subject may lead to compiler crashes instead of diagnosing the error.  (123604613)
- Fixed: Calling a borrowing method on a noncopyable existential (boxed protocol type) emits an error saying “usage of a noncopyable type that compiler can’t verify”  (125864434)
- Fixed: With the implementation of [`SE-0110`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0110-distinguish-single-tuple-arg.md), a closure parameter syntax consisting of only a parameter type — and no parameter name — was accidentally made legal for certain unambiguous type syntaxes in Swift 4. For example: ```swift
   let closure = { ([Int]) in }
``` Having been [`gated`](https://developer.apple.comhttps://github.com/apple/swift/pull/28171) behind a compiler warning since at least Swift 5.2, this syntax is now rejected. [`#70065`](https://developer.apple.comhttps://github.com/apple/swift/pull/70065)  (125992431)
- Fixed: _SwiftConcurrencyShims used to declare the `exit` function, even though it might not be available. The declaration has been removed, and must be imported from the appropriate C library module (e.g. Darwin or SwiftGlibc).  (125992667)
- Fixed: Writing a composition of a protocol and ~Copyable in the inheritance clause of a struct or enum results in incorrect generated swiftinterface, where ~Copyable is missing.  (126090425)
- Fixed: Accessing a value in memory through an `UnsafeBufferPointer` of `~Copyable` type may raise a spurious “unexpected exclusivity violation” error.  (127335590)
- Fixed: When a `consuming` or `borrowing` parameter of `Copyable` type is implicitly captured by a closure, uses of the parameter do not get checked against implicit copies inside of the closure body, and misuse of the parameter may lead to a miscompile and the program crashing at runtime.  (127382105)
- Fixed: Using the `!` operator on a non-`Copyable` `Optional` value always tries to consume the operand, even if that isn’t possible or necessary.  (127459955)
- Fixed: In Swift 6.0, the standard library functions `UnsafeRawPointer.loadUnaligned<T>(as:)`, `UnsafeMutableRawPointer.loadUnaligned<T>(as:)`, and `UnsafeMutableRawPointer.storeBytes<T>(of:as:)` are incorrectly marked as deprecated.  (128709914)
- Fixed: Calling a mutating method on a noncopyable existential (boxed protocol type) emits an error saying “usage of a noncopyable type that compiler can’t verify”  (128900124)
- Fixed: Conditional conformances for Copyable can be written without explicitly specifying which generic parameters need to conform to Copyable. This is an issue due to a difference in behavior from the SE-427 proposal.  (128904812)
- Fixed: Reinitializing a variable that has been consumed using the `consume` operator inside of a `defer` block that also contains `if` statements or other control flow may lead to the compiler generating invalid code that leads to runtime memory corruption.  (129303198)

###### Known Issues

- By default, async initializers on actors use flow-sensitive isolation: at first, the initializer is a non-isolated function, but it becomes isolated to the actor when the actor object is fully initialized.  There is a known issue in this logic when the actor is initialized by delegating to another initializer call, and it is possible to observe data races if the actor is shared with concurrent contexts, then accessed later during the initializer.  Developers should take care when writing such initializers to avoid these data races.  This does not apply to initializers for non-actor types, non-async initializers, initializers that do not delegate to other initializers, or initializers that are explicitly non-isolated or isolated to a global actor, such as `@MainActor`.  (87485045)
- When a `let` binding inside of a function has a `~Copyable` type, and the initialization occurs after the declaration, then the compiler may either crash or raise a spurious “copy of noncopyable” error diagnostic: ```None
 let x: NonCopyableType
 x = NonCopyableType()
``` (126774469)  Either refactor the code so that the `let` binding is immediately initialized in its declaration, or change the `let` into a `var` binding. ```None
 let x = NonCopyableType()
 
 // or:
 
 var x: NonCopyableType
 x = NonCopyableType()
```
- Calling a consuming method on a noncopyable existential (boxed protocol type) emits an error saying “usage of a noncopyable type that compiler can’t verify”  (128696001)
- In functions that are isolated to an optional actor reference, the Swift compiler does not currently understand that accesses to `actor!` and `actor?` are also isolated as described in SE-0420.  (133095873)
- The closure passed to Task.init and Task.detached was changed from @Sendable to sending. As a result, the compiler no longer tells the programmer exactly which captured values create the potential for a data-race, making it difficult to determine how to fix this error. Instead the compiler prints out that the closure is a ‘task-isolated’ value without describing that the closure is ‘task-isolated’ since one of the variables that closure captures may still be used by code in the task where the closure is formed.  (133798044)
- Designed for iPad apps built without compiler optimizations enabled may crash when run on versions of macOS before 15.0 if the app directly uses Swift Standard Library APIs related to `CheckedContinuation`, `TaskGroup`, `ThrowingTaskGroup`, and `TaskLocal`.  (134793410)

##### Swift Packages

###### New Features

- Privacy manifests are automatically included as a copied resource for packages with tools version >= 6.0.  (111119227)
- The current Git commit, tag, and whether there are any uncommitted changes is available through a new `Context.gitInformation` API (see `GitInformation`).  (111523616)
- The user module version of Swift package targets is now set based on the package’s semantic version when building in Xcode, allowing use of `#if canImport(moduleName, _version: <version>)` expressions within Swift code.  (113513935)
- `swift test` now supports running tests written using Swift Testing. To enable these tests at the command line, pass `--enable-swift-testing`.  (114997435)
- Swift Testing is enabled by default in `swift build` and `swift test`. It can be explicitly disabled with `--disable-swift-testing.`  (120864035)
- `swiftLanguageVersion` can be specified at the target level, allowing for gradual per-target migration to the Swift 6 language mode.  (125732014)
- [`SE-0301`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0301-package-editing-commands.md) has been implemented, allowing `Package.swift` to be edited through new package commands `add-dependency`, `add-product`, and `add-target`. See `swift package <command> -h` for more details.  (126377239)
- `swiftLanguageVersions` and the new `swiftLanguageVersion` setting have been renamed to `swiftLanguageModes` and `swiftLanguageMode` respectively as per [`SE-0441`](https://developer.apple.comhttps://github.com/swiftlang/swift-evolution/blob/main/proposals/0441-formalize-language-mode-terminology.md).  (132484168)

###### Resolved Issues

- Fixed: Files generated by plugins are available in plugins run at later stages through two new APIs on `SourceModuleTarget` - `pluginGeneratedSources` and `pluginGeneratedResources`.  (103808529)
- Fixed: Swift packages containing macros will fail to build when cross-compiling with `swift build --swift-sdk`  (105991372)
- Fixed: It is now possible to specify resources outside of a target’s source in its listed resource paths.  (119040426)
- Fixed an issue where Swift package targets built as frameworks could generate invalid bundle identifiers and result in failures when uploading apps to App Store Connect.  (124554622)
- Fixed: Packages using `swift-tools-version: 6.0` did not infer the Swift 6 language mode when compiling within Xcode (or `xcodebuild`).  (130079815) (FB13957723)

##### Templates

###### Resolved Issues

- Fixed: Creating a new tvOS app extension now sets the correct product type in the Xcode project file. In previous releases, the product type could be set incorrectly, which could lead to issues launching the app extension at runtime.  (115338579) (FB13156098)
- Fixed: Widgets for macOS will not be run under the WidgetKit Simulator for testing or debugging on the macOS 15 Beta.  (128987748)

##### Test Report

###### New Features

- The test report displays new metadata “traits” from the Swift Testing framework.  (112429531)
- The test report now displays “failure distribution” insights when multiple tests with the same tag or related bug fail, or if failures align across specific device or test plan configuration axes.  (122047922)
- Test Report now supports filtering by test run status. Depending on repetition policy on Test Plan configuration, number of Test Plan configurations, and test parameterization, tests can be executed multiple times. Different runs of the same test can have different results. The Test Report now allows the user specify both the test status and the test run status in the filter bar.  (127015832)

###### Resolved Issues

- Fixed: Setting a baseline in the test report metrics tab does not save.  (129367944)

##### Testing

###### New Features

- Test Plans now support including or excluding Swift Testing tests and suites. Whenever at least one Swift Testing test or suite is referenced, all test identifiers in the JSON-based document are re-encoded using a new, hierarchical structure.  (71461811)
- The Test Navigator now displays information about the arguments passed to each Swift Testing parameterized test. This information is shown shortly after a Test action is initiated. Selecting an individual set of arguments shows details about them and their sub-values in a source editor gap at the location of that test. Clicking the Run button for a set of arguments causes their associated test to re-run with the selected arguments. (Note: This is supported for arguments which conform to `Codable` or another protocol supported by Swift Testing — see its documentation for more details.)  (91899389)
- Xcode 16 includes Swift Testing, an all-new testing framework built for Swift from the ground up. It includes expressive APIs that make it easy to write and organize tests. It provides detailed output when a test fails using macros like `#expect`. And it scales to large codebases with features like parameterization to easily repeat a test with different arguments. Swift Testing tests are discovered automatically in Xcode 16 and shown in the Test Navigator and source editor where they can be run selectively. Their results are shown in the Test Report and included in .xcresult bundles. Test bundle targets may contain a mixture of Swift Testing tests and XCTests.  (103401672)
- When an expectation such as `#expect` in a Swift Testing test fails, details about the expression and its sub-values are captured automatically. Expanding the failure message and clicking “Show” causes these details to be shown in a source editor gap on the line where the failure occurred.  (117535385)
- The Test Plan editor now support including or excluding Swift Testing tests and suites by tag.  In the top of the Test Plan editor there is a filter field where tags can be added.  There is both an include and exclude field where there is an option to select between including/excluding all or any of the tags in the field for the Test Plan.  All is the default.  (118952285)
- In the test navigator, there is now an ability to filter the outline view’s content for tests that have either been previously executed or never executed  (120959490)
- The Test Plan editor shows a preview of what tests are included or excluded in a Test Plan.  Another column was added for tags associated with a test or suite.  The Test Plan can be filtered by XCTest or Swift Testing and will show on the test row what is causing a test to be excluded by specifying excluded by tag, excluded by a condition in code, or inactive if the check box is off.  There is a count of tests in the Test Plan In the bottom bar and choosing targets has moved from the bottom left to the top right of the editor.  (123704261)
- The test navigator now has the ability to group all of your Swift Testing suites and tests by tag when there is one or more tag applied. In the group by hierarchy mode, tests will appear as they did previously in Xcode 15. In Xcode 16 there is a new section in the outline view that will display all of the Swift Testing tags found in your test plan. In the group by tag mode, tags will appear as child nodes of the currently active test plan. Tagged suites and tests will be organized as child nodes of each tag in the outline view.   (124498440)

###### Resolved Issues

- Fixed: Screen recordings will not be available when running UI tests using a scheme with a space in its name, or when producing an .xcresult bundle with a space in its path.  (122016656)
- Fixed: When using Swift Testing, a test failure that occurs on a detached task or background thread may cause `swift test` to crash.  (122190668)
- Fixed: Swift Testing tests in an extension which is in a separate file from the extended type’s main declaration are now discovered and shown in the Test navigator and source editor correctly.  (123030494)
- Fixed: Missing targets in test plans are automatically removed by Xcode from the test plan file.  (125990965)
- Fixed: If a test target is not set to automatically include new tests, parameterized tests cannot be enabled in the test plan editor.  (126111492)
- Fixed: Testing.framework no longer strips symbol names, so backtraces seen while running Swift Testing tests are easier to interpret.  (128081663)
- Fixed: When opening a Swift package in Xcode, its autogenerated test plan defaults to running tests in serial instead of in parallel even when using Swift Testing.  (128969071)
- Fixed: When running UI tests against watchOS using xcodebuild or in Xcode Cloud, tests may fail with an error message that Accessibility has not loaded.  (129170180)
- Fixed: Workflows using Swift Testing against Mac Catalyst run destinations will crash on macOS 14.X or below.  (133854987)

###### Known Issues

- Using `await confirmation {}` or `await withKnownIssue {}` with an actor-isolated closure fails to compile.  (134375046)  Pass an explicitly `@Sendable` closure to these functions.

##### Textureconverter

###### New Features

- TextureConverter now supports volume textures and 2d texture arrays. Additionally cubemap , volumes textures and 2D texture arrays can now be built from a series of 2d textures using the –build_array,  –build_cubemap & –build_volume options.  (70571617)
- TextureConverter now supports reading and writing OpenEXR texture files.  (85262544)
- Convert mode adds support for converting between uncompressed texture formats.  (120931250)
- Color gamut of textures can be specified with —gamut_in & —gamut_out, with color gamut conversion performed as necessary. Textures saved as KTX or KTX2 files store gamut information as metadata (for KTX 1.1 using the key com.apple.image.colorGamut).  (121144249)
- The AppleTextureConverter API has been refactored to minimise memory usage.  (121388351)

###### Resolved Issues

- Fixed: Linking with the AppleTextureConverter library no longer requires additional libraries to be linked.  (123455882)

###### Deprecations

- Support for PVRTC compressed textures is deprecated in TextureConverter.  (123431036)

##### Virtualization

###### Resolved Issues

- Fixed: When running in a virtualized macOS environment, Apple ID sign-in is not supported in Xcode.  (127624414)

##### Visionos Sdk

###### Resolved Issues

- Fixed: Warnings generated by realitytool print “unknown” instead of the deployment target  (131497951)

##### Widgetkit

###### Resolved Issues

- Fixed: An error building a control template that states “Template request failed: WidgetKit.ChronoError.AppIntent.conversionFailure(underlyingError: AppIntent has missing parameter value for ’timerName’” might occur. Users might need to set a default value in the initializer of @Parameter, or using the default method on Query.  (129066701)
- Fixed: WidgetKit mac target crashes on launch.  (130238387)

##### Xcode

###### Resolved Issues

- Fixed: Adding an asset for a visionOS app icon crashes Xcode, impacts any developer adding new app icons for a visionOS app  (130081736)

##### Xcode Cloud

###### New Features

- The test report displayed in Xcode for Xcode Cloud builds now includes a Coverage node for builds which collect coverage data.  (121216727)

###### Resolved Issues

- Fixed: From the Xcode Cloud tab, any action causing an update to the build results list while it is visible in Xcode Editor crashes Xcode. Such actions include clicking on the “Start Build” button in the top right corner of the list of builds, or viewing the build results list while a build is running in Xcode Editor.  (127102192)

##### Xcode Cloud Package Integration

###### Resolved Issues

- Fixed: In cloud environments, Xcode workspaces that contain a single project with package dependencies would not be able to locate the Package.resolved file. Now, workspaces with a single project will also consider the project’s Package.resolved file.  (124713280) (FB13688344)

##### Xcode Playgrounds

###### Resolved Issues

- Fixed: Playgrounds that use packages may not build.  (132428278)

##### Xcodebuild

###### Resolved Issues

- Fixed an issue where xcodebuild silently selects the first compatible run destination when it fails to match the destination specifier provided by the user.  (112043381)

##### Xcresulttool

###### New Features

- The xcresulttool CLI has introduced new interfaces to streamline the extraction of test and other results data from xcresult bundles.  (118990069)

##### Xctest

###### New Features

- A new API on XCUIElement adds the ability to wait for any property on XCUIElement to become a value given a timeout. Also, `waitForNonExistence` has been added as a new API.  (35419925)
- XCTest has new API for performing a “double tap” hand gesture on Apple Watch from UI tests.  (102866220)

## See Also

- [Xcode 16.4 Release Notes](xcode-16_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 16.3 Release Notes](xcode-16_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 16.2 Release Notes](xcode-16_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 16.1 Release Notes](xcode-16_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-16-release-notes)*