# Xcode 15 Release Notes

**Framework**: Xcode Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

Xcode 15 includes SDKs for iOS 17, iPadOS 17, tvOS 17, watchOS 10, and macOS Sonoma. The Xcode 15 release supports on-device debugging in iOS 12 and later, tvOS 12 and later, and watchOS 4 and later. Xcode 15 requires a Mac running macOS Ventura 13.5 or later.

##### General

###### New Features

- When a structured text-based file such as a property list or storyboard fails to open due to a merge conflict, Xcode will offer to open the file as text.  (9148845)
- The “View by Time” / “View by Group” selector in the Report navigator has moved into the navigator’s action menu.  (73892015)
- The build log reports now show their sections in the jump bar, allowing for quicker navigation and showing the location of the current selection.  (90320021)
- The `xed` tool has been rewritten for performance and reliability. Invoke it from the command line to edit an existing or new file in Xcode, optionally opening to a given line number, and waiting for the file to close.  (105476406)
- The Find navigator now offers additional symbolic queries that act on types, such as Find Ancestor Types and Find Conforming Types. These find operations replace the functionality of the Symbol navigator, and provide a stable set of results that change only when the query is re-executed.  (105622182)
- Xcode 15 validates the signing identity of XCFrameworks that are used in your project. The signature information for an XCFramework is displayed in the File inspector, and the last known identity is saved in the project file. During a build, the signature of XCFrameworks are validated and the signing identity is compared to the expected identity in the project file.  (106036191)
- The new “Quick Actions” panel provides keyboard access to perform commands across Xcode.  (108024215)

###### Resolved Issues

- Fixed: macOS Previews can now be interacted with directly in the canvas. You can press and hold the Live preview mode button to switch between previewing in Xcode and previewing in the app-under-preview.   (49271058)
- Fixed: For apps linked on or after iOS 17 and aligned OS versions, `URL` parsing has updated from the obsolete RFC 1738/1808 parsing to the same RFC 3986 parsing as `URLComponents`. This unifies the parsing behaviors of the `URL` and `URLComponents` APIs. Now, `URL` automatically percent- or IDNA-encodes invalid characters to help create a valid URL. To check if a `urlString` is strictly valid according to the RFC, use the new `URL(string: urlString, encodingInvalidCharacters: false)` initializer. This init leaves all characters as they are and will return `nil` if `urlString` is explicitly invalid.  (93368104)
- Fixed: TypeScript (.ts) files are directly editable in Xcode.  (93525048) (FB10021626)
- Fixed: Swift function declarations across multiple lines are now more reliably pinned by Xcode’s “Show Code Structure While Scrolling” feature.  (94476783) (FB10047088)
- Fixed notifications not displaying for build and test status if the actions complete when Xcode is not the frontmost application.  (105997391)
- Fixed: Console, Safari, and Accessibility Inspector are unable to wirelessly connect to devices running iOS and tvOS 16.4 and 16.5.  (108032308)
- Fixed: Offline compilation targeting AMD hardware and macOS Ventura isn’t available using Xcode 15.  (108372489)
- Fixed: Xcode Organizer window TestFlight Internal Only distribution support isn’t currently available.  (111340185)

###### Known Issues

- Devices running iOS 17 may prompt the user twice in rapid succession to trust a Mac when connected to the Mac with a USB cable. The second prompt for trust may obscure the first prompt and prevent the user from entering the passcode.  (109539668)  To configure the iOS device to trust the Mac, tap “Trust” and enter the device passcode on any passcode screen that isn’t occluded. Disconnect and reconnect the iOS device to the Mac. The iOS device may prompt once more to trust the Mac. To accept, tap “Trust” and enter the device passcode.
- Executing Unit/UI tests from Xcode on the iOS Simulator takes an extended time to launch on first run of the suite. (115187363)  (110330776) (FB12237092)
- Xcode 15 may not be able to communicate with devices running iOS 17+ and tvOS 17+, and Apple Watch devices paired to an iPhone running iOS 17+ with certain VPNs active.  (110337781) (FB12243540)  Disable the VPN to interact with the device and reach out to the VPN vendor for resolution.
- On macOS Sonoma, when attempting to automatically install command line tools (such as after running `xcode-select --install`), you may receive an error that they aren’t currently available.  (110346766)  Install [`Command Line Tools`](https://developer.apple.comhttps://developer.apple.com/download/all/?q=command%20line%20tools) manually or run the following commands in Terminal: ```None
 sudo mkdir -p /Library/Developer/CommandLineTools   
 sudo touch /Library/Developer/CommandLineTools/.beta   
``` and try again.
- Swift macro definitions from the macOS/iOS/tvOS/watchOS SDKs are not available in Swift Playgrounds.  (112122752) (FB12581131)
- The simulator may crash when opening Settings or Action Button settings on iPhone 15 Pro devices.  (115388496)

##### App Intents

###### Resolved Issues

- Fixed: Apps that implement App Intents may fail to compile with watchOS SDK if an App Entity with Entity Query is present.  (111455662)

##### App Shortcuts Preview

###### Known Issues

- If an app adds a new App Shortcuts trigger phrase string that already exists in an accompanying `AppShortcuts.strings` or `AppShortcuts.xcstrings` file, the App Shortcuts Preview may not refresh upon rebuild.  (109494636)  Cleaning prior to rebuilding the app causes App Shortcuts Preview to be in its most up-to-date state.

##### Apple Clang Compiler

###### New Features

- There is a new reference page for C++ support on Apple platforms: [`https://developer.apple.com/xcode/cpp/`](https://developer.apple.comhttps://developer.apple.com/xcode/cpp/).  (100245338) (FB11563150)
- Clang and the build system support a new mode for building module dependencies called explicit modules which improves build performance, reliability, and correctness. The new mode is opt-in, and can be enabled by setting `_EXPERIMENTAL_CLANG_EXPLICIT_MODULES` as a user-defined build setting in C and Objective-C projects which build with modules enabled.  (104438594)
- Wide multi-characters literals such as L’ab’ that would previously be interpreted as L’b’ are now ill-formed in all language modes in C and C++. The motivation for this change is outlined in character literals [`P2362`](https://developer.apple.comhttp://wg21.link/P2362). The following C++20 language features have been implemented: - Immediate functions [consteval] is fully implemented. (P1073R3) The following C++23 language features have been implemented: - De-deprecating volatile compound operations. (P2327R1)
- Support for `#warning`. (P2437R1)
- Delimited escape sequences. (P2290R3)
- Named universal character escapes. (P2071R2)
- Support for UTF-8 as a portable source file encoding. (P2295R6)
- Relax requirements on `wchar_t` to match existing practices. (P2460R2)  (108334479)

###### Resolved Issues

- Fixed: Improvements in the ARC optimizer allow Objective-C and Swift objects to be released earlier. This causes code to misbehave or crash when it relies on weak or unowned references to remain valid without a strong reference to the target object. For example this can happen inadvertently in code that unnecessarily uses a “weak self” capture in a one-shot asynchronous block callback.  (108386578)
- Fixed: The x86 vectorizer uses saturated arithmetic instructions that can result in shorter and faster code. This may change program behavior for applications that implicitly rely on overflow behavior, e.g., by casting floating point values to integer types that can’t represent the original value.  (108386879)

##### Asset Catalogs

###### New Features

- Xcode now generates Swift and Objective-C symbols for each color and image in the asset catalog. These symbols provide a safer, more assistive way to reference assets that’s resilient to renames & typos, leverages compiler type checking, and integrates with code completion. Swift asset symbols are generated in the module associated with a given asset catalog. They’re generated as static properties on the new `ColorResource` and `ImageResource` types. To instantiate colors and images with asset symbols, use the SwiftUI, UIKit, and AppKit initializers that take the resource types. For example: Given an asset catalog with a color “spaceGray” and image “appleLogo,” instantiate the color symbol `ColorResource.spaceGray` with `Color(.spaceGray)`, `UIColor(resource: .spaceGray)`, and `NSColor(resource: .spaceGray)`, and the image symbol `ImageResource.appleLogo` with `Image(.appleLogo)`, `UIImage(resource: .appleLogo)`, and `NSImage(resource: .appleLogo)`. With the opt-in build setting “Generate Swift Asset Symbol Extensions” (`ASSETCATALOG_COMPILER_GENERATE_SWIFT_ASSET_SYMBOL_EXTENSIONS`) set to `YES`, asset catalog colors and images can be accessed directly on system color and image types, e.g. `Color.spaceGray`, `UIColor.spaceGray`, `NSColor.spaceGray`, `UIImage.appleLogo`, and `NSImage.appleLogo`. Objective-C asset symbols are provided as string constants and can be accessed by importing the “GeneratedAssetSymbols.h” header. Asset symbol generation is enabled by default but can be disabled by setting the build setting “Generate Asset Symbols” (`ASSETCATALOG_COMPILER_GENERATE_ASSET_SYMBOLS`) to `NO`. Symbols support is generated for SwiftUI, UIKit, and AppKit by default. This can be customized if required by setting the build setting “Generate Swift Asset Symbol Framework Support” (`ASSETCATALOG_COMPILER_GENERATE_ASSET_SYMBOL_FRAMEWORKS`) to a smaller set of frameworks, e.g. “UIKit AppKit” or “AppKit.”  (14758734)
- Asset Catalog automatically infers a single scale slot when adding PDF images.  (32661471) (FB5752517)
- Asset catalog color inspectors remember the last used color configuration when creating new colors.  (48965482) (FB5697990)

###### Resolved Issues

- Fixed: Jump-to-definition on an asset symbol now jumps to the asset in the catalog.  (102385742)
- Fixed: The “Add New Asset” menu now has a “Folder with Namespace” item for creating new folders with namespaces.  (108468310)
- Fixed: Asset symbols are now generated for assets in Swift packages.  (110083791)

##### Build System

###### New Features

- Archive builds now support the same set of eager compilation optimizations as other build actions, improving build performance.   (98526053)
- Xcode now automatically generates intermediate text-based dynamic library (TBD) files for dynamic libraries and frameworks in your project. These stubs allow linker dependencies to be tracked more accurately, meaning changes which don’t change the set of exported symbols no longer require all transitive dependencies to relink, speeding up incremental builds.   (99972271)
- Xcode now supports building and consuming macros defined in Swift Packages.   (101818756)
- XCFrameworks can be created from mergeable libraries and frameworks and will be merged or have mergeable metadata removed as appropriate when they are used. See the documentation [`Configuring your project to use mergeable libraries`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/configuring-your-project-to-use-mergeable-libraries).  (109124251)

###### Resolved Issues

- Fixed: Embedding a static framework using a Copy Files build phase now removes the static archive from the framework when it is embedded in the target bundle. The `REMOVE_STATIC_EXECUTABLES_FROM_EMBEDDED_BUNDLES` build setting can be set to `NO` to opt out of this behavior. The `COPY_RESOURCES_FROM_STATIC_FRAMEWORKS` build setting, previously used in the legacy build system to extract and copy the resources from a static framework to the target bundle, no longer has any effect with the new build system as the entire framework is copied instead (minus the static archive as described above).  (47164939)
- Fixed: Xcode now tracks dependencies on additional files specified by various linker flags specified in the `OTHER_LDFLAGS` build setting. In some cases this may require build setting flags to be adjusted to become SDK-relative. For example, instead of: ```None
 OTHER_LDFLAGS = $(inherited) -weak_library /usr/lib/swift/libswiftAppleArchive.dylib
``` You must use: ```None
 OTHER_LDFLAGS = $(inherited) -weak_library $(SDKROOT)/usr/lib/swift/libswiftAppleArchive.tbd
``` In other cases where the files referenced by linker flags may be produced by another build task, such as a build rule or shell script build phase, ensure that the file is explicitly listed as an output file of that build rule or shell script build phase.  (92049062)
- Fixed an issue where build warnings in Swift files sometimes disappeared after an incremental build.   (105421512)
- Fixed: If Xcode isn’t used to generate your content for App Store submission, the `Signatures` folder from your `xcarchive` will need to be added sidecar content.  (106438176)
- Fixed: Using single-file build actions such as Preprocess or Assemble now works correctly when used on files with an overridden File Type. Previously, this may have produced a “missing input and no rule to build it” error.  (107736241) (FB12102123)
- Fixed an issue where localization export of dependent frameworks could fail after running a regular build of the project.   (108867135) (FB12165312)

###### Deprecations

- Bitcode support has been removed, and the `ENABLE_BITCODE` build setting no longer has any effect.  (105281961)

##### C++ Standard Library

###### New Features

- The following new features have been implemented: - Implemented the C++17 `<memory_resource>` library
- P2499R0 - `string_view` range constructor should be `explicit`
- P2417R2 - A more constexpr bitset
- P2445R1 - `std::forward_like`
- P2273R3 - Making `std::unique_ptr` constexpr
- P0591R4 - Utility functions to implement uses-allocator construction
- P2291R3 - Add constexpr modifiers to functions `to_chars` and `from_chars` for integral types in `<charconv>` header
- P0220R1 - Adopt Library Fundamentals V1 TS Components for C++17
- P0482R6 - `char8_t`: A type for UTF-8 characters and strings
- P2438R2 - `std::string::substr() &&`
- P0600R1 - `nodiscard` in the library
- P0339R6 - `polymorphic_allocator<>` as a vocabulary type
- P1169R4 - Implemented the library parts of `static operator()`
- P0415R1 - `constexpr` for `std::complex`
- P1208R6 - `std::source_location`
- P0323R12 - `std::expected`
- P1035R7 - Input Range Adaptors
- P2325R3 - Views shouldn’t be required to be default constructible
- P2446R2 - `views::as_rvalue`
- P1020R1 - Smart pointer creation with default initialization
- P2210R2 - Superior String Splitting
- The `ranges` versions of `copy`, `move`, `copy_backward` and `move_backward` are now also optimized for `std::deque<>::iterator`, which can lead to up to 20x performance improvements on certain algorithms.
- The `std` and `ranges` versions of `copy`, `move`, `copy_backward` and `move_backward` are now also optimized for `join_view::iterator`, which can lead to up to 20x performance improvements on certain combinations of iterators and algorithms.  (108380402)

###### Deprecations

- The following items have been deprecated or removed: - `unary_function` and `binary_function` are no longer provided in C++17 and newer Standard modes. They can be re-enabled with `_LIBCPP_ENABLE_CXX17_REMOVED_UNARY_BINARY_FUNCTION`.
- Several incidental transitive includes have been removed from libc++. Those includes are removed based on the language version used. If you see errors related to missing `std::` entities in your code after upgrading, ensure you have all required includes.
- The functions `to_chars` and `from_chars` for integral types are only available starting with C++17. Libc++ offered these functions in C++11 and C++14 as an undocumented extension. This extension makes it hard to implement the C++23 paper that makes these functions `constexpr`, therefore the extension has been removed.
- The `_LIBCPP_ENABLE_CXX03_FUNCTION` macro that allowed re-enabling the now-deprecated C++03 implementation of `std::function` has been removed. Users who need to use `std::function` should switch to C++11 and above.
- The contents of `<experimental/memory_resource>` are now deprecated since libc++ ships `<memory_resource>` now. Please migrate to `<memory_resource>` instead. Per libc++’s TS deprecation policy, `<experimental/memory_resource>` will be removed in the next release.
- The base template for `std::char_traits` has been marked as deprecated and will be removed in the next release. If you are using `std::char_traits` with types other than `char`, `wchar_t`, `char8_t`, `char16_t`, `char32_t` or a custom character type for which you specialized `std::char_traits`, your code will stop working when we remove the base template. The Standard doesn’t mandate that a base template is provided, and such a base template is bound to be incorrect for some types, which could currently cause unexpected behavior while going undetected.
- `_LIBCPP_ENABLE_NODISCARD` and `_LIBCPP_DISABLE_NODISCARD_AFTER_CXX17` are no longer respected. Any standards-required `[[nodiscard]]` applications in C++20 are now always enabled. Any extended applications are now enabled by default and can be disabled by defining `_LIBCPP_DISABLE_NODISCARD_EXT`.
- In freestanding mode, `atomic<small enum class>` doesn’t contain a lock byte anymore if the platform can implement lockfree atomics for that size. This ABI break only affects users that compile with `-ffreestanding`, and only for `atomic<T>` where `T` is a non-builtin type that could be lockfree on the platform.  (108380359)

##### Console

###### New Features

- By default, Xcode streams `os_logs` through the unified logging and activity tracing infrastructure. The output may be formatted differently compared to previous versions of Xcode, and its order relative to standard IO may also change. To customize the behavior of logging, edit the Run scheme action to set the environment variable `IDELogRedirectionPolicy`. The value “oslogToStdio” redirects `os_log` messages to standard IO and formats them in a style identical to previous versions of Xcode. The value stdioToOSLog redirects standard IO to the `os_log` messages, and presents them in the debug console with additional metadata.  (109380695)

###### Resolved Issues

- Fixed: The debug console’s action to jump from an `os_log` message to the line of source code which emitted it is only supported when debugging executables on the local Mac or Simulators. The menu item is disabled when debugging executables on connected devices.  (109171925)
- The maximum permitted size of `os_log` messages shown in the debug console is smaller than in previous Xcode versions. This may cause long messages to more commonly appear truncated in the debug console.  (109381234)

##### Create Ml

###### Resolved Issues

- Fixed: With the new macOS Seed 1 build of macOS Sonoma, users of the CreateML app from Developer Tools inside Xcode can’t train machine learning models using hand action classifier and hand pose classifier. The specific error message is Unexpected Error when Train button is clicked.  (108227967)

##### Debugging

###### New Features

- LLDB now omits defaulted template arguments in type summaries. For example, ```None
 (lldb) frame variable
 (std::vector<std::vector<std::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::basic_string<char, std::char_traits<char>, std::allocator<char> > > >, std::allocator<std::vector<std::basic_string<char, std::char_traits<char>, std::allocator<char> >, std::allocator<std::basic_string<char, std::char_traits<char>, std::allocator <char> > > > > >) nested = size=0 {}
``` will now display as: ```None
 (lldb) frame variable
 (std::vector<std::vector<std::string> >) nested = size=0 {}
``` One can still see the default arguments by using the `frame variable --raw-output` option.  (101329922)
- LLDB now supports referring to generic type parameters in expression evaluation. For example, given the following code: ```None
 func use<T>(_ t: T) { 
   print(t) // Break here 
 }
  
 use(5)
 use("Hello!”)
``` Running `po T.self`, when stopped in `use`, will print `Int` in the first call, and `String` in the second. This can be especially useful in combination with conditional breakpoints to stop only when a generic function is instantiated with a certain concrete type. For example, adding the following expression as the condition to a breakpoint inside use will only stop when the variable `t` is a `String: T.self == String.self`.  (101976441)
- The `p` and `po` command aliases have been redefined to the new `dwim-print` command. The `dwim-print` command prints values using the most user friendly implementation. “DWIM” is an acronym for “Do What I Mean”. Specifically, when printing variables, `dwim-print` will use the same implementation as `frame variable` or `v`. The output of `p` no longer includes a persistent result variable, such as `$0`, `$R0`, etc. Users who want persistent results on occasion, can use `expression` (or a unique prefix such as `expr`) directly instead of `p`. To enable persistent results every time, the `p` alias can be redefined in the `~/.lldbinit` file: ```None
 command unalias p
 command alias p dwim-print --persistent-result on --
``` The `dwim-print` also gives `po` new functionality. The `po` command can now print Swift objects by their address. When running `po <object-address>`, the embedded Swift compiler will instead evaluate the expression `unsafeBitCast(<object-address>, to: AnyObject.self)`.  (104348863)
- Xcode now shows AppKit runtime issues. Some examples are auto-layout constraint issues for constraints constructed in code.  (105229806)
- When you create a watchpoint, you can see its ancestry path hierarchy. This gives you better context, especially in case of conflicts.  (106777931)

###### Resolved Issues

- Fixed: Xcode stops showing you zombie processes when you’re trying to attach from the menu. It was previously confusing and cumbersome to sieve through these non-debuggable processes for the actual process to debug. This works for all platforms.  (11113209)
- Fixed: External Swift macros can’t be invoked from the LLDB expression evaluator.  (109854291)

##### Devicediscoveryui

###### Resolved Issues

- Fixed: DeviceDiscoveryUI isn’t available when building for tvOS Simulator.  (109224355)

##### Devices

###### Resolved Issues

- Fixed: Devices running iOS 17 don’t support specifying a Routing App Coverage File for Apps launched from Xcode 15.  (80105713)
- Fixed: Apple Watch simulators now appear as standalone simulators in the Devices and Simulators Window.  (106664675)
- Fixed: Xcode requires an internet connection to prepare a device running iOS 17, watchOS 10, or tvOS 17 for development. When preparation for development fails due to the lack of an internet connection, Xcode doesn’t automatically retry preparing the device for development.  (109511717)
- Fixed: Xcode 15 is unable to connect wirelessly for development with devices running iOS and tvOS versions older than 16.0.  (113153131)

###### Known Issues

- The Xcode Devices and Simulators Window doesn’t accurately reflect the color of devices connected to the Mac.  (98003308)
- Xcode doesn’t automatically refresh the name of a device running iOS 17, watchOS 10, or tvOS 17 when the user renames the device from the Settings app.  (98406919)  Quit and restart Xcode.
- Xcode’s Devices and Simulators Window doesn’t display icons for applications installed on devices running iOS 17, watchOS 10, and tvOS 17.  (108568165)
- When Xcode is wirelessly connected to a device running iOS 17, Xcode doesn’t automatically switch to using the fastest connection when the device is connected to the Mac using a USB cable. If the wireless connection is slower than the USB connection, Xcode may continue to communicate with the device using the wireless connection.  (109466074)  Disable and re-enable WiFi on the Mac to interrupt the wireless connection. Xcode automatically reconnects to the device over USB.
- The Xcode Devices and Simulators Window allows users to click on the “Take Screenshot” button when targeting devices that do not support the screenshot capability. When the button is clicked in this circumstance, Xcode hangs.  (110086301)
- When an Apple TV is wirelessly paired to more than one device,  Xcode’s Device and Simulator Window will show the status of the Apple TV go into a “Preparing for development” loop.  (112046227)  Pair the Apple TV to one device at a time to prevent seeing the status in a loop
- When plugging in a iPhone paired to an Apple Watch, the Apple Watch may not appear in Xcode’s Device and Simulator Window  (114714784)  Restart and replug the iPhone

##### Documentation

###### New Features

- Xcode 15 now includes an assistant editor that provides a real-time preview of your Swift-DocC documentation as you type. You can access Documentation Preview by first activating the assistant editor via Editor > Assistant, and then selecting “Documentation Preview” in the assistant editor’s jump bar. The assistant editor is supported in Swift files, Objective-C header files, and documentation markup files.  (56250383)
- Documentation built with Xcode 15 now includes pages for Swift extensions to external modules. For example, you might extend SwiftUI’s Image struct to include an additional initializer: ```swift
 public extension Image {
    /// Create an image from the given sloth.
    ///
    /// This initializer is useful for displaying static sloth
    /// images. To create an interactive view containing a sloth,
    /// use ``SlothView``.
    ///
    /// ![A screenshot of an ice sloth, with the text Ice Sloth underneath.](iceSloth)
    init(_ sloth: Sloth) {
       self.init("\(sloth.power)-sloth")
    }
 }
``` The documentation for this initializer will now be included alongside the rest of the documentation for your project. If you would prefer to exclude these pages, set the `DOCC_EXTRACT_EXTENSION_SYMBOLS` build setting to `NO`. See the [`build settings reference`](https://developer.apple.comhttp://developer.apple.com/documentation/xcode/build-settings-reference) for details.  (63987302)
- To support easier migration from other documentation tools, some basic Doxygen-style commands like `@param` and `@returns` are now supported in Swift-DocC.  (69835334)
- Diagnostics for documentation links now include details about why the link failed and offer suggestions for how to update the link to refer to a known symbol.  (73903936)
- Swift-DocC now supports designing pages with fully custom layouts by utilizing new directives like `@Row`, `@TabNavigator`, `@Links`, and `@Metadata`. To learn more, see the [`API Documentation`](https://developer.apple.comhttps://developer.apple.com/documentation/docc/api-reference-syntax).  (97705029)
- Swift-DocC websites built with Xcode 15 now include a quick navigation feature that allows you to navigate directly to a page just by activating a keyboard shortcut and typing the page’s name. Press Shift+Cmd+O or Shift+/ while browsing a Swift-DocC website to activate the new quick navigation popover.  (100346089)

###### Resolved Issues

- Fixed: Swift-DocC now correctly allows you to customize the title of an API link using markdown’s link syntax. ```md
 SlothCreator includes a number of [different sloth foods](doc:Sloth/Food) that you can feed to your virtual sloths.
``` (79992417)
- Fixed: Documentation links to symbols with unicode characters in the symbol name fail to resolve.  (85531439) (FB9766665)
- Fixed: Documentation links to symbols from protocol requirements need to be disambiguated to distinguish them from a possible default implementation.  (98781530) (FB11291552)
- Fixed: Xcode crashes on macOS Sonoma Beta 1 and Beta 2 when scrolling documentation in Quick Help, the documentation window, and the Swift Package dependency manager.  (109810157)

###### Known Issues

- Xcode documentation includes some sample code projects that require macOS Sonoma to run.  (114836179)

##### Indexing

###### Resolved Issues

- Fixed: Enabling “Build Libraries for Distribution” for a target no longer significantly slows down the indexing of its files  (111703158)

##### Instruments

###### New Features

- Instruments now allows for opening `.memgraph` files in the Allocations, Leaks and VM Tracker Instruments and visualizing timeline of live allocations if Malloc Stack Logging was enabled for the process. Xcode Memory Graph debugger features a new share button to view captured `.memgraph` file in Instruments.  (53014738)
- Instruments 15 includes a new RealityKit Trace template. This template contains several new instruments for profiling apps and games on visionOS. The RealityKit Frames instrument will visualize the different stages of rendering a frame. RealityKit Metrics detects bottlenecks across the rendering stack and provides recommendations and key metrics to diagnose and eliminate rendering bottlenecks. These key metrics include CoreAnimation statistics, 3D Rendering Statistics, RealityKit Systems CPU time, System Power Impact, and much more.  (104091516)
- Instruments 15 includes a new dyld Activity Instrument which visualizes `dlopen`, `dlclose`, static initializers and other dyld statistics relevant for application launch profiling. dyld Activity is included in the App Launch template and replaces Static Initializer Instrument.   (106383871)
- Instruments 15 includes a new Audio System Trace template, providing a comprehensive view of the audio and operating systems. It visualizes how your application interacts with the audio server, giving you insight into Audio Thread I/O Cycles and other general performance metrics.  (106843172)

###### Resolved Issues

- Fixed: Significantly improved the performance of opening new documents with complex templates like Game Performance, System Trace and Metal System Trace.  (72983621)
- Fixed an issue where an application would hang when selecting a HTTP transaction containing a large request or response body in the HTTP Traffic Instrument.  (87893253) (FB9854651)

##### Interface Builder

###### New Features

- The Cocoa storyboard Popover presentation segues support a full size content inspector property that allows the presented content to push beyond the safe area insets and past the arrow region of the popover.  (102107829)
- `NSView` supports a Clips Bounds property inspector for finer control on whether the view’s contents should be clipped.  (104581720)

###### Resolved Issues

- Fixed: Text views, Text fields and Labels support additional text Content Types in the inspector to classify the data for birthdate, credit card, address, names, and more.  (102866350)
- Fixed an issue so that the `NSToolbarItem` position centered inspector previews and persists to runtime correctly.  (105597623)
- Fixed a compilation issue with some iOS storyboards that are marked with a target runtime of “iOS.CocoaTouch.iPad.”  (111328594) (FB12453705)

###### Known Issues

- Interface Builder documents using custom App fonts may load incorrect font at runtime.  (113624207) (FB12903371)  Set font manually in code.

##### Linking

###### New Features

- A new linker has been written to significantly speed up static linking.  It’s the default for all macOS, iOS, tvOS and visionOS binaries and anyone using the “Mergeable Libraries” feature.  The classic linker can still be explicitly requested using -ld64, and will be removed in a future release.   (108915312)

###### Known Issues

- Binaries using symbols with a weak definition crash at runtime on iOS 14/macOS 12 or older. This impacts primarily C++ projects due to their extensive use of weak symbols.  (114813650) (FB13097713)  Bump the minimum deployment target to iOS 15, macOS 12, watchOS 8 or tvOS 15, or add `-Wl,-ld_classic` to the `OTHER_LDFLAGS` build setting.
- Weak symbol imports are linked as non-weak imports, when used from LTO object files.  (115521975) (FB13171424)  Add `-Wl,-weak_reference_mismatches,weak` or `-Wl,-ld_classic` options to the `OTHER_LDFLAGS` build setting.

##### Localization

###### New Features

- String Catalogs (`.xcstrings`) are a new file type in Xcode that make it easy to localize your app by managing strings and keeping track of translation progress. Xcode automatically extracts localizable strings from source code to keep any String Catalogs in sync. String Catalogs can be viewed and edited in a native editor to preview and manage the localized strings in your project. To get started, add a new String Catalog via the File Chooser or migrate existing `.strings` and `.stringsdict` files by choosing Edit > Convert > To String Catalog… in the Menu Bar.  (67254382)
- The Localization Catalog Editor now displays the translation status of strings when viewing and editing exported strings (for files where this information is available).  (79101944)
- Xcode now gives you more flexibility when localizing App Intents phrases. You can now add or remove phrases in `AppShortcuts.xcstrings` independently in each locale using the String Catalog editor.  (97283450)
- Exporting localizations from a Swift Package target will now prefer to generate string tables in the String Catalog format for targets that already contain at least one String Catalog.  (106170507)

###### Resolved Issues

- Fixed: Xcode now gives you the option to unlocalize a resource when removing all localizations from a localizable file in the File Inspector.  (11795220)
- Fixed an issue where there was no way to add a new localization when exporting localizations in a Swift package. New localizations can now be added using the String Catalog editor.  (92296781)
- Fixed: Xcode now builds multi-platform targets on all platforms when exporting localizations.  (99457038)
- Fixed: Using the return and tab keys in the String Catalog editor will now move focus to the next text field. Use option (⌥) to enter newlines and tab characters.  (107203366)
- Fixed: The build system will now consistently produce an error if a String Catalog coexists with .strings or .stringsdict files of the same name, within the same target.  (108866595)
- Fixed an issue where importing a Localization Catalog with translated strings from a String Catalog would not add the appropriate supported languages to the project.  (109236378)
- Fixed: Migrating InfoPlist.strings to InfoPlist.xcstrings now prefers to keep comments from the original .strings file when present.  (110333696) (FB12242621)

##### Metal

###### Resolved Issues

- Fixed: Xcode’s GPU debugging service automatically tries to connect to all devices running iOS 17, watchOS 10, and tvOS 17 that have been discovered in the local area network. If the device trusts the Mac, it accepts the connection and may drain its battery at a faster rate than normal for a sleeping device.  (108682066)

##### Metal Debugger

###### New Features

- The Geometry Viewer and Shader Debugger are now available for Mesh and Object render stages. Bound resources now supports filtering by shader access for Mesh pipelines.  (81698727)
- The Metal Debugger has been updated with improved support for MetalFX. You can easily navigate to your MetalFX calls, see the bound resources, and compare the input and output results. The dependencies viewer has also been updated so that you can see where your input dependencies are coming from and even see how long it takes to complete the upscaling work.  (101047483)
- The Buffer Viewer has been updated with new features, improved user interface, and performance improvements. New features include data search, column pinning, column filtering, and type casting.  (101241716)

##### Organizer

###### New Features

- Some crashes that were the result of a Foundation exception have their exception reason displayed in the Organizer. If there is an exception reason, it’s displayed in the inspector to the right of the backtrace view.  (103453197)

##### Particle Emitters

###### Resolved Issues

- Fixed: Adding a particle emitter or loading a particle emitter in Reality Composer Pro can result in a crash on an Intel-based Mac.  (110794948)
- Fixed: The particle emitter property called `simulationSpace` has been renamed to `particlesInheritTransform`, with possible values changing from `.global`/`.local` to `false`/`true`.  (111411344)

##### Playgrounds

###### New Features

- The Playgrounds console uses Xcode 15’s new console and gains features such as inline find.  (42891656) (FB5398496)
- The result sidebar in Xcode Playgrounds shows summaries for all expressions on the line, and a new control allows you to see a popover with details about each expression.  (105740414)
- The Playgrounds Map template has been updated to use modern MapKit API.  (107284909)

###### Resolved Issues

- Fixed: The result sidebar in Xcode Playgrounds always shows a summary of the most recent result instead of the number of results.  (105108520)
- Fixed: Selecting an inline result in Xcode Playgrounds highlights the source code that produced the result.  (105426026)
- Fixed: SwiftUI spring animations now have a dedicated visualization result.  (106978230)
- Fixed: Inline results can’t be added from the results sidebar.  (111376539)
- Fixed: macOS Playgrounds may fail to launch on some macOS Sonoma configurations in Xcode 15.0.  (111478555)

##### Previews

###### New Features

- The preview canvas has a new control for picking which device to use for previewing. By default it tracks the device family of the selected run destination, but a specific device can be selected. This should be used in favor of the `previewDevice` modifier.  (100562366)
- Previews can now be created with the `#Preview` macro. This includes support for previewing SwiftUI, `UIView` & `UIViewController`, `NSView` & `NSViewController`, and widget timeline providers, timeline entries, and live activities.  (101566716)
- macOS previews now show window chrome and toolbars in the canvas.  (105705642)
- Selecting a device connected to your Mac for previewing now previews exclusively for that device. The selection mode and variants mode now also use the connected device for rendering content to show in Xcode.  (106208191)
- Right clicking on a `PreviewProvider` in the source editor now offers an action to automatically convert it to the new #Preview API.  (107319323)
- The `#Preview` can now be used in projects with deployment targets prior to iOS 17 and macOS 14. Usages of `#Preview` for SwiftUI can also be previewed on OS versions earlier than iOS 17 and macOS 14 by adding `@available(iOS 16.0, macOS 13.0, *)` to the `#Preview` (or whichever version you’d like to preview). Usages of `#Preview` for UIKit & AppKit views and view controllers, and for widgets can’t be previewed on OS versions prior to iOS 17 and macOS 14.  (110676526)

###### Resolved Issues

- Fixed: Previews failed when renaming or deleting the actively edited file.  (62916700)
- Fixed: Previews failed when using `@objc` annotations on certain types.  (96018813)
- Fixed: Canvas settings such as canvas mode, device settings, and the selected preview device are maintained when navigating files.  (100999447)
- Fixed: Index of pinned preview is lost when navigating files.  (106986986)
- Fixed: Projects could take several minutes to open the Previews canvas after updating the project on disk.  (107974497)
- Fixed: Previews can crash when running on iOS 14.x and earlier devices.  (108129587) (FB12125687)
- Fixed: Previews failed when pinning and navigating to a file not in the same target as the pinned preview.  (108738163)
- Fixed: Previews failed when using `@objc` annotations on some types.   (108892859)
- Fixed: Timeline entries in the preview canvas did not update when navigating files.  (109223294)
- Fixed: Previews failed when syncing StoreKit configuration files in watchOS apps.  (109238974)
- Fixed: `#Preview` instances that return a `UIViewController` and `NSViewController` properly follow or do not follow the safe area.  (109281049)
- Fixed: Previews did not refresh the device picker in the canvas when connecting new devices to your Mac.  (109661791)
- Fixed: New Widget projects created on macOS 13 fail to build.  (109897205)
- Fixed: Using the #Preview syntax failed when the project defined local types for `View` and `Preview`.  (110290974)
- Fixed: Previews failed when using #Preview in a project that did not import SwiftUI but had types named the same as some SwiftUI types.  (110584929) (FB12304442)
- Fixed: `#Preview` can’t reference symbols in Swift type extensions when they’re defined in the same module as the Preview.  (110671628)
- Fixed: Closing a project after previewing for macOS would keep multiple instances of the app under preview running.  (110743090)
- Fixed: Previews can fail when editing in files with functions marked `@nonobjc`.  (111355441) (FB12457473)
- Fixed: Previews content for macOS can shrink to zero size when previewed on a secondary display.  (111533438)
- Previewing view code in a SwiftData app results in a linker failure for the canvas despite that code compiling successfully for device and simulator.  (111657477)
- Fixed: On-devices previews can fail when first plugging in devices.  (111712368)
- Fixed: Previews can fail when editing in files using the new Swift syntax for switch and if/else expressions.  (111819050) (FB12528170)
- Fixed: Previews can fail when navigating between a file previewed in a widget and a file previewed in an app target.  (111874103)
- Fixed: Previewing a view inside of a Swift Package or framework fails.  (113143384)

###### Known Issues

- Previews can fail when previewing files in a widget shared by both a watchOS app and an iOS app.  (108017929)
- After loading a LiveActivity preview and making a code change, Xcode will get in a state where all previews time out across any project.  (111934738)  Restart Xcode.
- AppKit previews in projects that have a deployment target less than macOS 14.0 will fail to compile.  (113047811)  Add a `@available(macOS 14.0, *)` annotation to the `#Preview`.

##### Reality Composer

###### Deprecations

- Starting in Xcode 15, Reality Composer for macOS is no longer included, but remains available for iOS and iPadOS on the App Store. Reality Composer Pro will be available in a future release.  (114833716)

##### Realitykit

###### Resolved Issues

- Fixed: Some 3D models loaded with `model3D` or `ModelEntity(named:)` and make use of MaterialX may take longer or fail entirely to load.  (111301582)

##### Sanitizers

###### Resolved Issues

- Fixed: Programs built with Address Sanitizer will hang on launch on Intel-based Macs.  (111288234)

##### Shazamkit

###### Resolved Issues

- Fixed: `SHManagedSession` doesn’t work on simulator.  (109672477)

##### Signing Distribution

###### Known Issues

- Xcode may crash if you encounter an error while notarizing your app.  (115425915) (FB13163393)  You may need to sign a new Program License Agreement in your account at [`https://developer.apple.com/`](https://developer.apple.comhttps://developer.apple.com/) account. If that does not resolve the issue, you can also notarize with an older version of Xcode or using the `notarytool` command line utility.

##### Signing and Distribution

###### New Features

- The Archive action is now available when the simulator run destination is selected. Building an archive with the simulator selected produces an app with all the CPU architectures for the devices on the selected platform.  (13094592)
- The Xcode Signing & Capabilities tab in the project editor now supports adding [`Apple approved managed capabilities`](https://developer.apple.comhttps://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities) that are associated with your development team and App ID. Associated managed Capabilities are visible in the Library and work with automatic signing.  (27253063) (FB5468762)
- `xcodebuild -exportArchive` supports using App Store Connect authentication keys to upload apps to App Store Connect and the Apple notary service.  (76036452)
- Xcode now delivers app upload status push notifications to the person who uploaded to App Store Connect.  (100033585)
- Xcode Organizer window now supports streamlined archive distribution. Uploading or exporting an archive can now be accomplished with one click. Streamlined distribution methods use recommended settings. The custom method allows selection of other options.  (103967573)

###### Resolved Issues

- Fixed: If your app integrates with Game Center, make sure that the `com.apple.developer.game-center` entitlement is present in your `Entitlements.plist` file. Previous Xcode versions automatically injected the entitlement into your app’s signature if it was present in your provisioning profile. That behavior was inconsistent with most other entitlements, and has been removed in Xcode 15.  (106596235)
- Fixed: Resolved an issue where the “Manage version and build number” distribution option in Xcode and Xcode Cloud overwrote the version and build number of framework dependencies in apps. When distributing an app, framework dependencies retain their original version and build numbers.  (106869375)
- Fixed: Automatic signing may fail to create a provisioning profile for DriverKit Driver targets.   (109588156)
- Fixed: When uploading using the streamlined distribution workflow the optionally exported ExportOptions.plist is missing destination key/value.  (114233867)

###### Known Issues

- Streamlined distribution methods in the Xcode Organizer window don’t support all the same error recovery options available when using the custom workflow. For example: if uploading an app without an app record, using streamlined distribution, Xcode shows an error rather than allowing you to create an app record.   (109097705)  Use the custom method.

##### Simulator

###### Resolved Issues

- Fixed: The simulator application running on macOS 14 beta 1 may crash if a game controller is connected.  (110038857)

###### Known Issues

- Status bar overrides may be set incorrectly when using the iOS 14 or later simulator runtime.  (101511614) (FB11716688)
- Simulator doesn’t support all features of Spatial Audio. You can use Simulator to test a subset of audio features; however, final testing should be performed on device.  (109912117)

##### Source Control

###### New Features

- Source Control operations and Xcode Cloud operations have been moved into a new combined “Integrate” menu replacing the “Source Control” menu.  (105752873)
- Xcode now fully integrates with git’s staging features and committing code is now performed in a non-modal fashion.  (107490188)

###### Resolved Issues

- Fixed an issue that could erroneously insert additional apostrophes when reviewing pull requests.  (107586336)
- Fixed: Upstream changes may be displayed as staged changes in the Xcode editor.  (109285038)
- Fixed an issue which may cause git credential helper keychain items to be deleted.  (109411746) (FB12190300)

###### Known Issues

- In-line Code Review Mode does not show when “Show Source Control Changes” is disabled in Xcode Settings.  (114499800)  Use Side-by-Side Mode instead.

###### Deprecations

- Xcode 15 no longer includes Xcode Server. Xcode Cloud is the best way to get automated build/test/deploy workflows for your code changes. The `xcodebuild` tool is also available for custom automation needs.  (99606507)

##### Source Editor

###### New Features

- Inactive code in `#if`…`#endif` blocks is now dimmed. This can be disabled in the  preferences.  (2450148)
- The  now supports commenting a selection within a single line.  (9245498)
- Quick Help now supports rendering images that are included in a documentation comment. Both external images referenced via URL and local images from your [`project’s documentation catalog`](https://developer.apple.comhttps://developer.apple.com/documentation/xcode/formatting-your-documentation-content#Add-images-to-your-content) are supported.  (45258339) (FB5708868)
- Xcode now supports accessing SDK framework documentation by invoking Quick Help on a reference to a module name. For example, activating Quick Help by option-clicking on an `import SwiftUI` statement now shows SwiftUI’s documentation.  (46583395) (FB5667593)
- Jump to definition “gd” Vim command is now supported.  (81116920) (FB9404427)
- The  command has been replaced with  to quickly access any menu command. By default, Command-clicking a token in the editor now performs . This can be changed in the  preferences. Control-clicking a token brings up the standard contextual menu that now contains all the commands that were available in the .  (86179596)
- Added  command to the  menu to split code onto separate lines. It has a default key binding of control-M.  (93150897)
- Editing with VoiceOver support has been improved. Source code landmarks and line number information now appear in the VoiceOver “More Content” menu. Accessories, including breakpoints, source control changes, and code folding ribbons appear as VoiceOver linked items. Source Editor Indentation preferences are also synced with VoiceOver’s speech and sound indentation preferences. Additionally, navigating the Source Editor with VoiceOver has been improved and important sections of the editor are now included as VoiceOver Window Spots.  (100877198)
- When using QuickHelp, information for multiple symbols is shown when the type is ambiguous.  (101256759)
- In Code Completion, functions that only contain one default parameter, now show as automatically expanded in code completion. Pressing right arrow on a function that contains more than one default parameter, expands to show all possible permutations of its parameters.  (103815908)
- Select inner block “i<” and “i>” Vim commands are now supported.  (104433144)
- Standalone and attached macros can be expanded in-line in the editor with the  command.  (104491696)
- Code completion now suggests names when declaring a type in Swift.  (106005529)

###### Resolved Issues

- Fixed: The font size used in the Quick Help popover now automatically adjusts to match the size of the editor’s current theme.  (6955736)
- Fixed: The source editor shouldn’t add an extra line when hitting Return right before a closing curly brace.  (64872737)
- Fixed: A number of issues were fixed with the syntax highlighting of multi-line string literals and string interpolations.  (75009350)
- Fixed: Jump to counterpart “%” Vim command now works in visual mode.  (79076961) (FB9146442)
- Fixed: Typing an open paren when an entire content of the line is selected incorrectly inserts newlines before and after the selected code.  (98690994)
- Fixed: With “trim trailing whitespace” turned on, don’t trim whitespace when discarding changes for a section of code or an entire file.  (102984729)
- Fixed: Scroll upwards “^u” / downwards “^d” Vim commands now extend selection in visual mode.  (103835213)
- Fixed: Put text after cursor “p” Vim command now inserts text without an extra new line.  (104037351)
- Fixed: Scroll upwards “^u” / downwards “^d” Vim commands now handle count prefix.  (104635013)
- Fixed: Select paragraphs forward “{” / backward “}” Vim commands now extend selection in visual mode.  (104782625)
- Fixed: Change case “gu{motion}” and “gU{motion}” Vim commands now change the characters rather than the whole word.  (104870847)
- Fixed: The source editor may hang for a short period while opening a file if the current toolchain doesn’t match the selected Xcode.  (109723219)

###### Known Issues

- Live Issues aren’t shown in macro expansions.  (108375601)

##### Storekit

###### Resolved Issues

- Fixed: The following StoreKitTest APIs are now available when testing on iOS 17 beta, watchOS 10 beta, tvOS 17 beta, and visionOS beta: [`setSimulatedError(_:forAPI:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession/4196369-setsimulatederror), [`simulatedError(forAPI:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession/4196370-simulatederror), and [`buyProduct(identifier:options:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession/4196368-buyproduct).  (110547289)

##### Storekit Testing in Xcode

###### New Features

- You can now create new in-app purchase transactions from the StoreKit Transaction Manager in Xcode. Just click the “+” button in the Transaction Manager, and configure your new transaction using the menu. Some functionality is only available when you’re testing your app on macOS 14.0, iOS 17.0, watchOS 10.0, or tvOS 17.0. You can use the new [`buyProduct(identifier:options:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession/4196368-buyproduct) API on [`SKTestSession`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession) to programmatically create an in-app purchase transaction based on a product identifier in your automated tests. When you use the `StoreKitTest` framework in your automated tests, there are additional new `Product.PurchaseOption` values available for configuring properties like the purchase date for your test transactions.  (101591947)
- The StoreKit Configuration Editor has a new App Configuration menu that allows you to configure global properties of your local StoreKit Testing in Xcode environment. In the App Configuration menu, you can choose an error to simulate for any throwing StoreKit 2 API. This causes that API to always fail with the error you configure, so you can verify your app handles each StoreKit errors properly. You can also use the new [`setSimulatedError(_:forAPI:)`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession/4196369-setsimulatederror) method on [`SKTestSession`](https://developer.apple.comhttps://developer.apple.com/documentation/storekittest/sktestsession) to programmatically simulate failures in your automated tests.  (101592113)
- You can now use the StoreKit Transaction Manager in Xcode to manage transactions without an active debug session. Once you install an app from Xcode using a StoreKit Configuration, it appears in the Transaction Manager’s navigator as long as a device, or simulator, is connected and running. To manage transactions outside of a debug session on a Mac app, you’ll need to be running macOS 14.0 or later. To manage transactions on other devices and simulators, you’ll need the test system to be running iOS 17.0, watchOS 10.0, or tvOS 17.0. You can still manage transactions on older operating systems as long as you have an active debug session.  (101592166)

###### Resolved Issues

- Fixed: When editing an auto-renewable subscription in the transaction manager via the “subscription options” dialog, a new transaction is created but the renewal is disabled. This causes the newly selected subscription to expire, and not renew.  (109403724)

##### Swift

###### New Features

- Swift 5.9 introduces , allowing you to write generic code that accepts any number of type parameters. A type parameter pack is declared with the `each` keyword, and you can iterate over a type parameter pack with the `repeat` keyword: ```None
 struct Pair<First, Second> {
   init(_ first: First, _ second: Second)
 }
 
 func makePairs<each First, each Second>(
   firsts first: repeat each First,
   seconds second: repeat each Second
 ) -> (repeat Pair<each First, each Second>) {
   return (repeat Pair(each first, each second))
 }
 
 let pairs = makePairs(firsts: 1, "hello", seconds: true, 1.0)
 // 'pairs' is '(Pair(1, true), Pair("hello", 2.0))'
``` Parameter packs were introduced in [`SE-0393`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0393-parameter-packs.md) and [`SE-0398`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0398-variadic-types.md).  (17414398) (FB5387236)
- Introduce `withDiscardingTaskGroup` and `withThrowingDiscardingTaskGroup`. New kinds of structured concurrency task groups, which efficiently discard completed tasks as soon as possible, without having to `await` their results explicitly from the parent task. [`SE-0381`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0381-task-group-discard-results.md)  (101965913)
- Non-copyable types are supported following [`SE-0390`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0390-noncopyable-structs-and-enums.md).  (104489948)
- The `consume` operator is supported following [`SE-0366`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0366-move-function.md).  (104490005)
- The `borrowing` and `consuming` parameter modifiers can only be used on parameters noncopyable type. Using either modifier on a parameter of copyable type will result in a compile time error.  (108383660)
- The `borrowing` and `consuming` modifiers are supported for function parameters following [`SE-0377`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0377-parameter-ownership-modifiers.md).  These provide more detailed control over object copying behavior and are required when passing noncopyable types to functions.  (108511703)
- Marking stored properties as unavailable with `@available` has been banned, closing an unintentional soundness hole that had allowed arbitrary unavailable code to run and unavailable type metadata to be used at runtime: ```swift
 @available(*, unavailable)
 struct Unavailable {
   init() {
     print("Unavailable.init()")
   }
 }
 
 struct S {
   @available(*, unavailable)
   var x = Unavailable()
 }
 
 _ = S() // prints "Unavailable.init()"
``` Marking `deinit` as unavailable has also been banned for similar reasons.  (108800140)
- The lifetime of a local variable value can be explicitly ended using the `consume` operator, forwarding ownership to the surrounding call, assignment, or initialization without copying: ```swift
 var x: [String] = []
 x.append("apples")
 x.append("bananas")
 x.append("oranges")
 
 process(consume x) // forward the current value, without copying
 
 x = [] // start building a new value
 x.append("broccoli")
 x.append("cauliflower")
 x.append("asparagus")
 ...
``` [`SE-0366`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0366-move-function.md)  (108800422)
- Functions can now declare whether they take value parameters by `borrowing` access to a value provided by the caller, or by `consuming` a value that the callee is allowed to take ownership of: ```swift
 struct HealthyFoods {
   var values: [String] = []
 
   // Ask to `consume` the parameter, since we want to use it
   // to incorporate into our own `values` array
   mutating func add(_ value: consuming String) {
       values.append(value)
   }
 }
``` [`SE-0377`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0377-parameter-ownership-modifiers.md)  (108800628)
- `if` and `switch` statements may now be used as expressions to: - Return values from functions, properties, and closures (either with implicit or explicit `return`)
- Throw errors using `throw`
- Assign values to variables
- Declare variables Each branch of the `if` or `switch` must be a single expression, the value of which becomes the value of the overall expression when that branch is chosen ```swift
 let bullet =
   if isRoot && (count == 0 || !willExpand) { "" }
   else if count == 0 { "- " }
   else if maxDepth <= 0 { "▹ " }
   else { "▿ " }
``` ```swift
 public static func width(_ x: Unicode.Scalar) -> Int {
   switch x.value {
     case 0..<0x80: 1
     case 0x80..<0x0800: 2
     case 0x0800..<0x1_0000: 3
     default: 4
     }
   }
``` [`SE-0380`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0380-if-switch-expressions.md)  (109305622)
- Swift 5.9 includes a new macro system that can be used to eliminate boilerplate and provide new forms of expressive APIs. Macros are declared with the new `macro` introducer: ```swift
 @freestanding(expression)
 macro assert(_ condition: Bool) = #externalMacro(module: "PowerAssertMacros", type: "AssertMacro")
``` Macros have parameter and result types, like functions, but are defined as separate programs that operate on syntax trees (using [`swift-syntax`](https://developer.apple.comhttps://github.com/apple/swift-syntax)) and produce new syntax trees that are incorporated into the program. Freestanding macros, indicated with the `@freestanding` attribute, are expanded in source code with a leading `#`: ```swift
 #assert(x + y == z) // expands to check the result of x + y == z and report failure if it's false
``` Macros can also be marked as `@attached`, in which case they will be meaning that they will be expanded using custom attribute syntax. For example: ```swift
 @attached(peer, names: overloaded)
 macro AddCompletionHandler() = #externalMacro(
   module: "ConcurrencyHelperMacros",
   type: "AddCompletionHandlerMacro"
 )
   
 @AddCompletionHandler
 func fetchAvatar(from url: URL) throws -> Image { ... }
   
 // expands to...
 func fetchAvatar(from url: URL, completionHandler: @escaping (Result<Image, Error>) -> Void) {
   Task.detached {
     do {
       let result = try await fetchAvatar(from: url)
       completionHandler(.success(result))
     } catch {
       completionHandler(.failure(error))
     }
   }
 }
``` Macros are implemented in separate programs, which are executed by the Swift compiler. The Swift Package Manager’s manifest provides a new `macro` target type to describe macros: ```swift
 import PackageDescription
 import CompilerPluginSupport
   
 let package = Package(
     name: "ConcurrencyHelpers",
     dependencies: [
           .package(url: "https://github.com/apple/swift-syntax", from: "509.0.0"),
      ],
      targets: [
           .macro(name: "ConcurrencyHelperMacros",
                  dependencies: [
                      .product(name: "SwiftSyntaxMacros", package: "swift-syntax"),
                      .product(name: "SwiftCompilerPlugin", package: "swift-syntax")
                  ]),
           .target(name: "ConcurrencyHelpers", dependencies: ["ConcurrencyHelperMacros"]),
           .testTarget(name: "ConcurrencyHelperMacroTests", dependencies: ["ConcurrencyHelperMacros"]),
     ]
 )
``` [`SE-0382`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0382-expression-macros.md), [`SE-0389`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0389-attached-macros.md), [`SE-0394`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0394-swiftpm-expression-macros.md), [`SE-0397`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0397-freestanding-declaration-macros.md)  (109903303)

###### Resolved Issues

- Fixed: [`#64927`](https://developer.apple.comhttps://github.com/apple/swift/issues/64927): Swift 5.9 introduces warnings that catch conversions from an inout argument in the caller to an `UnsafeRawPointer` in the callee whenever the original type contains an object reference. ```swift
 func inspectString(string: inout String) {
   readBytes(&string)
   // warning: forming an 'UnsafeRawPointer' to an inout variable of type String
   // exposes the internal representation rather than the string contents.
 }
``` ```swift
 func inspectData(data: inout Data) {
   readBytes(&data)
   // warning: forming an 'UnsafeRawPointer' to a variable of type 'T';
   // this is likely incorrect because 'T' may contain an object reference.
 }
``` (97963116)
- Fixed: A ”Failed to produce diagnostic” message can occur when forgetting to write `.element`.  (107160966)
- Fixed: Can’t ‘discard self’ in a consuming method of generic non-copyable type.  (108975216)
- Fixed: If a `~Copyable` type contains stored properties of generic or protocol type, then trying to access computed properties of the type might lead to a compiler crash. For example: ```swift
 struct Foo<T> : ~Copyable {
   var value: T
 
   var property: Int { return 0 }
 }
``` (109161396)
- Fixed: An `if` or `switch` expression that introduces a new variable may produce a spurious “cannot find ‘’ in scope” error when that `if` or `switch` is used in an assignment.  (109192116)
- Fixed: Escaping closures currently consume a noncopyable captured value instead of borrowing it as specified in [`SE-0390`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0390-noncopyable-structs-and-enums.md).  (109217216)
- Fixed: When a noncopyable type is consumed and reassigned, lldb no longer displays the variable in the current frame.  (109218404)
- Fixed: Applying the consume operator to a noncopyable var results in an unnecessary copy.  (109222496)
- Fixed: An `if` or `switch` expression may produce a spurious “may only be used in …” error when attempting to assign to an optional chain.  (109305454)
- Fixed: Swift modules with a very large number of extensions may experience slow build times.  (109543968)
- Fixed: Noncopyable types with deinits that are referenced outside of the defining file cause a compile time crash.  (109679168)

###### Known Issues

- Noncopyable types can’t currently be used in tuples or as generic types.  In particular, this means they can’t currently be stored in Arrays, Dictionaries, or Sets, nor can you form Optionals of noncopyable types or `print` them.  (104669935)
- Noncopyable types don’t currently work correctly when library evolution mode is enabled.  (107371421)
- Noncopyable types can’t mutate or consume ‘self’ in their deinit.  (108682993)
- Noncopyable enums can’t have a `deinit` or have indirect cases unlike in [`SE-0390`](https://developer.apple.comhttps://github.com/apple/swift-evolution/blob/main/proposals/0390-noncopyable-structs-and-enums.md).  (109686538)  To add a `deinit` to an `enum`, add a `struct` with `deinit` as a payload to the relevant cases. To work around indirect cases is to wrap the `enum` payload in a class.
- In some cases, using `_ = x` to suppress “unused variable” warnings about a `borrowing` parameter may raise incorrect “cannot be consumed” errors.  (109958008)  Mark the parameter as unused by using `_` as the binding name: ```None
 func method(parameter _: borrowing Type) {
 }
```
- Swift apps built with Xcode 15.0 crash on launch on macOS 10.13.  (114820860)  Add `$(TOOLCHAIN_DIR)/usr/lib/swift-5.0/macosx/libswiftAppKit.dylib` to the Other Linker Flags build setting in Xcode. This should be removed when the deployment target is increased to 10.14 or later.

##### Swift and C++ Interoperability

###### New Features

- Swift supports bidirectional interoperability with C++ / Objective-C++. You can now use a subset of C++ APIs in Swift and Swift APIs from C++. Enable C++ interoperability by selecting “C++ / Objective-C++” in the “C++ and Objective-C interoperability” build setting. For more information on C++ interoperability please see [`Mixing Swift and C++`](https://developer.apple.comhttps://swift.org/documentation/cxx-interop).  (100830806)

###### Resolved Issues

- Fixed: Calling `append` on a `std::string` value from Swift can crash compiler.  (107018724)
- Fixed: A Swift extension that adds an initializer to a C++ type could lead to a compiler crash when debugging is enabled.  (107561753)
- Fixed: Use of one C++ class template with multiple specializations in Swift could lead to duplicate definition link errors.  (107757051)
- Fixed: C++ std::set type can’t be initialized using a Swift set value in Swift.  (107909624)
- Fixed: C++ structure or class that contains Objective-C pointers data members, and no other non-trivial data members or special member functions, is passed incorrectly to an Objective-C method that’s called from Swift on Intel, leading to incorrect runtime behavior or crashes.  (109714315)
- Fixed: Can’t call default initializer of C types when C++ interoperability is enabled.  (109727620)

###### Known Issues

- Xcode code-completion results in Swift code can sometimes show C++ methods having incorrect parameter types (`Any`).  (108855791)
- Xcode doesn’t offer code-completion results for C++ namespace members in Swift.  (109714059)
- C++ members imported as properties via the `SWIFT_COMPUTED_PROPERTY` annotation aren’t indexed correctly in Swift files.  (109714153)

##### Swift Packages

###### New Features

- You can now create Swift Packages of various types using the File > New > Package… menu command.  Templates include macros, package plug-ins, as well as a command line tool configured to use swift-argument-parser.  (60274812) (FB7621436)
- Adding a dependency to a Swift package on the filesystem (instead of a remote URL) now participates in up-front package verification, such as checking transitive dependencies for conflicting version requirements.  (79576228)

###### Resolved Issues

- Fixed: When viewing Package Dependencies in the project editor, any packages with an Exact Version rule had the version number reset to 1.0.0.  (110303613) (FB12234300)
- Fixed: Swift Macros may fail to build when target destination is a platform other than macOS.  (110541100) (FB12291279)

###### Known Issues

- If the `Package.swift` file of a Swift App Playground project has been hand-edited to include unit test targets, the app playground fails to build with an error about duplicate commands.  (113752456)  Comment out or remove the unit test targets in the `Package.swift` file.

##### Swift Standard Library

###### New Features

- Instances of `Zip2Sequence` (that is, the result of calling `zip()`) now conform to `Sendable` if the sequences they zip also conform to `Sendable`.  (103840319)

##### Swiftdata

###### New Features

- Existing `@Query` property declarations might not always correctly infer the model type for predicate and sort descriptor parameters. (Note: the `@Query` attribute is now resolved as a macro, instead of as a property wrapper.) For example, specifying a filter predicate as a parameter to the `@Query` attribute will now require explicitly providing the model type used in the predicate, i.e. `#Predicate<ModelType> { … }` instead of `#Predicate { … }`: ```swift
 @Query(filter: #Predicate<Person> { ... }) var people: [Person]
``` Another example: passing a sort descriptor or key path will now require explicitly providing the model type used for the root type of the key path, i.e. `\ModelType.property` instead of `\.property`: ```swift
 @Query(sort: [SortDescriptor(\Person.name)]) var people: [Person]
 
 @Query(sort: \Person.name) var people: [Person]
``` In all cases, the model type used in the `filter:` and `sort:` parameters is still required to be the same type used as the element in the query’s wrapped array type, and will emit a build error if not.  (109433172)

###### Resolved Issues

- Fixed: After deleting an item, SwiftUI might attempt to reference the deleted content during the animation causing a crash.  (109838173)
- Fixed: `@Model` classes with initial values for stored properties result in an error that `self._$backingData` is used before being initialized.  (113572344)

##### Templates

###### New Features

- New Package offers some template package types, making it faster to create new command line tools in addition to libraries.  (107065338)

###### Resolved Issues

- Fixed: The App and Document App templates, when used with a SwiftUI interface, can opt in to using SwiftData for persistent storage.  (112229757)
- Fixed: The Audio Unit App template defines its App as a class.  (113652618)

##### Test Navigator

###### New Features

- The test navigator has been redesigned and re-written for a faster develop-test-debug loop. It reports and executes tests faster, and has a new filtering system which supports additional test results and recalling prior filters.   (94313839)
- The filter bar in the test navigator uses tokens instead of toggles now. A token can be added by clicking on the filter icon within the filter bar, or by typing “failed,” “skipped,” or “expected failure” into the bar and taking the autocompletion. Filters can be inverted by clicking on the inserted token and selecting the opposite predicate of what’s currently in use.   (101487428)

###### Resolved Issues

- Fixed: Test suites occasionally appear as “(Missing Suite).”  (109423329)

##### Test Report

###### Resolved Issues

- Fixed: Dragging a Test Report tab will cause Xcode to crash.  (113509332)

##### Testflight

###### Resolved Issues

- Fixed: watchOS apps that have a minimum deployment target below 6.0 may not install properly with TestFlight.  (109797881)

##### Testing

###### New Features

- `xcodebuild` now supports enumerating the test suite that would otherwise be executed by a test or test-without-building invocation. Test enumeration will list every target, class, and method contained within the suite in either human-readable or JSON format. Additionally, enumerated tests can be grouped hierarchically or as a flat list of identifiers (suitable for passing to future invocations of `xcodebuild`). Examples: - Build and then enumerate the tests within a project & scheme: ```None
 xcodebuild test -enumerate-tests -project MyProject.xcodeproj -scheme MyScheme -destination 'platform=iOS Simulator,name=iPhone 14 Pro'
``` - Build and then enumerate already-compiled tests in an xctestproducts bundle: ```None
 xcodebuild test-without-building -enumerate-tests -testProductsPath MyBuiltTests.xctestproducts -destination 'platform=iOS Simulator,name=iPhone 14 Pro'
``` - Build and then enumerate already-compiled tests specified by an xctestrun file: ```None
 xcodebuild test-without-building -enumerate-tests -xctestrun MyBuiltTests.xctestrun -destination 'platform=iOS Simulator,name=iPhone 14 Pro'
``` See xcodebuild’s `man` page for additional information.  (27230120) (FB5782338)
- XCTest now supports automatic screen recordings in addition to screenshots. Screen recordings allow for a fine-grained view of what happened during a test run, which can be meaningful to investigate UI test failures.  Screen recordings are enabled by default (in favor of screenshots). They can be disabled in the test plan or the scheme’s Test action options.  (35129014)
- UI Tests on watchOS will now automatically dismiss alerts if they were not handled.  (59571331)
- Xcode’s Test Report has been redesigned to provide a simplified understanding of test results across many different devices and testing configurations  (100825750)
- Instances of `XCTWaiter` can now be reused.  (101293832)

###### Resolved Issues

- Fixed: XCTest has a public API on iOS and iPadOS for typing in hardware keyboard support for modifier keys.  To access this API, use `XCUIElement.typeKey(_:modifierFlags:)`.  (20185910)
- Fixed: XCTest is now built with full exception handling enabled for Objective-C tests. This change may cause some objects to be released or deallocated when they were previously leaked.  (47727351)
- Fixed: The handler blocks for `XCTestExpectation` subclasses are now annotated `@Sendable` in Swift.  (102144121)
- Fixed: Support has been added for symbolicating backtraces captured by XCTest with symbols from other bundles in your project.  (103923199)
- Fixed: For tests that are executed without parallelization, a watchdog timer is now in place that covers the period during which `XCTestCase` instances are constructed (i.e. the designated initializer `-initWithInvocation:` is called). Hangs and long delays that occur during this period cause the test harness to abort testing early and attach a spindump to the result bundle for further investigation. If you have expensive work that occurs during a test case initializer, this work should be moved to `-setUp` or otherwise refactored to occur during the test method itself.  (104390801)
- Fixes known issues with the XCUIDevice.open(URL) and XCUIApplication.open(URL) API’s.  (109419759)

##### Tipkit

###### Resolved Issues

- Fixed: Tips and TipKit views will not display on Apple TV hardware.  (108286122)
- Fixed: TipKit does not build on Simulators or macOS due to macro “could not be found” errors.  (112663003)

##### Ui Testing

###### New Features

- Accessibility Audit support: An Accessibility Audit is an automated check performed on a given view for many kinds of Accessibility issues. These issues include missing labels, text which doesn’t scale with Dynamic Type, and low contrast. See `XCUIApplication().performAccessibilityAudit()`  (100732814)

###### Resolved Issues

- Fixed: UI Tests that choose screenshots over screen recordings may not see screenshots attached.  (109908952)

##### Videotoolbox

###### Resolved Issues

- Fixed: `canImport(VideoToolbox)` doesn’t return false for watchOS.  (109324910)

##### Xcode

###### Resolved Issues

- Fixed: Xcode might crash when creating a new file.  (112337760)

##### Xcode Cloud

###### New Features

- Xcode now supports a new Notarize Post-Action in Xcode Cloud workflows for macOS products.  (64009778)

###### Resolved Issues

- Fixed: An “Editor cannot be opened” dialog may show immediately after onboarding a new product to Xcode Cloud.  (109781276)
- Fixed: Xcode may crash when clicking the “Manage Workflows…” button from the Xcode Cloud Workflow Editor.  (110788363)
- Fixed: Downloading test artifacts from Xcode Cloud from within Xcode may sometimes crash.  (113418021)

## See Also

- [Xcode 15.4 Release Notes](xcode-15_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.3 Release Notes](xcode-15_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.2 Release Notes](xcode-15_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.1 Release Notes](xcode-15_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [Xcode 15.0.1 Release Notes](xcode-15_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode-release-notes/xcode-15-release-notes)*